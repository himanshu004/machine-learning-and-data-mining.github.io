go:- write('Enter List(-1 to end)'),nl,
    createList(L),
    write('List: '),
    printList(L),nl,
    is_subsequence(S,L),
    write('Yes, it is a subsequence'),nl;
    write('Not a subsequence').

is_subsequence([],[_|_]).
is_subsequence([H|T],[H|T1]):- is_subsequence(T,T1),!.
is_subsequence([H|T],[H1|T1]):- is_subsequence([H|T],T1),!.

:- initialization(go).