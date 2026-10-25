// @ts-check
import { defineConfig } from "astro/config";

// Static site. No integrations, no client-side framework, no analytics.
export default defineConfig({
  site: "https://syncophant.app",
  build: {
    // Keep CSS in external files so the page stays cacheable.
    inlineStylesheets: "never",
  },
});
