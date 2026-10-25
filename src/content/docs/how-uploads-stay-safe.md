---
title: How uploads stay safe
description: Why Syncophant checks every upload, keeps both sides of a conflict, and refuses storage that can't make the same promises.
section: Explanation
order: 1
---

Most sync tools tell you a file is "synced" when they have sent it. Syncophant tells you a file is **verified** only when it has proof that the copy on your storage is the file you sent. This page explains what that proof is, and what it doesn't cover.

## Nothing replaces your file until it is complete

An upload never writes over the file you see. Syncophant first sends the data to a separate partial file on your storage. Only when every byte has arrived does it put the new file in place, using an operation the server must refuse if the destination changed in the meantime.

So an interrupted upload, a lost connection or a full disk leaves the old file as it was. You never see half a file.

Interrupted uploads resume. Before resuming, Syncophant checks the part already on the storage against your copy, so it never builds on data that changed in between.

## Verified means the checksums matched

After the file is in place, Syncophant works out its SHA256 checksum on the storage and compares it with the checksum of your copy. On SFTP the server runs `sha256sum`; on other storage Syncophant reads the file back.

The check is tied to the exact version it saw. If the file changes later, the old proof doesn't carry over to the new version.

When Syncophant can't get a checksum, it says **Uploaded · not verified**. It never shows a file as verified on a guess.

## Both sides of a conflict are kept

Two Macs, or a Mac and someone on the server, can change the same file at the same time. Syncophant writes only if the file is still the version it last saw. If it isn't, the write is refused, and Syncophant keeps both versions as a **Conflict copy · both kept**. You choose which to keep.

This is why storage must refuse stale writes. A server that quietly accepts them would let one Mac overwrite another's work without anyone noticing.

## The safe-write check proves it first

These guarantees depend on the server keeping its promises: refusing overwrites, refusing stale writes, reporting versions. Many servers do; some don't, and some only claim to.

So Syncophant doesn't trust a server's description. Before saving a connection, it tests each promise against the real server with a small test file. A server that fails isn't saved. The [Storage requirements](/docs/storage-requirements/#the-safe-write-check) page lists the steps.

## Deleting is recoverable

When you delete a file, Syncophant moves it to a recently deleted folder on your storage, where it stays for 30 days. Cloud drives use their own trash. On S3-compatible storage, Move to Trash is turned off, because S3 has no safe way to move a file.

## What this doesn't protect against

- **A server that lies.** Syncophant can test a server, but it can't stop a malicious server from breaking its own rules later.
- **Losing your only copy.** Verified uploads aren't backups. Keep another copy of anything you can't lose, especially while Syncophant is an early build.
- **Google Drive conflicts.** Google Drive can't refuse stale writes, so Syncophant checks in the app. A change made elsewhere at the same moment can still be lost or duplicated. That is why it is marked Experimental.

## Where your secrets are

Passwords, keys and tokens are saved only in your Keychain. They never go into settings files, logs or diagnostics. Syncophant has no server and no account: your Mac talks straight to your storage.
