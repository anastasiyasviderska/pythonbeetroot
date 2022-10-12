from logging.config import dictConfig


def validate(str1, str2):
    if len(str1) != len(str2):
        return False
    trans = {}
    for i in range (len(str1)):
        if  str1[i] in trans and trans [str1[i]] != str2 [i]:
            return False
        else:
            trans [str1[i]] = [str2[i]]
    return True
  

print(validate ("egg", "add"))