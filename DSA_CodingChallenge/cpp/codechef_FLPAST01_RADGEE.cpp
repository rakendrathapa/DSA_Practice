/**
 * PROBLEM NAME: Maths and Games
 * In a far away Galaxy of Tilky Way, there was a planet Tarth where the sport of Tompetitive Toding was very popular.
 * According to legends, there lived a setter known for his very tricky mathematical Game Theory problems.
 *
 * Radhesh was chosen for a game theory project under Ms Geethakoomaree! To celebrate it, he decided to play a game of cards with her.
 * The rules of the game are as follows-
 *
 * There are 3 piles of card with them, Radhesh's pile, Geethakoomaree's pile, and an extra pile.
 * The extra pile has an even number of cards (i.e. number of cards is a multiple of 2).
 * In each pile, the cards are stacked on top of each other.
 *
 * Each card has an integer written on it.
 * In each round, both of them will take the topmost card from their own piles.
 * The player whose card has the greater value wins the round and earns one point (It is guaranteed that their cards won't have same value in this step).
 * Both of them then discard the cards they used in that round permanently.
 * Now, if there are cards in the extra pile, the winner of that turn will pick the topmost card from the extra pile,
 * and place it at the bottom of their own pile.
 * And then the loser of that round will pick the next topmost card from the extra pile and place it at the bottom of their own pile.
 * Otherwise, the game continues as it is.
 *
 * The game continues on until all cards are discarded.
 * The player with most points wins.
 * Given the cards in each of the 3 piles, find the winner of the game, or determine if it is a tie!
 *
 * Input:
 * The first line has a single integer T, denoting number of test cases per file.
 *
 * Next line has 2 integers N and M, each where N is number of cards in Radhesh and Geethakoomaree's deck respectively,
 * and M is number of cards in the extra pile.
 *
 * Next 2 lines contain N integers each denoting cards in Radhesh and Geethakoomaree's pile respectively.
 * The first integer denotes the value on the topmost card, the second integer denotes the card beneath it, and so on.
 *
 * Next line has M integers denoting cards in extra pile. The first integer denotes the value on the topmost card, the second integer denotes the card beneath it, and so on.
 *
 * Output:
 * For each test case T print the answer in a new line as follows -
 * If Radhesh wins the game, print Radhesh wins
 * If Geethakoomaree wins, print Geethakoomaree wins
 * If the game results in a tie, print Tie
 *
 * Constraints
 * 1≤T≤10^5
 * 1≤N,M≤10^5
 * Sum of N,M over the entire test file does not exceed 10^6 and 2∗10^6 respectively.
 * M is a multiple of 2.
 * 0≤ values on the cards ≤10^9
 *
 * Subtasks
 * 30% points - N,M≤200
 * 70% points - Original Constraints
 *
 * Sample Input:
 * 3
 * 5 4
 * 1 4 7 10 12
 * 3 6 4 8 22
 * 7 8 9 14
 * 1 2
 * 1
 * 5
 * 2 5
 * 5 2
 * 1 2 3 4 5
 * 10 9 8 7 6
 * 12 11
 *
 * Sample Output:
 * Radhesh wins
 * Tie
 * Geethakoomaree wins
 *
 * EXPLANATION:
 * In the first testcase, the following happens-
 * Radhesh has card 1 and Geethakoomaree has card 3.
 * Geethakoomaree wins the round, she then takes the first card from extra deck and (i.e. 7) and Radhesh takes the next card, i.e. 8.
 * Geethakoomree's deck is (6,4,8,22,7) and Radhesh's deck is (4,7,10,12,8)
 *
 * Geethakoomaree wins next round as well. She has 2 points now. Her deck is (4,8,22,7,9) and Radhesh's deck is (7,10,12,8,14).
 * Note that now extra deck has no cards so no cards can be drawn from it after this.
 *
 * Based on above decks, Radhesh wins in turn 3,4,6,7 and has total of 4 points.
 * Geethakoomaree ends up with 3 points. Hence, Radhesh wins.
 */

#include <iostream>
#include <queue>

using namespace std;

extern void GetSolution(queue<long long>& rad, queue<long long>& gee, long long* extra, const int e_size);
int main()
{
    int t=0, n=0, m=0;

    long long val = 0;
    queue<long long> rad;
    queue<long long> gee;
    long long extra[100000] = {0};

    cin >> t;
    while(t--){
        cin >> n >> m;
        for(int i=0; i<n; i++){
            cin >> val;
            rad.push(val);
        }

        for(int i=0; i<n; i++){
            cin >> val;
            gee.push(val);
        }

        for(int i=0; i<m; i++){
            cin >> val;
            extra[i] = val;
        }

        GetSolution(rad, gee, extra, m);
    }

    return EXIT_SUCCESS;
}

void GetSolution(queue<long long>& rad, queue<long long>& gee, long long* extra, const int e_size)
{
    if((rad.size() == 0) || (gee.size() == 0)){
        return;
    }
    if(rad.size() != gee.size()){
        return;
    }

    int e_i=0;
    int c_rad=0;
    int c_gee=0;

    bool rad_w = false;
    while(rad.empty() != true){
        cout << "rad:" << rad.front() << " " << "gee:" << gee.front() << " ";
        if(rad.front() > gee.front()){
            c_rad++;
            cout << "WIN: rad";
            rad_w = true;
        } else {
            c_gee++;
            cout << "WIN: gee";
            rad_w = false;
        }
        cout << endl;

        if(e_i < e_size){
            if(rad_w){
                rad.push(extra[e_i++]);
                gee.push(extra[e_i++]);
            }else{
                gee.push(extra[e_i++]);
                rad.push(extra[e_i++]);
            }
        }

        rad.pop();
        gee.pop();
    }

    if(c_rad > c_gee){
        cout << "Radhesh wins" << endl;
    }
    else if(c_rad < c_gee){
        cout << "Geethakoomaree wins" << endl;
    }
    else{
        cout << "Tie" << endl;
    }
}
