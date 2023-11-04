# glossary 2

glossary2 = {
    'string': 'A series of characters.',
    'if': 'To make a conditional statement .',
    'elif': 'Used in conditional statements, same as else if .',
    'loop': 'Work through a collection of items, one at a time.',
    'def': "To define a function .",
    'list': 'a data structure in Python that is a mutable, or changeable, ordered sequence of elements.',
    'value': 'An item associated with a key in a dictionary.',
    'del': 'Delete the reference of any object in Python. ',
    'float': 'A numerical value with a decimal component.',
    'variable': 'a reserved memory location to store values.',
    }

for word, definition in glossary2.items():
    print("\n" + word.title() + ": " + definition)