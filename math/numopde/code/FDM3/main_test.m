%% һάһά���񶯷������޲�ַ��������Խű� main_test.m
%   ���β��ԣ�
%       �Ը�ʽ (theta = 0)
%       ����ʽ��theta = 0.5)
%   �����ӻ���ֵ��������
%
% ���ߣ�κ���t <weihuayi@xtu.edu.cn> 

t0 = 0;
t1 = 2;
x0 = 0;
x1 = 1;
pde = model_data(t0, t1, x0, x1); %ģ�����ݽṹ��

% �Ը�ʽ
[X,T,U] = wave_equation_fd1d(100,800,pde);
showvarysolution(X,T,U);% ����ʱ��仯��ʽ��ʾ��ֵ��
showsolution(X,T,U); % �Զ�Ԫ������ʽ��ʾ��ֵ��

% ����ʽ
[X,T,U] = wave_equation_fd1d(100,400,pde,0.5);
showvarysolution(X,T,U);% ����ʱ��仯��ʽ��ʾ��ֵ��
showsolution(X,T,U); % �Զ�Ԫ������ʽ��ʾ��ֵ��
