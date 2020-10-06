from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import os
import ogr

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Reading a shapefile
in_path = os.path.join('c:\\','Users', 'OHM', 'Desktop','Final project', \
'Original Data','movebank', 'goose', 'dataclipped.shp')

# Get the correct driver and open file for reading
driver = ogr.GetDriverByName('ESRI Shapefile')
track = driver.Open(in_path, 0)
# Get the layer
layer = track.GetLayer(0)

# Not really necessary with one subplot
#f, axarr = plt.subplots(1)

# Access single features in the places layer
# And plot them
x = []
y = []
ele = []
for feat in layer:
    pt = feat.geometry()
    #lon = pt.GetX()
    #lat = pt.GetY()
    x.append(pt.GetX())
    y.append(pt.GetY())
    elevation = round(feat.GetField('clipped_de'), 1)
    ele.append(elevation)
    
#plt.scatter(x, y)

#ax.scatter(x, y, ele) 
#ax.scatter(x, y, ele, c=ele)
pnt3D = ax.(x,y, ele,c=ele)
cbar = plt.colorbar(pnt3D)

#c = ['r', 'g', 'b', 'y']
#cs = [c] * len(x)
#cs[0] = 'c'
#ax.bar(x, ele, zs=y, zdir='y', color=c, alpha=0.8)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Elevation')

plt.show()