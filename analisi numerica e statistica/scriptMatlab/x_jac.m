function [output] = x_jac(A,b,xzero,tol,maxIt)
output = xzero;
it = 0;
n = length(xzero);
while 1
   next = output;
    for i=1:n
        sum = 0;
        for j=1:n
            if (i ~= j)
                sum = sum + A(i,j) * output(j);
            end
        end
        next(i) = (b(i) - sum)/A(i,i); 
    end
end
end