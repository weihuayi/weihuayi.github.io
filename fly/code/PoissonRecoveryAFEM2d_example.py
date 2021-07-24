#!/usr/bin/env python3
#

import numpy as np
import matplotlib.pyplot as plt

from scipy.sparse.linalg import spsolve
import pyamg

from fealpy.decorator import cartesian
from fealpy.mesh import TriangleMesh
from fealpy.functionspace import LagrangeFiniteElementSpace
from fealpy.boundarycondition import DirichletBC

from fealpy.mesh.adaptive_tools import mark
from fealpy.tools.show import showmultirate

class PDE_0:
    """
    -\Delta u = f
    u = x**a
    """
    def __init__(self, a=0.6):
        self.a = a 

    def domain(self):
        return np.array([0, 1, 0, 1])

    def init_mesh(self, n=4):
        """ generate the initial mesh
        """
        node = np.array([
            (0, 0),
            (1, 0),
            (1, 1),
            (0, 1)], dtype=np.float64)

        cell = np.array([(1, 2, 0), (3, 0, 2)], dtype=np.int_)
        mesh = TriangleMesh(node, cell)
        mesh.uniform_refine(n)
        return mesh


    @cartesian
    def solution(self, p):
        """ The exact solution 
        Parameters
        ---------
        p : 


        Examples
        -------
        p = np.array([0, 1], dtype=np.float64)
        p = np.array([[0, 1], [0.5, 0.5]], dtype=np.float64)
        """
        x = p[..., 0]
        y = p[..., 1]
        pi = np.pi
        val = np.power(x, self.a)
        return val 


    @cartesian
    def source(self, p):
        """ The right hand side of Possion equation
        INPUT:
            p: array object,  
        """
        x = p[..., 0]
        y = p[..., 1]
        a = self.a
        val = a*(1-a)*np.power(x, a-2) 
        return val

    @cartesian
    def gradient(self, p):
        """ The gradient of the exact solution 
        """
        x = p[..., 0]
        y = p[..., 1]
        a = self.a
        val = np.zeros(p.shape, dtype=np.float64)
        val[..., 0] = a*np.power(x, a-1) 
        return val # val.shape == p.shape


    @cartesian
    def dirichlet(self, p):
        return self.solution(p)

pde = PDE_0(a=0.8) 
mesh = pde.init_mesh(n=4)

theta = 0.2
maxit = 75 
p = 1
errorType = ['$|| u - u_h||_{0}$',
             '$||\\nabla u - \\nabla u_h||_{0}$',
             '$||\\nabla u - G(\\nabla u_h)||_{0}$',
             '$||\\nabla u_h - G(\\nabla u_h)||_{0}$',
             '$||u - u_I||_{0}$']

NDof = np.zeros((maxit,), dtype=np.int_)
errorMatrix = np.zeros((len(errorType), maxit), dtype=np.float64)

mesh.add_plot(plt)
plt.savefig('./test-0.png')
plt.close()

for i in range(maxit):
    print('step:', i)
    space = LagrangeFiniteElementSpace(mesh, p=p)
    A = space.stiff_matrix(q=6)
    F = space.source_vector(pde.source, q=6)

    NDof[i] = space.number_of_global_dofs()
    bc = DirichletBC(space, pde.dirichlet) 

    uh = space.function()
    A, F = bc.apply(A, F, uh)
    uh[:] = spsolve(A, F)

    rguh = space.grad_recovery(uh)
    uI = space.interpolation(pde.solution)
    errorMatrix[0, i] = space.integralalg.error(pde.solution, uh.value)
    errorMatrix[1, i] = space.integralalg.error(pde.gradient, uh.grad_value)  
    errorMatrix[2, i] = space.integralalg.error(pde.gradient, rguh.value) 
    eta = space.recovery_estimate(uh)
    errorMatrix[3, i] = np.sqrt(np.sum(eta**2))
    errorMatrix[4, i] = space.integralalg.error(pde.solution, uI.value, q=6)

    if i < maxit - 1:
        isMarkedCell = mark(eta, theta=theta)
        mesh.bisect(isMarkedCell)
        mesh.add_plot(plt)
        plt.savefig('./test-' + str(i+1) + '.png')
        plt.close()

uh.add_plot(plt)

fig = plt.figure()
axes = fig.gca()
mesh.add_plot(axes)
showmultirate(plt, maxit - 5, NDof, errorMatrix, errorType)
plt.show()
