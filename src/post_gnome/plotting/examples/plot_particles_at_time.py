from post_gnome.plotting import geo_plots
import matplotlib.pyplot as plt
import datetime

plt.clf()

ax = geo_plots.add_map(bbox=(-125.2,-124.2,47.7,48.3), bna='coast_wa.bna') 
#if bbox not specified, this will use map bounds from bna

#add particles at one time
t0 = datetime.datetime(2016,8,18,12)
ax = geo_plots.plot_particles(ax,'WA_particles.nc',t0,color='b')

t1 = t0 + datetime.timedelta(hours=1)
ax = geo_plots.plot_particles(ax,'WA_particles.nc',t1,color='g')

ax.legend()

#add initial location
t = datetime.datetime(2016,8,18,1)
geo_plots.plot_particles(ax,'WA_particles.nc',t,marker='+',markersize=8)

plt.show()