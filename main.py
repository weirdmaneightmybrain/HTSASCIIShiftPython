import urllib.request
import certifi
request_url = urllib.request.urlopen('https://www.hackthissite.org/missions/prog/11/', cafile=certifi.where())
string = input("Input:")
print(string)
word = ""
list = []
newlist = []
subnumber = -22 # Setting variables, newlist is subtracted bu subnumber

for x in string: # checks if input is a number, if it is add to word
    if x.isnumeric():
        word += x
    else: # if it aint, add word to list and reset
        list.append(word)
        word = ""

for i in list: #
    newint = int(i)
    newint -= subnumber
    newlist.append(newint)
    word += str(chr(newint))
print(newlist)
print(word)
print(request_url.read())
