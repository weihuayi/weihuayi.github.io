%% ׼����ʼ����

% ����[a,b]
a = 0; 
b = 1;

%�����ʷֳߴ�
h = 0.1;

% ΢�ַ���ģ�����ݡ����� sindata ����һ���ṹ�� pde
% pde.f : �Ҷ����
% pde.exactu : ��⺯��
% pde.Du ����⵼��
% pde.g_D: D �ϱ߽���������
pde = sindata();

% �趨Gauss���־���
option.fQuadOrder = 3;
option.errQuadOder = 3;

%% �����ʷ�
[node,elem,bdFlag] = intervalmesh(a,b,h);

%% ��װ�նȾ���A���Ҷ�����b���߽������������
uh = Poisson1d(node, elem, pde, bdFlag,option);

%% ���� L2 �� H1 ��������ӻ�
errL2 = getL2error1d(node,elem,pde.exactu,uh,option.errQuadOder);
errH1 = getH1error1d(node,elem,pde.Du,uh,option.errQuadOder);
showsolution1d(node,elem,uh,'-+k');

