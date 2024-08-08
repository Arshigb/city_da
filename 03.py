import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from mpl_toolkits.basemap import Basemap


lons = df["lon"]
lats = df["lat"]
sizes = df["population"]/10000
fig=plt.figure()
ax=fig.add_axes([0.1,0.1,0.8,0.8])

m = Basemap(llcrnrlon=40.,llcrnrlat=24.,urcrnrlon=65.,urcrnrlat=40.,\
            rsphere=(6378137.00,6356752.3142),\
            resolution='l',projection='merc',\
            lat_0=10,lon_0=-20.,lat_ts=20.)
m.drawcoastlines()
x , y =m(lons,lats)

m.drawparallels(np.arange(10,90,20),labels=[1,1,0,1])
m.drawmeridians(np.arange(-180,180,30),labels=[1,1,0,1])

df = pd.read_csv("ctr.csv")

ax.set_title('most papulated city in iran')

plt.show()