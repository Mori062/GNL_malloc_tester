/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   test.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: morishitashoto <morishitashoto@student.    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/09/26 18:36:10 by morishitash       #+#    #+#             */
/*   Updated: 2023/09/26 18:46:23 by morishitash      ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

# include "libc.h"
# include "get_next_line.h"
int	g_cnt = 0;
#define N 0

char	*fmalloc(int i)
{
	char	*str;

	if (g_cnt == N)
		str = NULL;
	else
		str = malloc(i);
	g_cnt++;
	return (str);
}

int	main(void)
{
	int		fd;
	char	*line;
	int		i;

	i = 0;
	fd = open("get_next_line.c", O_RDONLY);
	while (1)
	{
		line = get_next_line(fd);
		printf("line:[%d]    [%s]", i++, line);
		if (line == NULL)
			break ;
		free(line);
	}
	close(fd);
	system("leaks -q gnl");
	return (0);
}
