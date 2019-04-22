%% һά�ȴ����������޲�ַ��������Խű� main_test.m
%   ���β��ԣ�
%       ��ǰ���
%       �����
%       ����ԳƸ�ʽ
%   �����ӻ���ֵ��������
%
% ���ߣ�κ���t <weihuayi@xtu.edu.cn> 

pde = model_data(); %ģ�����ݽṹ��

% ��ǰ��ָ�ʽ
[X,T,U] = heat_equation_fd1d(100,10000,pde,'forward');
showvarysolution(X,T,U);% ����ʱ��仯��ʽ��ʾ��ֵ��
showsolution(X,T,U); % �Զ�Ԫ������ʽ��ʾ��ֵ��

% ����ָ�ʽ
[X,T,U] = heat_equation_fd1d(100,100,pde,'backward');
showvarysolution(X,T,U);% ����ʱ��仯��ʽ��ʾ��ֵ��
showsolution(X,T,U); % �Զ�Ԫ������ʽ��ʾ��ֵ��

% ����ԳƸ�ʽ���� Crank-Nicholson ��ʽ
[X,T,U] = heat_equation_fd1d(100,100,pde,'crank-nicholson');
showvarysolution(X,T,U);% ����ʱ��仯��ʽ��ʾ��ֵ��
showsolution(X,T,U); % �Զ�Ԫ������ʽ��ʾ��ֵ��