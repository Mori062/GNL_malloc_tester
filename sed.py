import re

file_path = "get_next_line.c"

with open(file_path, 'r') as file:
    file_content = file.read()

modified_content = re.sub(r'\(char \*\)malloc', 'fmalloc', file_content)

with open(file_path, 'w') as file:
    file.write(modified_content)

file_path = "get_next_line_utils.c"

with open(file_path, 'r') as file:
    file_content = file.read()

modified_content = re.sub(r'\(char \*\)malloc', 'fmalloc', file_content)

with open(file_path, 'w') as file:
    file.write(modified_content)