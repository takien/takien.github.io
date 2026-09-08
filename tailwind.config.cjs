/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}',
    './src/content/**/*.{md,markdown}'
  ],
  darkMode: ['selector', '[data-theme="dark"]'],
  corePlugins: {
    preflight: false, // Pertahankan base style, typography, dan reset yang ada di global.css
  },
  theme: {
    extend: {
      colors: {
        accent: 'var(--accent)',
        'accent-hover': 'var(--accent-hover)',
        'bg-primary': 'var(--bg-primary)',
        'bg-secondary': 'var(--bg-secondary)',
        'bg-card': 'var(--bg-card)',
        'text-primary': 'var(--text-primary)',
        'text-secondary': 'var(--text-secondary)',
        'text-muted': 'var(--text-muted)',
        border: 'var(--border)',
      },
      typography: {
        DEFAULT: {
          css: {
            '--tw-prose-body': 'var(--text-primary)',
            '--tw-prose-headings': 'var(--text-primary)',
            '--tw-prose-lead': 'var(--text-secondary)',
            '--tw-prose-links': 'var(--accent)',
            '--tw-prose-bold': 'var(--text-primary)',
            '--tw-prose-counters': 'var(--text-muted)',
            '--tw-prose-bullets': 'var(--text-muted)',
            '--tw-prose-hr': 'var(--border)',
            '--tw-prose-quotes': 'var(--text-secondary)',
            '--tw-prose-quote-borders': 'var(--accent)',
            '--tw-prose-captions': 'var(--text-muted)',
            '--tw-prose-code': 'var(--text-primary)',
            '--tw-prose-pre-code': 'var(--text-primary)',
            '--tw-prose-pre-bg': 'var(--bg-secondary)',
            '--tw-prose-th-borders': 'var(--border)',
            '--tw-prose-td-borders': 'var(--border)',
            color: 'var(--text-primary)',
            maxWidth: 'none',
            h1: {
              fontWeight: '800',
              letterSpacing: '-0.025em',
              marginBottom: '0.5rem',
            },
            h2: {
              fontWeight: '700',
              letterSpacing: '-0.015em',
              borderBottomWidth: '1px',
              borderBottomColor: 'var(--border)',
              paddingBottom: '0.4rem',
            },
            h3: {
              fontWeight: '600',
              letterSpacing: '-0.015em',
            },
          },
        },
      },
    },
  },
  plugins: [
    require('@tailwindcss/typography'),
  ],
};
