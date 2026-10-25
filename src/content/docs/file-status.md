---
title: File status
description: Every status a file can show in Finder and in Syncophant, what it means, and what you can do about it.
section: Reference
order: 1
---

Syncophant shows the same words in Finder, in its window and in the menu bar. A status is always shown as words and a symbol, never color alone.

## Statuses

| Status | Meaning | What you can do |
| --- | --- | --- |
| **On your box** | The file is on your storage. It takes no space on your Mac until you open it. | Open it to download it, or choose **Keep Downloaded** to keep a copy here. |
| **Uploading 42%** | The file is being sent. The number is the share sent so far. | Wait, pause or cancel from the transfer queue. Cancelling keeps your copy. |
| **Verifying on your box** | The upload finished. Syncophant is comparing the SHA256 checksum on your storage with your copy. | Wait. This is usually quick. |
| **On your box · verified** | The checksums matched. The file on your storage is exactly the file you sent. | Nothing to do. |
| **Uploaded · not verified** | The file arrived, but Syncophant couldn't work out its checksum on the storage, so it makes no claim that the copy is intact. | Check the [storage requirements](/docs/storage-requirements/). On SFTP, the server must let you run `sha256sum`. |
| **Conflict copy · both kept** | The file changed in two places at once. Syncophant kept both versions instead of choosing one. | Right-click and choose **Compare Versions…**, then keep the one you want. |
| **Kept on this Mac** | You chose to keep this file downloaded. It is never removed to save space. | Choose **Stop Keeping Downloaded** to let Syncophant manage it again. |
| **Upload failed · storage unreachable** | The upload stopped. The part after the dot says why. | Right-click and choose **Why Did It Stop?** or **Retry Upload**. |

## Finder actions

Right-click a file or folder in a Syncophant storage to see these actions. Each one appears only when it applies.

| Action | Shown when |
| --- | --- |
| **Keep Downloaded** | The item is on your storage and not kept yet. |
| **Stop Keeping Downloaded** | The item is kept. |
| **Retry Upload** | Every selected item failed to upload. |
| **Why Did It Stop?** | One item failed to upload. |
| **Compare Versions…** | One item has a conflict copy. |
| **Browse Versions…** | One item has earlier versions, for example in snapshots. |
| **Share…** | One item can be shared from this storage. |
| **Copy Path** | Always. |
| **Open in Terminal** | Always. |
| **Refresh from Storage** | Always. Asks the storage for the latest listing. |

macOS also adds **Remove Download**, which frees the space a downloaded file uses without removing it from your storage.
