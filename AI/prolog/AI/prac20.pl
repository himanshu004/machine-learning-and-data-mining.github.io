go:- write('Enter List(-1 to end)'),nl,
    createList(L),
    write('List: '),
    printList(L),nl,
    print("Enter the list to be checked:"),nl,
    createList(S),nl,
    subList(S,L),
    write('Yes'),nl;
    write("No").

enterElement(X):- write('Enter the new element: '),
                  read(X).

createList(L):- enterElement(X),
                createListHelper(X, L).
createListHelper(-1, []):- !.
createListHelper(X, [X|Y]):- enterElement(X1),
                       createListHelper(X1, Y).

printList([]).
printList([X|Y]):-  write(X),
                    write(' '),
                    printList(Y).
                
conc([], L2, L2).
conc([X|T1], L2, [X|T2]):- conc(T1, L2, T2).

subList(S, L):- conc(L1, L2, L),
                subList(S, L3, L2).
:- initialization(go).
