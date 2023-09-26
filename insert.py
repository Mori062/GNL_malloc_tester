file_name = "get_next_line.c"

line_to_insert = '#include "test.h"\n'

with open(file_name, 'r') as file:
    lines = file.readlines()

lines.insert(11, line_to_insert)

with open(file_name, 'w') as file:
    file.writelines(lines)

file_name = "get_next_line_utils.c"

line_to_insert = '#include "test.h"\n'

with open(file_name, 'r') as file:
    lines = file.readlines()

lines.insert(11, line_to_insert)

with open(file_name, 'w') as file:
    file.writelines(lines)