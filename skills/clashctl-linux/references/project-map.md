# Project Map

These notes were derived from the upstream repository files that define the actual behavior:

- `README.md`
- `.env`
- `install.sh`
- `uninstall.sh`
- `scripts/preflight.sh`
- `scripts/cmd/common.sh`
- `scripts/cmd/clashctl.sh`

Re-check the upstream repository when versions or command behavior matter.

## Bundled Fallback

This skill includes a bundled trimmed copy of the upstream project under `scripts/upstream-project/`.

Snapshot source:

- repository: `https://github.com/nelvko/clash-for-linux-install`
- commit: `9993f38dfd994a781f42f425befb11d19cbf4c7e`
- commit date: `2026-03-31`

Use the bundled copy only after a normal `git clone` attempt fails or stalls.

## Repository and Install Layout

The installer copies the repository tree into `CLASH_BASE_DIR`. The default install path from `.env` is `~/clashctl`.

Key installed paths:

- `.env`
- `bin/$KERNEL_NAME`
- `bin/yq`
- `bin/subconverter/`
- `resources/config.yaml`
- `resources/mixin.yaml`
- `resources/runtime.yaml`
- `resources/temp.yaml`
- `resources/profiles.yaml`
- `resources/profiles/*.yaml`
- `resources/profiles.log`

Non-root or `nohup`-managed runs also keep these under `resources/`:

- `${KERNEL_NAME}.log`
- `${KERNEL_NAME}.pid`

## Important Environment Knobs

The installed `.env` controls the broad behavior:

- `KERNEL_NAME`: `mihomo` or `clash`
- `CLASH_BASE_DIR`: install target
- `CLASH_CONFIG_URL`: initial subscription URL
- `CLASH_SUB_UA`: user agent for subscription downloads
- `INIT_TYPE`: optional manual init override
- `ZIP_UI`: local Web UI archive path
- `URL_GH_PROXY`: GitHub download proxy prefix
- `URL_CLASH_UI`: public UI URL shown by `clashui`
- `VERSION_MIHOMO`, `VERSION_YQ`, `VERSION_SUBCONVERTER`: currently pinned versions

Prefer editing `.env` before install. After install, change it only for install-wide defaults.

## Install and Uninstall Commands

Fresh install from repo root:

```bash
bash install.sh
bash install.sh mihomo
bash install.sh clash
bash install.sh 'https://example.com/subscription?...'
```

Recommended preparation step before running those commands:

```bash
rm -rf /tmp/clash-for-linux-install
git clone --depth 1 https://github.com/nelvko/clash-for-linux-install.git /tmp/clash-for-linux-install || {
  mkdir -p /tmp/clash-for-linux-install
  cp -R scripts/upstream-project/. /tmp/clash-for-linux-install/
}
cd /tmp/clash-for-linux-install
```

The installer:

- validates required commands: `xz`, `pgrep`, `curl`, `tar`, `unzip`
- auto-detects architecture and init system
- downloads the matching kernel, `yq`, and `subconverter`
- copies the repo into `CLASH_BASE_DIR`
- sets up service integration or `nohup`
- merges config, prints the Web UI endpoint, and generates a random secret

Uninstall from repo root:

```bash
bash uninstall.sh
```

If Tun is still enabled, turn it off first.

## CLI Command Map

Primary entrypoint:

```bash
clashctl COMMAND [OPTIONS]
```

Common wrappers and what they do:

- `clashon`: start the kernel and set shell proxy variables when enabled
- `clashoff`: stop the kernel and clear shell proxy variables
- `clashstatus`: inspect service status
- `clashlog`: inspect service logs
- `clashproxy [on|off]`: manage shell proxy variables and the mixin switch
- `clashui`: print local and public Web UI addresses
- `clashsecret [new_secret]`: show or rotate the Web UI secret
- `clashmixin [-e|-c|-r]`: inspect or edit mixin, base config, and runtime config
- `clashupgrade [-v] [-r|--release|-a|--alpha]`: trigger the kernel upgrade endpoint
- `clashtun [on|off]`: manage Tun mode
- `clashsub add|ls|del|use|update|log`: manage subscriptions

The repo also ships `clashctl.fish` for Fish completions.

