import fs from 'node:fs/promises';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const rootDir = path.resolve(__dirname, '..');
const postsDir = path.join(rootDir, 'src', 'content', 'posts');
const publicDir = path.join(rootDir, 'public');
const blogsJsonPath = path.join(rootDir, 'src', 'data', 'blogs.json');

/**
 * Parse frontmatter and content from markdown text
 */
function parseMarkdown(raw) {
  const match = raw.match(/^---\r?\n([\s\S]*?)\r?\n---\r?\n([\s\S]*)$/);
  if (!match) {
    return { frontmatter: {}, content: raw };
  }

  const yamlStr = match[1];
  const content = match[2];
  const frontmatter = {};

  const lines = yamlStr.split('\n');
  let inComments = false;
  let commentsBuffer = '';

  for (let i = 0; i < lines.length; i++) {
    const line = lines[i];

    if (inComments) {
      commentsBuffer += '\n' + line;
      if (line.trim().endsWith(']')) {
        try {
          frontmatter['comments'] = JSON.parse(commentsBuffer.trim());
        } catch {
          frontmatter['comments'] = [];
        }
        inComments = false;
      }
      continue;
    }

    const colonIdx = line.indexOf(':');
    if (colonIdx > 0 && !line.startsWith(' ') && !line.startsWith('\t')) {
      const key = line.slice(0, colonIdx).trim();
      let val = line.slice(colonIdx + 1).trim();

      if (key === 'comments') {
        if (val.startsWith('[')) {
          if (val.endsWith(']')) {
            try {
              frontmatter[key] = JSON.parse(val);
            } catch {
              frontmatter[key] = [];
            }
          } else {
            inComments = true;
            commentsBuffer = val;
          }
        } else {
          frontmatter[key] = [];
        }
        continue;
      }

      if (val.startsWith('"') && val.endsWith('"')) {
        val = val.slice(1, -1).replace(/\\"/g, '"');
      } else if (val.startsWith("'") && val.endsWith("'")) {
        val = val.slice(1, -1);
      } else if (val.startsWith('[') && val.endsWith(']')) {
        try {
          val = JSON.parse(val);
        } catch {
          val = val.slice(1, -1).split(',').map(s => s.trim().replace(/^["']|["']$/g, ''));
        }
      } else if (val === 'true') {
        val = true;
      } else if (val === 'false') {
        val = false;
      }

      frontmatter[key] = val;
    }
  }

  return { frontmatter, content };
}

/**
 * Format frontmatter object and markdown content back to string
 */
function stringifyMarkdown(fm, content) {
  const escapeStr = (s) => (s || '').replace(/"/g, '\\"');
  
  const categoriesJson = JSON.stringify(fm.categories || []);
  const tagsJson = JSON.stringify(fm.tags || []);
  const commentsJson = JSON.stringify(fm.comments || []);

  const lines = ['---'];
  lines.push(`title: "${escapeStr(fm.title || '')}"`);
  lines.push(`date: "${fm.date || ''}"`);
  lines.push(`categories: ${categoriesJson}`);
  lines.push(`tags: ${tagsJson}`);
  lines.push(`slug: "${fm.slug || ''}"`);
  
  if (fm.legacyUrl) lines.push(`legacyUrl: "${fm.legacyUrl}"`);
  if (fm.legacyUrls && fm.legacyUrls.length) lines.push(`legacyUrls: ${JSON.stringify(fm.legacyUrls)}`);
  if (fm.source) lines.push(`source: "${fm.source}"`);
  if (fm.author) lines.push(`author: "${escapeStr(fm.author)}"`);
  if (fm.group) lines.push(`group: "${escapeStr(fm.group)}"`);
  
  if (fm.isTimeline) {
    lines.push('isTimeline: true');
  }

  if (fm.nowNote) {
    lines.push(`nowNote: ${JSON.stringify(fm.nowNote)}`);
  }
  if (fm.nowDate) {
    lines.push(`nowDate: "${escapeStr(fm.nowDate)}"`);
  }

  lines.push(`comments: ${commentsJson}`);
  lines.push('---');
  lines.push('');
  lines.push((content || '').trim());
  lines.push('');

  return lines.join('\n');
}

/**
 * Extract image references from markdown/HTML content
 */
function extractImages(content) {
  const images = [];

  // 1. Missing image placeholder figures
  const placeholderRegex = /<figure[^>]*class=["'][^"']*image-missing-placeholder[^"']*["'][^>]*>([\s\S]*?)<\/figure>/gi;
  let match;
  while ((match = placeholderRegex.exec(content)) !== null) {
    const fullTag = match[0];
    const inner = match[1];
    
    // Extract aria-label or placeholder-text
    const ariaLabelMatch = fullTag.match(/aria-label=["']([^"']*)["']/i);
    const textMatch = inner.match(/<span[^>]*class=["']placeholder-text["'][^>]*>([\s\S]*?)<\/span>/i);
    const label = (ariaLabelMatch && ariaLabelMatch[1]) || (textMatch && textMatch[1].trim()) || 'Gambar Hilang';

    images.push({
      alt: label,
      url: '',
      fullMatch: fullTag,
      type: 'placeholder',
      isPlaceholder: true
    });
  }

  // 2. Markdown images
  const mdRegex = /!\[(.*?)\]\((.*?)\)/g;
  while ((match = mdRegex.exec(content)) !== null) {
    images.push({ alt: match[1], url: match[2], fullMatch: match[0], type: 'markdown' });
  }

  // 3. HTML img tags
  const htmlRegex = /<img[^>]+src=["']([^"']+)["'][^>]*>/gi;
  while ((match = htmlRegex.exec(content)) !== null) {
    const tag = match[0];
    const src = match[1];
    const altMatch = tag.match(/alt=["']([^"']*)["']/i);
    images.push({
      alt: altMatch ? altMatch[1] : '',
      url: src,
      fullMatch: tag,
      type: 'html'
    });
  }

  return images;
}

/**
 * Admin API Middleware handler for Vite dev server
 */
export function adminApiMiddleware(req, res, next) {
  const url = new URL(req.url, 'http://localhost');
  const pathname = url.pathname;

  const sendJson = (data, statusCode = 200) => {
    res.statusCode = statusCode;
    res.setHeader('Content-Type', 'application/json; charset=utf-8');
    res.end(JSON.stringify(data));
  };

  const sendError = (msg, statusCode = 400) => {
    sendJson({ error: msg }, statusCode);
  };

  const readBody = () => new Promise((resolve, reject) => {
    let data = '';
    req.on('data', chunk => { data += chunk; });
    req.on('end', () => {
      try {
        resolve(data ? JSON.parse(data) : {});
      } catch (err) {
        reject(err);
      }
    });
    req.on('error', reject);
  });

  if (pathname === '/posts' && req.method === 'GET') {
    (async () => {
      try {
        const files = await fs.readdir(postsDir);
        const mdFiles = files.filter(f => f.endsWith('.md'));
        const posts = [];

        for (const file of mdFiles) {
          const raw = await fs.readFile(path.join(postsDir, file), 'utf-8');
          const { frontmatter } = parseMarkdown(raw);
          posts.push({
            file,
            title: frontmatter.title || file,
            date: frontmatter.date || '',
            slug: frontmatter.slug || '',
            categories: frontmatter.categories || [],
            tags: frontmatter.tags || [],
            source: frontmatter.source || 'takien.com',
            author: frontmatter.author || 'takien',
            group: frontmatter.group || '',
            hasNowNote: Boolean(frontmatter.nowNote),
            nowNote: frontmatter.nowNote || '',
            nowDate: frontmatter.nowDate || '',
            isTimeline: Boolean(frontmatter.isTimeline),
            commentsCount: Array.isArray(frontmatter.comments) ? frontmatter.comments.length : 0
          });
        }

        posts.sort((a, b) => new Date(b.date || 0).getTime() - new Date(a.date || 0).getTime());
        sendJson(posts);
      } catch (err) {
        sendError(err.message, 500);
      }
    })();
    return;
  }

  if (pathname === '/post' && req.method === 'GET') {
    (async () => {
      try {
        const file = url.searchParams.get('file');
        if (!file) return sendError('Parameter file wajib diisi');

        const filePath = path.join(postsDir, path.basename(file));
        const raw = await fs.readFile(filePath, 'utf-8');
        const { frontmatter, content } = parseMarkdown(raw);
        const images = extractImages(content);

        sendJson({
          file: path.basename(file),
          frontmatter,
          content,
          images
        });
      } catch (err) {
        sendError(err.message, 500);
      }
    })();
    return;
  }

  if (pathname === '/save' && req.method === 'POST') {
    (async () => {
      try {
        const body = await readBody();
        let {
          file,
          isNew,
          title,
          date,
          categories,
          tags,
          slug,
          source,
          author,
          group,
          nowNote,
          nowDate,
          isTimeline,
          content
        } = body;

        if (!title) return sendError('Judul postingan wajib diisi');
        if (!date) {
          date = new Date().toISOString();
        }

        if (!slug) {
          const d = new Date(date);
          const y = d.getFullYear() || 2026;
          const m = String(d.getMonth() + 1).padStart(2, '0');
          const day = String(d.getDate()).padStart(2, '0');
          const slugified = title.toLowerCase().replace(/[^a-z0-9\s-]/g, '').trim().replace(/\s+/g, '-');
          slug = `${y}/${m}/${day}/${slugified}`;
        }

        let targetFilename = file;

        if (isNew || !targetFilename) {
          const d = new Date(date);
          const y = d.getFullYear() || 2026;
          const m = String(d.getMonth() + 1).padStart(2, '0');
          const day = String(d.getDate()).padStart(2, '0');
          const slugBase = (slug.split('/').pop() || 'post').slice(0, 50);
          targetFilename = `${y}_${m}_${day}_${slugBase}.md`;

          let counter = 1;
          while (true) {
            try {
              await fs.access(path.join(postsDir, targetFilename));
              targetFilename = `${y}_${m}_${day}_${slugBase}-${counter}.md`;
              counter++;
            } catch {
              break;
            }
          }
        }

        const filePath = path.join(postsDir, path.basename(targetFilename));

        let existingFm = {};
        if (!isNew) {
          try {
            const rawOld = await fs.readFile(filePath, 'utf-8');
            existingFm = parseMarkdown(rawOld).frontmatter || {};
          } catch {}
        }

        const updatedFm = {
          ...existingFm,
          title,
          date,
          categories: Array.isArray(categories) ? categories : [],
          tags: Array.isArray(tags) ? tags : [],
          slug,
          legacyUrl: `/${slug.replace(/^\//, '').replace(/\/$/, '')}/`,
          source: source || existingFm.source || 'takien.com',
          author: author || existingFm.author || 'takien',
          group: group !== undefined ? group : (existingFm.group || ''),
          nowNote: nowNote ? nowNote.trim() : undefined,
          nowDate: nowDate ? nowDate.trim() : undefined,
          isTimeline: Boolean(isTimeline)
        };

        const finalMarkdown = stringifyMarkdown(updatedFm, content || '');
        await fs.writeFile(filePath, finalMarkdown, 'utf-8');

        // Trigger Astro content sync & route regeneration automatically
        try {
          const now = new Date();
          await fs.utimes(path.join(rootDir, 'src', 'content.config.ts'), now, now);
        } catch {}

        sendJson({
          success: true,
          file: path.basename(targetFilename),
          slug,
          message: 'Postingan berhasil disimpan!'
        });
      } catch (err) {
        sendError(err.message, 500);
      }
    })();
    return;
  }

  if (pathname === '/delete' && req.method === 'POST') {
    (async () => {
      try {
        const body = await readBody();
        const { file } = body;
        if (!file) return sendError('Nama file postingan wajib disertakan');

        const cleanFile = path.basename(file);
        const filePath = path.join(postsDir, cleanFile);

        try {
          await fs.access(filePath);
        } catch {
          return sendError('File postingan tidak ditemukan', 404);
        }

        await fs.unlink(filePath);

        sendJson({
          success: true,
          file: cleanFile,
          message: `Postingan ${cleanFile} berhasil dihapus!`
        });
      } catch (err) {
        sendError('Gagal menghapus postingan: ' + err.message, 500);
      }
    })();
    return;
  }

  if (pathname === '/upload' && req.method === 'POST') {
    (async () => {
      try {
        const body = await readBody();
        const { dataUrl, filename, targetPath } = body;

        if (!dataUrl) return sendError('Data gambar tidak ditemukan');

        const matches = dataUrl.match(/^data:([A-Za-z-+\/]+);base64,(.+)$/);
        if (!matches || matches.length !== 3) {
          return sendError('Format data gambar tidak valid');
        }

        const buffer = Buffer.from(matches[2], 'base64');

        let destRelPath = '';
        if (targetPath) {
          const cleanTarget = targetPath.replace(/^\/+/, '');
          const absTarget = path.join(publicDir, cleanTarget);
          
          if (!absTarget.startsWith(publicDir)) {
            return sendError('Jalur file target tidak diizinkan');
          }

          await fs.mkdir(path.dirname(absTarget), { recursive: true });
          await fs.writeFile(absTarget, buffer);
          destRelPath = '/' + cleanTarget;
        } else {
          const cleanName = (filename || 'image.jpg').toLowerCase().replace(/[^a-z0-9.-]/g, '-');
          const time = Date.now();
          const savedName = `${time}_${cleanName}`;
          const uploadsDir = path.join(publicDir, 'images', 'uploads');
          await fs.mkdir(uploadsDir, { recursive: true });
          await fs.writeFile(path.join(uploadsDir, savedName), buffer);
          destRelPath = `/images/uploads/${savedName}`;
        }

        sendJson({
          success: true,
          url: destRelPath,
          message: 'Gambar berhasil disimpan!'
        });
      } catch (err) {
        sendError(err.message, 500);
      }
    })();
    return;
  }

  if (pathname === '/blogs' && req.method === 'GET') {
    (async () => {
      try {
        const raw = await fs.readFile(blogsJsonPath, 'utf-8');
        const blogs = JSON.parse(raw);
        sendJson(blogs);
      } catch (err) {
        sendError('Gagal membaca data blogs: ' + err.message, 500);
      }
    })();
    return;
  }

  if (pathname === '/blogs/save' && req.method === 'POST') {
    (async () => {
      try {
        const body = await readBody();
        const { blogs } = body;
        if (!Array.isArray(blogs)) {
          return sendError('Data blogs harus berupa array');
        }

        await fs.mkdir(path.dirname(blogsJsonPath), { recursive: true });
        await fs.writeFile(blogsJsonPath, JSON.stringify(blogs, null, 2), 'utf-8');

        sendJson({
          success: true,
          message: 'Data info blog berhasil disimpan!'
        });
      } catch (err) {
        sendError('Gagal menyimpan data blogs: ' + err.message, 500);
      }
    })();
    return;
  }

  next();
}
