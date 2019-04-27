function [X, T, U] = wave_equation_fd1d_hlz(pde)
%% WAVE_EQUATION_FD1D �������޲�ַ�������һά���񶯷���
%   
%   ���������

%       pde �ṹ�壬������΢�ַ���ģ�͵���֪���ݣ�
%                  ��߽硢��ʼ��ϵ�����Ҷ��������.
 
%   ���������
%       X ����Ϊ NS+1 �����������ռ������ʷ�
%       T ����Ϊ NT+1 ����������ʱ�������ʷ�
%       U (NS+1)*(NT+1) ����U(:,i) ��ʾ�� i ��ʱ������񲿷��ϵ���ֵ��


[X,h ] = pde.space_grid();
[T,tau ] = pde.time_grid();

N = length(X);
M = length(T);
r = pde.a()*tau/h;
if r >1 
   error('ʱ��ռ���ɢ�������Ը�ʽ���ȶ�������') 
end
r2 = r*r;
U = zeros(N,M);
% ��ֵ����
U(:,1) = pde.init_solution(X); 
U(:, 2) =U(:, 1)+ tau*pde.init_dt_solution(X);
% ��ֵ����
U(1,:) = pde.left_solution(T);
U(end,:) = pde.right_solution(T);

%% ����ʽ
d = ones(N-2,1);
A2 = diag(d);

d = 2 - 2*ones(N-2,1)*r2;
c = ones(N-3,1)*r2;
A1 = diag(c,-1) + diag(c,1)+diag(d);

d = -1*ones(N-2,1);
A0 = diag(d);
for i=3:M
    U(2:end-1,i) = A2\(A1*U(2:end-1,i-1) + A0*U(2:end-1,i-2));
end

end
