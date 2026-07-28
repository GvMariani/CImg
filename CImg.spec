%global		debug_package %{nil}

%define		oname	CImg

Summary:	Tools for advanced image processing
Name:		cimg
Version:		4.0.3
Release:		1
License:		CeCILL
Group:	Graphics/Utilities
Url:		https://cimg.eu/
Source0:	https://cimg.eu/files/%{oname}_%{version}.zip
Source100:	cimg.rpmlintrc
BuildRequires:		doxygen
BuildRequires:		make
BuildRequires:		gomp-devel
BuildRequires:		pkgconfig(fftw3)
BuildRequires:		pkgconfig(libcurl)
BuildRequires:		pkgconfig(libjpeg)
# In Restricted
#BuildRequires:		pkgconfig(libheif)
BuildRequires:		pkgconfig(libpng)
BuildRequires:		pkgconfig(libjpeg)
BuildRequires:		pkgconfig(libtiff-4)
BuildRequires:		pkgconfig(libwebp)
BuildRequires:		pkgconfig(opencv4)
BuildRequires:		pkgconfig(OpenEXR)
BuildRequires:		pkgconfig(sdl3)
BuildRequires:		pkgconfig(x11)
BuildRequires:		pkgconfig(xrandr)
BuildRequires:		pkgconfig(zlib)

%description
Advanced image manipulation algorithms, including the GREYCSTORATION image
regularization algorithm which is mainly used for removing image noise.
This package contains example tools based on the CImg source library.

%files
%{_bindir}/*

#-----------------------------------------------------------------------------

%package devel
Summary:		Library for advanced image processing (development files)
Group:	Development/C
Provides:	%{name}-devel = %{version}-%{release}

%description devel
This package contains the development files for the CImg library. It is needed
to compile programes which use functions of the CImg library.
Note that this package doe not contain a dynamic library. The whole library
code is in the CImg.h file which is in this package.

%files devel
%license Licence_CeCILL*
%doc README.txt examples
%doc resources/%{oname}_reference.pdf
%{_includedir}/%{oname}*

#-----------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{oname}-%{version}


%build
# No binary library: build only the examples
%ifarch %{arm}
	export NO_MTUNE_GENERIC=1
%endif
pushd examples
	%make_build olinux
popd


%install
mkdir -p %{buildroot}%{_bindir}
# We need move them rhater than installing to avoid later rpmlint errors
pushd examples
	mv captcha %{buildroot}%{_bindir}
	mv CImg_demo %{buildroot}%{_bindir}
	mv curve_editor2d %{buildroot}%{_bindir}
	mv dtmri_view3d %{buildroot}%{_bindir}
	mv edge_explorer2d %{buildroot}%{_bindir}
	mv fade_images %{buildroot}%{_bindir}
	mv gaussian_fit1d %{buildroot}%{_bindir}
	mv generate_loop_macros %{buildroot}%{_bindir}
	mv hough_transform2d %{buildroot}%{_bindir}
	mv image2ascii %{buildroot}%{_bindir}
	mv image_registration2d %{buildroot}%{_bindir}
	mv image_surface3d %{buildroot}%{_bindir}
	mv jawbreaker %{buildroot}%{_bindir}
	mv mcf_levelsets2d %{buildroot}%{_bindir}
	mv mcf_levelsets3d %{buildroot}%{_bindir}
	mv odykill %{buildroot}%{_bindir}
	mv pde_heatflow2d %{buildroot}%{_bindir}
	mv pde_TschumperleDeriche2d %{buildroot}%{_bindir}
	mv plotter1d %{buildroot}%{_bindir}
	mv scene3d %{buildroot}%{_bindir}
	mv spherical_function3d %{buildroot}%{_bindir}
	mv tetris %{buildroot}%{_bindir}
	mv tron %{buildroot}%{_bindir}
	mv tutorial %{buildroot}%{_bindir}
	mv use_chlpca %{buildroot}%{_bindir}
	mv use_draw_gradient %{buildroot}%{_bindir}
	mv use_nlmeans %{buildroot}%{_bindir}
	mv use_RGBclass %{buildroot}%{_bindir}
	mv use_skeleton %{buildroot}%{_bindir}
	mv wavelet_atrous %{buildroot}%{_bindir}
popd

mkdir -p %{buildroot}%{_includedir}/%{oname}
mv plugins %{buildroot}%{_includedir}/%{oname}
mv %{oname}.h %{buildroot}%{_includedir}/%{oname}
ln -s %{oname}/%{oname}.h %{oname}.h
mv %{oname}.h %{buildroot}%{_includedir}
