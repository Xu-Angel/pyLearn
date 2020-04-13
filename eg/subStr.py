def checkStr(str, sub_str):
  if (str.find(sub_str) != -1):
    return True
  else:
    return False

string = 'xxdfsdfsdf'
sub_str = 'xx'

print(checkStr(string,sub_str))