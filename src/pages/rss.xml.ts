import rss from '@astrojs/rss';
import { getCollection } from 'astro:content';

export async function GET(context: any) {
  const posts = (await getCollection('posts')).sort((a, b) => {
    return (b.data.date || '').localeCompare(a.data.date || '');
  });

  return rss({
    title: "takien.com • don't cover a judge by its book",
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
