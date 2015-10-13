#include <stdio.h>

char decode(char c, int index);

int main(int argc, char* argv[])
{

	//printf("%c:%c\n",argv[1][0], 'A'+(10+argv[1][0]-'A')%26);
	//KLMNOPQRSTUVWXYZABCDEFGHIJ <--cipher key
	//ABCDEFGHIJKLMNOPQRSTUVWXYZ <--plain key

 	char key[27];
 	for(int i = 0; i < 26; i++)
 		key[i] = 'A'+(10+i)%26;

 	printf("\n");
                          //0,  1   2   3   4   5   6   7   8   9   10  11  12
	const char cipher[] = {'H','R','X','D','Z','N','W','E','A','W','W','C','P'};
	char plain[] = {'A','A','A','A','A','A','A','A','A','A','A','A','A'};

	for(int i = 0; i < 13; i++)
	{
		plain[i] = decode(cipher[(i+10)%13],i);
		printf("%c", plain[i]);
	}

	printf("\n");

	return 0;
}

char decode(char c, int index)
{
	char p = c-10;
	if(p<=65)
		return 'Z'-(c%65)+10;
	return p;
	return p;
}