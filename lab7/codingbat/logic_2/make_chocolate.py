def make_chocolate(small, big, goal):
  if small + 5*big < goal:
    return -1
  if goal%5 > small:
    return -1
  if goal>=5*big:
    return goal - 5*big
  return goal % 5 