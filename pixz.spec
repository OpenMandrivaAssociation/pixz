# Keep in mind with: 
# Large file support NOT perfect:  https://github.com/vasi/pixz/issues/44
# Not OOM-safe! Still persists:    https://github.com/vasi/pixz/issues/45

Name:           pixz
Version:        1.0.7
Release:        3
Summary:        Parallel indexed xz compressor
License:        MIT
URL:            https://github.com/vasi/pixz/
Source0:        https://github.com/vasi/pixz/releases/download/v%{version}/pixz-%{version}.tar.xz
BuildRequires:	pkgconfig(libarchive)
BuildRequires:	pkgconfig(liblzma)

%description
Pixz (pronounced pixie) is a parallel, indexing version of xz.

** pixz vs xz

The existing XZ Utils provide great compression in the .xz file format, but
they produce just one big block of compressed data. Pixz instead produces a
collection of smaller blocks which makes random access to the original data
possible. This is especially useful for large tarballs.

** Differences to xz

* Automatically indexes tarballs during compression.
* Supports parallel decompression, which xz does not.
* Defaults to using all available CPU cores, while xz defaults to using
only one core.
* Provides -i and -o command line options to specify input and output file.

%prep
%autosetup -p1
# Drop redundant -lm, but it doesn't affect anything serious, and this hack
# requires autoreconf, so just ignore for a while.
# https://github.com/vasi/pixz/pull/49
# sed -i 's|-lm ||g' src/Makefile.am

# Drop cppcheck test, it doesn't make sense to downstream, should be checked
# BEFORE release.
sed -i 's|cppcheck-src||g' test/Makefile*

%build
%configure
%make_build

%install
%make_install

%check
make check

%files
%doc NEWS README* TODO
%{_bindir}/pixz
