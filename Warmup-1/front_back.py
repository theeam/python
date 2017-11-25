'''

Given a string, return a new string where the first and last chars have been exchanged.


front_back('code') → 'eodc'
front_back('a') → 'a'
front_back('ab') → 'ba'

'''

def front_back(str):
  if len(str) > 2:
    return str[-1] + str[1:-1] + str[0]
  elif 3 > len(str) > 1:
    return str[-1] + str[0]
  else:
    return str
  


    