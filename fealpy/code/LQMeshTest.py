
import numpy as np


from fealpy.mesh import LagrangeQuadrangleMesh
from fealpy.functionspace import IsoLagrangeFiniteElementSpace
from fealpy.decorator import cartesian


@cartesian
def u(p):
    x = p[..., 0]
    y = p[..., 1]
    return x**2*y**2

@cartesian
def gu(p):
    x = p[..., 0]
    y = p[..., 1]
    val = np.zeros_like(p)
    val[..., 0] = 2*x*y**2
    val[..., 1] = 2*x**2*y
    return val 

node = np.array([
    (0, 0),
    (0, 1),
    (1, 0),
    (1, 1)], dtype=np.float64)
cell = np.array([(0, 1, 2, 3)], dtype=np.int_)
mesh = LagrangeQuadrangleMesh(node, cell, p=2)
#mesh.uniform_refine(n=2)
space = IsoLagrangeFiniteElementSpace(mesh, p=2)


qf = mesh.integrator(2)
bcs, ws = qf.get_quadrature_points_and_weights()
ps = mesh.bc_to_point(bcs)
print(bcs)
print(ps)

uI = space.interpolation(u) 
val = uI.grad_value(bcs)
print('uI.grad:', val-gu(ps))
error1 = space.integralalg.error(gu, uI.grad_value) 
print(error1)

