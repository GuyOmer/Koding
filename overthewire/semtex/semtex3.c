#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>
#include <time.h>

#define LOCKS 5
#define MAX_MOVES 256

//PASSWORD d%kj1//..

//prototypes
void reset_locks(void);
bool brute(char* seq);
void logger(char* seq, bool done, long counter,FILE* out);
int status(void);
void mover(int action);
void sort(char* seq);

int locks[LOCKS];
int results[8][5] = {
					{  5,   2,   1,   7, 5},   // 1
					{13,  -7,  -4,   1,  5},   // 2
					{9,  12,   9,  70,  -4},   // 3
					{-11,   9,   0,  5,-13},   // 4
					{4,  17,  12,   9,  24},   // 5
					{ 11, -17,  21,   5,14},   // 6
					{15,  31,  22, -12,  3},   // 7
					{19, -12,   4,   3, -7}    // 8
					}; 

int main(int argc, char* argv[])
{
	
	if(argc == 1)
	{
		bool done = false;
		char* seq = malloc(sizeof(char)*MAX_MOVES);
		if(seq == NULL)
		{
			printf("Couldn't allocate memory\n");
			return 1;
		}
		
		long counter = 1;
		srand(time(NULL));

		FILE* flog = fopen("log.txt","w");
		if(flog==NULL)
		{
			printf("Couldn't open log.txt\n");
			return 2;
		}
		
		do
		{
			reset_locks();
			done = brute(seq);
			logger(seq,done, counter, flog);

			counter++;
		}
		while(!done);

		int len = strlen(seq);
		sort(seq);
		printf("Attempt #%ld succeeded:\n", counter);
		printf("Snapshot:\n");
		for(int i = 0; i < LOCKS; i++)
			printf("L%d: %d ", i+1,locks[i]);

		printf("\n");

		printf("%s",seq);
		printf(".\nTook %d moves.\n", len);

		free(seq);
		fclose (flog);
	}
	else
	{
		reset_locks();
		for(int i = 0, combo = strlen(argv[1]); i < combo;i++)
		{
			mover(argv[1][i]-'0'-1);

			for(int j = 0; j < LOCKS; j++)
				printf(" %d",locks[j]);
			printf("\n");
		}
	}
	return 0;
}

void reset_locks(void)
{
	for(int i = 0; i < LOCKS; i++)
		locks[i] = 300;
	return;
}

bool brute(char* seq)
{
	for(int i = 0; i < (MAX_MOVES-1); i++)
	{
		int move = -1;
		switch(status())
		{
			/**case(-1):			//only do reducing moves
				for(move = (rand()%8)+1;(move ==1 || move ==5) ||move == 9;move = (rand()%8)+1)
				;
				break;**/
			case(LOCKS):
				seq[i+1] = '\0';//terminate string
				return true;	//done
				break;
			case(0-LOCKS):
				seq[i+1] = '\0';//terminate string
				return false;	//done
				break;
			default:			//do all moves
				for(move = (rand()%8)+1;(move == 9) || (move == 0);move = (rand()%8)+1)   
					;
				break;
		}

		mover(move-1);
		seq[i] = '0' + move; //log movement into seq
	}

	return false;
}

int status(void)
{
	int status = 0;
	for(int i = 0; i < LOCKS;i++)
	{
		if(locks[i]>400)  //over 400 pts
		{
			status--;
		}
		else if(locks[i] == 400)
		{
			status++;
		}
	}
	return status;
}

void mover(int action)
{
	for(int i = 0; i < LOCKS; i++)
		locks[i] += results[action][i];
	return;
}

void logger(char* seq, bool done, long counter,FILE* out)
{
	int len = strlen(seq);
	if(done)
		fprintf(out,"Attempt #%ld succeeded with sequence:\n", counter);
	else
		fprintf(out,"Attempt #%ld failed with sequence:\n", counter);

	fprintf(out,"Snapshot:\n");
	for(int i = 0; i < LOCKS; i++)
		fprintf(out,"L%d: %d ", i+1,locks[i]);

	fprintf(out,"\n");

	for(int i = 0; i < len;i++)
		fprintf(out,"%c,",seq[i]);
	fprintf(out,".\nTook %d moves.\n", len);

	return;
}

void sort(char* arr)
{
	bool sort = true;
	int len = strlen(arr);
	char temp;

	do
	{
		sort = false;
		for(int i =0; i < len-1;i++)
		{
			if(arr[i] > arr[i+1])
			{
				temp = arr[i];
				arr[i] = arr[i+1];
				arr[i+1] = temp;

				sort = true;
			}
		}

	}
	while(sort);
	return;
}