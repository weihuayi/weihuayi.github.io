function [X,T,U] = advection_fd1d(NS,NT,pde,method)
%% WAVE_EQUATION_FD1D �������޲�ַ�������һά˫������
%   
%   ���������
%       NS ���ͣ��ռ��ʷֶ���.
%       NT ���ͣ�ʱ���ʷֶ���.
%       pde �ṹ�壬������΢�ַ���ģ�͵���֪���ݣ�
%                  ��߽硢��ʼ��ϵ�����Ҷ��������.
%       method �ַ���������������ø�ʽ
%           'explicity' �� 'e' �� 'E' ����ʽӭ���ʽ
%           'inv explicity'�� 'inve' �� 'invE': ����ʽӭ���ʽ
%           'implicity' �� 'i' �� 'I' : ��ʽӭ���ʽ
%           'inv implicity' �� 'invi' �� 'invI', ����ʽӭ���ʽ
%           'explicity center' �� 'ec' �� 'EC' : ��ʽ���ĸ�ʽ
%           'implicity center' �� 'ic' �� 'IC': ��ʽ���ĸ�ʽ
%           'explicity lax' �� 'el' �� 'EL': ��ʽ Lax ��ʽ
%           'explicity laxw' �� 'elw' �� 'ELW': ��ʽ Lax windroff ��ʽ 
%           'leap frog' �� 'lf' �� 'LF' : ���ܸ�ʽ
%   ���������
%       X ����Ϊ NS+1 �����������ռ������ʷ�
%       T ����Ϊ NT+1 ����������ʱ�������ʷ�
%       U (NS+1)*(NT+1) ����U(:,i) ��ʾ�� i ��ʱ������񲿷��ϵ���ֵ��
%
%   ���ߣ�κ���t <weihuayi@xtu.edu.cn>

[X, h] = pde.space_grid(NS);
[T, tau] = pde.time_grid(NT);
N = length(X);
M = length(T);


U = zeros(N, M);
% ��ֵ����
U(:, 1) = pde.init_solution(X); 
a = pde.a();
r = a*tau/h;
% ��ֵ����
if a >= 0 % ���ֵ����
   U(1, :) = pde.left_solution(T);  
else
   U(end, :) = pde.right_solution(T); %�ұ�ֵ����
end



%% 
switch(method)
    case {'explicity','e','E'}
        explicity();
    case {'inv explicity','inve','invE'}
        inv_explicity();
    case {'explicity laxw','elw','ELW'}
        explicity_laxw();
    case {'explicity laxf','elf','ELF'}
        explicity_laxf();
    case {'implicity','i','I'}
        implicity();
    case {'inv implicity','invi','invI'}
        inv_implicity();
    case {'explicity center', 'ec','EC'}
        explicity_center();
    case {'implicity center', 'ic','IC'}
        implicity_center();
    case {'leap frog','lf','LF'}
        leap_frog();
    otherwise
        disp(['Sorry, I do not know your ', method]);
end

    function explicity()
        for i = 2:M
           if a > 0
               U(2:end, i) = U(2:end, i-1) - r*(U(2:end, i-1) - U(1:end-1, i-1));
           else
               U(1:end-1, i) = U(1:end-1, i-1) - r*(U(2:end, i-1) - U(1:end-1, i-1));
           end
        end    
    end

    function inv_explicity()
        for i = 2:M
           if a > 0
               U(2:end-1, i) = U(2:end-1, i-1) - r*(U(3:end, i-1)-U(2:end-1, i-1));
               U(end, i) = 2*U(end-1, i)-U(end-2, i);
           else
               U(2:end-1, i) = U(2:end-1, i-1) - r*(U(2:end-1, i-1) - U(1:end-2, i-1));
               U(1, i) = 2*U(2, i) - U(3, i);
           end
        end    
    end

    function explicity_laxf()
        for i = 2:M
           U(2:end-1, i) = (U(1:end-2, i) + U(3:end, i-1))/2 - r*(U(3:end, i-1)-U(1:end-2, i-1))/2;
           if a > 0
               U(end, i) = 2*U(end-1, i)-U(end-2, i);
           else
               U(1, i) = 2*U(2, i) - U(3, i);
           end
        end    
    end

    function explicity_laxw()
        for i = 2:M
           U(2:end-1, i) = U(2:end-1, i-1) - 0.5*r*(U(3:end, i-1)-U(1:end-2, i-1)) + ...
               0.5*r*r*(U(3:end, i-1)- 2*U(2:end-1, i-1)+U(1:end-2, i-1));
           if a > 0
               %U(end, i) = 2*U(end-1, i)-U(end-2, i);
               %U(end, i) = U(end-1, i);
               U(end, i) = U(end, i-1) - r*(U(end, i-1) - U(end-1, i-1));
           else
               %U(1, i) = 2*U(2, i) - U(3, i);
               %U(1, i) = U(2, i);
               U(1, i) = U(1, i-1) - r*(U(2, i-1) - U(1, i-1));
           end
        end    
    end

    function implicity()
        if a > 0
            d = (1+r)*ones(N-1, 1);
            c = -r*ones(N-2, 1);
            A = diag(d) + diag(c, -1);
            for i = 2:M
                F = zeros(N-1, 1);
                F(1) = r*U(1, i);
                U(2:end, i) = A\(U(2:end, i-1)+F);
            end
        else
            d = (1-r)*ones(N-1, 1);
            c = r*ones(N-2, 1);
            A = diag(d) + diag(c, 1);
            for i = 2:M
                F = zeros(N-1, 1);
                F(end) = -r*U(end, i);
                U(1:end-1, i) = A\(U(1:end-1, i-1)+F);
            end
        end
    end
    function explicity_center()
        for i = 2:M
            U(2:end-1, i) = U(2:end-1, i-1) - r*(U(3:end, i-1)-U(1:end-2, i-1))/2;
            if a > 0
                U(end, i) = 2*U(end-1, i)-U(end-2, i);
            else
                U(1, i) = 2*U(2, i) - U(3, i);
            end
        end
    end

    function implicity_center()

    end

    function leap_frog()

    end

end