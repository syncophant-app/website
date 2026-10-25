---
title: Connect a Hetzner Storage Box
description: Use a Hetzner API token to give this Mac its own sub-account, an SSH key and snapshot access, with no password to type.
section: Guides
order: 1
---

This guide sets up a Hetzner Storage Box with an API token. With the token, Syncophant can create a sub-account for this Mac, turn on SSH, show snapshots and add a key, so you don't type a password.

You need a Hetzner Storage Box and access to the Hetzner Console project that holds it.

If you prefer not to use a token, connect the box as an SFTP server instead. Paste its address (`u123456.your-storagebox.de`) in **Add Storage** and follow [Connect an SFTP server](/docs/connect-sftp-server/). Port 23 is the box's SFTP port.

## Create an API token

1. Open Hetzner Console and pick the project with your Storage Box.
2. Go to **Security**, then **API tokens**, and choose **Generate API token**.
3. Choose **Read and Write**, then copy the token.

Syncophant sends the token only to `api.hetzner.com`, and saves it in your Keychain.

## Set up the box

1. In Syncophant, choose **Add Storage** and paste the token. Syncophant shows **Works. Found 1 Storage Box.** (or the number it found).
2. Under **Which Storage Box?**, pick the box this Mac should use.
3. Give the storage a name and a color. Both show in Finder and the menu bar.
4. Review the plan. Each item is on by default and you can turn any off:
   - **Give this Mac its own sub-account**: this Mac can see only one folder on the box. If the Mac is lost, revoke that one sub-account in Hetzner.
   - **Sign in with a key made for this Mac**: turns on SSH and keeps the private key in your Keychain.
   - **Show snapshots in Time Travel**: makes the snapshot folder visible so you can browse old versions.
   - **Prove it works with a 1 MB test**: uploads, reads back and compares a small file, then deletes it.
5. Check the folder name. The default is `Syncophant`. With a sub-account, this Mac sees only that folder.
6. Choose **Set Up This Mac**. Nothing changes on your box before you do.

Syncophant runs each step and shows its progress: creating the sub-account, turning on SSH, checking the box's fingerprint, adding this Mac's key, testing safe reads and writes, saving the sign-in, and adding the storage to Finder.

## Use the whole box instead

To give this Mac the whole box, turn off **Give this Mac its own sub-account**. Syncophant then signs in with the main account and asks for its password once. A sub-account is safer: a lost or compromised Mac can then reach only its own folder.

## If a step fails

- **The box's fingerprint can't be checked right after setup.** A new sub-account's address can take a few minutes to appear in DNS. Wait, then choose **Retry**. Setup carries on from where it stopped; you don't need to start again.
- **The token doesn't work.** Make sure it has **Read and Write** permission and belongs to the project that holds the box.

For other problems, see [Troubleshooting](/docs/troubleshooting/).

## Undo the setup

You can remove the storage from **Settings › Storage**. To remove the sub-account itself, delete it in Hetzner Console. The rest of the box is not affected.

To forget the API token, go to **Settings › Privacy** and choose **Forget Token**. Snapshots, sharing and the space-used display need the token; file access does not.
