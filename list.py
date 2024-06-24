# list.py

def create_list():
    # Creating a list
    fruits = ["apple", "banana", "cherry", "date"]
    print("Created list:", fruits)

def access_elements():
    # Accessing elements in a list
    fruits = ["apple", "banana", "cherry", "date"]
    print("First fruit:", fruits[0])
    print("Last fruit:", fruits[-1])
    print("Second to last fruit:", fruits[-2])

def modify_list():
    # Modifying elements in a list
    fruits = ["apple", "banana", "cherry", "date"]
    print("Original list:", fruits)
    fruits[1] = "blueberry"
    print("Modified list:", fruits)

def list_operations():
    # Various list operations
    fruits = ["apple", "banana", "cherry", "date"]
    
    # Append an element
    fruits.append("elderberry")
    print("List after appending elderberry:", fruits)
    
    # Insert an element at a specific position
    fruits.insert(2, "fig")
    print("List after inserting fig at position 2:", fruits)
    
    # Remove an element
    fruits.remove("banana")
    print("List after removing banana:", fruits)
    
    # Pop an element from the end
    popped_fruit = fruits.pop()
    print("Popped fruit:", popped_fruit)
    print("List after popping:", fruits)
    
    # Sort the list
    fruits.sort()
    print("Sorted list:", fruits)
    
    # Reverse the list
    fruits.reverse()
    print("Reversed list:", fruits)
    
    # Find the length of the list
    print("Length of the list:", len(fruits))

def list_comprehensions():
    # List comprehensions
    numbers = [1, 2, 3, 4, 5]
    squares = [x**2 for x in numbers]
    print("Original numbers:", numbers)
    print("Squares of the numbers:", squares)

def main():
    create_list()
    access_elements()
    modify_list()
    list_operations()
    list_comprehensions()

if __name__ == "__main__":
    main()
