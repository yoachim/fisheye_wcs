import numpy as np
from astropy.io import fits
from astropy.time import Time
from astropy.coordinates import SkyCoord, EarthLocation, AltAz
import astropy.units as u
import os


default_location = EarthLocation(lat=-30.2444*u.degree, lon=-70.7494*u.degree,
                                 height=2650.0*u.meter)



def chop_image(filename):
    """
    Run Astrometry.net on sub-sections of an image

    Parameters
    ----------
    filename : str
        The fits file to try and chop up
    """
    outfile = 'chop_image_temp.fits'
    
    if os.path.exists(outfile):
        os.unlink(outfile)
    in_image = fits.open(filename)
    date = in_image[0].header['DATE-OBS']
    image_time = Time(date, format='isot', scale='utc')

    # Make some loop to chop up the thing. Kind of a pain that I'm going to have to write each
    # sub array to disk just to have astrometry.net read it in.

    sub_image = in_image[0].data[1100:1300, 900:1200]
    hdu = fits.PrimaryHDU(sub_image)
    hdu.writeto(outfile)

    # clean up any old files

    # Call solve-field


    # Read in the results

    # Add the offsets back onto the x,y positions

    # Something like:
    # # solve-field --scale-units arcsecperpix --scale-low 150 --scale-high 300  --overwrite  chop_image_temp.fits


