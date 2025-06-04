#!/usr/bin/python3
write_file = __import__('1-write_file').write_file

text = "Hello, Holberton!\nThis is Task 1.\n"
filename = "file_for_task_1.txt"
count = write_file(filename, text)
print(count)
print("----- CONTENU DU FICHIER -----")
with open(filename, 'r', encoding='utf-8') as f:
    print(f.read(), end="")
