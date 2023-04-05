#include <iostream>

using namespace std;

bool get_yn(string answer);

int main()
{
    string answer;
    while (true)
    {
        cout << "Hello! Would you like to play FizzBuzz? (y/n) ";
        cin >> answer;
        if (get_yn(answer) == true)
        {

        }
        else
        {
            cout << "That's too bad, let's play another time then!" << endl << "Goodbye!";
            return 0;
        }
    }
}

//validate yes or no replies
bool get_yn(string answer)
{
    while (true)
    {
        answer[0] = toupper(answer[0]);
        if (answer[0] == 'Y' || answer[0] == '1')
        {
            return true;
        }
        else if (answer[0] == 'N' || answer[0] == '0')
        {
            return false;
        }
        else
        {
            cout << "Sorry, I didn't understand!" << endl << "You should reply with yes or no!" << endl << "Would you like to play FizzBuzz? (y/n) ";
            cin >> answer;
        }
    }
}