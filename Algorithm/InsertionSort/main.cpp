#include <iostream>

using namespace std;

void insetionSort(int*, int );

int main()
{
    int arr[] = {9,3,12,12,32,12,121,212};
    int n = sizeof(arr)/sizeof(arr[0]);

    cout << n << endl;
    insetionSort(arr, n);

    for(int i = 0 ; i < n; i++)
            cout << arr[i] << " ";

    cout << "\n";
    return 0;
}


void insetionSort(int* arr, int n)
{

    for(int i =1; i < n; i++)
    {
        int value = arr[i];
        int hole = i;   // left side of the partition is sorted and right side is unsorted

        while(hole > 0 && arr[hole-1] > value )   // for ascending order we have to check if the value of arr[hole-1] > value
        {
                arr[hole] = arr[hole-1]; //moving the value to fill up right hole creates new hole on the left side
                hole = hole - 1;
        }
        arr[hole] = value;
    }

}
