%% һάһά���񶯷������޲�ַ��������Խű� main_test.m

t0 = 0;
t1 = 2;
x0 = 0;
x1 = 1;
NX = 80;
NT = 320;

pde = model_data_hlz(t0, t1, x0, x1,NT,NX); 

[X,T,U] = wave_equation_fd1d_hlz(pde);

e = get_maxreeor_hlz(X,T,U,pde);

disp(e);

show_solution_hlz(X,T,U,pde);