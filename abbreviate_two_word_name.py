def abbrev_name(name):
  name = name.upper()
  parts = name.split(' ')

  if len(parts) != 2:
        return "Error: Name must consist of two parts"
  
  first,last = parts
  
  return first[0] + '.' + last[0]
