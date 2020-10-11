//dynamically allocated array

#include <iostream>

// M x N matrix
#define M 4
#define N 5

using namespace std;
// Dynamically Allocate Memory for 2D Array in C++
int main()
{

    int row;
    int col;

    cout << "enter number of rows \n";
    cin >> row;


    int *elemsPerRow = new int[row];



    int** A = new int*[row];


    for(int i = 0; i < row; i++){
              cout << "enter number of elements in row " << i << "\n";
        cin >> col;

        A[i] = new int[col];

        elemsPerRow[i] = col;

    }

    for(int i = 0; i < row; i++){
            cout << "enter elements per row \n";
        for(int j = 0; j < elemsPerRow[i]; j++){
            int x;
            cin >> x;
            A[i][j] = x;
        }
    }


  for(int i = 0; i < row; i++){
        for(int j = 0; j < elemsPerRow[i]; j++){

           cout << A[i][j] <<" ";
        }
        cout << "\n";
    }

    for(int i = 0 ; i < row; i++){
        delete [] A[i];
    }

    delete [] A;


	// dynamically allocate memory of size M*N
//	int* A = new int[M * N];
//
//	// assign values to allocated memory
//	for (int i = 0; i < M; i++)
//		for (int j = 0; j < N; j++)
//			*(A + i*N + j) = rand() % 100;
//
//	// print the 2D array
//	for (int i = 0; i < M; i++)
//	{
//		for (int j = 0; j < N; j++)
//			std::cout << *(A + i*N + j) << " ";	// or (A + i*N)[j])
//
//		std::cout << std::endl;
//	}
//
//	// deallocate memory
//	delete[] A;
//
//	return 0;

//double * a;
//
//   std::cout << sizeof a;


}

//	3. Using array of pointers
//	#include <iostream>
//
//	// M x N matrix
//	#define M 4
//	#define N 5
//
//	// Dynamic Memory Allocation in C++ for 2D Array
//	int main()
//	{
//		// dynamically create array of pointers of size M
//		int** A = new int*[M];
//
//		// dynamically allocate memory of size N for each row
//		for (int i = 0; i < M; i++)
//			A[i] = new int[N];
//
//		// assign values to allocated memory
//		for (int i = 0; i < M; i++)
//			for (int j = 0; j < N; j++)
//				A[i][j] = rand() % 100;
//
//		// print the 2D array
//		for (int i = 0; i < M; i++)
//		{
//			for (int j = 0; j < N; j++)
//				std::cout << A[i][j] << " ";
//
//			std::cout << std::endl;
//		}
//
//		// deallocate memory using delete[] operator
//		for (int i = 0; i < M; i++)
//			delete[] A[i];
//
//		delete[] A;
//
//		return 0;
//	}
//

