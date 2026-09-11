import fs from 'node:fs/promises';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import yaml from 'js-yaml';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const rootDir = path.resolve(__dirname, '..');
const postsDir = path.join(rootDir, 'src', 'content', 'posts');
const publicDir = path.join(rootDir, 'public');
const blogsJsonPath = path.join(rootDir, 'src', 'data', 'blogs.json');
const navigationJsonPath = path.join(rootDir, 'src', 'data', 'navigation.json');

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
  let frontmatter = {};

  try {
    frontmatter = yaml.load(yamlStr) || {};
  } catch (e) {
    frontmatter = {};
  }

  if (!Array.isArray(frontmatter.categories)) {
    frontmatter.categories = frontmatter.categories ? [frontmatter.categories] : [];
  }
  if (!Array.isArray(frontmatter.tags)) {
    frontmatter.tags = frontmatter.tags ? [frontmatter.tags] : [];
  }
  if (!Array.isArray(frontmatter.comments)) {
    frontmatter.comments = [];
  }
  if (!Array.isArray(frontmatter.photos)) {
    frontmatter.photos = [];
  }
  frontmatter.album = frontmatter.album || '';
  frontmatter.coverImage = frontmatter.coverImage || '';
  frontmatter.format = frontmatter.format || frontmatter.type || 'post';

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
  if (fm.format && fm.format !== 'post') {
    lines.push(`format: "${fm.format}"`);
  }
  
  if (fm.legacyUrl) lines.push(`legacyUrl: "${fm.legacyUrl}"`);
  if (fm.legacyUrls && fm.legacyUrls.length) lines.push(`legacyUrls: ${JSON.stringify(fm.legacyUrls)}`);
  if (fm.source) lines.push(`source: "${fm.source}"`);
  if (fm.author) lines.push(`author: "${escapeStr(fm.author)}"`);
  if (fm.group) lines.push(`group: "${escapeStr(fm.group)}"`);
  if (fm.album) lines.push(`album: "${escapeStr(fm.album)}"`);
  if (fm.coverImage) lines.push(`coverImage: "${fm.coverImage}"`);
  if (Array.isArray(fm.photos) && fm.photos.length > 0) {
    lines.push(`photos: ${JSON.stringify(fm.photos)}`);
  }
  
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

