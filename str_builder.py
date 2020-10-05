
def comma_builder(lst):
  str = ''
  count = len(lst)
  for i in range(0, count):
    str += lst[i]
    if i < count:
        str += ', '

cast:  ['Tom Hanks', 'Elizabeth Perkins', 'Robert Loggia', 'John Heard', 'Jared Rushton', 'David Moscow', 'Jon Lovitz']