#define _GNU_SOURCE
#include <stdio.h>
#include <stdint.h>
#include <dlfcn.h>
#include <sys/types.h>

int geteuid(void)
{	
    return 666;
}
//gcc -m32 -shared -ldl -fPIC semtex2.c -o proglib2.so

//pass: jJjl2Msl