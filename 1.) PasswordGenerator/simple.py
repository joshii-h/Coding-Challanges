import sys
from random import randrange
#author joshuahirsig@gmail.com
lengthOfPassword = int(sys.argv[1])
print("Length of the Password: [%s]" % (lengthOfPassword))
# ALL UTF caracters
utfCharFile = open('./utf8_sequence_0-0x10ffff_assigned_printable.txt', 'r')
utfChars = utfCharFile.read().split()
genPassword, counter = "", 0
while (counter < lengthOfPassword):
    genPassword = genPassword + utfChars[randrange(len(utfChars))]
    counter = counter + 1
utfCharFile.close()
print("Password:\n", genPassword)