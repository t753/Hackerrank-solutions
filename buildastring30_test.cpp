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

void solve(int n ,int a, int b, string s, string filename)  {
	
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



	//for (unsigned char i : chars)  {
	//	pos[i].clear();
	//}


	cout << cost << endl;

	int result;
	string result_str;
	result = cost;


	//cout << endl << cost_1 << endl;
	//cout << endl << cost_2 << endl;

	if (filename == "")
	{
		ostringstream buf;

		result_str = to_string(result);
		cout << result << endl;
	}

	else if (filename != "")
	{

		filename = "test_" + filename;

		fstream output_file;
		output_file.open(filename, fstream::app);
		result_str = to_string(result);
		output_file << result_str << endl;
		//output_file << result;
		output_file.close();
	}

}

int main(int argc, char* argv[])
{
	ios_base::sync_with_stdio(0);

	if (argc > 1) {
		int start_s = clock();

		int test = 0;
		int t, n, a, b;
		string s;

		for (int i = 1; i < argc; i++) {

			string filename = argv[i];
			ifstream ifs;
			ifs.open(filename);
			string line;
			test += 1;

			if (ifs.is_open() == true) {

				ofstream output_file;
				string output_filename = "test_" + filename;
				output_file.open(output_filename, fstream::out);

				output_file << "";

				output_file.close();

				ifs >> t;

				while (t--) {

					ifs >> n >> a >> b >> s;

					solve(n, a, b, s, filename);


				}

			} else {
				//cout << endl << "file not open";
			}

			ifs.close();
			string hr_filename = "";

			string test_filename = "test_" + filename;

			////cout << "test = " << to_string(test) << endl;

			if (test < 11)
				hr_filename = "output0" + to_string(test - 1) + ".txt";
			else
				hr_filename = "output" + to_string(test - 1) + ".txt";

			////cout << "hr_filename = " << hr_filename << endl;

			ifstream test_file;
			test_file.open(test_filename);
			ifstream hr_file;
			hr_file.open(hr_filename);

			bool passed = true;

			while (!test_file.eof() && !hr_file.eof()) {

				getline(test_file, line);
				string line2;
				getline(hr_file, line2);

				////cout <<"line =" << line << "     line 2 = "  << line2 << endl;

				if (line != line2)
					passed = false;

			}

			if (passed == true)
				cout << "Test " + to_string(test - 1) + " passed" << endl;
			else
				cout << "Test " + to_string(test - 1) + " failed" << endl;

			test_file.close();
			hr_file.close();

		}

		int stop_s = clock();
		float run_time = (stop_s - start_s) / double(CLOCKS_PER_SEC);
		cout << "build a string.cpp  \t\tExecution time = " << run_time << " seconds" << endl;
		string run_file = "runtimes.txt";
		fstream output_file;
		output_file.open(run_file, fstream::out);
		string result_str = "RegexToDFA10.cpp  \t\tExecution time = "
				+ to_string(run_time) + " seconds";
		output_file << result_str << endl;
		output_file.close();
	}
	else
	{
		string filename = "";
		int t;
		cin >> t;

		while (t > 0) {
			string s;
			int n, a, b ;
			cin >> n >> a >> b >> s;

			solve(n ,a, b, s, filename);
			t--;

		}
	}
	return 0;
}

