function [out, sctructure ] = DWT ( in, max_level, low_pass, high_pass )

% --- forward discrete wavelet transform
% nicholas maxwell, 10/29/09
%
% takes a 1xn or nx1 input vector and performs a wavelet decomposition,
% specified by the low_pass convolution kernel,
% and the high_pass convolution kernel
%
% applies max_level levels of resolution ( max_level passes through DWT algorithm)
% if the algorithm runs out of data ( decomposes untill only one scaling coefficient, DC term )
% then the algotithm quits
%
% assuming periodic boundary conditions for now...
%

% validate the input

if ( length(size(in)) ~= 2 | min(size(in)) ~= 1 )
    warning('DWT error: can only deal with column or row vectors at this time')
    return,
end

if ( length(size(low_pass)) ~= 2 | min(size(low_pass)) ~= 1 )
    warning('DWT error: low_pass needs to be a vector')
    return,
end

if ( length(size(high_pass)) ~= 2 | min(size(high_pass)) ~= 1 )
    warning('DWT error: high_pass needs to be a vector')
    return,
end

if ( length(max_level) ~= 1 )
    out = "DWT error: max_level needs to be a number";
    return,
end

if ( max(size(in)) <= max(size(low_pass)) )
    warning('DWT error: low_pass too long for input vector')
    return,
end

if ( max(size(in)) <= max(size(high_pass)) )
    warning('DWT error: high_pass too long for input vector')
    return,
end

if ( size(in)(1) ~= 1)
    in = in';
end

if ( size(low_pass)(1) ~= 1)
    low_pass = low_pass';
end

if ( size(high_pass)(1) ~= 1)
    high_pass = high_pass';
end

% return will be a vector containing wavelet coefficients and
% scaling function coefficients, decalring these here.
% DWT algorithm is recursive, starts with input vector, interpreted as
% scaling function coefficients at highest level
% no wavelet_coefficients to begin with, so empty vector.

wavelet_coefficients = [];
scaling_coefficients = in;
sctructure = [];

for j=1:max_level
    
    L = size(scaling_coefficients)(2);
    
    %check if done
    if (L == 1 | j > max_level)
        break
    end
    
    %high_pass convolution to find wavelet coefficients, save in temp
    temp = zeros(1,ceil(0.5*L));
    for k=1:ceil(0.5*L)
        for i=1:size(high_pass)(2)
            % assuming periodic boundary conditions for now...
            if ( 2*k+i <= L+2 )
                temp(k) = temp(k) + scaling_coefficients(2*k+i-2)*high_pass(i);
            else
                temp(k) = temp(k) + scaling_coefficients(2*k+i-2-L)*high_pass(i);
            end
        end
    end
    
    % concatenate result with wavelet coefficients already found
    wavelet_coefficients = cat(2,temp,wavelet_coefficients);
    sctructure = [ length(temp), sctructure ];
    
    %low_pass convolution to find scaling coefficients, save in temp
    temp = zeros(1,ceil(0.5*L));
    for k=1:ceil(0.5*L)
        for i=1:size(low_pass)(2)
            % assuming periodic boundary conditions for now...
            if ( 2*k+i <= L+2 )
                temp(k) = temp(k) + scaling_coefficients(2*k+i-2)*low_pass(i);
            else
                temp(k) = temp(k) + scaling_coefficients(2*k+i-2-L)*low_pass(i);
            end
        end
    end
    
    % recursion:
    scaling_coefficients = temp;
    
end

% stick scaling coefficients in front, then wavelet coefficients, return
out = cat(2,scaling_coefficients,wavelet_coefficients);
sctructure = [ length(scaling_coefficients), sctructure ];
