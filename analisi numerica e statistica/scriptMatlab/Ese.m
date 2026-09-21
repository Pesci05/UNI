clear;
clc;

n = input("insrisci l'ordine della matrice:");
A = rand(n);
xzero = zeros(1,n);
tol = 0.000001;

D = eye(n);
D = D * n;
A = A + D;

xtrue = ones(n,1);
b = A * xtrue

disp(A);