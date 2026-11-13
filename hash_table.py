class Contact:
    '''
    Contact class to represent a contact with a name and number.
    Attributes:
        name (str): The name of the contact.
        number (str): The phone number of the contact.
    '''
    def __init__(self, name, number):
        self.name = name
        self.number = number

    def __str__(self):
        return f"{self.name}: {self.number}"

class Node:
    '''
    Node class to represent a single entry in the hash table.
    Attributes:
        key (str): The key (name) of the contact.
        value (Contact): The value (Contact object) associated with the key.
        next (Node): Pointer to the next node in case of a collision.
    '''
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    HashTable class to represent a hash table for storing contacts.
    Attributes:
        size (int): The size of the hash table.
        data (list): The underlying array to store linked lists for collision handling.
    Methods:
        hash_function(key): Converts a string key into an array index.
        insert(key, value): Inserts a new contact into the hash table.
        search(key): Searches for a contact by name.
        print_table(): Prints the structure of the hash table.
    '''
    
    def __init__(self, size):
        self.size = size
        self.data = [None] * size
  
    def hash_function(self, key):
        total = 0
        for char in key:
            total += ord(char)
        return total % self.size

    
    def insert(self, key, value):
        contact = Contact(key, value)
        index = self.hash_function(contact.name)
        current = self.data[index]

    # If the index is empty, insert the first node
        if current is None:
            self.data[index] = Node(contact.name, contact.number)
            return

    # Traverse the linked list
        while current:
            if current.key == key:
                current.value = value
                return

            if current.next is None:
                break

            current = current.next

    # Append new contact
        current.next = Node(contact.name, contact.number)
    
    def search(self, key):
        index = self.hash_function(key)
        current = self.data[index]

        while current:
            if current.key == key:
                return current.value
            current = current.next
    
        return None

    def print_table(self):
        for index, item in enumerate(self.data):
            print(f"Index {index}:", end=" ")

            if item is None:
                print("Empty")
                continue

            current = item

            while current:
                print(f"{current.key}: {current.value}", end="")

                if current.next is not None:
                    print(" -> ", end="")

                current = current.next

            print()

table = HashTable(10)
table.print_table()
'''
Index 0: Empty
Index 1: Empty
Index 2: Empty
Index 3: Empty
Index 4: Empty
Index 5: Empty
Index 6: Empty
Index 7: Empty
Index 8: Empty
Index 9: Empty 
'''
# Add some values
table.insert("John", "909-876-1234")
table.insert("Rebecca", "111-555-0002")
# Print the new table structure 
table.print_table()
'''
Index 0: Empty
Index 1: Empty
Index 2: Empty
Index 3: Empty
Index 4: Empty
Index 5: Empty
Index 6: Empty
Index 7: - Rebecca: 111-555-0002 
Index 8: Empty
Index 9: - John: 909-876-1234 
'''
# Search for a value
contact = table.search("John") 
print("\nSearch result:", contact)  # Search result: John: 909-876-1234 

# Continuation of code from above
# Edge Case #1 - Hash Collisons (assuming these hash to the same index) 
table.insert("Amy", "111-222-3333") 
table.insert("May", "222-333-1111")  # May collide with Amy depending on hash function 
table.print_table()
'''
Index 0: Empty
Index 1: Empty
Index 2: Empty
Index 3: Empty
Index 4: Empty
Index 5: - Amy: 111-222-3333 - May: 222-333-1111 
Index 6: Empty
Index 7: - Rebecca: 111-555-0002 
Index 8: Empty
Index 9: - John: 909-876-1234 
'''
# Edge Case #2 - Duplicate Keys 
table.insert("Rebecca", "999-444-9999")  # Should update Rebecca's number 
table.print_table()
'''
Index 0: Empty
Index 1: Empty
Index 2: Empty
Index 3: Empty
Index 4: Empty
Index 5: - Amy: 111-222-3333 - May: 222-333-1111 
Index 6: Empty
Index 7: - Rebecca: 999-444-9999 
Index 8: Empty
Index 9: - John: 909-876-1234 
'''
# Edge Case #3 - Searching for a value not in the table
print(table.search("Chris")) # None

