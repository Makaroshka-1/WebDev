def front_back(str):
  n = len(str)
  if n!=1:
    return str[n-1] + str[1:-1] + str[0]
  return str
