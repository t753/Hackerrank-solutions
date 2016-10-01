// MatrixRotation.cpp : Defines the entry point for the console application.
//

//#include "stdafx.h"
#include <iostream>

using namespace std;

int main()
{
//	int i, j, k;
	int m, n, r;
	int rotations, rot;
	int loop_decrement, loop_rotation;
	int m_start, m_end, m_len;
	int n_start, n_end, n_len;
	int m_curr, n_curr;

//-------------------------------------------------------------------------
// For hackerrank testing
//-------------------------------------------------------------------------

	int i, j;

	for (i = 1; i <= 3; i++)
	{

		if (i == 1) std::cin >> m;
		else if (i == 2) std::cin >> n;
		else std::cin >> r;

	}

	int **matrix = new int*[m];
	for (int i = 0; i < m; ++i) {
		matrix[i] = new int[n];
	}

	for (i = 0; i < m; i++)
		for (j = 0; j < n; j++)
			std::cin >> matrix[i][j];
			

	//-------------------------------------------------------------------------
	// For local machine in Visual Studio testing
	//-------------------------------------------------------------------------

/*	

	int i, j, k;

	m = 4;
	n = 4;
	r = 2;

	int **matrix = new int*[m];
	for (int i = 0; i < m; ++i) {
		matrix[i] = new int[n];
	}

	k = 1;
	for (i = 0; i < m; i++)
		for (j = 0; j < n; j++)
		{
			matrix[i][j] = k;
			k += 1;
		}

	for (i = 0; i < m; i++)
		for (j = 0; j < n; j++)
		{
			std::cout << matrix[i][j] << " ";

			if (j == n - 1)
				std::cout << endl;

		}

	std::cout << endl;

	*/

	//-------------------------------------------------------------------------
	// Begin computations
	//-------------------------------------------------------------------------

	m_start = 0;
	m_end = m - 1;

	n_start = 0;
	n_end = n - 1;

	m_len = m_end - m_start;
	n_len = n_end - n_start;

	
	// Following while loop is all rotations
	// for all loops one loop at a time

	loop_decrement = 1;

	while (m_len >= 1 && n_len >= 1)
	{
		// loop_rotation = number of items in current loop
		
		loop_rotation = (n - loop_decrement) + (m - loop_decrement) + (n - loop_decrement) + (m - loop_decrement);

		rot = r % loop_rotation;

		for (rotations = 1; rotations <= rot; rotations++)
		{

			int loop_start = matrix[m_start][n_start];

			// Following for loop is for top row in current loop

			m_curr = m_start;
			n_curr = n_start;

			for (i = 1; i <= n_len  ; i++)
			{

				matrix[m_curr][n_curr] = matrix[m_curr][n_curr + 1];
				n_curr += 1;

			}

			// Following for loop is for right col in current loop

			m_curr = m_start;
			n_curr = n_end;

			for (i = 1; i <= m_len  ; i++)
			{

				matrix[m_curr][n_curr] = matrix[m_curr + 1][n_curr];
				m_curr += 1;

			}

			// Following for loop is for bottom row in current loop

			m_curr = m_end;
			n_curr = n_end;

			for (i = 1; i <= n_len  ; i++)
			{

				matrix[m_curr][n_curr] = matrix[m_curr][n_curr - 1];
				n_curr -= 1;

			}

			// Following for loop is for left col in current loop

			m_curr = m_end;
			n_curr = n_start;

			for (i = 1; i <= m_len   ; i++)
			{
				if (i < m_len )
				{
					matrix[m_curr][n_curr] = matrix[m_curr - 1][n_curr];
					m_curr -= 1;

				
				}

				else
				{
			
					matrix[m_curr][n_curr] = loop_start;


				}
			
			}

		} // End for loop

		m_start += 1;
		m_end -= 1;

		n_start += 1;
		n_end -= 1;

		m_len = m_end - m_start;
		n_len = n_end - n_start;

		loop_decrement += 2;

	} // End while loop

	// End computations, now output to command line

	for (i = 0; i < m; i++)
		for (j = 0; j < n; j++)
		{
			std::cout << matrix[i][j] << " ";

			if (j == n - 1)
				std::cout << endl;

		}


    return 0;
}

