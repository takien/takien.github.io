import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

const posts = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/posts' }),
  schema: z.object({
    title: z.string(),
    date: z.string().optional().default(''),
    categories: z.array(z.string()).default([]),
    tags: z.array(z.string()).default([]),
    slug: z.string(),
    format: z.string().optional().default('post'),
    type: z.string().optional(),
    legacyUrl: z.string().optional(),
    legacyUrls: z.array(z.string()).optional().default([]),
    source: z.string().optional(),
    author: z.string().optional(),
    group: z.string().optional(),
    nowNote: z.string().optional(),
    nowDate: z.string().optional(),
    isTimeline: z.boolean().optional().default(false),
    isFresh: z.boolean().optional().default(false),
    comments: z.array(z.object({
      author: z.string(),
      date: z.string().optional().default(''),
      text: z.string(),
    })).default([]),
  }),
});

export const collections = { posts };
