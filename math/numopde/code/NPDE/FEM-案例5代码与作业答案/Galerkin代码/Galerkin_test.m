%% ׼����ʼ����

% ΢�ַ���ģ�����ݡ����� modeldata ����һ���ṹ�� pde
% pde.f : �Ҷ����
% pde.exactu : ��⺯��
% pde.Du ����⵼��
pde = modeldata();


% �������㴦�����
x = [1/4;1/2;3/4];
format long e
u = pde.exactu(x) ;
xt = 0:0.01:1;
plot(xt,pde.exactu(xt),'-r');
hold on

% ����
I = [0,1];

% ���־���
option.quadOrder = 10;

% �ռ�ά����������������
n=1;
% Galerkin �������
uh = Galerkin(pde,I,n,option);
% ��ʾ��ֵ��ͼ��
showsolution(uh,':k');
% �������㴦����ֵ��
v = basis(x,n);
u_1 = v'*uh

%%
n=2;
uh = Galerkin(pde,I,n,option);
showsolution(uh,'-.b');
v = basis(x,n); 
u_2 = v'*uh

%%
n=3;
uh = Galerkin(pde,I,n,option);
showsolution(uh,'-.m');
v = basis(x,n); 
u_3 = v'*uh

%%
n=4;
uh = Galerkin(pde,I,n,option);
showsolution(uh,'--c');
v = basis(x,n);
u_4 = v'*uh

legend('u^*','u_1','u_2','u_3','u_4');
xlabel('X')
ylabel('Y')
u = [u'; u_1';u_2';u_3'; u_4']