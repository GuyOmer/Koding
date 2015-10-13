#include <stdio.h>
#include <sys/types.h>
#include <unistd.h>

int main(void)
{
	char *arr[] = {""};
	setreuid(1006,1006);
	execve("/bin/sh",arr,arr);	
	
	return 0;
}
