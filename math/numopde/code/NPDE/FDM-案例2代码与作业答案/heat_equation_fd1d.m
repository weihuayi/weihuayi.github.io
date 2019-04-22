function [X,T,U] = heat_equation_fd1d(NS,NT,pde,method)
%% HEAT_EQUATION_FD1D �������޲�ַ�������һά�ȴ�������
%   
%   ���������
%       NS ���ͣ��ռ��ʷֶ���
%       NT ���ͣ�ʱ���ʷֶ���
%       pde �ṹ�壬������΢�ַ���ģ�͵���֪���ݣ�
%                  ��߽硢��ʼ��ϵ�����Ҷ��������
%       method �ַ������������������ɢ��ʽ
%           F �� f �� forward �� ��ǰ��ָ�ʽ
%           B �� b �� backward �� ����ָ�ʽ
%           CN �� cn �� crank-nicholson �� Crank-Nicholson ��
%                      -- ����ԳƸ�ʽ( Crank-Nicholson ��ʽ)
%   ���������
%       X ����Ϊ NS+1 �����������ռ������ʷ�
%       T ����Ϊ NT+1 ����������ʱ�������ʷ�
%       U (NS+1)*(NT+1) ����U(:,i) ��ʾ�� i ��ʱ������񲿷��ϵ���ֵ��
%
%   ���ߣ�κ���t <weihuayi@xtu.edu.cn>

[X,h] = pde.space_grid(NS);
[T,tau] = pde.time_grid(NT);
N = length(X);M = length(T);
r = pde.a()*tau/h/h;
if r >= 0.5 && ismember(method,{'F','f','forward'})
    error('ʱ��ռ���ɢ��������ǰ��ֵ��ȶ�������')
end
U = zeros(N,M);
U(:,1) = pde.u_initial(X);
U(1,:) = pde.u_left(T);
U(end,:) = pde.u_right(T);
switch(method)
    case {'F','f','forward'}
        forward();
    case {'B','b','backward'}
        backward();
    case {'CN','cn','crank-nicholson','Crank-Nicholson'}
        crank_nicholson();
    otherwise
        disp(['Sorry, I do not know your ', method]);
end
%% ��ǰ��ַ���
    function forward()
        d = 1 - 2*ones(N-2,1)*r;
        c = ones(N-3,1)*r;
        A = diag(c,-1) + diag(c,1)+diag(d);
        for i = 2:M
            RHS = tau*td.f(X,T(i));
            RHS(2) = RHS(2) + r*U(1,i-1);
            RHS(end-1) = RHS(end-1) + r*U(end,i-1);
            U(2:end-1,i)=A*U(2:end-1,i-1)+ RHS(2:end-1);
        end
    end
%% ����ַ���
    function backward()
        d = 1 + 2*ones(N-2,1)*r;
        c = -ones(N-3,1)*r;
        A = diag(c,-1) + diag(c,1)+diag(d);    
        for i = 2:M
            RHS = tau*td.f(X,T(i));
            RHS(2) = RHS(2) + r*U(1,i);
            RHS(end-1) = RHS(end-1) + r*U(end,i);
            U(2:end-1,i)=A\(U(2:end-1,i-1)+ RHS(2:end-1));
        end 
    end
%% ����ԳƸ�ʽ�� �� Crank_Nicholson ��ʽ
    function crank_nicholson()
        d1 = 1 + ones(N-2,1)*r;
        d2 = 1 - ones(N-2,1)*r;
        c = 0.5*ones(N-3,1)*r;
        A1 = diag(-c,-1) + diag(-c,1)+diag(d1);  
        A0 = diag(c,-1) + diag(c,1) + diag(d2);
        for i = 2:M
            RHS = tau*td.f(X,T(i));
            RHS(2) = RHS(2) + 0.5*r*(U(1,i)+U(1,i-1));
            RHS(end-1) = RHS(end-1) + ...
                0.5*r*(U(end,i)+U(end,i-1));
            U(2:end-1,i)=A1\(A0*U(2:end-1,i-1)+ RHS(2:end-1));
        end 
    end
end