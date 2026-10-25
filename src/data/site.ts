// Site-wide facts. Everything here should stay true: the design system says
// never to claim what the app can't back up today.

export const links = {
  repo: "https://github.com/syncophant-app/macos",
  releases: "https://github.com/syncophant-app/macos/releases/latest",
  license: "https://github.com/syncophant-app/macos/blob/main/LICENSE",
  status: "https://github.com/syncophant-app/macos/blob/main/docs/STATUS.md",
} as const;

export const site = {
  name: "Syncophant",
  url: "https://syncophant.app",
  tagline: "Remote storage that feels local.",
  description:
    "Syncophant puts your SFTP server, WebDAV, S3-compatible storage or SMB share in Finder. Free and open source, with no account and no telemetry.",
  requirement: "macOS 26 or later",
  /** 1200×630 social card in public/. */
  ogImage: "/og.png",
  ogImageAlt: "Syncophant: remote storage that feels local. A Finder window with remote storage and a status for every file.",
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

/** The FAQ on the page, also published as FAQPage structured data. */
export const questions = [
  {
    q: "Which storage does it work with?",
    a: "SFTP servers, WebDAV, S3-compatible object storage and SMB shares. That covers most NAS devices, VPSs and hosted storage. Hetzner Storage Boxes also get a guided setup.",
  },
  {
    q: "What does my server need?",
    a: "SFTP needs SSH access and permission to run sha256sum. WebDAV and S3-compatible storage need HTTPS. SMB shares must require SMB3 encryption and signing. Without a checksum, Syncophant won't call an upload verified.",
  },
  {
    q: "Do my files take up space on my Mac?",
    a: "Only the ones you open or keep. Everything else stays on your storage and shows in Finder without using disk space. The cache is 5 GB per storage by default, and it never drops a file that hasn't finished uploading.",
  },
  {
    q: "Does it work when the app is closed?",
    a: "Yes. Your storage stays in Finder after you quit the menu bar app.",
  },
  {
    q: "Where are my passwords and keys kept?",
    a: "In your Keychain. They never go into settings files, logs or diagnostics.",
  },
  {
    q: "Can anyone else see my files?",
    a: "Syncophant connects your Mac straight to your storage. There's no Syncophant server in between and no account to sign in to.",
  },
  {
    q: "Is it really free?",
    a: "Yes. The app is GPL-3.0-or-later and its storage libraries are MIT. There are no paid plans.",
  },
  {
    q: "Can I trust it with my only copy of something?",
    a: "Not yet. Syncophant is an early build. Keep another copy of anything you can't lose.",
  },
  {
    q: "Which Macs does it run on?",
    a: "Macs with macOS 26 or later.",
  },
];
