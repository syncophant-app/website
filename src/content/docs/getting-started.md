---
title: Get started
description: Install Syncophant, connect your first storage, and upload a file you can see verified in Finder.
section: Get started
order: 1
---

In this tutorial you install Syncophant, connect one storage, and upload a file. At the end, the file shows **On your box · verified** in Finder, and you know what each step did.

It takes about ten minutes. You need:

- A Mac with macOS 26 or later.
- Storage you can sign in to: an SFTP server, a Hetzner Storage Box, WebDAV, S3-compatible storage, an SMB share, or a cloud drive. If you are not sure what your storage needs, read [Storage requirements](/docs/storage-requirements/) first.

> Syncophant is an early build. Use a test folder for this tutorial, and keep another copy of anything you can't lose.

## 1. Install the app

Download `Syncophant.dmg` from the [latest release](https://github.com/syncophant-app/macos/releases/latest), open it, and drag Syncophant to Applications.

Or, on an Apple silicon Mac, install it with Homebrew:

```sh
brew install --cask syncophant-app/tap/syncophant
```

Open Syncophant from Applications. Its icon appears in the menu bar and its window opens. With nothing connected yet, the window says **Connect your storage to start**.

## 2. Add your storage

1. Choose **Add Storage**.
2. Paste anything that points at your storage: a server address such as `user@example.com`, a URL that starts with `https://`, `s3://` or `smb://`, a Storage Box address such as `u123456.your-storagebox.de`, or a Hetzner API token.

Syncophant works out the type from what you paste and tells you what it needs next. If it can't, pick a type under **Or choose a type**.

For your storage type, the guides have the details:

- [Connect a Hetzner Storage Box](/docs/connect-hetzner-storage-box/)
- [Connect an SFTP server](/docs/connect-sftp-server/)
- [Connect a cloud drive](/docs/connect-cloud-drive/)

## 3. Let the checks run

Before anything is saved, Syncophant checks the connection. For an SFTP server you see:

1. **Reach the server**
2. **Confirm its fingerprint**: compare the picture and the SHA-256 text with what your provider publishes, then choose **Trust This Key**.
3. **Sign in**
4. **Test safe reads and writes**: Syncophant writes a 1 MB test file in a new folder, reads it back, checks that the server refuses to overwrite it, and deletes the folder.

**Connect** unlocks when every check passes. Choose it. Syncophant saves the sign-in to your Keychain and adds the storage to Finder.

If a check fails, the step says what went wrong. [Troubleshooting](/docs/troubleshooting/) has fixes for the common ones.

## 4. Open your storage in Finder

Open a Finder window. Your storage is in the sidebar, under its name.

The files you see there take no space on your Mac yet. Each one shows **On your box**: it is on your storage, and Syncophant downloads it when you open it.

## 5. Upload a file

Drag a small file from your Desktop into the storage in Finder. Watch its status:

1. **Uploading 42%**: the file is being sent.
2. **Verifying on your box**: Syncophant works out the file's SHA256 checksum on your storage and compares it with your copy.
3. **On your box · verified**: the checksums match. The file on your storage is exactly the file you sent.

You can also upload with **Upload Files…** in the app, or by dropping files on the menu bar icon.

## What you did

- You installed Syncophant and connected one storage. Its password or key is in your Keychain, nowhere else.
- Syncophant proved the server can store files safely before it saved the connection.
- You uploaded a file and saw Syncophant prove it arrived intact.

## Next steps

- [File status](/docs/file-status/) explains every status a file can show.
- [How uploads stay safe](/docs/how-uploads-stay-safe/) explains verification and conflict copies.
- To keep a file on your Mac when you're offline, right-click it in Finder and choose **Keep Downloaded**.
