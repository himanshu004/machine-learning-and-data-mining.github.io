go :-   write('Enter the first number:'),
        read(X1),
        write('Enter the second number:'),
        read(X2),
        prod(X1,X2,R),nl,
        write('The product is: '),write(R).


        prod(A,B,R):-R is A * B.

:-initialization(go).
