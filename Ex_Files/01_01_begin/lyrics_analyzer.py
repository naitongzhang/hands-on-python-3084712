text = """i wish nothing but the best for you too"""
print(text)
print(len(text.split()))

text = """
a b c a a b
"""
print(text.split())

word_count = {}

for word in text.split():
  print(word)
  if word in word_count:
    word_count[word] += 1
  else:
    word_count[word] = 1

print(word_count)