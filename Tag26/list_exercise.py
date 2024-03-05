
# Square numbers
numbers = [1,1,2,3,5,8,13,21,34,55]

squared_numbers = [item ** 2 for item in numbers]

print(squared_numbers)

# Filter even numbers
list_of_strings = input().split(',')

result = [int(num) for num in list_of_strings if int(num) % 2 == 0]

print(result)


# Data overlap, compare two data lists (file1, file2)
def file_opener(name):
    with open(name) as data:
        return [num.strip() for num in data]


file1 = file_opener('file1.txt')
file2 = file_opener('file2.txt')


result = [int(num) for num in file1 if num in file2]

print(result)
