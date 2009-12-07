% Example of 1-D signal with several kind of singularities.
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
function [U,x]  = mysigex(N)
% N = size of the signal 

sig = .1;
width = .3;

U = zeros(N,1);
x = linspace(0,5,N);

k = find(1.1-width < x & x < 1.1);
U(k) = exp(-(x(k)-1.1).^2./sig^2);
  
k = find(1.1 < x & x < 2);
U(k) = ones(size(k));
  
k = find(abs(x-3) == min(abs(x-3)));
U(k) = 1;  

k = find(4.1-width < x & x < 4.1+width);
U(k) = exp(-(x(k)-4.1).^2./sig^2);
  
