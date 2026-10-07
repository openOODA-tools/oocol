Name:           oocol
Version:        0.1.0
Release:        1%{?dist}
Summary:        Reverse line feed filter removing backspaces and half-line feeds from terminal output.
License:        ASL 2.0
URL:            https://github.com/openOODA-tools/oocol
Source0:        oocol-linux-x86_64
Source1:        uninstall.sh
BuildArch:      x86_64
Requires:       glibc

%description
oocol is a sovereign, capability-bounded ESCAPE FILTER written
in pure openOODA, featuring zero ambient authority, oote color themes,
and an MCP stdio server.

%install
mkdir -p %{buildroot}/usr/bin
install -m 0755 %{SOURCE0} %{buildroot}/usr/bin/oocol
install -m 0755 %{SOURCE1} %{buildroot}/usr/bin/oocol-uninstall

%files
/usr/bin/oocol
/usr/bin/oocol-uninstall

%changelog
* Wed Oct 07 2026 openOODA-tools <ops@openooda.org> - 0.1.0-1
- Initial sovereign blueprint scaffolding
