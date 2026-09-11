import blogsData from '../data/blogs.json';

export interface BlogItem {
  id: string;
  name: string;
  shortName: string;
  slug: string;
  period: string;
  description: string;
  color: string;
  dotClass: string;
  badgeClass?: string;
}

export interface SourceInfo {
  key: string;
  name: string;
  shortName: string;
  slug: string;
  color: string;
  dotClass: string;
  badgeClass: string;
  period?: string;
  description?: string;
}

export function getBlogSources(): BlogItem[] {
  return blogsData as BlogItem[];
}

export function getBlogDescription(rawSource?: string): string {
  const info = getSourceInfo(rawSource);
  const found = (blogsData as BlogItem[]).find(b => b.slug === info.slug || b.id === info.slug || b.name === info.name);
  return found?.description || '';
}

export function getSourceInfo(rawSource?: string): SourceInfo {
  const s = (rawSource || 'takien.com').toLowerCase().trim();
  const allBlogs = blogsData as BlogItem[];

  // Match by id or slug or shortName
  const match = allBlogs.find(b => {
    const slug = b.slug.toLowerCase();
    const id = b.id.toLowerCase();
    const shortName = (b.shortName || '').toLowerCase();
    const name = (b.name || '').toLowerCase();
    return s === slug || s === id || s === shortName || s === name || (shortName && s.includes(shortName)) || slug.includes(s) || name.includes(s) || s.includes(name);
  });

  if (match) {
    return {
      key: match.shortName,
      name: match.name,
      shortName: match.shortName,
      slug: match.slug,
      color: match.color,
      dotClass: match.dotClass,
      badgeClass: match.badgeClass || `badge-src-${match.shortName}`,
      period: match.period,
      description: match.description
    };
  }

  // Fallback: Takien.com
  const defaultBlog = allBlogs.find(b => b.id === 'takien.com') || {
    id: 'takien.com',
    name: 'takien.com',
    shortName: 'takien.com',
    slug: 'takien.com',
    period: '2007–2016',
    description: 'Koleksi tulisan utama di blog takien.com sejak 2007 hingga 2016.',
    color: '#a855f7',
    dotClass: 'dot-takien',
    badgeClass: 'badge-src-takien'
  };

  return {
    key: 'takien',
    name: defaultBlog.name,
    shortName: defaultBlog.shortName,
    slug: defaultBlog.slug,
    color: defaultBlog.color,
    dotClass: defaultBlog.dotClass,
    badgeClass: defaultBlog.badgeClass || 'badge-src-takien',
    period: defaultBlog.period,
    description: defaultBlog.description
  };
}

export function isTimelinePost(postData: any): boolean {
  if (!postData) return false;
  return Boolean(postData.isTimeline);
}

export function isFreshPost(postData: any): boolean {
  if (!postData) return false;
  if (postData.isTimeline) return false;
  if (postData.isFresh) return true;
  if (postData.date) {
    const y = parseInt(postData.date.slice(0, 4), 10);
    if (!isNaN(y) && y >= 2026) return true;
  }
  return false;
}

export const STATIC_PAGE_SLUGS = new Set(['about', 'contact', 'gabung-komunitas', 'vibe-coding', 'wordpress-plugins', 'jquery-plugins']);

