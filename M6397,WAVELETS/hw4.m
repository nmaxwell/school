


N = 1024;
W = 64;


X = [1:N];
F = mysigex(N);

s = 1/sqrt(2);

FT = fft(F );

FT_lina = zeros(size(FT));
FT_lina(1:W) = FT(1:W);
FT_lina( end-W+1: end ) = FT( end-W+1: end );
FT_lina = real(ifft(FT_lina));



temp = abs(FT(1:N/2+1));
mask = zeros(size(temp));

while( sum(mask) < W )
    
    mask = mask + ( temp == max(temp));
    
    temp = temp .* (ones(size(mask)) - mask );
    
end

mask = mask';
mask = [mask, fliplr(mask)(2:end-1) ] ;
mask = mask';

FT_nlina = real(ifft(FT.*mask));



[HT S] = DWT( F, 10, [s,s], [s,-s] );

HT_lina = zeros(size(HT));
HT_lina(1:W) = HT(1:W);

HT_lina = IDWT( HT_lina, S, [s,s], [s,-s] )';


temp = abs(HT);
mask = zeros(size(temp));

while( sum(mask) < W )
    
    mask = mask + ( temp == max(temp));
    
    temp = temp .* (ones(size(mask)) - mask );
    
end


HT_nlina = IDWT( HT.*mask, S, [s,s], [s,-s] )';



norm(F-FT_lina)^2
norm(F-FT_nlina)^2
norm(F-HT_lina)^2
norm(F-HT_nlina)^2







