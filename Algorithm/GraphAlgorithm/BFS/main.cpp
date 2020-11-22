//shortest path finding

#include <iostream>
#include <vector>
#include <queue>
#include <climits>


using namespace std;

void path(vector<int>&prev, int nodeToFind)
{


    int i = nodeToFind;
    vector<int>path;
    while(i!=INT_MIN)    //backtracking
    {
        path.push_back(i);
        i = prev[i];
    }
    for(int i = path.size()-1; i>=0; i--)
        cout << path[i] <<" ";

}

void bfs(vector<vector<int>>&v, int s, int nodeToFind)
{

    vector<bool>visited;
    int nodes = v.size();
    for(int i=0; i<nodes; i++)
        visited.push_back(false);
    queue<int>q;
    q.push(s);
    vector<int>prev;
    visited[s] = true;
    

    for(int i=0; i<nodes; i++)
        prev.push_back(INT_MIN);
//        cout << prev[0] << " prev";

    while(!q.empty())
    {
        int parent = q.front();
        q.pop();

        int childsNumber = v[parent].size();

        for(int i =0 ; i < childsNumber ; i++)
        {
            if(visited[v[parent][i]] == false)
            {
                q.push(v[parent][i]);
                prev[v[parent][i]] = parent;
                visited[v[parent][i]] = true;  //keeping the tracks/marks of the parent nodes for backtracking
            }
        }
    }


    path(prev, nodeToFind);

}


int main()
{
    int n;
    cout << "enter number of nodes \n";
    cin >> n;
    vector<vector<int>> v(n);

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
    cout << "enter source node & destinationNode\n";
    int s, d;

    cin >> s >> d;
//   cout << s << " value of s";


    bfs( v, s, d);

//Input data for testing

//10
//9
//1 2
//1 3
//2 6
//2 4
//6 9
//4 9
//9 8
//3 7
//7 8
//1 9

    return 0;
}
