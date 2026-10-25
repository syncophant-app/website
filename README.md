# syncophant.app

The Syncophant landing page. Astro, static output, no client-side JavaScript, no analytics and no third-party requests: Onest is served from `public/fonts/`.

```sh
cd website
npm install
npm run dev       # http://localhost:4321
npm run build     # static site in dist/
```

The scripts set `ASTRO_TELEMETRY_DISABLED=1`, so building the site sends nothing to Astro either.

## Design

Built from the Syncophant design system (brand kit artifact and `DESIGN.md`), in monochrome:

- **Colour:** `ink`, `paper`, `mist`, `ink-muted` and `line` only, with the design system's light and dark values. Syncophant Blue, the coloured light field (sky, lavender, ember) and the status hues are left out on purpose. File status is carried by a glyph and the exact status words, which the design system requires anyway.
- **Type:** Onest (variable, OFL) for everything on the page; the system font inside the app mock-ups, as in the app; system monospace for hosts, fingerprints and checksums.
- **Material:** glass only where it floats (the navigation capsule, the menu bar panel) over a monochrome light field; paper for anything you read.
- **Logo:** mark and lockup paths are copied verbatim into `src/data/brand.ts`. Small cut below 48px, regular cut above. They take `currentColor`.

Tokens live in `src/styles/tokens.css`. Dark mode follows the system and can be forced with `data-theme="dark"` or `"light"` on `<html>`.

## Before launch

- Replace the drawn Finder window, menu bar panel and feature fragments with real screenshots of the app. The design system shows the product only in real screenshots; the drawings use real status wording but sample files.
- Point the download buttons at the release you want (`src/data/site.ts`; currently GitHub's latest release).
- Add an Open Graph image (the brand kit's `social-card-*` art, or a monochrome version of it).
- Re-check every claim against `docs/STATUS.md`. WebDAV, S3 and SMB are described as "in early testing".

## Structure

```
src/
  data/brand.ts        mark and lockup geometry
  data/site.ts         links, tagline, the file-state vocabulary
  styles/tokens.css    design tokens (light and dark)
  styles/global.css    base, type scale, glass, buttons, layout
  components/          Nav, Hero, FinderWindow, MenuBarPanel, Status, Icon, Mark, Lockup, Footer
  components/sections/ WhatItIs, HowItWorks, FileStates, Features, Privacy, WorksWith, Cta, Faq
  pages/index.astro
```