function getFilenameFromUrl(urlStr) {
  if (!urlStr) return '';
  try {
    const clean = urlStr.split('?')[0].split('#')[0].replace(/\/+$/, '');
    const parts = clean.split('/');
    const last = parts.pop() || '';
    return decodeURIComponent(last);
  } catch {
    return (urlStr.split('/').pop() || '').split('?')[0];
  }
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
    const filename = getFilenameFromUrl(label) || label;

    images.push({
      alt: label,
      filename,
      url: '',
      fullMatch: fullTag,
      type: 'placeholder',
      isPlaceholder: true
    });
  }

  // 2. Markdown images
  const mdRegex = /!\[(.*?)\]\((.*?)\)/g;
  while ((match = mdRegex.exec(content)) !== null) {
    const filename = getFilenameFromUrl(match[2]) || match[1] || 'image';
    images.push({ alt: match[1], filename, url: match[2], fullMatch: match[0], type: 'markdown' });
  }

  // 3. HTML img tags
  const htmlRegex = /<img[^>]+src=["']([^"']+)["'][^>]*>/gi;
  while ((match = htmlRegex.exec(content)) !== null) {
    const tag = match[0];
    const src = match[1];
    const altMatch = tag.match(/alt=["']([^"']*)["']/i);
    const alt = altMatch ? altMatch[1] : '';
    const filename = getFilenameFromUrl(src) || alt || 'image';
    images.push({
      alt,
      filename,
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
            format: frontmatter.format || frontmatter.type || 'post',
            categories: frontmatter.categories || [],
            tags: frontmatter.tags || [],
            source: frontmatter.source || 'takien.com',
            author: frontmatter.author || 'takien',
            group: frontmatter.group || '',
            album: frontmatter.album || '',
            coverImage: frontmatter.coverImage || '',
            photosCount: Array.isArray(frontmatter.photos) ? frontmatter.photos.length : 0,
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
          format,
          categories,
          tags,
          slug,
          source,
          author,
          group,
          album,
          coverImage,
          photos,
          nowNote,
          nowDate,
          isTimeline,
          content,
          comments
        } = body;

        if (!title) return sendError('Judul postingan wajib diisi');
        if (!date) {
          date = new Date().toISOString();
        }

        if (!slug) {
          const slugified = title.toLowerCase().replace(/[^a-z0-9\s-]/g, '').trim().replace(/\s+/g, '-');
          if (format === 'gallery') {
            slug = `gallery/${slugified}`;
          } else {
            const d = new Date(date);
            const y = d.getFullYear() || 2026;
            const m = String(d.getMonth() + 1).padStart(2, '0');
            const day = String(d.getDate()).padStart(2, '0');
            slug = `${y}/${m}/${day}/${slugified}`;
          }
        }

        let targetFilename = file;

        if (isNew || !targetFilename) {
          const slugBase = (slug.split('/').pop() || 'gallery').slice(0, 50);
          if (format === 'gallery') {
            targetFilename = `gallery_${slugBase}.md`;
          } else {
            const d = new Date(date);
            const y = d.getFullYear() || 2026;
            const m = String(d.getMonth() + 1).padStart(2, '0');
            const day = String(d.getDate()).padStart(2, '0');
            targetFilename = `${y}_${m}_${day}_${slugBase}.md`;
          }

          let counter = 1;
          while (true) {
            try {
              await fs.access(path.join(postsDir, targetFilename));
              if (format === 'gallery') {
                targetFilename = `gallery_${slugBase}-${counter}.md`;
              } else {
                const d = new Date(date);
                const y = d.getFullYear() || 2026;
                const m = String(d.getMonth() + 1).padStart(2, '0');
                const day = String(d.getDate()).padStart(2, '0');
                targetFilename = `${y}_${m}_${day}_${slugBase}-${counter}.md`;
              }
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

        let finalComments = existingFm.comments || [];
        if (Array.isArray(comments)) {
          finalComments = comments.map(c => ({
            author: String(c.author || c.nama || c.name || 'Anonymous').trim(),
            date: (c.date === null || c.date === undefined) ? (c.tanggal === null || c.tanggal === undefined ? '' : String(c.tanggal).trim()) : String(c.date).trim(),
            text: String(c.text !== undefined ? c.text : (c.komentar !== undefined ? c.komentar : (c.comment !== undefined ? c.comment : ''))).trim()
          })).filter(c => c.text.length > 0 || c.author.length > 0);
        }

        let finalPhotos = existingFm.photos || [];
        if (Array.isArray(photos)) {
          finalPhotos = photos.map(p => ({
            url: String(p.url || '').trim(),
            caption: String(p.caption || '').trim(),
            alt: String(p.alt || p.caption || '').trim(),
            date: p.date ? String(p.date).trim() : undefined
          })).filter(p => p.url.length > 0);
        }

        const updatedFm = {
          ...existingFm,
          title,
          date,
          format: format || existingFm.format || existingFm.type || 'post',
          categories: Array.isArray(categories) ? categories : [],
          tags: Array.isArray(tags) ? tags : [],
          slug,
          legacyUrl: `/${slug.replace(/^\//, '').replace(/\/$/, '')}/`,
          source: source || existingFm.source || 'takien.com',
          author: author || existingFm.author || 'takien',
          group: group !== undefined ? group : (existingFm.group || ''),
          album: album !== undefined ? album : (existingFm.album || ''),
          coverImage: coverImage !== undefined ? coverImage : (existingFm.coverImage || (finalPhotos[0]?.url || '')),
          photos: finalPhotos,
          nowNote: nowNote ? nowNote.trim() : undefined,
          nowDate: nowDate ? nowDate.trim() : undefined,
          isTimeline: Boolean(isTimeline),
          comments: finalComments
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

  if (pathname === '/merge' && req.method === 'POST') {
    (async () => {
      try {
        const body = await readBody();
        const { targetFile, sourceFiles, options = {} } = body;

        if (!targetFile) return sendError('Target file wajib disertakan');
        if (!Array.isArray(sourceFiles) || sourceFiles.length === 0) {
          return sendError('Minimal satu file sumber harus dipilih');
        }

        const cleanTarget = path.basename(targetFile);
        const targetFilePath = path.join(postsDir, cleanTarget);

        // Read target file
        let targetRaw;
        try {
          targetRaw = await fs.readFile(targetFilePath, 'utf-8');
        } catch {
          return sendError(`File target "${cleanTarget}" tidak ditemukan`, 404);
        }

        const parsedTarget = parseMarkdown(targetRaw);
        const targetFm = parsedTarget.frontmatter;
        let mergedContent = (parsedTarget.content || '').trim();

        const includeHeading = options.includeHeading !== false;
        const mergeCategories = options.mergeCategories !== false;
        const mergeTags = options.mergeTags !== false;
        const mergeComments = options.mergeComments !== false;
        const addLegacyUrls = options.addLegacyUrls !== false;
        const deleteSourceFiles = options.deleteSourceFiles !== false;

        // Sets for unique categories and tags
        const categorySet = new Set(targetFm.categories || []);
        const tagSet = new Set(targetFm.tags || []);
        let allComments = Array.isArray(targetFm.comments) ? [...targetFm.comments] : [];

        // Legacy URLs set
        const legacyUrlsSet = new Set(
          (Array.isArray(targetFm.legacyUrls) ? targetFm.legacyUrls : []).map(u => u.replace(/^\/+|\/+$/g, ''))
        );

        const processedSourceFiles = [];

        for (const src of sourceFiles) {
          const cleanSrc = path.basename(src);
          if (cleanSrc === cleanTarget) continue; // skip self

          const srcPath = path.join(postsDir, cleanSrc);
          let srcRaw;
          try {
            srcRaw = await fs.readFile(srcPath, 'utf-8');
          } catch {
            console.warn(`File sumber ${cleanSrc} tidak ditemukan, dilewati.`);
            continue;
          }

          const parsedSrc = parseMarkdown(srcRaw);
          const srcFm = parsedSrc.frontmatter;
          const srcContent = (parsedSrc.content || '').trim();

          // 1. Append content
          if (srcContent) {
            if (mergedContent) mergedContent += '\n\n';
            if (includeHeading && srcFm.title) {
              mergedContent += `## ${srcFm.title}\n\n`;
            } else if (mergedContent) {
              mergedContent += '---\n\n';
            }
            mergedContent += srcContent;
          }

          // 2. Categories & tags
          if (mergeCategories && Array.isArray(srcFm.categories)) {
            srcFm.categories.forEach(c => c && categorySet.add(c));
          }
          if (mergeTags && Array.isArray(srcFm.tags)) {
            srcFm.tags.forEach(t => t && tagSet.add(t));
          }

          // 3. Comments
          if (mergeComments && Array.isArray(srcFm.comments)) {
            allComments = allComments.concat(srcFm.comments);
          }

          // 4. Legacy URLs
          if (addLegacyUrls) {
            const cleanSlug = (s) => (s || '').replace(/^\/+|\/+$/g, '');
            if (srcFm.slug) legacyUrlsSet.add(cleanSlug(srcFm.slug));
            if (srcFm.legacyUrl) legacyUrlsSet.add(cleanSlug(srcFm.legacyUrl));
            if (Array.isArray(srcFm.legacyUrls)) {
              srcFm.legacyUrls.forEach(u => u && legacyUrlsSet.add(cleanSlug(u)));
            }
          }

          processedSourceFiles.push(cleanSrc);
        }

        if (processedSourceFiles.length === 0) {
          return sendError('Tidak ada file sumber valid yang dapat digabungkan');
        }

        // Clean target legacyUrls: remove target's own slug and target's own legacyUrl from legacyUrls set
        const targetCleanSlug = (targetFm.slug || '').replace(/^\/+|\/+$/g, '');
        const targetCleanLegacy = (targetFm.legacyUrl || '').replace(/^\/+|\/+$/g, '');
        legacyUrlsSet.delete(targetCleanSlug);
        if (targetCleanLegacy) legacyUrlsSet.delete(targetCleanLegacy);
        legacyUrlsSet.delete('');

        // Sort comments chronologically if possible
        if (mergeComments && allComments.length > 1) {
          allComments.sort((a, b) => {
            const da = a.date ? new Date(a.date).getTime() : 0;
            const db = b.date ? new Date(b.date).getTime() : 0;
            return da - db;
          });
        }

        // Apply metadata updates
        if (options.customTitle && options.customTitle.trim()) {
          targetFm.title = options.customTitle.trim();
        }
        if (mergeCategories) {
          targetFm.categories = Array.from(categorySet);
        }
        if (mergeTags) {
          targetFm.tags = Array.from(tagSet);
        }
        if (mergeComments) {
          targetFm.comments = allComments;
        }
        if (addLegacyUrls) {
          targetFm.legacyUrls = Array.from(legacyUrlsSet);
        }

        // Stringify & write target
        const newTargetContent = stringifyMarkdown(targetFm, mergedContent);
        await fs.writeFile(targetFilePath, newTargetContent, 'utf-8');

        // Delete source files if requested
        const deletedFiles = [];
        if (deleteSourceFiles) {
          for (const sFile of processedSourceFiles) {
            try {
              await fs.unlink(path.join(postsDir, sFile));
              deletedFiles.push(sFile);
            } catch (err) {
              console.error(`Gagal menghapus file sumber ${sFile}:`, err);
            }
          }
        }

        sendJson({
          success: true,
          targetFile: cleanTarget,
          slug: targetFm.slug,
          mergedCount: processedSourceFiles.length,
          deletedFiles,
          message: `Berhasil menggabungkan ${processedSourceFiles.length} post ke dalam "${targetFm.title}"!`
        });
      } catch (err) {
        sendError('Gagal menggabungkan postingan: ' + err.message, 500);
      }
    })();
    return;
  }

  if (pathname === '/upload' && req.method === 'POST') {
    (async () => {
      try {
        const body = await readBody();
        const { dataUrl, filename, targetPath, files } = body;

        const saveSingleImage = async (imgData, imgName, imgTarget) => {
          let buffer;
          const commaIdx = imgData.indexOf(',');
          const base64Str = commaIdx !== -1 ? imgData.slice(commaIdx + 1) : imgData;
          buffer = Buffer.from(base64Str.replace(/\s+/g, ''), 'base64');
          if (!buffer || buffer.length === 0) {
            throw new Error('Data gambar kosong');
          }

          let destRelPath = '';
          if (imgTarget && !imgTarget.startsWith('http://') && !imgTarget.startsWith('https://')) {
            const cleanTarget = imgTarget.split('?')[0].split('#')[0].replace(/^\/+/, '');
            const absTarget = path.join(publicDir, cleanTarget);
            if (!absTarget.startsWith(publicDir)) {
              throw new Error('Jalur file target tidak diizinkan');
            }
            await fs.mkdir(path.dirname(absTarget), { recursive: true });
            await fs.writeFile(absTarget, buffer);
            destRelPath = '/' + cleanTarget;
          } else {
            let cleanName = (imgName || 'image.png').toLowerCase().replace(/[^a-z0-9.-]/g, '-');
            if (!path.extname(cleanName)) cleanName += '.png';
            const time = Date.now() + Math.floor(Math.random() * 1000);
            const savedName = `${time}_${cleanName}`;
            const uploadsDir = path.join(publicDir, 'images', 'uploads');
            await fs.mkdir(uploadsDir, { recursive: true });
            await fs.writeFile(path.join(uploadsDir, savedName), buffer);
            destRelPath = `/images/uploads/${savedName}`;
          }
          return destRelPath;
        };

        // Multi-file batch upload support
        if (Array.isArray(files) && files.length > 0) {
          const results = [];
          for (const item of files) {
            if (item && item.dataUrl) {
              const url = await saveSingleImage(item.dataUrl, item.filename, item.targetPath);
              results.push({
                url,
                filename: item.filename || path.basename(url),
                caption: item.caption || ''
              });
            }
          }
          return sendJson({
            success: true,
            uploaded: results,
            message: `Berhasil mengunggah ${results.length} foto!`
          });
        }

        // Single file upload
        if (!dataUrl) return sendError('Data gambar tidak ditemukan');
        const destRelPath = await saveSingleImage(dataUrl, filename, targetPath);

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

  if (pathname === '/navigation' || pathname === '/nav') {
    if (req.method === 'GET') {
      (async () => {
        try {
          const raw = await fs.readFile(navigationJsonPath, 'utf-8');
          const nav = JSON.parse(raw);
          sendJson(nav);
        } catch (err) {
          sendError('Gagal membaca data navigasi: ' + err.message, 500);
        }
      })();
      return;
    }
  }

  if (pathname === '/navigation/save' || pathname === '/nav/save') {
    if (req.method === 'POST') {
      (async () => {
        try {
          const body = await readBody();
          const { items, navigation } = body;
          const navArray = Array.isArray(items) ? items : (Array.isArray(navigation) ? navigation : (Array.isArray(body) ? body : null));
          if (!navArray) {
            return sendError('Data navigasi harus berupa array item menu');
          }

          // Sanitize items
          const cleaned = navArray.map(item => {
            const cleanItem = {
              title: String(item.title || '').trim() || 'Menu',
              url: String(item.url || '').trim() || '#'
            };
            if (item.target === '_blank' || item.newWindow || item.targetBlank) {
              cleanItem.target = '_blank';
            }
            if (Array.isArray(item.children) && item.children.length > 0) {
              cleanItem.children = item.children.map(child => {
                const cleanChild = {
                  title: String(child.title || '').trim() || 'Sub Menu',
                  url: String(child.url || '').trim() || '#'
                };
                if (child.target === '_blank' || child.newWindow || child.targetBlank) {
                  cleanChild.target = '_blank';
                }
                return cleanChild;
              });
            }
            return cleanItem;
          });

          await fs.mkdir(path.dirname(navigationJsonPath), { recursive: true });
          await fs.writeFile(navigationJsonPath, JSON.stringify(cleaned, null, 2), 'utf-8');

          sendJson({
            success: true,
            navigation: cleaned,
            message: 'Menu navigasi berhasil disimpan!'
          });
        } catch (err) {
          sendError('Gagal menyimpan menu navigasi: ' + err.message, 500);
        }
      })();
      return;
    }
  }

  next();
}
