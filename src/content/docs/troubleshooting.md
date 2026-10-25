---
title: Troubleshooting
description: Fixes for connection checks that fail, uploads that stop, changed server keys and storage missing from Finder.
section: Guides
order: 5
---

Find the message or symptom you see, then follow the steps under it. If nothing here helps, see [Get help](#get-help).

## Connect stays disabled

**Connect** unlocks only when every check passes. Look at the step marked as failed and find its message below.

### "Nothing answered on port …"

The server didn't accept a connection on that port.

1. Check the port. SFTP is usually 22. Hetzner Storage Boxes use 23.
2. Check that SSH or SFTP is turned on for your account.
3. Check that a firewall on the server or your network isn't blocking the port.

### "That server name was not found."

1. Check the address for typos.
2. If you just created a Hetzner sub-account, its address can take a few minutes to appear. Wait, then choose **Retry**. Setup carries on from where it stopped.

### "The server refused the sign-in."

1. Check the user name. For SFTP it comes before the `@` in the address.
2. If you use **Key for this Mac**, make sure the public key is in `~/.ssh/authorized_keys` on the server. Choose **Copy Public Key** to copy it again.
3. If you use a key file with a passphrase, check the passphrase.

### "The server did not answer in time."

Check the address and your network, then try again. A slow VPN can cause this.

### "The folder was not found."

The folder you entered doesn't exist on the server. Check its path and spelling.

## A safe-write check fails

These messages mean the server answered, but broke a promise Syncophant needs to keep your files safe. Syncophant won't save the connection. See [Storage requirements](/docs/storage-requirements/) for what each kind of storage must support.

- **"This server replaced a file it was told to keep…"** The server overwrote a file instead of refusing. On WebDAV, the server must honour `Overwrite: F`. On S3-compatible storage, it must support `If-None-Match: *`.
- **"This server accepted a change based on an outdated version…"** The server ignores `If-Match`. Two Macs could overwrite each other's changes.
- **"This server ignores partial downloads…"** The server doesn't support range requests.
- **"This server doesn't report file versions…"** On WebDAV, the server must send strong ETags.
- **"Syncophant couldn't delete its empty test folder…"** Delete the `.syncophant-check-…` folder named in the message yourself. On WebDAV, folder deletion needs `LOCK` support.

Some providers support these features but turn them off by default, or behind a setting. Check your provider's documentation, or ask their support which of these they support.

## SMB share won't connect

1. Make sure the share **requires** SMB3 encryption and signing. Allowing them isn't enough. Syncophant never changes SMB settings.
2. When macOS asks whether Syncophant may access network volumes, allow it. If you denied it, allow it in System Settings › Privacy & Security.

## The server key changed

Syncophant shows **The server key changed**, with the key you approved next to the key the server shows now.

This can mean the server was reinstalled or its keys were rotated. It can also mean someone is intercepting the connection.

1. Don't trust the new key yet.
2. Ask your provider or server admin whether they changed the key. Get the new fingerprint from them, or from your provider's control panel.
3. If it matches the new key Syncophant shows, turn on **I checked with my provider and want to trust the new key**, then choose **Trust New Key**.

If you can't confirm the change, leave it. Syncophant won't sign in to a server whose key doesn't match.

## A file shows "Uploaded · not verified"

Syncophant couldn't work out the file's checksum on the storage.

- **On SFTP:** check that your user can run `sha256sum`. Sign in with `ssh` and run `sha256sum --version`. If it isn't found or not allowed, ask your provider to enable it.
- **Elsewhere:** try **Refresh from Storage**. If the status stays, the file may have changed on the storage while Syncophant checked it.

The file did arrive. Syncophant just won't claim it is intact without proof.

## An upload stopped

The status reads **Upload failed** followed by a reason.

1. Right-click the file in Finder and choose **Why Did It Stop?**
2. Fix the cause, for example reconnect to the network.
3. Choose **Retry Upload**.

Uploads made from the Syncophant app are queued and resume the next time the app runs.

## A file shows "Conflict copy · both kept"

The file changed in two places at once. Both versions are on your storage.

1. Right-click the file and choose **Compare Versions…**
2. Choose the version to keep, or keep both.

## Storage doesn't appear in Finder

1. In Syncophant, open the storage and choose **Add to Finder**. The connection works in the app even if this step failed.
2. In System Settings › General › Login Items & Extensions, check that Syncophant's File Provider extension is allowed.
3. If you built Syncophant yourself: Finder integration needs a build signed with your own Apple Developer team. An ad-hoc build runs the app but can't add storage to Finder. See [Source code](/docs/source-code/).

## A cloud drive asks you to sign in again

- **Google Drive, after about 7 days:** your consent screen is in **Testing**. Set its publishing status to **In production** in Google Cloud, then sign in again.
- **Any service:** you may have revoked the app, changed its secret or removed the redirect URI. Fix it in the developer console, then sign in again. See [Connect a cloud drive](/docs/connect-cloud-drive/).

## Syncophant asks you to review an interrupted operation

A move or upload stopped at a moment where Syncophant can't tell how far it got, for example if the connection dropped halfway through. Syncophant pauses changes to those files rather than guess.

1. Stop any other app or Mac that writes to this storage.
2. Look at the files on the storage. For an upload, check the original and any conflict copies.
3. Turn on **All writers are stopped, and I checked the remote files**, then continue.

## Get help

1. Open **Settings › Privacy** and choose **Save Log…** next to **Diagnostics**. The log is saved to Downloads, with host and user names removed. It is never sent anywhere.
2. Read it, and remove anything you don't want to share.
3. Open **Settings › About** and choose **Report a Problem**, or go to [GitHub issues](https://github.com/syncophant-app/macos/issues). Attach the log.

[Contributing](/docs/contributing/#report-a-problem) lists what to include.
