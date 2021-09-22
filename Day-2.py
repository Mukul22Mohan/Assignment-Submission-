#Write a Python program to print the even numbers from a given list.

list_of_number = list(range(1,21,1))
print("List of Given Numbers")
print(list_of_number)

list_of_even_number = [even for even in list_of_number if even % 2 == 0]
print("List of Even Numbers")
print(list_of_even_number)