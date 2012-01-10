Summary:	git-bridgesvn - a git-svn without altering the commit hashes
Name:		git-bridgesvn
Version:	0.1
Release:	0.20120109.2
License:	LGPL v2+
Group:		Development/Version Control
Source0:	%{name}.tar.gz
# Source0-md5:	51b90ae4f91de5077d2977214f06e7c5
URL:		https://github.com/boris-unterer/Git-SVN-Bridge/
BuildRequires:	git-core
Requires:	git-core
Requires:	perl-Encode
Requires:	perl-subversion
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		git_libdir	%(git --exec-path)

%description
git-bridgesvn supports a maintainer model, where one maintainer
revises the pushes and fetches to and from SVN, but the resultant git
repository can be shared with other git users.

%prep
%setup -q -n %{name}

%build

%install
rm -rf $RPM_BUILD_ROOT
install -D git-bridgesvn.perl $RPM_BUILD_ROOT%{git_libdir}/git-bridgesvn

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{git_libdir}/%{name}
