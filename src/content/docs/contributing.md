---
title: Contributing
description: How to report a problem, suggest a change and send a pull request to Syncophant.
section: Contribute
order: 2
---

Syncophant is built in the open, and help is welcome: bug reports, testing against storage the maintainers don't have, fixes, and docs.

## Report a problem

Open an issue on [GitHub](https://github.com/syncophant-app/macos/issues). Include:

- Your Syncophant version (**Settings › About**) and macOS version.
- The kind of storage: SFTP, Hetzner Storage Box, WebDAV, S3-compatible, SMB or a cloud drive. Name the provider or server software if you know it.
- What you did, what you expected, and what happened. Quote messages exactly.
- A diagnostics log: **Settings › Privacy › Diagnostics › Save Log…**. It removes host and user names, but read it before you attach it.

Never post passwords, keys, tokens or signed links in an issue.

### Testing against your storage

Syncophant has to work with a lot of storage the maintainers can't test. If a provider passes or fails the [safe-write check](/docs/storage-requirements/#the-safe-write-check), an issue saying so, with the exact message, is very useful.

## Suggest a change

For anything bigger than a small fix, open an issue first to describe the problem and your idea. It saves you building something that doesn't fit.

Syncophant follows a few rules that shape what changes fit:

- **Never call an upload safe without proof.** A file is verified only when its checksum matched.
- **Never lose data to resolve a conflict.** Keep both sides.
- **Trust is explicit.** Host keys are approved by the person, never accepted silently.
- **Secrets stay in Keychain.** Never in settings, logs or diagnostics.
- **No accounts, telemetry or project servers.** The app talks only to the storage the person connects, and to GitHub for updates they turn on.
- **Native and accessible.** Native controls, full keyboard use, and status in words, not only color.
- **Only claim what works.** Docs, UI and the website describe only what the app does today. Planned features aren't described as shipped.

## Send a pull request

1. Fork the repository and create a branch.
2. Set up the build: see [Source code](/docs/source-code/#build-from-source).
3. Make your change. Keep it focused on one thing.
4. Add or update tests for behavior you change. Storage changes need a test against a local fixture, never against real storage or real credentials.
5. Run the tests:

   ```sh
   bash scripts/test.sh
   ```

6. Write the commit message in [Conventional Commits](https://www.conventionalcommits.org/) style, for example `fix(sftp): retry the host-key step after DNS propagates`.
7. Open the pull request. Say what changed, why, and how you tested it.

Continuous integration builds the app and runs `scripts/test.sh` on every push and pull request.

### Licensing of contributions

Contributions are made under the license of the code they change: GPL-3.0-or-later for the app and extension, MIT for CoreKit and HetznerKit.

## Improve these docs

These pages are Markdown files in the website's `src/content/docs` folder. Each page has a `title`, a `description`, a `section` and an `order` at the top.

Keep each page to one purpose: a tutorial teaches, a guide solves one problem, reference lists facts, and an explanation says why. Use the exact words the app uses for buttons and statuses.
