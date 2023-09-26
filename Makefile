FILES = get_next_line.c get_next_line_utils.c get_next_line_utils.h get_next_line.h

test:
	@ sh tester.sh

clean:
	@ rm -rf $(FILES)
	@ rm -rf gnl*

fclean: clean

re: fclean test
