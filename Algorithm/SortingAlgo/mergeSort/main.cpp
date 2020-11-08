#include <iostream>
#include <vector>

using namespace std;

void fmerge(vector<int>&leftArr, vector<int>&rightArr, vector<int>&arr)
{
    int lenLeft = leftArr.size();
    int lengRight = rightArr.size();

    int i,j,k;
    i = j = k = 0;
    while(i < lenLeft && j < lengRight)
    {
        if(leftArr[i] <= rightArr[j])
        {
            arr[k] = leftArr[i];
            i++;
            k++;
        }
        else
        {
            arr[k] = rightArr[j];
            k++;
            j++;
        }
    }

    while(i < lenLeft)
    {
        arr[k] = leftArr[i];
        i++;
        k++;
    }
    while(j < lengRight)
    {
        arr[k] = rightArr[j];
        k++;
        j++;
    }
    return;
}

void mergeSort(vector<int> &arr)
{



    int n = arr.size();
    if(n < 2)
        return;
    int mid = n/2;


    vector<int> leftArr;
    vector<int> rightArr;

    for(int i = 0 ; i < mid; i++)
        leftArr.push_back(arr[i]);




    for(int i = mid; i < n; i++)
        rightArr.push_back(arr[i]);

    mergeSort(leftArr);
    mergeSort(rightArr);

    fmerge(leftArr, rightArr, arr);


    return;

}

int main()
{

    vector<int> arr;

    int n;
    cout << "enter number of elements \n";
    cin>>n;
    int var;
    for(int i= 0; i < n; i++)
    {
        cin >> var;
        arr.push_back(var);

    }


    mergeSort(arr);

    for(int i = 0; i < n; i++)
        cout << arr[i] <<" ";

    cout << "\n";




    return 0;
}
