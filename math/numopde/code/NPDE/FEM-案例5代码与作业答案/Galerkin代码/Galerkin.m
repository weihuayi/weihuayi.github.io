function uh = Galerkin(pde,I,n,option)
%% GALERKIN ��װ���� A ���Ҷ����� b �������
%
%   pde: ģ������
%   I : ����
%   n ���ռ�ά��

% ���䳤��
h = I(2) - I(1);

% ���� [0,1] �ϵ� Gauss ���ֵ㼰Ȩ��
[lambda, weight] = quadpts1d(option.quadOrder);
%���ֵ����
nQuad = length(weight); 

%% ���� A �� b
A = zeros(n,n);
b = zeros(n,1);
for q = 1:nQuad
  gx = lambda(q);
  w = weight(q);
  [phi,gradPhi] = basis(gx,n);
  A = A+(-gradPhi*gradPhi' + phi*phi')*w;
  b = b + pde.f(gx)*phi*w;
end
A = h*A;
b = h*b;

%% ���
uh = A\b;

