#include <iostream>

using namespace std;

struct AB
{
    int a;
    int b;
};

bool getYN(string answer);
void fizzbuzz();
AB getAB();

int main()
{
    string answer;
    while (true)
    {
        cout << "Hello! Would you like to play FizzBuzz? (y/n) ";
        cin >> answer;
        if (getYN(answer) == true)
        {
            fizzbuzz();
        }
        else
        {
            cout << "That's too bad, let's play another time then!" << endl << "Goodbye!";
            return 0;
        }
    }
}

//validate yes or no replies
bool getYN(string answer)
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

void fizzbuzz()
{
    cout << "Great! I love this game!" << endl << "First we need to set the range!" << endl << "We need two numbers, one for the start and one for the end." << endl << "Make sure you only insert integers (whole numbers) over 0!" << endl;    
    AB range, fizzbuzz;
    do
    {
        range = getAB();
        if (range.a > range.b)
        {
            cout << "That doesn't seem right... the game can't end before it starts!" << endl << "Make sure you're writing a second number that is larger than the first" << endl;
        }
    } while (range.a > range.b);
    cout << "Awsome!" << endl << "We will start with " << range.a << " and end with " << range.b << "!" << endl;
    do
    {
        fizzbuzz = getAB();
        if (fizzbuzz.a == fizzbuzz.b)
        {
            cout << "That doesn't seem right... we cant use the same number twice!" << endl << "Make sure you're writing a second number that is diferent than the first" << endl;
        }
    } while (fizzbuzz.a == fizzbuzz.b);
    cout << "Great! We're gonna replace multiples of " << fizzbuzz.a << "with the word fizz and multiples of " << fizzbuzz.b << " with the word buzz!" << endl << "Multiples of both will be replaced with FizzBuzz!" << endl;
    for (int i = range.a; i <= range.b; i++)
    {
        if (i % fizzbuzz.a == 0 || i % fizzbuzz.b == 0)
        {
            if (i % fizzbuzz.a == 0 && i % fizzbuzz.b == 0)
            {
                cout << "FizzBuzz!" << endl;
            }
            else if (i % fizzbuzz.a == 0 && i % fizzbuzz.b != 0)
            {
                cout << "Fizz!" << endl;
            }
            else if (i % fizzbuzz.a != 0 && i % fizzbuzz.b == 0)
            {
                cout << "Buzz!" << endl;
            }
        }
        else
        {
            cout << i << endl;
        }
    }
}

AB getAB()
{
    AB pair;
    do
    {
        cout << "What should the first number be? ";
        cin >> pair.a;
        if (pair.a < 1)
        {
            cout << "Sorry, it has to be an integer over 0!" << endl;
        }
    } while (pair.a < 1);
    do
    {
        cout << "What should the second number be? ";
        cin >> pair.b;
        if (pair.b < 1)
        {
            cout << "Sorry, it has to be an integer over 0!" << endl;
        }
    } while (pair.b < 1);
    return pair;
}