#include<iostream>
#include<string>

using namespace std;

int main(int argc, char** argv)
{
	int n, k;
	cin >> n >> k;

	string factory;
	cin >> factory;

	int answer = 0;
	for(int i=0; i<factory.size(); i++) {
		if (factory[i] == 'P') {
			for(int j=i-k; j<i+k+1; j++) {
				if (j<0 || j==i || j>=factory.size()) continue;
				if (factory[j] == 'H'){
					answer += 1;
					factory[j] = 'N';
					break;
				}
			}
		}
	}

	cout << answer << endl;
	return 0;
}
