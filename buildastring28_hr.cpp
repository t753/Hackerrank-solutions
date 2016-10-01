#define _USE_MATH_DEFINES
#define _CRT_SECURE_NO_WARNINGS
#include <vector>
#include <algorithm>
#include <iostream>
#include <string>


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
			while ((i + k < n) && (j + k < i) && (s[j + k] == s[i + k]))  {
				count++;
				k++;
			}
			if (count > max_count)
				max_count = count;
		}
	}
	return max_count;
}

void update_costs(int max_len_curr, int max_len_nxt, int &cost, int &i,  int a, int b, string s, vector<int> (&pos)[123], int n, bool found, int run)  {

	if (found == false)  {
		cost += a;
		i += 1;
	}
	else  {

		if (max_len_curr > 1)  {

			if (max_len_nxt >= max_len_curr && a < b)  {

				int next_pos = 	i + max_len_curr;
				unsigned char next_char = s[next_pos];
				int len = get_length(next_char, pos, s, next_pos, n, found, 3);
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
				if (cost_nxt <= cost_curr && (len_nxt >= len_curr))  {
					 cost += a + b ;
					 i += len_nxt;
				}
				else if (cost_nxt < cost_curr && (len_curr > len_nxt))  {
					if (run == 1)  {
						cost += a + a + b ;
						i += len_nxt + 1;
					}
					else  {
						cost += b;
						i += max_len_curr;
					}
				}
				else  {
					cost += b;
					i += max_len_curr;
				}
			}
			else   {
				int cost_a = a * max_len_curr;
				if (cost_a < b)
					cost += cost_a;
				else
					cost += b;
				i += max_len_curr;
			}
		}
		else  {
			cost += a;
			i += 1;
		}
	}
}

void get_costs(int n, int &cost, string s, int &i,  int a, int b, vector<int> (&pos)[123], int run)  {

	unsigned char c  = s[i];
	string curr_str = s.substr(0, i);
	bool found = false;

	int max_len_curr = 0;
	int max_len_nxt = 0;
	max_len_curr = get_length(c, pos, s, i, n, found, 1);

	int next_pos = i + 1;
	unsigned char next_char = s[next_pos];

	if (found == true)  {

		max_len_nxt = get_length(next_char, pos, s, i+1, n, found , 2);

	}

	update_costs(max_len_curr, max_len_nxt, cost, i,  a, b, s, pos, n, found,  run);

}
void solve(int n ,int a, int b, string s)  {
	
	static vector<int> pos[123];
	vector<string> substrings[26];
	string chars = "abcdefghijklmnopqrstuvwxyz";

	for (unsigned int i = 0; i < s.size(); i++) {
		pos[(unsigned char) s[i]].push_back(i);
	}

	int cost = a;
	int i = 1;
	int run = 1;

	while (i < n)  {
		get_costs(n, cost, s, i,  a,  b, pos,  run);
	}

	int cost_1 = cost;

	cost = a;
	run = 2;
	i = 1;

	while (i < n)  {
		get_costs(n, cost, s, i,  a,  b, pos, run);
	}

	int cost_2 = cost;

	if (cost_1 <= cost_2)
		cost = cost_1;
	else
		cost= cost_2;

	for (unsigned char i : chars)  {
		pos[i].clear();
	}
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

