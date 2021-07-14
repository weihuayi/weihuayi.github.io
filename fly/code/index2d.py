
import sys

import numpy as np
import matplotlib.pyplot as plt


from fealpy.mesh import StructureQuadMesh

n = int(sys.argv[1])
mesh = StructureQuadMesh([0, n, 0, n], nx=n, ny=n)

index = mesh.multi_index()

I = index[:, 0].copy() 
t = index[:, 0] + index[:, 1]
t = index[:, 1]
I+= t*(t + 1)//2

fig = plt.figure()
axes = fig.gca()
mesh.add_plot(axes)
mesh.find_node(axes, showindex=True, multiindex=index)

fig = plt.figure()
axes = fig.gca()
mesh.add_plot(axes)
mesh.find_node(axes, showindex=True, multiindex=I)
plt.show()
