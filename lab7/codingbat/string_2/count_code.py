def count_code(str):
  sum = 0
  letters = 'abcdefghijklmnopqrstuvwxyz'
  for i in letters:
    sum+=str.count('co'+i+'e')
  return sum
  