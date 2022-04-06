Name: cookbook-ohai
Version: %{__version}
Release: %{__release}%{?dist}
BuildArch: noarch
Summary: Ohai cookbook with redborder plugins to install and configure it in redborder environments

License: AGPL 3.0
URL: https://github.com/redBorder/cookbook-ohai
Source0: %{name}-%{version}.tar.gz

Requires: ipmitool

%description
%{summary}

%prep
%setup -qn %{name}-%{version}

%build

%install
mkdir -p %{buildroot}/var/chef/cookbooks/ohai
cp -f -r  resources/* %{buildroot}/var/chef/cookbooks/ohai/
chmod -R 0755 %{buildroot}/var/chef/cookbooks/ohai
install -D -m 0644 README.md %{buildroot}/var/chef/cookbooks/ohai/README.md

%pre

%post
case "$1" in
  1)
    # This is an initial install.
    :
  ;;
  2)
    # This is an upgrade.
    su - -s /bin/bash -c 'source /etc/profile && rvm gemset use default && env knife cookbook upload ohai'
  ;;
esac

%files
%defattr(0755,root,root)
/var/chef/cookbooks/ohai
%defattr(0644,root,root)
/var/chef/cookbooks/ohai/README.md

%doc

%changelog
* Mon Apr 04 2022 David Vanhoucke <dvanhoucke@redborder.com> - 1.0.0-1
- first spec version
