%% һάһά���񶯷������޲�ַ��������Խű� main_test.m
%   ���β��ԣ�
%       �Ը�ʽ (theta = 0)
%       ����ʽ��theta = 0.5)
%   �����ӻ���ֵ��������
%
% ���ߣ�κ���t <weihuayi@xtu.edu.cn> 

pde = model_data(); %ģ�����ݽṹ��

% �Ը�ʽ
[X,T,U] = wave_equation_fd1d(100,800,pde);
showvarysolution(X,T,U);% ����ʱ��仯��ʽ��ʾ��ֵ��
showsolution(X,T,U); % �Զ�Ԫ������ʽ��ʾ��ֵ��

% ����ʽ
[X,T,U] = wave_equation_fd1d(100,400,pde,0.5);
showvarysolution(X,T,U);% ����ʱ��仯��ʽ��ʾ��ֵ��
showsolution(X,T,U); % �Զ�Ԫ������ʽ��ʾ��ֵ��

