import type { APIRoute } from "astro";
import { getCollection } from "astro:content";

// Built from the docs collection so new pages are listed without editing this file.
export const GET: APIRoute = async ({ site }) => {
  const paths = ["/", "/docs/", ...(await getCollection("docs")).map((d) => `/docs/${d.id}/`)];
  const urls = paths.map((p) => `  <url><loc>${new URL(p, site)}</loc></url>`).join("\n");
  return new Response(
    `<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n${urls}\n</urlset>\n`,
    { headers: { "Content-Type": "application/xml" } },
  );
};
