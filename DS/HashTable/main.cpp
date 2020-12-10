#include <iostream>
#include <string>

using namespace std;



class Dictionary
{

public:

    string keyWord;
    string definition;
    Dictionary* next;  //for separate chaining

    Dictionary(string keyWord, string definition)
    {
        this->keyWord = keyWord;
        this->definition = definition;
        this->next = NULL;
    }

};
Dictionary** dArray = new Dictionary*[10];

int hashFunction(string key)
{
    int sumOfStrAscii = 0;
    for(size_t i = 0; i < key.length(); i++)  //add all the ascii values of the string
    {
        int startAscii = 64;
        if(key[i] > 90)
            startAscii = 96;
        sumOfStrAscii += (((int)key[i]) * (i+((int)key[i])-startAscii));  //ASCII * ( position of char in string + pos in alphabet
    }
    return sumOfStrAscii;

}

void storeKeyValue(string key, string definition)
{


    int hashValue = hashFunction(key) % 10;

//    cout << "hash Values " << hashValue << "\n";
    if(dArray[hashValue] == NULL || (!dArray[hashValue]->keyWord.compare(key)))  //if hashvalue is unique or same key (means user want to update)
    {
//        cout << " dArray[hashValue] != NULL \n";
        dArray[hashValue] = new Dictionary(key, definition);
    }
    else // if duplicates hash exists
    {
        Dictionary* temp = dArray[hashValue];
        Dictionary* prev = temp;
        while(temp != NULL)
        {
            prev = temp;
            temp = temp->next;
        }
        prev->next = new Dictionary(key, definition);


    }



}

void printKeyValues(string word)
{

    int hashVal = hashFunction(word) % 10;

    if(dArray[hashVal] != NULL)
    {
        if(dArray[hashVal]->next == NULL)
        {
            cout <<"hashValue " <<hashVal<< " ||| " <<dArray[hashVal]->keyWord <<" => " << dArray[hashVal]->definition << "\n";

        }
        else
        {
            Dictionary* temp = dArray[hashVal];
//                    Dictionary* prev = temp;
            while(temp != NULL)
            {
                if(!temp->keyWord.compare(word))
                {
                    cout <<"hashValue " <<hashVal<< " ||| " <<temp->keyWord <<" => " << temp->definition << "\n";
                    break;
                }
                else
                {
                    temp = temp->next;
                }

            }
        }
    }




}


int main()
{

    //create an array of pointer that is going to point to the dictionary  object
//    cout << node->keyWord << " => " << node->definition << "\n";

    string keys[] = {"Door", "Search", "Next", "track", "camp", "boring", "digging", "Car", "thought", "open" };
    string values[] = {"Gate", "investigation", "following", "path", "tent", "annoying", "mining", "vehicle", "idea", "free"};

    //will be replaced with dynamic values
    for(int i = 0; i < 10; i++)
    {
        dArray[i] = NULL;
    }

    for(int i=0; i < 10; i++)
    {
        storeKeyValue(keys[i], values[i]);
    }


    cout << "Enter Keys Door, Search, Next, track, camp, boring, digging Car, thought, open \n";

    for(int i = 0 ; i < 10; i++)
    {

        printKeyValues(keys[i]);

    }


//    dArray[hashValue] = dictionary;










    return 0;
}
