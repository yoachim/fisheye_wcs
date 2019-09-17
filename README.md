# fisheye_wcs
Fit the WCS of fisheye all-sky cameras

The idea is to use astrometry.net to generate initial WCS solutions to subsections of the image. Then we can take the 
generated catalogs, convert the coordinates to altitude and azimuth, and fit a large-scale WCS.

In theory, if one knows the location of the camera and the times imags were taken, it should be possible to fit the 
alt,az mapping without needing a reference catalog. 


## Prerequisites

astrometry.net https://github.com/dstndstn/astrometry.net

(from my experience, I got astrometry.net to install by `conda install swig` and using macports to get netbmp)

## Primary Use Case

The main use case for this package is if one has a stable all-sky camera, the WCS solution (i.e., the mapping of altitude and azimuth to x,y, pixel) should remain nearly constant over time. Solving for this WCS solution should make it possible to do forced-photometry (measure the flux of known star positions), and determine if they are blocked by clouds.

Other potential uses include monitoring the brightness of the sky.

