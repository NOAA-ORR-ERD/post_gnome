from post_gnome.plotting import geo_plots
import matplotlib.pyplot as plt
import datetime


plt.clf()

ax = geo_plots.add_map(bbox=(-125.2,-124.2,47.7,48.3), bna='coast_wa.bna') 

#add particles at one time
t = datetime.datetime(2016,8,18,12)

filename = 'WA_particles.nc'
ax = geo_plots.contour_particles(ax,filename,t,levels=[0.1, 0.4, 0.6, 1])


plt.show()