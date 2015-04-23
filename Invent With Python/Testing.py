# combo(['swallow', 'snake', 'parrot'], 'abc')
# Output:
# [('swallow', 'a'), ('snake', 'b'), ('parrot', 'c')]
# If you use list.append(), you'll want to pass it a tuple of new values.
# Using enumerate() here can save you a variable or two.

def combo(first, second):
  count = 0
  list = []
  for item in first:
    a = first[count], second[count]
    list.append(a)
    count += 1
  return list

print(combo(['swallow', 'snake', 'parrot'], 'abc'))
