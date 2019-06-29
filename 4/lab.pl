
kth_element( 1 , X , [X|_]  ).
kth_element( k , X , [_|Xs] ) :-
  k > 1 ,
  k1 is k-1 ,
  kth_element( k1 , X , Xs ).
  
remove_duplicates([],[]).
remove_duplicates([H],[H]).
remove_duplicates([H ,H| T], List) :- remove_duplicates( [H|T], List).
remove_duplicates([H,Y | T], [H|T1]):- Y \= H,remove_duplicates( [Y|T], T1).
