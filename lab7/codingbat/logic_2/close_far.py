def close_far(a, b, c):
  if abs(a-b)<2 and abs(a-c)>=2 and abs(c-b)>=2:
    return True
  if abs(a-c)<2 and abs(a-b)>=2 and abs(c-b)>=2:
    return True
  return False