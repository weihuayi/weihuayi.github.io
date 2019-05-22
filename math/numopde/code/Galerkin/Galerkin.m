function uh = Galerkin(pde,I,n,option)
%% GALERKIN 组装矩阵  A 和右端向量 b， 并求解 
%
%   pde: 数据模型 
%   I : 模型区间 
%   n ：空间维数 

% 区间长度 
h = I(2) - I(1);

% 区间 [0,1] 上的 Gauss 积分点及权重 
[lambda, weight] = gquadpts1d(option.quadOrder);

% 积分点的个数
nQuad = length(weight); 

%% 构造矩阵 A 和 b
A = zeros(n,n);
b = zeros(n,1);
for q = 1:nQuad
  gx = lambda(q);
  w = weight(q);
  [phi, gradPhi] = basis(gx, n);
  A = A + (-gradPhi*gradPhi' + phi*phi')*w;
  b = b + pde.source(gx)*phi*w;
end
A = h*A;
b = h*b;

%% 求解
uh = A\b;
