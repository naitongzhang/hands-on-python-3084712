def double(number):
    return number * 2

result = double(5)
print(result)

def uppercase(word):
    return word.upper()

print(uppercase('hello'))

def lowercase(word):
    return word.lower()

print(lowercase('HELLO'))

name = ['John', 'Doe']

for name in name:
    print(uppercase(name))