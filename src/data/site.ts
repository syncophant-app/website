// Site-wide facts. Everything here should stay true: the design system says
// never to claim what the app can't back up today.

export const links = {
  repo: "https://github.com/syncophant/macos",
  releases: "https://github.com/syncophant/macos/releases/latest",
  license: "https://github.com/syncophant/macos/blob/main/LICENSE",
  status: "https://github.com/syncophant/macos/blob/main/docs/STATUS.md",
} as const;

export const site = {
  name: "Syncophant",
  url: "https://syncophant.app",
  tagline: "Remote storage that feels local.",
  description:
    "Syncophant puts your Hetzner Storage Box or SFTP server in Finder. Free and open source, with no account and no telemetry.",
  requirement: "macOS 26 or later",
} as const;

/**
 * File states. These are the only words the product uses for them
 * (design system, Voice and content). The glyph is a web stand-in for the
 * SF Symbol the app shows.
 */
export const fileStates = {
  remote: { words: "On your box", glyph: "cloud" },
  uploading: { words: "Uploading 42%", glyph: "uploading" },
  verifying: { words: "Verifying on your box", glyph: "verifying" },
  verified: { words: "On your box · verified", glyph: "verified" },
  unverified: { words: "Uploaded · not verified", glyph: "unverified" },
  conflict: { words: "Conflict copy · both kept", glyph: "conflict" },
  kept: { words: "Kept on this Mac", glyph: "pinned" },
  failed: { words: "Upload failed · storage unreachable", glyph: "failed" },
} as const;

export type FileState = keyof typeof fileStates;
