function [X,T,U] = wave_equation_fd1d(NS,NT,pde,theta)
%% WAVE_EQUATION_FD1D �������޲�ַ�������һά���񶯷���
%   
%   ���������
%       NS ���ͣ��ռ��ʷֶ���.
%       NT ���ͣ�ʱ���ʷֶ���.
%       pde �ṹ�壬������΢�ַ���ģ�͵���֪���ݣ�
%                  ��߽硢��ʼ��ϵ�����Ҷ��������.
%       theta ˫�������ͣ� ����ʽ������ �� [0,1] ֮�䣬 
%             �� theta=0 ʱ����ʽΪ�Ը�ʽ. 
%   ���������
%       X ����Ϊ NS+1 �����������ռ������ʷ�
%       T ����Ϊ NT+1 ����������ʱ�������ʷ�
%       U (NS+1)*(NT+1) ����U(:,i) ��ʾ�� i ��ʱ������񲿷��ϵ���ֵ��
%
%   ���ߣ�κ���t <weihuayi@xtu.edu.cn>

if nargin < 4
    theta = 0; % Ĭ�����Ը�ʽ
end
[X,h] = pde.space_grid(NS);
[T,tau] = pde.time_grid(NT);
N = length(X);M = length(T);
r = pde.a()*tau/h;
if r >=1 && theta==0
   error('ʱ��ռ���ɢ�������Ը�ʽ���ȶ�������') 
end
r2 = r*r;
U = zeros(N,M);
% ��ֵ����
U(:,1) = pde.u_initial(X); 
U(2:end-1,2) = r2/2*(U(1:end-2,1)+U(3:end,1)) + (1-r2)*U(2:end-1,1)...
    + tau*pde.udt_initial(X(2:end-1));
% ��ֵ����
U(1,:) = pde.u_left(T);
U(end,:) = pde.u_right(T);

%% ����ʽ
d = 1 + 2*ones(N-2,1)*r2*theta;
c = -ones(N-3,1)*r2*theta;
A2 = diag(c,-1) + diag(c,1)+diag(d);

d = 2 - 2*ones(N-2,1)*r2*(1-2*theta);
c = ones(N-3,1)*r2*(1-2*theta);
A1 = diag(c,-1) + diag(c,1)+diag(d);

d = -1 - 2*ones(N-2,1)*r2*theta;
c = ones(N-3,1)*r2*theta;
A0 = diag(c,-1) + diag(c,1)+diag(d);
for i=3:M
    RHS = tau*tau*pde.f(X,T(i));
    RHS(2) = RHS(2) + theta*r2*U(1,i) + ...
        (1-2*theta)*r2*U(1,i-1)+ theta*r2*U(1,i-2);
    RHS(end-1) = RHS(end-1) + theta*r2*U(end,i) + ...
        (1-2*theta)*r2*U(end,i-1)+ theta*r2*U(end,i-2);
    U(2:end-1,i) = A2\(A1*U(2:end-1,i-1) + A0*U(2:end-1,i-2)+RHS(2:end-1));
end

end
