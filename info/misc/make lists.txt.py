a = range(8)
# [0, 1, 2, 3, 4, 5, 6, 7]

a = range(1, 8)
# [1, 2, 3, 4, 5, 6, 7]

a = range(1, 8)[::-1]
# [7, 6, 5, 4, 3, 2, 1]

a = range(1, 8)[::-2]
# [7, 5, 3, 1]

a = {'x': 2, 'z': 1}
# {'x': 2, 'z': 1}
a['x'] = 5
# {'x': 5, 'z': 1}
a['b'] = 3
# {'x': 5, 'z': 1, 'b': 3}
a['x'] += 1
# {'x': 6, 'z': 1, 'b': 3}
a['c'] += 1
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# KeyError: 'c'

