import { getCollection } from 'astro:content';

export async function GET() {
  const posts = await getCollection('posts');
  const searchData = posts.map((post) => ({
    title: post.data.title,
    slug: `/${post.data.slug.replace(/^\//, '').replace(/\/$/, '')}/`,
    date: post.data.date ? post.data.date.slice(0, 10) : '',
    categories: post.data.categories || [],
    tags: post.data.tags || [],
  }));

  return new Response(JSON.stringify(searchData), {
    headers: {
      'Content-Type': 'application/json',
    },
  });
}
