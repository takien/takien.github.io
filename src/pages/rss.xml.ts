import rss from '@astrojs/rss';
import { getCollection } from 'astro:content';

export async function GET(context: any) {
  const excludedRssSlugs = new Set(['about', 'contact', 'gabung-komunitas', 'vibe-coding', 'wordpress-plugins', 'jquery-plugins']);
  const posts = (await getCollection('posts'))
    .filter((p) => {
      const isPage = p.data.format === 'page' || (p.data as any).type === 'page';
      const cleanSlug = p.data.slug.replace(/^\//, '').replace(/\/$/, '');
      return Boolean(p.data.date && p.data.date.trim().length > 0 && !isPage && !excludedRssSlugs.has(cleanSlug));
    })
    .sort((a, b) => {
      return (b.data.date || '').localeCompare(a.data.date || '');
    });

  return rss({
    title: "napak tilas jejak digital - my blog restoration",
    description: 'Arsip artikel blog takien.com (2006-2016)',
    site: context.site || 'https://takien.github.io',
    items: posts.map((post) => ({
      title: post.data.title,
      pubDate: post.data.date ? new Date(post.data.date) : new Date('2016-01-01'),
      description: `Artikel ${post.data.title} di takien.com`,
      link: `/${post.data.slug.replace(/^\//, '').replace(/\/$/, '')}/`,
      categories: post.data.categories || [],
    })),
    customData: `<language>id</language>`,
  });
}
