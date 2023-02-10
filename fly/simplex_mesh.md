# 单纯形网格 (Simplex Mesh)

## 重心坐标 

**重心坐标**是一个非常重要的概念， 它是定义单纯形网格的基础, 也是构造单纯形网格
上有限元基函数的 基础, 下面介绍重心坐标的相关知识。

设 $$\{\mathbf x_i = (x_{i,0}, x_{i, 1}, \cdots, x_{i, d-1})^T\}_{i=0}^{d}$$ 是
$$\mathbb R^d$$ 空间中的 $$d+1$$ 个点，如果它们不在一个超平面上， 即 $$d$$ 维向量集合
$$\{\mathbf x_0\mathbf x_i\}_{i=1}^d$$ 是线性独立的，也等价于下面的矩阵非奇异
$$
\begin{equation}
    \mathbf A =\begin{pmatrix}
        x_{0, 0} & x_{1, 0} & \cdots & x_{d, 0} \\
        x_{0, 1} & x_{1, 1} & \cdots & x_{d, 1} \\
        \vdots   & \vdots   & \ddots & \vdots \\
        x_{0, d-1} & x_{1, d-1} & \cdots & x_{d, d-1}\\
        1 & 1 & \cdots & 1
    \end{pmatrix}
\end{equation}
$$

 
给定任意点 $$\mathbf x=(x_0, x_1, \cdots, x_{d-1})^T\in \mathbb R^d$$, 可以得到
一组实数 值 $$\mathbf \lambda := (\lambda_0(\mathbf x), \lambda_1(\mathbf x),
\cdots, \lambda_d(\mathbf x))^T$$, 满足如下的方程
$$
\mathbf A \mathbf \lambda=
\begin{pmatrix}
    \mathbf x \\ 1
\end{pmatrix}
$$
即
$$
\mathbf x = \sum\limits_{i=0}^{d}\lambda_i(\mathbf x) \mathbf x_i,
\text{ with} \sum\limits_{i=0}^{d}\lambda_i(\mathbf x) = 1.
$$

点集 $$\{\mathbf x_i\}_{i=0}^d$$ 的凸壳
$$
\tau = \{\mathbf x = \sum_{i=0}^{d}\lambda_i\mathbf x_i | 0\leq \lambda_i \leq
1, \sum_{i=0}^d\lambda_i = 1\}
$$
就称为由点集 $$\{\mathbf x_i\}_{i=0}^d$$ 生成的几何 $$d$$-单纯形。 例如， 区间是
1-单纯形，三角形是一个 2-单纯形， 四面体是一个 3-单纯形。

而 $$\lambda_0(\mathbf x)$$, $$\lambda_1(\mathbf x)$$, $$\cdots$$,
$$\lambda_{d}(\mathbf x)$$ 就称为 $\mathbf x$$ 关于点集 $$\{\mathbf
x_i\}_{i=0}^d$$ 重心坐标 。  易知 $$\lambda_0(\mathbf x)$$, $$\lambda_1(\mathbf x)$$,
$$\cdots$$, $$\lambda_{d}(\mathbf x)$$ 是 关于 $$\mathbf x$$ 的线性函数并且，
$$
\lambda_i(\mathbf x_j) = 
\begin{cases}
    1, & i = j\\
    0, & i\not= j
\end{cases}, 
i, j = 0, \cdots, d
$$
## FEALPy 中的单纯形网格 

### 一维区间网格 `IntervalMesh`

### 二维三角形网格 `TriangleMesh`

### 三维四面体网格 `TetrahedronMesh`


### 单纯形网格对象中的程序命名约定


### 单纯形网格对象的接口