## Config and Merge Model

Treat the config pipeline as three layers:

1. `resources/config.yaml`
   The active raw subscription.
2. `resources/mixin.yaml`
   Local overrides with the highest precedence.
3. `resources/runtime.yaml`
   The merged runtime config passed to the kernel.

Important merge behavior from `clashctl.sh`:

- `rules` are combined as `prefix + config + suffix`
- `proxies` and `proxy-groups` support `prefix`, `override`, and `suffix`
- `_custom` data in the mixin is removed before generating the runtime file

Use `clashmixin -r` to inspect the final effective config instead of guessing.

## Subscription Flow

`clashsub add <url>`:

- downloads the raw subscription into `resources/temp.yaml`
- validates it with the kernel's `-t` config test
- falls back to local subconverter if validation fails
- stores the saved profile under `resources/profiles/<id>.yaml`
- records metadata in `resources/profiles.yaml`

`clashsub use <id>`:

- copies the selected saved profile into `resources/config.yaml`
- regenerates `resources/runtime.yaml`
- restarts the service if needed

`clashsub update [id]`:

- updates one saved profile from its original URL
- uses the active subscription ID when no ID is given
- supports `--convert` to force subconverter
- supports `--auto` to add a cron job that runs every two days

When a subscription fails, inspect:

- `resources/temp.yaml`
- `resources/temp.yaml.raw`
- `bin/subconverter/latest.log`
- `resources/profiles.log`

## Init System and Runtime Behavior

The project auto-detects the init system from `/proc/1/exe`.

Likely runtime modes:

- `systemd`
- `OpenRC`
- `SysVinit`
- `runit`
- `nohup`

Important fallbacks:

- containerized environments force `nohup`
- non-root installs force `nohup`
- non-root installs move logs and PID files into `resources/`

## Port Behavior

The scripts auto-randomize ports when conflicts are detected. This affects:

- `mixed-port`
- `port`
- `socks-port`
- `external-controller`
- subconverter server port

The auto-generated replacement is written into `mixin.yaml`, then re-merged into `runtime.yaml`.

Do not assume the documented default port is still active after installation. Re-read `runtime.yaml` or run `clashui`.

## Tun Notes

Tun requires elevated privileges and may fail on unsupported kernels.

Observed logic:

- enabling Tun stops the current service and restarts with elevated privileges
- if Mihomo hits a Tun startup error, the script retries with `.tun.auto-redirect = false`
- if the retry still fails, the script disables Tun and exits with an error

Useful log patterns:

- `Start TUN listening error`
- `unsupported kernel version`
- `Tun adapter listening at`
- `TUN listening iface`

## Troubleshooting Checklist

Install fails immediately:

- verify `xz`, `pgrep`, `curl`, `tar`, `unzip`
- verify the shell is `bash` or `zsh`
- verify the chosen install path is writable and not blocked by a non-root install under `/root`

Kernel binary download fails:

- inspect `URL_GH_PROXY`
- retry without the proxy
- manually place the expected archives under `resources/zip/`

Web UI or API endpoint fails:

- run `clashui`
- inspect `external-controller` in `resources/runtime.yaml`
- check whether the external controller port was rewritten because of a conflict
- verify firewall rules

Subscription add or update fails:

- quote the URL
- inspect `resources/temp.yaml.raw`
- inspect `bin/subconverter/latest.log`
- prefer `clashsub update --convert` only when needed

Uninstall fails:

- disable Tun first
- stop the service before deleting custom files

## Bundled Project Contents

The bundled copy is trimmed for offline initialization and routine operations.

Removed as non-essential:

- `.github/`
- `.editorconfig`
- `.gitattributes`
- `.gitignore`
- `.shellcheckrc`
- `resources/preview.png`
- transient macOS files such as `.DS_Store`

Kept as operationally relevant:

- `.env`
- `install.sh`
- `uninstall.sh`
- `scripts/`
- `resources/Country.mmdb`
- `resources/geosite.dat`
- `resources/mixin.yaml`
- `resources/profiles.yaml`
- `resources/profiles/.gitkeep`
- `resources/zip/dist.zip`
- `README.md`
- `LICENSE`
