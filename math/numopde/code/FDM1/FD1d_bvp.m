function [uh, x] = FD1d_bvp(model, NS)
%*************************************************************
%% FD1d_bvp �������Ĳ�ָ�ʽ��������ֵ����.
%
% Input
% -----
%   model : ģ������
%   NS    �������ʷֶ���
% Output
% ------
%   uh ��������������Ϊ NS+1�� ������
%   x  : ������������Ϊ NS+1�� ����ڵ�
%      

[x, h] = model.init_mesh(NS);
NV = NS + 1;

%
%  �������Բ�ַ�����ϵ������
%

c1 = -1/h/h;
c2 = 2/h/h;
g = [c1*ones(1, NV-2), 0];
c = [0, c1*ones(1, NV-2)];
d = [1, c2*ones(1, NV-2), 1];
A = diag(g, -1) + diag(d) + diag(c,1);

%
%  �������Բ�ַ������Ҷ���
%

rhs = model.source(x);
rhs(1) = model.solution(x(1));
rhs(end) = model.solution(x(end));

%
%  �����������ϵͳ.
%

uh = A \ rhs;
end

