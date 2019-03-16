#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-base64enc
Version  : 0.1.3
Release  : 15
URL      : https://cran.r-project.org/src/contrib/base64enc_0.1-3.tar.gz
Source0  : https://cran.r-project.org/src/contrib/base64enc_0.1-3.tar.gz
Summary  : Tools for base64 encoding
Group    : Development/Tools
License  : GPL-2.0 GPL-3.0
Requires: R-base64enc-lib = %{version}-%{release}
Requires: R-png
BuildRequires : R-png
BuildRequires : buildreq-R

%description
No detailed description available

%package lib
Summary: lib components for the R-base64enc package.
Group: Libraries

%description lib
lib components for the R-base64enc package.


%prep
%setup -q -c -n base64enc

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1552712393

%install
export SOURCE_DATE_EPOCH=1552712393
rm -rf %{buildroot}
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library base64enc
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library base64enc
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library base64enc
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc  base64enc || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/base64enc/DESCRIPTION
/usr/lib64/R/library/base64enc/INDEX
/usr/lib64/R/library/base64enc/Meta/Rd.rds
/usr/lib64/R/library/base64enc/Meta/features.rds
/usr/lib64/R/library/base64enc/Meta/hsearch.rds
/usr/lib64/R/library/base64enc/Meta/links.rds
/usr/lib64/R/library/base64enc/Meta/nsInfo.rds
/usr/lib64/R/library/base64enc/Meta/package.rds
/usr/lib64/R/library/base64enc/NAMESPACE
/usr/lib64/R/library/base64enc/NEWS
/usr/lib64/R/library/base64enc/R/base64enc
/usr/lib64/R/library/base64enc/R/base64enc.rdb
/usr/lib64/R/library/base64enc/R/base64enc.rdx
/usr/lib64/R/library/base64enc/help/AnIndex
/usr/lib64/R/library/base64enc/help/aliases.rds
/usr/lib64/R/library/base64enc/help/base64enc.rdb
/usr/lib64/R/library/base64enc/help/base64enc.rdx
/usr/lib64/R/library/base64enc/help/paths.rds
/usr/lib64/R/library/base64enc/html/00Index.html
/usr/lib64/R/library/base64enc/html/R.css

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/base64enc/libs/base64enc.so
