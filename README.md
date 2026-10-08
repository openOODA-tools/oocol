# oocol: Sovereign ESCAPE FILTER

<div align="center">

```
================================================================================
                                 oocol
                Sovereign openOODA ESCAPE FILTER
================================================================================
```

**Sovereign ESCAPE FILTER**  
*Reverse line feed filter removing backspaces, half-line feeds, and overstrikes from terminal output.*  
*Two Faces, One Engine:* Modern terminal ergonomics for humans • Zero-leakage MCP for AI agents  
Written in 100% pure [openOODA](https://github.com/openOODA).

[![License: Apache-2.0](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![openOODA](https://img.shields.io/badge/openOODA-1.0-emerald.svg)](https://openooda.org)
[![Version: 0.2.0](https://img.shields.io/badge/version-0.2.0-blue.svg)](https://github.com/openOODA-tools/oocol/releases/tag/v0.2.0)
[![Architecture: x86_64 | aarch64](https://img.shields.io/badge/Arch-x86__64%20%7C%20aarch64-lightgrey.svg)]()

</div>

---

## 1. Quick Install

### Automated Installer (Linux x86_64 & aarch64)
```bash
curl -fsSL https://openooda-tools.github.io/oocol/install.sh | bash
```

### Native Package Managers
```bash
# Arch Linux (AUR / PKGBUILD)
yay -S oocol-bin
# Or manual PKGBUILD:
cd packaging/arch && makepkg -si

# Debian / Ubuntu (.deb)
curl -fsSL https://openooda-tools.github.io/oocol/install.sh | bash -s -- --deb

# Fedora / RHEL (.rpm)
curl -fsSL https://openooda-tools.github.io/oocol/install.sh | bash -s -- --rpm
```

### Uninstallation
```bash
oocol-uninstall
# or: curl -fsSL https://openooda-tools.github.io/oocol/uninstall.sh | bash
```

---

## 2. CLI Usage

```
usage: oocol [options] [FILE]

Filter reverse line feeds, backspaces, and overstrikes from terminal output.

Options:
  -b, --no-backspaces    do not output backspaces; resolve overstrikes
  -f, --fine             permit forward half line feeds
  -p, --pass             pass unknown control sequences through
  -x, --spaces           do not convert spaces to tabs (expand tabs)
  -h, --tabs             compress multiple spaces into tabs
  -l, --lines=NUM        buffer at most NUM lines in memory
      --inspect          display buffer inspection telemetry report
      --demo             run demonstration scenario with synthetic overstrikes
      --json             output formatted as JSON telemetry
  -h, --help             display this help and exit
  -v, -V, --version      output version information and exit
      --mcp              run as Model Context Protocol stdio server
```

---

## 3. Model Context Protocol (MCP)

When invoked with `--mcp`, `oocol` runs a JSON-RPC 2.0 stdio server providing structured tools for AI coding agents:

| Tool Name | Parameters | Description |
|-----------|------------|-------------|
| `col_filter` | `text`, `path`, `no_backspaces`, `expand_tabs`, `compress_spaces`, `pass_control` | Comprehensive text filter resolving overstrikes and tabs. |
| `col_strip_backspaces` | `text`, `path` | Strips all backspaces and resolves overstrike sequences to clean text. |
| `col_clean_man` | `text`, `path` | Cleans formatted groff/nroff manual page output into readable plain text. |
| `col_tab_convert` | `text`, `path`, `expand_tabs`, `compress_spaces` | Converts between horizontal tab stops and space runs. |
| `col_inspect` | `text`, `path` | Audits text buffer and returns backspace and overstrike density metrics. |

```bash
printf '{"jsonrpc":"2.0","id":1,"method":"tools/call","params":{"name":"col_strip_backspaces","arguments":{"text":"a\\bax\\bxb"}}}\n' | oocol --mcp
```

---

## 4. Security & Zero Ambient Authority

* **Pure Capability Bounded:** Operates strictly with explicit tokens (`&FsReadCap`, `&ProcessCap`, `&EnvCap`). Physical absence of ambient disk or network authority.
* **Negative-Trust Architecture:** Strict buffer bounds and operational limits prevent memory leakage.
* **Hermetic Binary:** Standalone zero-dependency executable compiled natively via `oodac`.

---

## 5. License

Apache License, Version 2.0. See [LICENSE](LICENSE) for details.
