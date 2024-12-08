import pprint

dictionar = {"name": "juan", "age":""}
print(dictionar["name"])

birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}

#print(birthdays['Alice'] if "Alic1e" in birthdays else "")


#[print(birthdayDate) for birthdayDate in birthdays.values()]
#[print(key) for key in birthdays.keys()]
#[print(items) for  items in birthdays.items()]
print(birthdays.get("Alice"))
print(birthdays.get("Juan", "26 Mai"))

#---------------------------------------------

message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}
for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1
pprint.pprint(count)