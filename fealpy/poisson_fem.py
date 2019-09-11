
import numpy as np
import matplotlib.pyplot as plt
from fealpy.pde.poisson_2d import CosCosData
from fealpy.functionspace import LagrangeFiniteElementSpace
from fealpy.boundarycondition import DirichletBC
from scipy.sparse.linalg import spsolve

pde = CosCosData()

mesh = pde.init_mesh(n=5, meshtype='tri')

space = LagrangeFiniteElementSpace(mesh, p=1, q=3)
uh = space.function()

A = space.stiff_matrix()
b = space.source_vector(pde.source)

bc = DirichletBC(space, pde.dirichlet)
A, b = bc.apply(A, b)

uh[:] = spsolve(A, b)

uI = space.interpolation(pde.solution)
e = uh - uI
l2 = np.sqrt(np.mean(e**2))

L2 = space.integralalg.L2_error(pde.solution, uh)
H1 = space.integralalg.L2_error(pde.gradient, uh.grad_value)

print({'l_2 error': l2, 'L_2 error': L2, 'H_1 error': H1})

uh.add_plot(plt)
plt.show()

