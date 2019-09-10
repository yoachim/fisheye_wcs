import numpy as np
from astropy.io import fits
from astropy.time import Time
from astropy.coordinates import SkyCoord, EarthLocation, AltAz
import astropy.units as u
import os


default_location = EarthLocation(lat=-30.2444*u.degree, lon=-70.7494*u.degree,
                                 height=2650.0*u.meter)


def read_match(basefilename, image_time, location=default_location):
    """Read in an astrometry.net files to find the alt,az to x,y mapping
    """
    temp = fits.open(basefilename+'-indx.xyls')

    xy_positions = temp[1].data.copy()
    temp.close()
    temp = fits.open(basefilename+'.rdls')
    radec_positions = temp[1].copy()
    temp.close()

    # Convert to alt-az
    ref_catalog = SkyCoord(ra=radec_positions.data['RA']*u.degree, dec=radec_positions.data['DEC']*u.degree)
    alt_az = ref_catalog.transform_to(AltAz(obstime=image_time, location=location))

    names = ['x', 'y', 'alt', 'az']
    types = [float]*4
    result = np.empty(xy_positions.size, dtype=list(zip(names, types)))
    result['x'] = xy_positions['X']
    result['y'] = xy_positions['Y']
    result['alt'] = alt_az.alt
    result['az'] = alt_az.az

    return result


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


