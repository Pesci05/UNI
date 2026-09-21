clear 
clc
close all

rng(123);
n = input('Dimensione della matrice: \n');
A = rand(n);
display(A);
U = gaussMethod(A);

M = triu(U);
L = eye(n) + tril(U,-1);

display(L*M);