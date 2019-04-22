function pde = modeldata()
%% MODELDATA
%  u(x) = sin(x)/sin(1) - x
%  Du(x) = cos(x)/sin(1)
%  f(x) = -x

pde = struct('exactu',@exactu,'f',@f,'Du',@Du);
%% ��ȷ��
function z = exactu(x)
z = sin(x)/sin(1) - x;
end
%% �Ҷ���
function z = f(x)
z = -x;
end
%% ��ȷ���ݶ�
function z = Du(x)
z = cos(x)/sin(1);
end 
end 