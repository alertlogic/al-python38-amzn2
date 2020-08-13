#################
#
# Author:      Des Jones (dejones@alertlogic.com)
# Project:     defender automation
# Date:        Fri  7 Aug 12:36:41 UTC 2020
# Version:     1.0
# Git:         git@github.com:alertlogic/al-python38-amazn2.git
# Notes:       rpmbuild -ba al-python38-amazn2
#              please manage versioning automagically with git tags
# 
###################################################

Name:       al-python38-amzn2
Version:    %{version}
Release:    %{release}
Summary:    AlertLogic al-python38-amzn2
License:    AlertLogic (c). All rights reserved.
BuildArch:  noarch
Provides:   al-python
Requires(pre):   al-s3repo
Requires(pre):   python38

%description
Install and configure al-python38-amzn2

%prep
# add sources
cp -R %{_sourcedir}/%{name}/* .

%build

%install
cp -R usr/ %{buildroot}/
mkdir -p %{buildroot}/usr/bin/
ln -s python3.8 %{buildroot}/usr/bin/python38

%files
/usr/local/sbin/*
/usr/local/bin/*

%pre

%post

%preun
# turn things off before uninstalling

%clean
if [ -d %{buildroot} ] ; then
  rm -rf %{buildroot}/*
fi

%changelog
# date "+%a %b %d %Y"
* Thu Mar 26 2020 desmond jones <dejones@alertlogic.com> %{version}-%{release}
- initial release

