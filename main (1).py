age=20

#concatenation with +
first_name="Jane"
last_name="Doe"
print(first_name+last_name)

#separator
separator=" "
full_name=first_name+separator+last_name
print(full_name)

#print multiple times
double_name=last_name*10
print(double_name)
print(first_name,last_name,sep=":")

#string methods  str.capitalize
text="first character capitalized"
new_text=text.capitalize()
print(new_text)

#str.casefold
text1="CAseFolding IS Similar to lowerCAsing"
new_text1=text1.casefold()
print(new_text1)

#str.center
txt="apple"
x=txt.center(30)
print(x)

#str.count, returns the number of times the string appears
text2="i love grapes,grapes are my favourite"
y=text2.count("grape")
print(y)

#str. encode using utf8, will work even if not specified
name="my name is Bena"
z=name.encode('UTF8')
print(z)

#str. endswith
a=text2.endswith("e")
print(a)

#str. find, -1 if not found, true and index position if found
b=text2.find("my")
print(b)

#str. join
list=("Bridget","Bena","Liz","Daphne")
c=" ".join(list)
print(c)

#str. split
d=text2.split()
print(d)

#str. replace
e=text2.replace("grapes","apples")
print(e)

#str. strip,removes white spaces before and after
text3=" example "
g=text3.strip()
print(g)

#str. lstrip, removes left white space
text4="  grape  "
h=text4.lstrip()
print("of all fruits,", h, "is my fav")

#

