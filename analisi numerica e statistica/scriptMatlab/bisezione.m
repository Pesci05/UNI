function[c] = bisezione(a,b,f,tau);
    N = ceil( log2((b-a)/tau) );
    fa = f(a);
    fb = f(b);
    for k = 1:N
        c = a + (b-a)/2;
        fc = f(c);
        if (fc == 0)
            return 
        end
        
        if (fc * fb < 0) 
            a = c;
            fa = fc;
        else
            b = c;
            fb = fc;
        end
    end
    
end
