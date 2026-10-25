---
title: Source code
description: Where the code lives, how it is organized and licensed, and how to build and run Syncophant from source.
section: Contribute
order: 1
---

Syncophant is free and open source. The code is at [github.com/syncophant-app/macos](https://github.com/syncophant-app/macos).

## Licenses

| Part | License |
| --- | --- |
| The app and its File Provider extension | GPL-3.0-or-later |
| CoreKit and HetznerKit, the reusable storage libraries | MIT |

Bundled libraries keep their own licenses. SMB support uses AMSMB2 and libsmb2 under LGPL 2.1. Each release includes their source, notices and instructions to rebuild against a modified copy; see `docs/REBUILDING.md`.

## How the code is organized

| Folder | What it holds |
| --- | --- |
| `Sources/CoreKit` | Storage drivers (local, SFTP, WebDAV, S3, SMB, cloud drives), verified transfers, SQLite metadata. No UI. |
| `Sources/HetznerKit` | The Hetzner API client used for Storage Box setup, snapshots and sharing. |
| `Sources/SyncophantApp` | The SwiftUI and AppKit app: window, menu bar, setup, settings. |
| `Sources/FileProviderExtension` | The Finder integration. It runs the storage engine, so files work when the app is closed. |
| `Sources/PlatformShared` | Code built into both the app and the extension: Keychain, app-group settings, cache policy. |
| `scripts/` | Bootstrap, build, test, packaging and signing scripts, plus self-checks and fixtures. |
| `docs/` | Status, architecture, protocol notes and the product plan. |

Start with these documents in the repository:

- `docs/STATUS.md`: what is implemented, what has been verified, and which release checks are still open.
- `docs/INTEGRATION.md`: architecture and how the parts fit together.
- `docs/STORAGE_PROTOCOLS.md`: the guarantees and limits of each storage driver.
- `Sources/CoreKit/README.md`: the storage library's public contract.

## Build from source

You need macOS 26 or later, Xcode with the macOS 26 SDK or newer, Go, CMake, pkg-config, and Ruby with the `xcodeproj` gem.

1. Install the tools:

   ```sh
   brew install go cmake pkg-config ruby
   gem install xcodeproj --no-document
   ```

2. Build the pinned SSH and OpenSSL libraries. This downloads checksum-pinned sources and keeps the built libraries in `.deps/`:

   ```sh
   bash scripts/bootstrap.sh
   ```

3. Build and open the app:

   ```sh
   bash scripts/build.sh
   open build/DerivedData/Build/Products/Debug/Syncophant.app
   ```

The app doesn't use Homebrew libraries at runtime. Go builds the bundled encryption helper and isn't needed to run the app.

### Try it without storage

Demo mode opens the app with clearly labeled sample files. It connects to nothing and saves nothing:

```sh
open -n build/DerivedData/Build/Products/Debug/Syncophant.app --args --demo
```

### Add Finder integration

The default build is ad-hoc signed. It runs the app, but it can't add storage to Finder. For that, the app and extension need matching signing and provisioning:

1. Open `Syncophant.xcodeproj` and choose your Apple Developer team for both targets.
2. Register the bundle IDs, app group and Keychain group with your team, or change them consistently to your own. `docs/REBUILDING.md` lists every place they appear.
3. Build with your team ID:

   ```sh
   SYNCOPHANT_TEAM_ID=YOURTEAMID bash scripts/build.sh
   ```

A build you sign yourself isn't an official release. Don't present it as one.

### After adding source files

Regenerate the Xcode project:

```sh
ruby scripts/generate-project.rb
```

## Run the tests

```sh
bash scripts/test.sh
```

This runs the Swift tests and the self-checks. Other suites start local, throwaway servers and never touch real storage:

| Command | What it tests |
| --- | --- |
| `bash scripts/integration/sftp.sh` | SFTP against a temporary OpenSSH server on loopback. |
| `sh scripts/test-smb-fixture.sh` | SMB against a temporary Samba container. Needs port 445 free. |
| `bash scripts/integration/crypt.sh` | The encryption helper. |

See [Contributing](/docs/contributing/) before you send a change.
