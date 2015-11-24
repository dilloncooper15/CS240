from dcooper_test022 import Score
from dcooper_test022 import DetailedScore
from dcooper_test022 import sort_scores
from dcooper_test022 import search_scores

a = Score(100, 'DEL')
b = Score(90, 'JDK')
c = Score(80, 'ZGK')
d = Score(70, 'ACB')
e = Score(100, 'NAM')
list_of_scores = [a, b, c, d, e]
print(list_of_scores)
sort_scores(list_of_scores)
print(list_of_scores)
print(search_scores(list_of_scores, a))
print(search_scores(list_of_scores, b))
print(search_scores(list_of_scores, c))
print(search_scores(list_of_scores, d))
print(search_scores(list_of_scores, e))
a = DetailedScore(100, 'DEL', 2)
b = DetailedScore(90, 'JDK', 3)
c = DetailedScore(80, 'ZGK', 1)
d = DetailedScore(70, 'ACB', 2)
e = DetailedScore(100, 'NAM', 3)
list_of_scores = [a, b, c, d, e]
print(list_of_scores)
sort_scores(list_of_scores)
print(list_of_scores)
print(search_scores(list_of_scores, a))
print(search_scores(list_of_scores, b))
print(search_scores(list_of_scores, c))
print(search_scores(list_of_scores, d))
print(search_scores(list_of_scores, e))

