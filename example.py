# This file is part of AstroHOG
#
# Copyright (C) 2013-2017 Juan Diego Soler

import sys
import numpy as np
from astropy.io import fits
import matplotlib.pyplot as plt

sys.path.append('/Users/jsoler/Documents/astrohog/')
from astrohog import *

def astroHOGexample(vmin, vmax):

	dir='/Users/jsoler/PYTHON/HItest/'
	hdu1=fits.open(dir+'lite'+'THOR_and_VGPS_HI_without_continuum_L23.75_40arcsec.fits')
	dir='/Users/jsoler/PYTHON/COtest/'
	hdu2=fits.open(dir+'grs_L23.75.fits')

	v1=vmin*1000.;	v2=vmax*1000.
        v1str="%4.1f" % vmin     
	v2str="%4.1f" % vmax
	limsv=np.array([v1, v2, v1, v2])

	CTYPE3=hdu1[0].header['CTYPE3']
	CDELT3=hdu1[0].header['CDELT3']
	CRVAL3=hdu1[0].header['CRVAL3']
	CRPIX3=hdu1[0].header['CRPIX3']
	zmin1=int(CRPIX3+(v1-CRVAL3)/CDELT3)
	zmax1=int(CRPIX3+(v2-CRVAL3)/CDELT3)
	velvec1=np.arange(v1,v2,CDELT3)/1000.

	CTYPE3=hdu2[0].header['CTYPE3']
        CDELT3=hdu2[0].header['CDELT3']
        CRVAL3=hdu2[0].header['CRVAL3']
        CRPIX3=hdu2[0].header['CRPIX3']
        zmin2=int(CRPIX3+(v1-CRVAL3)/CDELT3)
        zmax2=int(CRPIX3+(v2-CRVAL3)/CDELT3)
	velvec2=np.arange(v1,v2,CDELT3)/1000.

	sz1=np.shape(hdu1[0].data)
	mask1=np.zeros(sz1)
	mask1[(hdu1[0].data > 0.15).nonzero()]=1
	mask1[:,0:sz1[1]*0.15,:]=0
	mask1[:,sz1[1]*0.85:sz1[1]-1,:]=0

	sz2=np.shape(hdu2[0].data)
	mask2=np.zeros(sz2)
        mask2[(hdu2[0].data > 0.0).nonzero()]=1
        mask2[:,0:sz2[1]*0.15,:]=0
        mask2[:,sz2[1]*0.85:sz2[1]-1,:]=0

	#corrplane=HOGcorr_cube(hdu1[0].data, hdu2[0].data, zmin1, zmax1, zmin2, zmax2, ksz=5)
	#corrplane=HOGcorr_cube(hdu1[0].data, hdu2[0].data, zmin1, zmax1, zmin2, zmax2, ksz=5, mask1=mask1)

	#corrplane=HOGcorr_cube(hdu1[0].data, hdu2[0].data, zmin1, zmax1, zmin2, zmax2, mask1=mask1, mask2=mask2)
	corrplane=HOGcorr_cube(hdu1[0].data, hdu2[0].data, zmin1, zmax1, zmin2, zmax2, ksz=5, mask1=mask1, mask2=mask2)
	#corrplane=HOGcorr_cube(hdu1[0].data, hdu2[0].data, zmin1, zmax1, zmin2, zmax2, ksz=5, mask1=mask1, mask2=mask2, wd=3)
	#corrplane=HOGcorr_cube(hdu1[0].data, hdu2[0].data, zmin1, zmax1, zmin2, zmax2, mask1=mask1, mask2=mask2, wd=3)

	#corrplane=HOGcorr_cube(hdu1[0].data, hdu1[0].data, zmin1, zmax1, zmin1, zmax1, mask1=mask1, mask2=mask1)
	#corrplane=HOGcorr_cube(hdu2[0].data, hdu2[0].data, zmin2, zmax2, zmin2, zmax2, mask1=mask2, mask2=mask2)

	plt.imshow(corrplane, origin='lower', extent=limsv/1e3)
	plt.xlabel(r'$v_{CO}$ [km/s]')
        plt.ylabel(r'$v_{HI}$ [km/s]')
        plt.yticks(rotation='vertical')
	plt.colorbar()
        plt.show()

        import pdb; pdb.set_trace()

astroHOGexample(-5., 45.)


