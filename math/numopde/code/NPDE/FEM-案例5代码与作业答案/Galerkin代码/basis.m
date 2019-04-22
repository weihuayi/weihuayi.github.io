function [phi,gradPhi] = basis(x,n)
%% BASIS ���� n ά�ռ� n ���������� m(=length(x)) �����ϵ�ȡֵ
%
%  H_0^1([0,1]) �� n ά�����ӿռ䣬 ȡ w(x) = x*(1-x)��n ���������ֱ�Ϊ��
%          phi_i = w(x)*x^{i-1}, i = 1, 2,..., n
%
%  ���룺
%   x(1:m,1): ��
%   n: �ռ�ά��
%
%  �����
%   phi(1:n,1:m): phi(i,j) Ϊ�� i ���������ڵ� j �����ڴ��ĺ���ֵ.
%   gradPhi(1:n,1:m): gradPhi(i,j) Ϊ�� i ���������ڵ� j ���㴦�ĵ���ֵ.


m = length(x);% ��ĸ���
%% ����ֵ
phi = cumprod(ones(n,m)*diag(x),1)*diag(1-x);


%% �����ݶ�ֵ
t = repmat(x',n,1);
t = cumprod(t,1);
v = ones(n,m);
v(2:end,:) = t(1:end-1,:);
gradPhi = diag(1:n)*v-diag(2:n+1)*t;

