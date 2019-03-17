function e = getmaxerror(X,T,U,u_exact)
%%  GETMAXERROR �����ģ���
%       E(h,\tau) = max_{x_i,t_j}| u_exact(x_i,t_j) - U(i,j)| 
%                 = O( \tau + h^2)
%
% ���������
%       X ����Ϊ N  �����������ռ��ʷ�
%       T ����Ϊ M  ����������ʱ���ʷ�
%       U N*M �ľ���U(:,i) ��ʾ�� i ��ʱ�䲽����ֵ��
%       u_exact �����������⺯��
% ���������
%       e ���ģ���
%
% ���ߣ�κ���t <weihuayi@xtu.edu.cn>

[x,t] = meshgrid(X,T);
ue = u_exact(x',t');
e = max(max(abs(ue - U)));