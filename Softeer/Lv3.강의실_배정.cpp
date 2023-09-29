#include<iostream>
#include<algorithm>
#include<vector>

using namespace std;

int main(int argc, char** argv)
{
	int N;
	scanf("%d", &N);

	vector<pair<int, int>> time;
	for(int i=0; i<N; i++){
		int start, end;
		scanf("%d %d", &start, &end);
		time.push_back({end, start});
	}

	sort(time.begin(), time.end());
	int answer = 0;
	int prev_end = 0;

	for(int i=0; i<N; i++){
		if (time[i].second >= prev_end){
			answer += 1;
			prev_end = time[i].first;
		}
	}

	printf("%d", answer);
	return 0;
}
