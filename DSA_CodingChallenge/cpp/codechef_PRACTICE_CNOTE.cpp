/**
 * PROBLEM NAME: Chef and Notebooks
 * Chef likes to write poetry. Today, he has decided to write a X pages long poetry, but unfortunately his notebook has only Y pages left in it.
 * Thus he decided to buy a new CHEFMATE notebook and went to the stationary shop. Shopkeeper showed him some N notebooks,
 * where the number of pages and price of the ith one are Pi pages and Ci rubles respectively.
 * Chef has spent some money preparing for Ksen's birthday, and then he has only K rubles left for now.
 *
 * Chef wants to buy a single notebook such that the price of the notebook should not exceed his budget and he is able to complete his poetry.
 * Help Chef accomplishing this task. You just need to tell him whether he can buy such a notebook or not. Note that Chef can use all of the Y pages
 * in the current notebook, and Chef can buy only one notebook because Chef doesn't want to use many notebooks.
 *
 * Input
 * The first line of input contains an integer T, denoting the number of test cases. Then T test cases are follow.
 * The first line of each test case contains four space-separated integers X, Y, K and N, described in the statement.
 * The ith line of the next N lines contains two space-separated integers Pi and Ci, denoting the number of pages and price of the ith notebook respectively.
 *
 * Output
 * For each test case, Print "LuckyChef" if Chef can select such a notebook, otherwise print "UnluckyChef" (quotes for clarity).
 *
 * Constraints and Subtasks
 * 1 ≤ T ≤ 10^5
 * 1 ≤ Y < X ≤ 10^3
 * 1 ≤ K ≤ 10^3
 * 1 ≤ N ≤ 10^5
 * 1 ≤ Pi, Ci ≤ 10^3
 *
 * Subtask 1: 40 points
 * Sum of N over all test cases in one test file does not exceed 10^4.
 *
 * Subtask 2: 60 points
 * Sum of N over all test cases in one test file does not exceed 106.
 *
 * Sample
 * Input
 * 3
 * 3 1 2 2
 * 3 4
 * 2 2
 * 3 1 2 2
 * 2 3
 * 2 3
 * 3 1 2 2
 * 1 1
 * 1 2
 *
 * Output
 * LuckyChef
 * UnluckyChef
 * UnluckyChef
 *
 * Explanation
 * Example case 1. In this case, Chef wants to write X = 3 pages long poetry, but his notebook has only Y = 1 page.
 * And his budget is K = 2 rubles, and there are N = 2 notebooks in the shop. The first notebook has P1 = 3 pages,
 * but Chef cannot buy it, because its price is C1 = 4 rubles. The second notebook has P2 = 2 pages, and its price is C2 = 2 rubles.
 * Thus Chef can select the second notebook to accomplish the task. He will write 1 page of poetry in the old notebook, and 2 page of poetry in the new notebook.
 *
 * Example case 2. Chef cannot buy any notebook, because the prices exceed the Chef's budget.
 * Example case 3. No notebook contains sufficient number of pages required to write poetry.
 **/

#include <iostream>
#include <utility>

using namespace std;

void GetSolution(const int req_p, const int k, const int n, const pair<int, int>* c_p)
{
    for (int i=0; i<n; i++){
        cout << "REQ_P:" << req_p << " REQ_C:"<< k << " page:" << c_p[i].first << " cost:"<< c_p[i].second << endl;
        if((c_p[i].first >= req_p) && (c_p[i].second <= k))
        {
            cout << "LuckyChef" << endl;
            return;
        }
    }
    cout << "UnluckyChef" << endl;
}

int main()
{
    int t=0, x=0, y=0, k=0, n=0;
    int req_p=0;

    pair <int, int> c_p[100000];
    int cost = 0, pages = 0;

    cin >> t;
    while(t--){
        cin >> x >> y >> k >> n;
        for(int i=0; i<n; i++){
            cin >> pages >> cost;
            c_p[i] = make_pair(pages, cost);
        }

        req_p = x - y;
        if(req_p <= 0){
            cout << "LuckyChef" << endl;
            continue;
        }
        GetSolution(req_p, k, n, c_p);
    }

    return EXIT_SUCCESS;
}
