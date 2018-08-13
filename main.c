#include <stdio.h>

#define MAXLINE 100

//Determines Player Base.
static int Players = 0;
static int Deck = 0;
static int Werewolves = 0;
static int Towns = 0;

//Specify What Roles to Include.
//Tanner
static int Tanner = 0;
//Werewolves
static int Alpha = 0;
static int Mystic = 0;
static int Minion = 0;
//Townies
static int PI = 0;
static int Aura_Sear = 0;
static int Robber = 0;
static int Troublemaker = 0;
static int Witch = 0;
static int Drunk = 0;
static int Doppelganger = 0;

int main(int argc, char **argv){
	char line[MAXLINE];
	char opt;
	if(argc > 1){
		
	}
	else{
		fprintf(stdout, "How many players?\n");
		do{
			fgets(line, MAXLINE, stdin);
			sscanf(line, "%d", &Players);
			if(Players<3){
				fprintf(stdout,"There should be atleast 3 players for a game.\n");
				fprintf(stdout,"Please enter the amount of players:\n");
			}
		}while(Players<3);
		
		Deck = Players + 3;
		do{
			fprintf(stdout,"Would you like to specify the number of Werewolves? (y/n): ");
			fgets(line, MAXLINE, stdin);
			sscanf(line, "%c", &opt);
		}while(opt != 'y' && opt != 'n');

		if(opt == 'y'){
			
		}
		else if(opt == 'n'){
			Werewolves = Deck/3;
			Towns = Deck - Werewolves;
			fprintf(stdout, "There are %d Werewolves and %d Villagers\n", Werewolves, Towns);
		}
	}
	return 0;
}
