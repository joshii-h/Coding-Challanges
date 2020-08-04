import hashlib
from random import randrange, choice
import random
from urllib.request import urlopen
import sys


lengthOfPassword = int(sys.argv[1])
websiteToFetchFrom = sys.argv[2]

html = urlopen(websiteToFetchFrom).read().decode('utf-8').split()

genPassword = ""
counter = 0
while (counter < lengthOfPassword):
    partOfPassword = html[randrange(len(html))]
    for fragment in partOfPassword:
        genPassword = genPassword + partOfPassword[randrange(len(fragment))]
        # print(fragment)
    counter = counter + 1

partOfPassword = "".join(dict.fromkeys(genPassword)).encode('utf-8')

hash_object = hashlib.sha512(partOfPassword)
hex_dig = hash_object.hexdigest()
chunkOfPassword = ""
counter2 = 0
for n in hex_dig:
    if counter2 < lengthOfPassword/1.5:
        counter2 = counter2 + 1
        chunkOfPassword = chunkOfPassword + n
    else:
        pass

missingCharactersinPassword = lengthOfPassword - len(chunkOfPassword)

specialChars = [',', '.', '-', ';', ':', '_', 'ö', 'ä', 'ü', 'é', 'à', 'è', '+', '*', 'ç', '%', '%', '&', '/',
                '(', ')', '=', '?', '`', '#', 'Ç', '[', ']', '|', '{', '}', '≠', '¿', '´', '§', '°', '‘', '¢', 'æ', '¶', '$', '£', '<', '>', '≤', '≥']

counter3 = 0
chunkOfPasswordP2 = ""
while counter3 < missingCharactersinPassword:
    chunkOfPasswordP2 = chunkOfPasswordP2 + \
        specialChars[randrange(len(specialChars))]
    counter3 = counter3 + 1

chunkOfPassword = chunkOfPassword + chunkOfPasswordP2

str_var = list(chunkOfPassword)
lowerPassword = ''.join(str_var)

print(''.join(choice((str.upper, str.lower))(c) for c in lowerPassword))
