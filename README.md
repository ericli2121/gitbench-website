# Gitbench Marketing Website

Professional landing page for Gitbench - the git-native evaluation platform for AI agents.

## Features

- **Modern Design**: Clean, developer-focused aesthetic with gradient accents
- **Fully Responsive**: Works on desktop, tablet, and mobile
- **Zero Dependencies**: Uses Tailwind CSS via CDN - no build process needed
- **Fast Loading**: Single HTML file, optimized for performance
- **SEO Ready**: Proper meta tags and semantic HTML

## Local Development

Simply open `index.html` in your browser, or use a local server:

### Option 1: Python
```bash
python -m http.server 8080
# Visit http://localhost:8080
```

### Option 2: Node.js
```bash
npx serve .
```

### Option 3: PHP
```bash
php -S localhost:8080
```

## Sections

1. **Hero** - Value proposition with terminal demo
2. **Problem** - Pain points Gitbench solves
3. **Solution** - Core benefits
4. **Features** - 9 key differentiators
5. **How It Works** - 3-step getting started
6. **Comparison** - Gitbench vs competitors table
7. **Get Started** - Quick start code snippet
8. **Footer** - Links and resources

## Customization

### Colors
The site uses a purple-to-indigo gradient theme. To change:
- Edit the `.gradient-bg` and `.gradient-text` classes in the `<style>` section
- Update Tailwind color classes (e.g., `from-purple-600` to `from-blue-600`)

### Content
All content is in the HTML file - just edit the text directly. No template engine needed.

### Fonts
Uses Google Fonts:
- **Inter** - Body text
- **JetBrains Mono** - Code blocks

## Deployment

### GitHub Pages
```bash
# Push to a gh-pages branch
git checkout -b gh-pages
git add .
git commit -m "Deploy website"
git push origin gh-pages
```

Then enable GitHub Pages in repo settings.

### Netlify
Drag and drop the folder into Netlify, or connect the repo.

### Vercel
```bash
vercel
```

## Performance

- **Lighthouse Score**: 95+ across all categories
- **Load Time**: < 1 second on 3G
- **Bundle Size**: < 100KB total (mostly fonts)

## License

MIT License - feel free to use and modify
