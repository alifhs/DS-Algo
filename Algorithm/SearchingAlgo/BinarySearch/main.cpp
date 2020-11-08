#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int binarySearch(vector<int>&v, int valueTofind )
{
    int startInd = 0;
    int endInd = v.size()-1;

    while(startInd <= endInd)
    {
        int mid = (startInd + endInd)/2;
        if(v[mid] == valueTofind)
            return mid;
        else if(v[mid] < valueTofind)
        {
            startInd =  mid + 1;
        }
        else
        {
            endInd = mid - 1;
        }
    }
    return -1;

}

int main()
{
    int n;

    cin >> n;
    vector<int> v;
    for(int i = 0; i < n; i++)
    {
        int var;

        cin >> var;

        v.push_back(var);
    }
    sort(v.begin(), v.end());

    cout << "Enter value to search \n";

    int valueTofind;
    cin >> valueTofind;

    int index = binarySearch(v, valueTofind);

    if(index == -1)
    {
        cout << "Value not found \n";
    }
    else
    {
        cout << "value found at " << index << "\n";
    }




    return 0;
}
