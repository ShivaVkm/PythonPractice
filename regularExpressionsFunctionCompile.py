import re
alphabetsToBeSearched = re.compile('[a-g]')
print(alphabetsToBeSearched.findall("Hi, Welcome to the world of programming."))

