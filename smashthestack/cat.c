#include <stdio.h>

int main(int argc, char** argv)
{
	for(int i = 0; argv[i] != NULL; i++)
		printf("Arg: %s\n", argv[i]);
	return 0;
}
