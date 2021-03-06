#! /usr/bin/python

import get_nodes
import csv
from osgeo import ogr

shpfile = '../data/shp/gRoad_guinea.shp'
output = '../data/gRoads_nodes.csv'

fields = ['id', 'task_x', 'task_y']
csvfile = open(output, 'wb')
writer = csv.writer(csvfile)
writer.writerow(fields)

driver = ogr.GetDriverByName("ESRI Shapefile")
source = driver.Open(shpfile, 0)
layer = source.GetLayer()

all_nodes = []
for feature in layer:
    geometry = feature.GetGeometryRef()
    lon = geometry.GetX()
    lat = geometry.GetY()
    task_x, task_y = get_nodes.cal_pixel(lat, lon)
    row = '%d, %d' % (task_x, task_y)
    all_nodes.append(row)

# all_nodes is already a "list", ?
all_xy = list(set(all_nodes))

for i, node in enumerate(all_xy):
    ind = node.index(',')
    task_x = int(node[0:ind])
    task_y = int(node[ind+1:])
    row = [i, task_x, task_y]
    writer.writerow(row)

csvfile.close()