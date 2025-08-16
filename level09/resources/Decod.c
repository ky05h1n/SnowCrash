#include <stdio.h>
#include <unistd.h>
#include <fcntl.h>

int main (int ac , char** av)
{
	char buff[26];

	if (ac == 2)
	{
			int fd = open(av[1], O_RDONLY);
			if (fd != -1){
			int max = read(fd, &buff, 26);
			buff[max - 1] = '\0';
			printf("DECODED PASS : %s\n", buff);
			printf("PASS HEX : ");

			int i = -1;
			while (buff[++i])
				fprintf(stdout,"%02x ", (unsigned char)buff[i]);
			close(fd);
			remove("hex.txt");

			i = -1;
			while(buff[++i])
				buff[i] = buff[i] - i;
			printf("\nPASSWORD : %s\n", buff);
			
		}

	}
}
