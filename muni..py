import itertools

iterator = iter(input,"")

lines = list(itertools.takewhile(lambda x: True, iterator))

for item in reversed(lines):
    print(item)