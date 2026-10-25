import { defineCollection } from "astro:content";
import { glob } from "astro/loaders";
import { z } from "astro/zod";
import { docSections } from "./data/docs";

const docs = defineCollection({
  loader: glob({ pattern: "**/*.md", base: "./src/content/docs" }),
  schema: z.object({
    title: z.string(),
    description: z.string(),
    section: z.enum(docSections),
    /** Position inside its section. Lower comes first. */
    order: z.number(),
  }),
});

export const collections = { docs };
