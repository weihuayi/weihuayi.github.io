function showsolution(X,T,U)
%%  SHOWSOLUTION  �Զ�Ԫ������ʽ��ʾ��ֵ��
% 
%  ���������
%       X ����ΪN�����������ռ������ʷ�
%       T �ڶ�ΪM����������ʱ�������ʷ�
%       U N*M ����U(:,i) ��ʾ��  i ��ʱ������񲿷��ϵ���ֵ��
%
%   ���ߣ�κ���t <weihuayi@xtu.edu.cn>   

[x,t] = meshgrid(X,T);
mesh(x,t,U');
xlabel('X');
ylabel('T');
zlabel('U(X,T)');

end


