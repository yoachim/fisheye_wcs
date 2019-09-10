# fisheye_wcs
Fit the WCS of fisheye all-sky cameras

The idea is to use astrometry.net to generate initial WCS solutions to subsections of the image. Then we can take the 
generated catalogs, convert the coordinates to altitude and azimuth, and fit a large-scale WCS.


## Prerequisites

astrometry.net https://github.com/dstndstn/astrometry.net

(from my experience, I got astrometry.net to install by `conda install swig` and using macports to get netbmp)

