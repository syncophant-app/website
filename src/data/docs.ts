import type { CollectionEntry } from "astro:content";

/** Sidebar groups, in order. Each docs page names one of them in its frontmatter. */
export const docSections = ["Get started", "Guides", "Reference", "Explanation", "Contribute"] as const;

/** Docs in reading order: by section, then by `order` inside it. */
export function sortDocs(entries: CollectionEntry<"docs">[]) {
  return entries.toSorted(
    (a, b) =>
      docSections.indexOf(a.data.section) - docSections.indexOf(b.data.section) || a.data.order - b.data.order,
  );
}
