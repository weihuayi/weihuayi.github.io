function showvarysolution(X, T, U)
%%  SHOWVARYSOLUTION  ��ʾ��ֵ������ʱ��ı仯
% 
%  ���������
%       X ����ΪN�����������ռ������ʷ�
%       T �ڶ�ΪM����������ʱ�������ʷ�
%       U N*M ����U(:,i) ��ʾ��  i ��ʱ������񲿷��ϵ���ֵ��
%
%   ���ߣ�κ���t <weihuayi@xtu.edu.cn>   

M = size(U, 2);
figure
xlabel('X');
ylabel('U');
s = [X(1), X(end), min(min(U)), max(max(U))];
axis(s);
for i = 1:M
   plot(X, U(:,i));
   axis(s);
   pause(0.01);
   title(['T=', num2str(T(i)),' ʱ����ֵ���ͼ��'])
end
