from mpl_toolkits.basemap import Basemap
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
# create new figure, axes instances.
fig=plt.figure()
ax=fig.add_axes([0.1,0.1,0.8,0.8])
# setup mercator map projection.
m = Basemap(llcrnrlon=40.,llcrnrlat=20.,urcrnrlon=70.,urcrnrlat=40.,\
            rsphere=(6378137.00,6356752.3142),\
            resolution='l',projection='merc',\
            lat_0=10,lon_0=-20.,lat_ts=20.)
m.drawcoastlines()
m.fillcontinents()

m.drawparallels(np.arange(10,90,20),labels=[1,1,0,1])

m.drawmeridians(np.arange(-180,180,30),labels=[1,1,0,1])
m.scatter(36,48)
ax.set_title('Iran')


cities = pd.read_csv("ctr.csv")


plt.scatter(cities["longitude"],cities["latitude"],s=cities["population"]/1000)
plt.show()