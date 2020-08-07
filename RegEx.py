import re

text = "The film, '@Pulp Fiction' was ? released in % $ year 1994."
text2 = "The film      Pulp Fiction,      was released in   year 1994."
text3 = "The film Pulp Fiction     s was b released in year 1994"
text4 = "I want to buy a mobile between 200 and 400 euros"

# result = re.match(".*", text)
# result = re.search("[a-zA-Z]+", text)
# result = re.search("\d+", text4)
result = re.findall("\d+", text4)
# result = re.sub("Pulp Fiction", "Forrest Gump", text)
# result = re.sub(r"[a-z]", "X", text)
# result = re.sub("\d", "", text) #Remove digits
# result = re.sub("[a-zA-Z\d]", "", text) #Remove alphabets and numbers
# result = re.sub("\w", "", text) #Remove alphabets and numbers| remove words
# result = re.sub("\W", "", text) #Remove non words
# result = re.sub(r"[,@\'?\.$%_]", "", text, flags=re.I)
# result = re.sub(r"\s+"," ", text2, flags = re.I) # Remove extra spaces in between word
result = re.sub(r"\s+[a-zA-Z]\s+", " ", text3) # Removing single character
# result = re.split(r"\s+", text2)
# result = re.split(',',text2)
result = result.lower().split()
print(result)
# print(result.group())