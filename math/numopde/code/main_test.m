%% һά˫���������޲�ַ��������Խű� main_test.m
%   ���β��ԣ�
%       �Ը�ʽ 
%       ����ʽ
%   �����ӻ���ֵ��������
%
% ���ߣ�κ���t <weihuayi@xtu.edu.cn> 

pde = model_data(0, 4, 0, 1); %ģ�����ݽṹ��
[X,T,U] = advection_fd1d(50, 400, pde, 'elw');
UE = pde.solution(X, T);
disp(max(abs(U(:) - UE(:))));
%showvarysolution(X, T, U, UE);

