---
title: Connect an SFTP server
description: Add any server you can SSH into, approve its host key, and choose how this Mac signs in.
section: Guides
order: 2
---

This guide connects a server you can reach with SSH: a VPS, a NAS, rsync.net, or a Storage Box without the API token setup.

Before you start, check that the server meets the [SFTP requirements](/docs/storage-requirements/#sftp). In short: SFTP must be on, and your user must be allowed to run `sha256sum`.

## Enter the address

1. Choose **Add Storage**.
2. Paste the address as `user@host`, `user@host:port` or `sftp://user@host:port`. The default port is 22.
3. Optionally, set the folder on the server. Syncophant shows only that folder and what is inside it.

If your `~/.ssh/config` has a `Host` entry for this server, Syncophant reads the host name, user, port and key file from it. It only reads the file; it never changes it.

## Choose how to sign in

| Option | What it does |
| --- | --- |
| **Key for this Mac** (recommended) | Syncophant makes a new Ed25519 key and keeps it in your Keychain. Choose **Copy Public Key** and add it to the server's `~/.ssh/authorized_keys`, or enter the server password once and Syncophant adds the key for you. |
| **Key from ~/.ssh** | Uses a private key file you already have. Syncophant copies it into your Keychain after sign-in. |
| **SSH agent** | Uses an agent such as 1Password or Secretive. Enter its socket path. Your agent may ask you to approve each connection. Finder can reach the agent only while the Syncophant app is running. |
| **Password** | Works, but a key is safer and doesn't expire. You can switch later in Settings. |

## Approve the host key

The first time you connect, Syncophant shows the server's host key as a picture and as SHA-256 text.

1. Get the server's fingerprint from a source you trust: your provider's control panel, or by running `ssh-keygen -lf /etc/ssh/ssh_host_ed25519_key.pub` on the server.
2. Compare it with what Syncophant shows.
3. If they match, choose **Trust This Key**.

Syncophant pins this key and checks it before every sign-in. If it ever changes, Syncophant stops and shows both keys side by side. See [The server key changed](/docs/troubleshooting/#the-server-key-changed).

## Finish

Syncophant runs the last checks: **Sign in**, then **Test safe reads and writes**. When every check passes, choose **Connect**. The storage is saved to your Keychain and added to Finder.
