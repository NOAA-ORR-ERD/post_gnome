###############################
Post Processing tools for GNOME
###############################

A python package of assorted scripts and utilities that can be used to post-process output from the General NOAA Operational Modeling Environment (GNOME).

These files may have come from the PyGNOME package:

https://github.com/NOAA-ORR-ERD/PyGnome

Or the WebGNOME web-based modeling system:

https://gnome.orr.noaa.gov

Installing
==========

As of now, the ``post_gnome`` package needs to be installed from source:

::
    pip install ./
    or
    pip install -e ./

Should work fine.

Included Tools:
===============

Scripts:
--------

installing the package should install these scripts::

gnome_nc2kmz.py
moss2kmz_series.py
params_example.yaml
make_erma_package.py
moss2kmz_simple.py
set_status_for_beached.py

Modules:
--------

``post_gnome.plotting`` -- assorted utilites for plotting output.

``post_gnome.nc_particles`` -- system for working with the netcdf particle tracking results

``post_gnome.readers`` -- code for reading other file formats

``post_gnome.kml`` -- code for woking with KML / KMZ file formats.

Contributing
============

Bug reports, questions, contributions ar welcome. Please use the gitHub issues / Pull Requests:

https://github.com/NOAA-ORR-ERD/post_gnome

