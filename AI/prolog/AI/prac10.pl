go :-   write('Enter the list:'),
        read(X1),
        write('Enter the the element to be searched for:'),
        read(X2),
        is_member(X1,X2),write("Yes");
        write("No").

        is_member(H,[H|_]):-    !.
        is_member(X,[H|T]):- is_member(X,T).

:-initialization(go).           