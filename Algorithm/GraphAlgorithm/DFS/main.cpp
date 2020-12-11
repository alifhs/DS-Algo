#include "bits/stdc++.h"
using namespace std;


//sample input

//7
//6
//0 1
//0 2
//1 2
//3 4
//4 5
//3 5

void initialize(vector<bool>&, int );
void dfs(int, vector<vector<int>>& );
//leftshift, rightshift operator

vector<bool>visited;
int main()
{
    int connectedComponents = 0;
      int nodes;
    cout << "enter number of nodes \n";
    cin >> nodes;
    vector<vector<int>> v(nodes);


    initialize(visited, nodes);

    cout << "enter the number of edges \n";

    int edges;

    cin >> edges;

    cout << "enter the edges \n";

    int x,y;
    for(int i = 0; i < edges; i++)
    {
        cin >> x >> y;
        v[x].push_back(y);
        v[y].push_back(x);
    }

    for(int i = 0 ;i < nodes; i++) {
         if(visited[i] == false)     {
             dfs(i, v);
             connectedComponents++;
         }
        }

    cout << "Number of connected components "<< connectedComponents << "\n";

    return 0;
}

 void initialize(vector<bool>&visited, int n) {
        for(int i = 0;i < n;++i)
         visited.push_back(false);
    }

void dfs(int s, vector<vector<int>>&v){
    visited[s] = true;

    for(size_t i = 0; i < v[s].size(); i++){
        if(visited[v[s][i]] == false){
            dfs(v[s][i], v);
        }
    }

}
