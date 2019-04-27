function show_solution_hlz(X,T,U,pde)

[x, t] = meshgrid(X, T);
u = pde.real_solution(x,t)';

[T ,tau] = pde.time_grid();
l = 0.5/tau + 1;
d = 0.5/tau;
r = l+3*d;

subplot(2,2,1);
plot(X,U(:,l:d:r));
ylim([-1,1.5]);
legend('t=0.5','t=1.0','t=1.5','t=2.0');
title('��ֵ��ͼ��');

subplot(2,2,2);
plot(X,u(:,l:d:r));
ylim([-1,1.5]);
legend('t=0.5','t=1.0','t=1.5','t=2.0');
title('���ͼ��');

subplot(2,2,4);
mesh(x,t,u');
zlim([-1,2]);
title('���ͼ��');

subplot(2,2,3);
mesh(x,t,U');
zlim([-1,2]);
title('��ֵ��ͼ��')

end
