---
title: Storage requirements
description: What each kind of storage must support before Syncophant connects to it, and the limits that apply.
section: Reference
order: 2
---

Syncophant only connects to storage that can keep your files safe. Every new connection runs a safe-write check against the real server before it can be saved. See [The safe-write check](#the-safe-write-check) below.

## SFTP

Includes Hetzner Storage Boxes and rsync.net.

- **SSH with SFTP.** Any port. Storage Boxes use port 23.
- **`sha256sum`.** Your user must be allowed to run it over SSH. Without it, uploads show **Uploaded · not verified**.
- **A host key you can check.** Syncophant pins the key before signing in and refuses a changed key.
- **Recommended:** a dedicated user or sub-account limited to one folder (a chroot). SFTP can't stop someone else on the server from swapping folders while Syncophant works; a server-side limit can.
- **Faster with:** GNU or BSD `stat`. Without it, Syncophant uses checksums to tell when files changed, which is slower.

Sign-in can use a key made for this Mac, your own key file, an SSH agent, or a password.

## WebDAV

Includes Nextcloud, pCloud, Koofr and kDrive.

- **HTTPS** with a valid certificate. Plain HTTP and redirects are refused.
- **Strong ETags** on files. Weak or missing ETags are refused.
- **Range requests**, answered with `206 Partial Content`.
- **Conditional requests:** `If-Match` and `If-None-Match`, and `MOVE` with `Overwrite: F`.
- **Locking** (`LOCK` with depth infinity) to delete folders. Without it, folders can't be deleted.

Moving a whole folder isn't supported on WebDAV.

## S3-compatible

Includes AWS, Cloudflare R2, Backblaze B2, Hetzner Object Storage and Wasabi.

- **HTTPS.** Path-style endpoints are supported. Bucket, region and folder prefix are separate fields.
- **Conditional writes:** `If-None-Match: *` and `If-Match` on uploads and multipart completion.
- **Range requests.**
- An access key and secret. Session tokens are supported.

Limits:

- Rename and **Move to Trash** are turned off. S3 has no safe rename, so Syncophant copies and keeps the original instead.
- Files over 64 MiB upload in parts. If an upload is interrupted, unfinished parts can stay on the server. Set a lifecycle rule on the bucket to expire incomplete multipart uploads.
- The largest file is 5 TiB.

## SMB

Includes most NAS devices, another Mac and Azure Files.

- **SMB3 with encryption and signing required** by the share. Older or unencrypted shares are refused. Syncophant never changes your Mac's or the server's SMB settings.
- macOS must allow Syncophant to access network volumes. Allow it when macOS asks.
- **Recommended:** a dedicated share for Syncophant, so the server enforces the boundary.

## Cloud drives

Each cloud drive needs an app you create in its developer console. See [Connect a cloud drive](/docs/connect-cloud-drive/).

| Service | Won't overwrite on create | Refuses stale writes | Safe moves |
| --- | --- | --- | --- |
| Dropbox | On the server | On the server | On the server |
| OneDrive | On the server | On the server | On the server |
| Box | On the server | On the server | On the server |
| Google Drive (Experimental) | Checked by Syncophant | Checked by Syncophant | Checked by Syncophant |

Because Google Drive can't enforce these on the server, a change made elsewhere at the same moment can be lost or duplicated. Google Docs are skipped.

## The safe-write check

Before a connection is saved, Syncophant creates a folder named `.syncophant-check-…` at the top of the storage and:

1. Writes 1 MiB and reads it back.
2. Reads a range from the middle of the file.
3. Checks the server reports a version for the file.
4. Tries to publish another file over it. The server must refuse.
5. Tries a create-only write and a write based on a made-up version. The server must refuse both.
6. Where the storage supports it, replaces the file using its current version.
7. Deletes the folder.

If any step fails, the connection isn't saved, and Syncophant says which promise the server broke. See [Troubleshooting](/docs/troubleshooting/#a-safe-write-check-fails).
