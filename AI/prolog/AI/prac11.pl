go :-   write('Enter the first list:'),
        read(X1),
        write('Enter the second list:'),
        read(X2),
        append(X1,X2,X3),nl,
        write('The new list is: '),write(X3).

:-initialization(go).
