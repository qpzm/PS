#include <iostream>
#include <string>
#define caesar(x) (((x) - 'A' - 3 + 26) % 26 + 'A')
using namespace std;

int main() {
  string input;
  string output = "";
  int i = 0;

  getline (cin, input);
  while(input[i] != '\0') {
    output += caesar(input[i]);
    i++;
  }
  cout << output << endl;
  return 0;
}
