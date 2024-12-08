animals = []
while True:
   animal = input("Name of the Animal: ")
   if(animal == "" or animal == " "):
      break
   animals.append(animal)

[print(animal) for animal in animals]