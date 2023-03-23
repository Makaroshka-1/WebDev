def xyz_there(str):
  if str.count('xyz')==0:
    return False
  
  index = str.find('xyz')
  index2 = str.rfind('xyz')
  if str[index-1]!='.' or str[index2-1]!='.':
    return True
  else:
    return False