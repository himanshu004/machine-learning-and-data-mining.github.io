go :-   write('Enter the first number:'),
        read(X1),
        write('Enter the second number:'),
        read(X2),
        max(X1,X2,R),nl,
        write('The maximum is: '),write(R).


    max(X,Y,M):- X > Y, 
		    	M is X,
                !.

	max(_,Y,M):- M is Y.

:-initialization(go).
