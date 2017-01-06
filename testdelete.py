
from __future__ import division
from ast import literal_eval

choice_list = [
[4.5, 23, 42, 9],
[12.5, 3, 80, 0],
[2,0,31.5,80]
]



def averageListValues(a):
    return round(sum(a) / len(a),1)

print map(averageListValues, zip(*choice_list))

results = "placeholder"
print literal_eval(results)

