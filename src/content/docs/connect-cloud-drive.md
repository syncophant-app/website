---
title: Connect a cloud drive
description: Create your own app in the Dropbox, OneDrive, Box or Google Drive developer console, then sign in from Syncophant.
section: Guides
order: 3
---

Syncophant can use Dropbox, OneDrive, Box and Google Drive. It ships no app keys of its own, so each person creates an app in the service's developer console. That way, your sign-in goes from your Mac to the service, through an app only you control.

This takes about five minutes per service, once.

## Before you start

- Google Drive support is **Experimental**. Google Drive allows several items with the same name in one folder, and it can't refuse a stale write. Syncophant does those checks itself, so a change made elsewhere at the same moment can be lost or duplicated. Google Docs aren't files and are skipped.
- Every service uses the same redirect URI:

```text
http://localhost:53682/
```

## 1. Create the app

In Syncophant, choose **Add Storage**, then **Cloud drive**, then your service. Syncophant shows the same steps as below and a button that opens the console.

### Dropbox

1. In the [Dropbox App Console](https://www.dropbox.com/developers/apps), create a **Scoped access** app with **Full Dropbox** access.
2. Under **Permissions**, turn on `files.metadata.write`, `files.content.write`, `files.content.read` and `account_info.read`.
3. Add the redirect URI, then copy the **App key**.

### OneDrive

1. In [Microsoft Entra app registrations](https://entra.microsoft.com/#view/Microsoft_AAD_RegisteredApps/ApplicationsListBlade), register an app for personal and work accounts.
2. Add a **Mobile and desktop** redirect URI with the address above, and allow public client flows.
3. Copy the **Application (client) ID**.

### Box

1. In the [Box Developer Console](https://app.box.com/developers/console), create a **Custom App** with **User Authentication (OAuth 2.0)**.
2. Turn on **Write all files and folders**, and add the redirect URI.
3. Copy the **Client ID** and **Client Secret**.

### Google Drive

1. In [Google Cloud credentials](https://console.cloud.google.com/apis/credentials), enable the Google Drive API and create an OAuth client of type **Desktop app**.
2. Set the consent screen's publishing status to **In production**. In **Testing**, sign-ins expire after 7 days.
3. Copy the **Client ID** and **Client secret**.

## 2. Sign in

1. Paste the client ID, and the client secret for Box or Google Drive.
2. Choose **Sign In**. Your browser opens the service's sign-in page.
3. Approve access. The browser hands the sign-in back to Syncophant on `localhost`, a listener only your Mac can reach.
4. Syncophant runs its checks, including **Test safe reads and writes**. When they pass, choose **Connect**.

Your client ID, secret and tokens are saved together in your Keychain.

## Good to know

- Deleting a file sends it to the service's own trash, so you can restore it there.
- If sign-in stops working, see [A cloud drive asks you to sign in again](/docs/troubleshooting/#a-cloud-drive-asks-you-to-sign-in-again).
