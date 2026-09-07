import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';
import { adminApiMiddleware } from './scripts/admin-api.mjs';

import fs from 'node:fs';
import path from 'node:path';

function adminApiPlugin() {
  return {
    name: 'takien-admin-api-plugin',
    configureServer(server) {
      // Endpoint API admin lokal
      server.middlewares.use('/api/admin', adminApiMiddleware);

      // Sajikan halaman panel admin hanya di dev server lokal
      server.middlewares.use((req, res, next) => {
        const url = req.url || '';
        if (url === '/admin' || url === '/admin/' || url.startsWith('/admin/?') || url.startsWith('/admin?')) {
          const adminHtmlPath = path.resolve('./scripts/local-admin/admin.html');
          if (fs.existsSync(adminHtmlPath)) {
            res.setHeader('Content-Type', 'text/html; charset=utf-8');
            return res.end(fs.readFileSync(adminHtmlPath, 'utf-8'));
          }
        }
        next();
      });
    }
  };
}

// https://astro.build/config
export default defineConfig({
  site: 'https://takien.github.io',
  integrations: [sitemap()],
  vite: {
    plugins: [adminApiPlugin()]
  },
  markdown: {
    shikiConfig: {
      theme: 'github-dark-dimmed',
      wrap: true,
    }
  }
});
