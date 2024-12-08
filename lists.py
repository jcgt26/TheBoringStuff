import copy

test = ["Juan",23, "pedro", True]
#print("Juan" in test)
#print(True in test)

li = ["Juan", "Camilo", "Guzman"]
firstNameSimple, firstNameComposed, lastName = li

#print(f'First Name Simple: {firstNameSimple} ');
#print(f'First Name Composed: {firstNameComposed} ');
#print(f'Last Name: {lastName}');

#print([1,2,"Juan", "Pedro"].sort())
lis = [4,2,48,-9]
lis.sort()
#print(lis)

# Sorting through alphabetical order
#Sort uses Asciibetical -> Uppercase sorting comes before Lowercase
test = ['a', 'b', 'Z']
test.sort() # 'Z', 'a', 'b'
#print(test)

def appendHello(seed: list):
    seed.append("Hello")

text = ["Moin"]
# better use copy.copy() to avoid manipulating the original list
# deepcopy for nested lists
appendHello(text) 
#print(text)

# exercise

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']];



for x in grid:
    print(x)
    newGrid = []

for row in range(0, len(grid[0]) - 1):
    newColumn = [x[row] for x in grid]
    newGrid.append(newColumn)

for row in newGrid:
    print(newGrid)