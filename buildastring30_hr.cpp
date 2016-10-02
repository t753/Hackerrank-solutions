#define _USE_MATH_DEFINES
#define _CRT_SECURE_NO_WARNINGS
#include <vector>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <cstring>
#include <string>
#include <ctime>
#include <queue>
#include <assert.h>
#include <bitset>
#include <cstring>
#include <fstream>
#include <istream>
#include <map>
#include <array>


using namespace std;


static int min(int a, int b){
	return a < b ? a : b;
}

static int add(int c, int (&costs_array) [30000], int array_length){

	int result = 0;
	//auto array_length = end(costs_array) - begin(costs_array);

	if (c < array_length){
		result = costs_array[c];
	}
	else {
		result =  0;
	}

	return result;
}

void solve(int n ,int a, int b, string s)  {
	
	static vector<int> pos[123];
	int costs_array [30000];

	string chars = "abcdefghijklmnopqrstuvwxyz";

	for (unsigned int i = 0; i < s.size(); i++) {
		pos[(unsigned char) s[i]].push_back(i);
	}

	 for(int i = n-1; i>=0;i--){

		 unsigned char c  = s[i];
		 bool found = false;

		 auto array_length = end(costs_array) - begin(costs_array);

		 int l = 1;

		 int tempCost = min(a,b) + add( i+l, costs_array, array_length);

		 for(int j : pos[c])  {
			if (j < i)  {
				found = true;
				int k = 0;
				int count = 0;

				while ((i +  k < n) && (j + k < i) && (s[j + k] == s[i + k]))  {
					count++;
					k++;
				}
				if (count > 1)  {
					int newCost = b + add( i+count, costs_array, array_length);
					tempCost = min(tempCost,newCost);
				}
			}

		 }

		 if (!found)  {
			 costs_array[i] = a + add( i+l, costs_array, array_length);
		 }

		costs_array[i] = tempCost;

	 }

	 int cost = costs_array[0];

	 cout << cost << endl;

}

int main(int argc, char* argv[])
{
		int t;
		cin >> t;

		while (t > 0) {
			string s;
			int n, a, b ;
			cin >> n >> a >> b >> s;

			solve(n ,a, b, s);
			t--;
		}

	return 0;
}

