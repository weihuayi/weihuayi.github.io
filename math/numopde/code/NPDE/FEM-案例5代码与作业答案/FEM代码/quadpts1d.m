function [lambda,weight] = quadpts1d(order)
%% QUADPTS1 quadrature points in 1-D.
%
% [lambda,weight] = QUADPTS1(order) return quadrature points with given
% order (up to 19) in the barycentric coordinates.
%
% The output lambda is a matrix of size nQ by 2, where nQ is the number of
% quadrature points. lambda(i,:) is two barycentric coordinate of the
% i-th quadrature point and lambda(:,j) is the j-th barycentric coordinate
% of all quadrature points. The coordinate of the p-th quadrature point
% can be computed as 
%
%    p = lambda(p,1)*a+ lambda(p,2)*b;
% where a and b are the end points of segment in 2D or 3D;
%
% References: 
% * Pavel Holoborodko
% http://www.holoborodko.com/pavel/numerical-methods/numerical-integration/
% 
% See also quadpts, quadpts3, verifyquadpts
%
% Added by Huayi Wei
%
% Copyright (C) Long Chen. See COPYRIGHT.txt for details. 

numPts = ceil((order+1)/2);

if numPts > 10
   numPts = 10; 
end

switch numPts
    case 1
        A = [0      2.0000000000000000000000000];
        
    case 2
        A = [0.5773502691896257645091488 	1.0000000000000000000000000
            -0.5773502691896257645091488 	1.0000000000000000000000000];
        
    case 3
        A = [0 	0.8888888888888888888888889
            0.7745966692414833770358531 	0.5555555555555555555555556
            -0.7745966692414833770358531 	0.5555555555555555555555556];
        
    case 4
        A = [0.3399810435848562648026658 	0.6521451548625461426269361
            0.8611363115940525752239465 	0.3478548451374538573730639
            -0.3399810435848562648026658 	0.6521451548625461426269361
            -0.8611363115940525752239465 	0.3478548451374538573730639];
        
    case 5
        A = [0 	                            0.5688888888888888888888889
            0.5384693101056830910363144 	0.4786286704993664680412915
            0.9061798459386639927976269 	0.2369268850561890875142640
            -0.5384693101056830910363144 	0.4786286704993664680412915
            -0.9061798459386639927976269 	0.2369268850561890875142640];
        
    case 6
        A = [0.2386191860831969086305017 	0.4679139345726910473898703
            0.6612093864662645136613996 	0.3607615730481386075698335
            0.9324695142031520278123016 	0.1713244923791703450402961
            -0.2386191860831969086305017 	0.4679139345726910473898703
            -0.6612093864662645136613996 	0.3607615730481386075698335
            -0.9324695142031520278123016 	0.1713244923791703450402961];
        
    case 7
        A = [0 	                            0.4179591836734693877551020
            0.4058451513773971669066064 	0.3818300505051189449503698
            0.7415311855993944398638648 	0.2797053914892766679014678
            0.9491079123427585245261897 	0.1294849661688696932706114
            -0.4058451513773971669066064 	0.3818300505051189449503698
            -0.7415311855993944398638648 	0.2797053914892766679014678
            -0.9491079123427585245261897 	0.1294849661688696932706114];
        
    case 8
        A = [0.1834346424956498049394761 	0.3626837833783619829651504
            0.5255324099163289858177390 	0.3137066458778872873379622
            0.7966664774136267395915539 	0.2223810344533744705443560
            0.9602898564975362316835609 	0.1012285362903762591525314
            -0.1834346424956498049394761 	0.3626837833783619829651504
            -0.5255324099163289858177390 	0.3137066458778872873379622
            -0.7966664774136267395915539 	0.2223810344533744705443560
            -0.9602898564975362316835609 	0.1012285362903762591525314];
        
    case 9
        A = [0 	                            0.3302393550012597631645251
            0.3242534234038089290385380 	0.3123470770400028400686304
            0.6133714327005903973087020 	0.2606106964029354623187429
            0.8360311073266357942994298 	0.1806481606948574040584720
            0.9681602395076260898355762 	0.0812743883615744119718922
            -0.3242534234038089290385380 	0.3123470770400028400686304
            -0.6133714327005903973087020 	0.2606106964029354623187429
            -0.8360311073266357942994298 	0.1806481606948574040584720
            -0.9681602395076260898355762 	0.0812743883615744119718922];
        
    case 10
        A = [0.1488743389816312108848260 	0.2955242247147528701738930
            0.4333953941292471907992659 	0.2692667193099963550912269
            0.6794095682990244062343274 	0.2190863625159820439955349
            0.8650633666889845107320967 	0.1494513491505805931457763
            0.9739065285171717200779640 	0.0666713443086881375935688
            -0.1488743389816312108848260 	0.2955242247147528701738930
            -0.4333953941292471907992659 	0.2692667193099963550912269
            -0.6794095682990244062343274 	0.2190863625159820439955349
            -0.8650633666889845107320967 	0.1494513491505805931457763
            -0.9739065285171717200779640 	0.0666713443086881375935688];
end
lambda1 = (A(:,1)+1)/2;
lambda2 = 1 - lambda1;
lambda = [lambda1, lambda2];
weight = A(:,2)/2;
%% Verification
% The order of the quadrature rule is verified by the function
% verifyquadpts1. See <matlab:ifem('verifyquadpts1') verifyquadpts1>.