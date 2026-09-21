clear
clc

%% Metodo di sostituzione in avanti
%L = [1 0 0 0; 2 4 0 0; 3 5 6 0; 1 2 3 4];

%b = [1; 2; 3; 4];

%x = forward(L,b);

%disp([L*x,b]);
%err = norm(L*x-b)/norm(b);
%fprintf('||Lx - b||/||b|| = %g\n',err);

%% Metodo di sostituzione all'indietro
U = [1 4 6 9; 0 2 2 1; 0 0 3 5; 0 0 0 7];

b = [27; 9; 8; 7];

x = backward(U,b);

disp([U*x,b]);
err = norm(U*x-b)/norm(b);
fprintf('||Ux - b||/||b|| = %g\n',err);




