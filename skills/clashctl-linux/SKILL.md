---
name: clashctl-linux
description: Bootstrap, operate, and troubleshoot `nelvko/clash-for-linux-install` on Linux hosts. Use when Codex needs to initialize Clash or Mihomo on a machine that may not already be installed, follow a daily-use SOP with `clashctl` and `clashsub`, inspect or edit `.env`, `resources/mixin.yaml`, or `resources/runtime.yaml`, manage subscriptions, Tun mode, Web UI secrets, upgrades, and uninstall, or quickly diagnose startup, port, service, subscription-conversion, or network-access problems. This skill vendors a trimmed upstream project copy under `scripts/upstream-project/` and should first try fetching the latest GitHub repository, then fall back to copying the bundled project files when GitHub access is slow or unavailable.
---

# Clash for Linux Install

Use this skill to initialize the project when it is missing, run the normal operator SOP when it is present, and shorten troubleshooting when something breaks.

## Start Here

1. Rebuild local state before making changes:

```bash
whoami
echo "$SHELL"
uname -m
readlink /proc/1/exe
command -v clashctl || true
```

2. Locate the actual install root before editing files. Default is `~/clashctl`, but the real path comes from the installed `.env`.
3. Decide which path applies:
   - no installation detected: initialize first
   - installation detected: follow the SOP sections below
   - failure or drift detected: troubleshoot before making bigger changes
4. Read [references/project-map.md](references/project-map.md) when you need exact file paths, bundled fallback details, or failure-mode notes.

## Initialization Workflow

Always prefer the latest upstream repository first. Only fall back to the bundled copy under `scripts/upstream-project/` when GitHub access is slow, blocked, or unavailable.

Prepare a working tree with:

```bash
rm -rf /tmp/clash-for-linux-install
git clone --depth 1 https://github.com/nelvko/clash-for-linux-install.git /tmp/clash-for-linux-install || {
  mkdir -p /tmp/clash-for-linux-install
  cp -R scripts/upstream-project/. /tmp/clash-for-linux-install/
}
cd /tmp/clash-for-linux-install
```

Then:

1. Review `.env` and change only the values that matter for this host.
2. Prefer `mihomo` unless the user explicitly needs legacy `clash`.
3. Set `CLASH_CONFIG_URL` in `.env` or pass the subscription URL directly to `install.sh`.
4. Run `bash install.sh`.
5. Verify with `clashctl status`, `clashui`, and `clashsecret`.

If the fallback copy was used, call out that it is a trimmed vendored upstream copy and may lag behind the current GitHub head.

## Installed-State Workflow

When an installation already exists:

1. Read the installed `.env` first.
2. Inspect these files in order:
   - `resources/config.yaml`
   - `resources/mixin.yaml`
   - `resources/runtime.yaml`
   - `resources/profiles.yaml`
3. Treat `runtime.yaml` as generated output. Do not hand-edit it unless the user explicitly wants a temporary experiment.
4. Prefer the built-in wrappers over raw edits whenever a wrapper already exists.

## Operator SOP

### Daily control

- `clashon`: start the kernel and enable shell proxy variables
- `clashoff`: stop the kernel and clear shell proxy variables
- `clashstatus`: inspect status
- `clashlog`: inspect logs
- `clashproxy on|off`: toggle only shell proxy variables

### Subscription management

- `clashsub add '<url>'`
- `clashsub ls`
- `clashsub use <id>`
- `clashsub update [id]`
- `clashsub update --convert [id]` only when validation or parser compatibility requires it
- `clashsub log`

Quote any subscription URL that contains `&`, `?`, or other shell-sensitive characters.

### Config management

Understand the merge model before editing anything:

- `config.yaml` is the active raw subscription
- `mixin.yaml` contains the highest-priority local overrides
- `runtime.yaml` is the merged runtime file actually passed to the kernel

Use:

- `clashmixin -e` to edit mixin safely
- `clashmixin -c` to inspect the base subscription
- `clashmixin -r` to inspect the effective runtime config

### Web UI and secrets

- `clashui` prints the effective local and public Web UI endpoints
- `clashsecret` shows the current secret
- `clashsecret <new_secret>` rotates the secret and restarts the service

### Tun mode

- `clashtun`
- `clashtun on`
- `clashtun off`

Require elevated privileges before changing Tun mode. Turn Tun off before uninstalling.

### Upgrade and uninstall

- `clashupgrade`
- `clashupgrade -v`
- `clashupgrade --release`
- `clashupgrade --alpha`
- `bash uninstall.sh`

## Troubleshooting Workflow

Use this sequence:

1. Confirm the install root, kernel choice, and init mode from `.env`.
2. Confirm required files exist under `bin/` and `resources/`.
3. Confirm whether the kernel process is running.
4. Read `resources/runtime.yaml` instead of guessing ports or Web UI endpoints.
5. Inspect the newest available log:
   - `/var/log/<kernel>.log` for many root installs
   - `resources/<kernel>.log` for `nohup` or non-root installs
6. For subscription problems, inspect:
   - `resources/temp.yaml`
   - `resources/temp.yaml.raw`
   - `bin/subconverter/latest.log`
   - `resources/profiles.log`
7. For port conflicts, let the project auto-randomize and then re-check `runtime.yaml` or `clashui`.
8. For Tun failures, search the logs for:
   - `Start TUN listening error`
   - `unsupported kernel version`
   - `Tun adapter listening at`
- `TUN listening iface`

## Operating Rules

- Always try the latest GitHub repository before using the bundled snapshot.
- Work from the prepared repo root when running `install.sh` or `uninstall.sh`.
- Do not manually delete the install directory when `uninstall.sh` can revoke shell hooks, service definitions, and cron entries cleanly.
- Prefer wrappers over raw edits:
  - `clashsub` for subscriptions
  - `clashmixin` for custom rules
  - `clashsecret` for the Web UI token
  - `clashtun` for Tun
- Edit `.env` only for installation-wide defaults such as kernel choice, install path, GitHub proxy, or subscription user agent.

## Bundled Resources

- `scripts/upstream-project/`
  Trimmed vendored copy of the upstream project with the install scripts, command wrappers, init scripts, and required resources preserved. Use it as the fallback source for `cp -R scripts/upstream-project/. /tmp/clash-for-linux-install/` when GitHub clone fails.

Read [references/project-map.md](references/project-map.md) whenever you need the exact file layout, bundled fallback details, command cheat sheet, or failure-mode map.
