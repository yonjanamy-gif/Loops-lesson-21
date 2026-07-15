# 1. Create the phonebook dictionary with name and phone number
phonebook = {
    "Amy": "9813052776",
    "John": "9813123949",
    "Bob": "9810414713"
}

name = input("Enter name to search: ")

if name in phonebook:
    print("Phone number:", phonebook[name])
else:
    print("Contact not found.")