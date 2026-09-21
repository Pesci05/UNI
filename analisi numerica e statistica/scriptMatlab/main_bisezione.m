clear;
clc;

f = @(x) x^3 + 1;
sol = bisezione(-5,5,f,1e-6)
