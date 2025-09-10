s = "hello world" #Strings are immutable
a = len(s)
print(a)
print(s.upper(), s)
print(s.lower())
print(s.capitalize())

text = " hello world "
print(text.strip())
print(text.lstrip())
print(text.rstrip())


text = "Python is fun"
print(text.find("is"))
print(text.replace("fun", "awesome"))


text = "Apples,Bananas,Pineapples"
print(text.split(","))
print(",".join(['Apples', 'Bananas', 'Pineapples']))


text = "Python123"
print(text.isalpha())
print(text.isdigit())
print(text.isalnum())
print(text.isspace())