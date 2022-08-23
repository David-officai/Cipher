# Convert English words into number#

#Capital letters are shown as negative number
#Space is converted into -64
#. is convert into -50
#, is convert into -52
#' is convert into -57
words = input("input words > ")
n = []

for num in words:
    n.append(ord(num) -96)
print(n)



##below code is to recognize capital letters or not. if c-letters, false

import re
RED = '\033[31m'
END = '\033[0m'
GREEN = '\033[32m' 

result = re.search('[A-Z]', words)
if result:
    print(RED + "Don't use capital letter because of converting to negative number" + END)
else:
    print(GREEN + "success" + END)


#2022/8/17 Wed --- David officail