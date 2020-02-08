go :-   write('Enter the first list:'),
        read(X1),
        write('Enter the second list:'),
        read(X2),
        conc(X1,X2,X3),nl,
        write('The new list is: '),write(X3).

        conc([],L2,L2).
        conc([H|T1],L2,[H|T2]):- conc(T1,L2,T2).

:-initialization(go).