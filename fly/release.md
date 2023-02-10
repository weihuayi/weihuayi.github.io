# 发布记录


## v1.1.10

日期：2021.06.02

今天发布了 FEALPy 的 v1.1.10 到 [PYPI](https://pypi.org/project/fealpy/1.1.10/),
用户可以用如下命令升级安装。

```
pip install -U fealpy
```

这个版本主要有如下更新：
1. 由变量的命名约定，更正了二维和三维网格对象中的变量名字，如 NVC（Number of
   Vertices of Cell） 等。
1. 清理了测试目录下的测试文件，把老的测试文件都移动到 example 目录下，目前 test
   目录下增加了如下文件
    * `mesh_test.py`
    * `space_test.py`
    * `quadrature_test.py`
    * `app_test.py`
   用于标准的单元测试
1. 清理了网格对象中的构建邻接关系矩阵代码中的 bug。


### 使用过程中的问题反馈

在使用 FEALPy 的过程中，如果遇到安装、代码运行出错、 bug 或者希望 FEALPy
加入新的功能， 强烈建议首先在 github、gitlab 或者 gitee 的 issues 页面提交相关信息， 
网址如下：

```
https://github.com/weihuayi/fealpy/issues
https://gitlab.com/weihuayi/fealpy/issues
https://gitee.com/whymath/fealpy/issues
```

对于安装的问题，issue 中一定要提供如下信息
1. 系统信息
2. fealpy 的安装方式，比如是克隆源码安装、还是直接 pypi 安装。 
3. 安装报错的信息

对于代码运行出错的信息，issue 中一定要提供如下信息
1. 系统信息
2. fealpy 的版本信息：
```
import fealpy as fly
print(fly.__version__)
```
3. 出错的代码，最好是可以重现你问题的简短代码。
4. 出错的信息

对于新的功能，在 issue 中要尽量描述清楚这个新的功能要满足一个什么的需要，这个功能可以应用什么场景下。

### 参考资料
1. [如何提出一个 issue](https://github.com/eggjs/egg/issues/3310)
1. [记录一些常见的沟通问题](https://github.com/atian25/blog/issues/29)




