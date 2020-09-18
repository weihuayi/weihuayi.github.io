import numpy as np
import mpl_toolkits.mplot3d as a3
import matplotlib.colors as colors
import pylab as pl

import sys

from fealpy.mesh.StructureHexMesh import StructureHexMesh 

n = int(sys.argv[1])
box = [0, n, 0, n, 0, n]

mesh = StructureHexMesh(box, n, n, n)
node = mesh.entity('node')

index = mesh.multi_index()
flag = (index[:, 0] < index[:, 1]) & (index[:, 1] < index[:, 2])

I = index[:, 0].copy()
I += index[:, 1]*(index[:, 1] + 1)//2
I += index[:, 2]*(index[:, 2] + 1)*(index[:, 2] + 2)//6

axes = a3.Axes3D(pl.figure())
mesh.add_plot(axes, showedge=True)
mesh.find_node(axes, showindex=True, markersize=300, color='r', multiindex=index)

axes = a3.Axes3D(pl.figure())
mesh.add_plot(axes, showedge=True)
mesh.find_node(axes,  showindex=True, markersize=300, color='r',
        multiindex=I)

axes = a3.Axes3D(pl.figure())
mesh.add_plot(axes, showedge=True)
mesh.find_node(axes, node=node[flag], showindex=True, markersize=300, color='r',
        multiindex=I[flag])
mesh.find_node(axes)

pl.show()
