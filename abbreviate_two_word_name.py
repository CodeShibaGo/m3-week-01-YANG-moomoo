def abbrev_name(name):
  name = name.upper()
  first,last = name.split(' ')
  
  return first[0] + '.' + last[0]
