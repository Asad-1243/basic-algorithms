def search(array, num):
  for i in range(len(array)):
    if array[i] == num:
      return i
  return -1

spaces = int(input("enter the number of elements in your array: "))
numbers = [int(input()) for i in range(spaces)]
number = int(input("enter the number you want to look for: ")) 

result = search(numbers, number)

if result == -1:
  print(f"the number is not in your array")
else:
  print(f"the number {number} is held in box number {result} of the array")
