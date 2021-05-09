# MSYS2


https://www.msys2.org/

##  环境配置

C:\msys64\mingw64  发送到桌面快捷方式

```
$ echo "Server = http://mirrors.ustc.edu.cn/msys2/REPOS/MINGW/i686/
Server = http://mirror.bit.edu.cn/msys2/REPOS/MINGW/i686/
Server = http://jaist.dl.sourceforge.net/project/msys2/REPOS/MINGW/i686/
Server = http://www.mirrorservice.org/sites/download.sourceforge.net/pub/sourceforge/m/ms/msys2/REPOS/MINGW/i686/
Server = ftp://148.251.42.38/MINGW/i686/
Server = http://downloads.sourceforge.net/project/msys2/REPOS/MINGW/i686/
" >> /etc/pacman.d/mirrorlist.mingw32 # 附加到文件尾部

$ echo " Server = http://mirrors.ustc.edu.cn/msys2/REPOS/MINGW/x86_64/
Server = http://mirror.bit.edu.cn/msys2/REPOS/MINGW/x86_64/
Server = http://jaist.dl.sourceforge.net/project/msys2/REPOS/MINGW/x86_64/
Server = http://www.mirrorservice.org/sites/download.sourceforge.net/pub/sourceforge/m/ms/msys2/REPOS/MINGW/x86_64/
Server = ftp://148.251.42.38/MINGW/x86_64/
Server = http://downloads.sourceforge.net/project/msys2/REPOS/MINGW/x86_64/
" >> /etc/pacman.d/mirrorlist.mingw64

$ echo "Server = http://mirror.bit.edu.cn/msys2/REPOS/MSYS2/$arch/
Server = http://mirrors.ustc.edu.cn/msys2/msys/$arch/
Server = http://jaist.dl.sourceforge.net/project/msys2/REPOS/MSYS2/$arch
Server = http://www.mirrorservice.org/sites/download.sourceforge.net/pub/sourceforge/m/ms/msys2/REPOS/MSYS2/$arch
Server = ftp://148.251.42.38/MSYS2/$arch
Server = http://downloads.sourceforge.net/project/msys2/REPOS/MSYS2/$arch
" >> /etc/pacman.d/mirrorlist.msys
```

更新 MSYS2 到最新

```
$ pacman -Suu
$ pacman -Sy
```

```
pacman -S make
pacman -S mingw-w64-x86_64-tools-git
pacman -S mingw-w64-x86_64-gcc-fortran
pacman -S mingw-w64-x86_64-cmake
pacman -S mingw-w64-x86_64-openblas
pacman -S mingw-w64-x86_64-metis
# python 3
pacman -S mingw-w64-x86_64-vtk
pacman -S mingw-w64-x86_64-cython
pacman -S mingw-w64-x86_64-python3
pacman -S mingw-w64-x86_64-python3-numpy
pacman -S mingw-w64-x86_64-python3-scipy
pacman -S mingw-w64-x86_64-python3-matplotlib
```



## old
安装最新的编译器和开发工具 
```
$ pacman -S base-devel # 基础工具
$ pacman -S mingw-w64-x86_64-toolchain # 编译器gcc, g++, gfortran
$ pacman -S git  # git 版本控制软件
$ pacman -S make  # make 程序
$ pacman -S mingw-w64-x86_64-cmake # CMake
$ pacman -S python3-pip
$ pacman -S cython
```

pacman -S mingw-w64-x86_64-python-numpy
pacman -S mingw-w64-x86_64-python-scipy
pacman -S mingw-w64-x86_64-python-matplotlib
pacman -S mingw-w64-x86_64-msmpi

pacman -S mingw-w64-x86_64-cython
pacman -S mingw-w64-x86_64-fftw

pacman -S mingw-w64-x86_64-vtk # 依赖 qt5

# Anaconda 

https://www.lfd.uci.edu/~gohlke/pythonlibs/

conda install -c conda-forge msmpi
conda install -c conda-forge mumps
pip install mpi4py
pip install PyMUMPS 
pip install pymumps --global-option="build_ext"  --global-option="-IC:\Users\why\anaconda3\Library\mingw-w64\include"  --global-option="-LC:\Users\why\anaconda3\Library\mingw-w64\lib"  

python setup.py build_ext --include-dirs="C:\Users\why\anaconda3\Library\mingw-w64\include"  --library-dirs="C:\Users\why\anaconda3\Library\mingw-w64\lib" -ldmumps_mpi -lmumps_common 
## 参考 

1. https://gitlab.uliege.be/am-dept/waves/wikis/build_win_msys

