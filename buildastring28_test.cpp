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


using namespace std;

int get_length(unsigned char c,  vector<int> (&pos)[123],  string &s, int i, int n, bool &found, int mode)  {


	if (mode == 1)
		found = false;
	int max_count = 0;


	for(int j : pos[c])  {
		if (j < i)  {
			found = true;
			int k = 0;
			int count = 0;

			while ((i +  k < n) && (j + k < i) && (s[j + k] == s[i + k]))  {
				count++;
				k++;
			}
			if (count > max_count)
				max_count = count;

		}
	}

	return max_count;
}

void update_costs(int max_len_curr, int max_len_nxt, int &cost, int &i,  int a, int b, string s, vector<int> (&pos)[123], int n, bool found,  int run)  {


	if (found == false)  {
		cost += a;
		i += 1;
	}
	else  {

		if (max_len_curr > 1)  {

			if (max_len_nxt >= max_len_curr && a < b)  {

				int next_pos = 	i + max_len_curr;
				unsigned char next_char = s[next_pos];
				int len = get_length(next_char, pos, s, next_pos, n, found , 1);
				int len_curr = len + max_len_curr;
				int len_nxt =  1 + max_len_nxt;
				int cost_nxt = a + b;
				int cost_curr = b;

				if (len <= 1)  {

					 cost_curr += a;
				}

				else  {
					 cost_curr += b;
				}

				if (cost_nxt < cost_curr && (len_nxt >= len_curr))  {

					 cost += a + b ;
					 i += len_nxt;
				}

				else if (cost_nxt < cost_curr && (len_curr > len_nxt))  {

					if (len_curr - len_nxt == 1 && run == 1)  {
						cost += a + b  + a;
						i += len_nxt + 1 ;
					}
					else  {
						cost +=  cost_curr;
						i += len_curr;
					}

				}
				else  {
					cost += cost_curr;
					i += len_curr;
				}
			}
			else   {

				i += max_len_curr;
				cost+= b;
				//b_count ++;
			}
		}
		else  {

			cost += a;
			i += 1;

		}
	}
}

void get_costs(int n, int &cost, string s, int &i,  int a, int b, vector<int> (&pos)[123], vector<int> (&curr_sizes), int run)  {


	if (i < n)  {


		unsigned char c  = s[i];
		string curr_str = s.substr(0, i);
		bool found = false;

		int max_len_curr = 0;
		int max_len_nxt = 0;

		max_len_curr = get_length(c, pos, s, i, n, found, 1);

		//curr_sizes.push_back(max_len_curr);

		unsigned char next_char = s[i + 1];

		if (found == true)  {

			max_len_nxt = get_length(next_char, pos, s, i + 1, n, found, 2);

		}

		update_costs(max_len_curr, max_len_nxt, cost, i,  a, b, s, pos, n, found, run);

	}

}
void solve(int n ,int a, int b, string s, string filename)  {
	
	static vector<int> pos[123];
	vector<string> substrings[26];
	vector<int> curr_sizes;
	vector<int> next_sizes;

	string chars = "abcdefghijklmnopqrstuvwxyz";

	for (unsigned int i = 0; i < s.size(); i++) {
		pos[(unsigned char) s[i]].push_back(i);
	}

	int cost = a;
	int i = 1;
	int run = 1;

	while (i < n)  {

		get_costs(n, cost, s, i,  a,  b, pos, curr_sizes, run);

	}

	int cost_1 = cost;

	cost = a;
	run = 2;
	i = 1;

	while (i < n)  {

		get_costs(n, cost, s, i,  a,  b, pos, next_sizes, run);

	}

	int cost_2 = cost;

	//int diff = b - a;
	//int mod = n / 300;

	//cost_2 -= diff * mod;

	/*string filenamex = "max_lens_" + filename;
	fstream output_file;
	output_file.open(filenamex, fstream::app);

	for ( int i = 0; i < n; i++)  {
		if (!curr_sizes.empty())  {
			curr_sizes.erase( unique( curr_sizes.begin(), curr_sizes.end() ), curr_sizes.end() );
		}
		else  {
			curr_sizes.push_back(-1);
		}
	}


	//cout << endl << "max lens = ";
	output_file << endl << endl;
	for (int i : curr_sizes)  {

		string result_str = to_string(i) + " ";
		output_file << result_str; // << endl;
	}
	output_file << endl << endl;
	output_file.close();*/

	//curr_sizes.clear();
	//next_sizes.clear();

	for (unsigned char i : chars)  {
		pos[i].clear();
	}

	if (cost_1 <= cost_2)
		cost = cost_1;
	else
		cost= cost_2;

	//cout << cost << endl;

	int result;
	string result_str;
	result = cost;


	cout << endl << cost_1 << endl;
	cout << endl << cost_2 << endl;

	if (filename == "")
	{
		ostringstream buf;

		result_str = to_string(result);
		//cout << result << endl;
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

	int option = 0;
	cout << "Enter 1 to run from file or 2 to run from termainal: ";
	cin >> option;

	if (argc > 1 && option == 1) {
		int start_s = clock();

		int test = 0;
		int t, n, a, b;
		string s;
		//int length = 0;

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
	//	int test = 0;
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

