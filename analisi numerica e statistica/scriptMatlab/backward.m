function [output] = backward(matrix,b);
output = zeros(length(b), 1);
l = length(b);
for i=l:-1:1
    x(i) = b(i);
    for j=1:l
        x(i) = x(i) - matrix(i,j)*b(i) ; 
    end
   output(i) = x(i) / matrix(i,i);
   
end
