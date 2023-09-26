import re

file_path = "get_next_line.c"
text_to_insert = '#include "test.h"\n'

with open(file_path, 'r') as file:
    file_content = file.read()

modified_content = re.sub(r'\(char \*\)malloc', 'fmalloc', file_content)

with open(file_path, 'w') as file:
    file.write(modified_content)

with open(file_path, 'r') as file:
    lines = file.readlines()

lines.insert(11, text_to_insert)

with open(file_path, 'w') as file:
    file.writelines(lines)

file_path = "get_next_line_utils.c"
text_to_insert = '#include "test.h"\n'

with open(file_path, 'r') as file:
    file_content = file.read()

modified_content = re.sub(r'\(char \*\)malloc', 'fmalloc', file_content)

with open(file_path, 'w') as file:
    file.write(modified_content)

with open(file_path, 'r') as file:
    lines = file.readlines()

lines.insert(11, text_to_insert)

with open(file_path, 'w') as file:
    file.writelines(lines)