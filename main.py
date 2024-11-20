string = input()
print(string)
word = ""
list = []
newlist = []
subnumber = -22

for x in string:
  if x.isnumeric():
    word += x
  else:
    list.append(word)
    word = ""

for i in list:
  newint = int(i)
  newint -= subnumber
  newlist.append(newint)
  word += str(chr(newint))
print(newlist)
print(word)
