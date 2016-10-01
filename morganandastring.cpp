

//#include "stdafx.h"
#include <cmath>
#include <cstdio>
#include <vector>
#include <unordered_set>
#include <string>
#include <iostream>
#include <algorithm>
#include <sstream>
#include <iterator>  
#include <assert.h>

using namespace std;



void printupto(string &a, int  &i, int &k)
{
		while (i < k)
		{
	
			printf("%c", a[i]);
			i += 1;

		}
	
}

void popthestack(string &a, int  &i)
{

			printf("%c", a[i]);
			i += 1;

}

void findnextchar(string &a, string &b, int len_a, int len_b, int &i, int &j)
{
	// Next, check if next char's from current indexes are identical
	if (i < len_a - 1 && j < len_b - 1 && a[i + 1] == b[j + 1])
	{
		int k = i;
		int l = j;

		int print_up_to = 0;

		char ak = a[k];
		char bk = b[l];
		char akp = a[k + 1];
		char blp = b[l + 1];

		// Check for identical strings
		while (k < len_a - 1 && l < len_b - 1 && a[k] == b[l])
		{
			// Check for identical chars in identical strings
			if (akp == a[k + 1] && blp == b[l + 1] && ak >= akp && bk >= blp)

				print_up_to += 1;

			k++;
			l++;


		}

		// Print string of identical chars in identical strings
		if (print_up_to == k - i - 1 && print_up_to >= 1)
		{
	
			if (a[k] <= b[l])
			{
	
				printupto(a, i, k);

			}

			else if (a[k] > b[l])
			{
	
				printupto(b, j, l);

			}

		}

		// Pop stack and print char in identical strings
		else
		{
			if (a[k] == b[l])
			{
				if (len_a - i > len_b - j)
				{
					popthestack(a, i);
				}
				else
				{
					popthestack(b, j);
				}
			}
			
			else if (a[k] < b[l])
			{

				popthestack(a, i);

			}

			else if (b[l] < a[k])
			{
	
				popthestack(b, j);


			}



		}

	}

	// Current chars are identical but next chars are not
	else if (i < len_a - 1 && j < len_b - 1 && a[i + 1] != b[j + 1])
	{

		if (a[i + 1] < b[j + 1])
		{

			popthestack(a, i);

		}
		
		else if (b[j + 1] < a[i + 1])
		{
			popthestack(b, j);

		}

	}

	// End of at least one string
	else if (i == len_a - 1 || j == len_b - 1)
	{

		popthestack(a, i);
	
	}

}


int main()
{
	int t, i, j, k, l, m;
	string a, b;

	cin >> t;

	string *strings = new string[t * 2];

	for (i = 0; i < t * 2; i++)
	{
		cin >> strings[i];
	}

	int str = 0;

	for (m = 0; m < t; m++)
	{
		a = strings[str];
		b = strings[str + 1];

		int len_a = a.length();
		int len_b = b.length();

		for (i = 0; i < len_a; i++) {
			if (a[i] >= 'A' && a[i] <= 'Z')  continue;
			assert(0);
		}
		assert(len_a <= 100000);

		for (i = 0; i < len_b; i++) {
			if (b[i] >= 'A' && b[i] <= 'Z')  continue;
			assert(0);
		}
		assert(len_b <= 100000);

		for (i = 0, j = 0; i < len_a && j < len_b;)
		{

			if (a[i] < b[j])
			{
				popthestack(a, i);

			}

			else if (b[j] < a[i])
			{

				popthestack(b, j);

			}

			else // Current char's in strings are identical
			{
			
				findnextchar(a, b, len_a, len_b, i, j);

			}

		}

		while (i < len_a)
		{

			printf("%c", a[i]);
			i++;

		}

		while (j < len_b)
		{
			printf("%c", b[j]);
			j++;

		}

		str += 2;

		printf("\n");

	}

	return 0;
}

