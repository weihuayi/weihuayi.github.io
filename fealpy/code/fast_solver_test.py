#!/usr/bin/env python3
# 

import sys 
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from fealpy.pde.poisson_2d import CosCosData 
from fealpy.functionspace import LagrangeFiniteElementSpace

from fealpy.tools.show import showmultirate

# solver
from fealpy.solver import HighOrderLagrangeFEMFastSolver

p = int(sys.argv[1])
n = int(sys.argv[2])
maxit = int(sys.argv[3])
d = int(sys.argv[4])

if d == 2:
    from fealpy.pde.poisson_2d import CosCosData as PDE
elif d == 3:
    from fealpy.pde.poisson_3d import CosCosCosData as PDE

pde = PDE()
mesh = pde.init_mesh(n=n)

errorType = ['$|| u - u_h||_{\Omega,0}$',
             '$||\\nabla u - \\nabla u_h||_{\Omega, 0}$'
             ]
errorMatrix = np.zeros((2, maxit), dtype=np.float)
NDof = np.zeros(maxit, dtype=np.float)

for i in range(maxit):
    print("The {}-th computation:".format(i))

    space1 = LagrangeFiniteElementSpace(mesh, p=1)

    spacep = LagrangeFiniteElementSpace(mesh, p=p)
    NDof[i] = space.number_of_global_dofs()

    uh = space.function()
    if d == 2:
        A = spacep.stiff_matrix()
        P = space1.stiff_matrix()
    elif d == 3:
        A = spacep.parallel_stiff_matrix(q=p)
        P = space1.parallel_stiff_matrix(q=1)

    F = spacep.source_vector(pde.source)


    errorMatrix[0, i] = spacep.integralalg.L2_error(pde.solution, uh)
    errorMatrix[1, i] = spacep.integralalg.L2_error(pde.gradient, uh.grad_value)

    if i < maxit-1:
        mesh.uniform_refine()



if d == 2:
    fig = plt.figure()
    axes = fig.gca(projection='3d')
    uh.add_plot(axes, cmap='rainbow')
elif d == 3:
    print('The 3d function plot is not been implemented!')

showmultirate(plt, 0, NDof, errorMatrix,  errorType, propsize=20)

plt.show()
