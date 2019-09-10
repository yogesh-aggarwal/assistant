#include <iostream>
#include "tools.h"
#include <bits/stdc++.h>

using namespace std;


int main()
{
    string query = "hey jarvis can you play a song for me";

    string words[] = {"hey", "jarvis", "please", "can", "may", "you"};

    for (int index = 0; index < sizeof(words)/sizeof(words[0]); index++)
    {
        cout << "Word: " << words[index] << endl;
        if (true)
        {
            try
            {
                transform(query.begin(), query.end(), query.begin(), ::tolower);
                query.replace(query.find(words[index]), words[index].length(), "");
            }
            catch (out_of_range &e) {}
        }
    }
    cout << query << endl;
    return 0;
}
