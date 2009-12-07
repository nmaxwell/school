function out = IDWT ( in, structure, low_pass, high_pass  )

% --- inverse discrete wavelet transform
% nicholas maxwell, 11/29/09
%
% only works on data which is a power of two, for now. should be easy to fix.
% only been tested on haar wavelet.
%


if ( length(size(in)) ~= 2 | min(size(in)) ~= 1 )
    warning('IDWT error: can only deal with column or row vectors at this time')
    return,
end

if ( length(size(low_pass)) ~= 2 | min(size(low_pass)) ~= 1 )
    warning('IDWT error: low_pass needs to be a vector')
    return,
end

if ( length(size(high_pass)) ~= 2 | min(size(high_pass)) ~= 1 )
    warning('IDWT error: high_pass needs to be a vector')
    return,
end

if ( max(size(in)) <= max(size(low_pass)) )
    warning('IDWT error: low_pass too long for input vector')
    return,
end

if ( max(size(in)) <= max(size(high_pass)) )
    warning('IDWT error: high_pass too long for input vector')
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


N = length(structure);

reconstruction = zeros( 1, structure(end)*2 );

while ( length(structure)>1 )

    s = structure(end);
    structure = structure(1:end-1);
    
    cs = in( end-s+1: end );    
    in = in(1:end-s);
    
    temp = [];
    
    for k=1:s
        temp = [ temp, high_pass*cs(k) ];
    end
    
    reconstruction = reconstruction + temp;
    
    if (length(structure)>1)
    
        temp = high_pass;
        high_pass = zeros(1, 2*size(temp)(2));
        for i=1:size(temp)(2)
            high_pass(2*i-1) = temp(i);
            high_pass(2*i) = temp(i);
        end
        
        temp = low_pass;
        low_pass = zeros(1, 2*size(temp)(2));
        for i=1:size(temp)(2)   
            low_pass(2*i-1) = temp(i);
            low_pass(2*i) = temp(i);
        end
        
        low_pass /= sqrt(2);
        high_pass /= sqrt(2);
    end
    
    
end

temp = [];

for k=1:s
    temp = [ temp, low_pass*in(k) ];
end

reconstruction = reconstruction + temp;

out = reconstruction;



