function showvarysolution(X,T,U,UE)
%%  SHOWVARYSOLUTION  ��ʾ��ֵ������ʱ��ı仯
% 
%  ���������
%       X ����ΪN�����������ռ������ʷ�
%       T �ڶ�ΪM����������ʱ�������ʷ�
%       U N*M ����U(:,i) ��ʾ��  i ��ʱ��������ϵ���ֵ��
%       UE N*M ����UE(:,i) ��ʾ�� i ��ʱ��������ϵ���ֵ��
%   ���ߣ�κ���t <weihuayi@xtu.edu.cn>   

M = size(U,2);
figure
xlabel('X');
ylabel('U');
s = [X(1),X(end),min(min(U)),max(max(U))];
axis(s);
for i = 1:M
   if nargin < 4
      plot(X,U(:,i),'-b+');
   else 
      plot(X,U(:,i),'-b+',X,UE(:,i),'-rs');
   end
   axis(s);
   pause(0.01);
   title(['T=',num2str(T(i)),' ʱ�̵��¶ȷֲ�'])
end