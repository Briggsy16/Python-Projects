def sillycase(string):
  string_length = len(string)
  new_string = string[:2].lower()
  new_string += string[2:len(string)].upper()
  return new_string

print(sillycase('Matt'))