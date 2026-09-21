function [matrix] = gaussMethod(matrix);
[r,c] = size(matrix);
if (r ~= c)
    error('La matrice non è quadrata');
end 

for k=1:r-1
    if (matrix(k,k) == 0)
        error('Il primo elemento non può essere 0');
    end
    for i=k+1:c
        matrix(i,k) = matrix(i,k)/matrix(k,k);
        for j=k+1:r
            matrix(i,j) = matrix(i,j) - matrix(i,k)*matrix(k,j);
        end
    end
end 
