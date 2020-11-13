#include <bits/stdc++.h>

using namespace std;

//Generic doubly linked list

//compiler will first look for the use of class. If there is a use it will be kept otherwise it will be discarded

template <class T> // can't declare same variable twice
class DoublyLinkedList
{
private:

template <class U>  // can't declare same variable twice like class T...you either use it or declare a new one
    class Node
    {
    public:
        U data;
        Node<U>* prev;
        Node<U>* next;


        Node(U data, Node<U>* prev, Node<U>* next)
        {
            this->data = data;
            this->prev = prev;
            this->next = next;
        }


    };
    int size = 0;
    Node<T>* head = NULL; //since there is a use of Node class U will be replaced with the type provided in DoublyLinkedList<type>
    Node<T>* tail = NULL;


    // Internal node class to represent data


public:
    void clear()
    {
        Node<T>* trav = head;

        while(trav != NULL)
        {
            Node<T>* next = trav->next;
            delete trav;
            trav = next;
        }
    }

    int listSize()
    {
        return size;
    }

    bool isEmpty()
    {
        return listSize() == 0;
    }

    void add(T elem)
    {
        addLast(elem);
    }
    void addLast(T elem)
    {
        if(isEmpty())
        {
            head = tail = new Node<T>(elem, NULL,NULL);
        }
        else
        {
            tail->next = new Node<int>(elem, tail, NULL);
            tail = tail->next;
        }

        size++;
    }

    void addFirst(T elem)
    {

        if(isEmpty())
        {
            head = tail = new Node<T>(elem, NULL, NULL);
        }
        else
        {
            head.prev = new Node<T>(elem, NULL, head);
            head = head.prev;
        }
        size++;
    }

    bool addAt(int index, T data)
    {
        if (index < 0)
        {
            return false;
        }
        if(index > size+1)
        {
            return false;
        }
        if (index == 0)
        {
            addFirst(data);
            return true;
        }

        if (index == size)
        {
            addLast(data);
            return true;
        }

        Node<T>* temp = head;
        //already at 0 and in first iteration at index/position 1 (2nd element)
        for (int i = 0; i < index - 1; i++)
        {
            temp = temp->next;
        }
        Node<T>* newNode = new Node<T>(data, temp, temp->next);
        temp->next->prev = newNode;
        temp->next = newNode;

        size++;
        return true;
    }

    T peekFirst()
    {
        if (isEmpty())
            throw "empty list error";
        return head->data;
    }

    T peekLast()
    {
        if (isEmpty())
            throw "Empty list";
        return tail->data;
    }

    T removeFirst()
    {

        if (isEmpty())
            throw "Empty list";


        T data = head->data;
        head = head->next;
        --size;


        if (isEmpty())  //since head already assigned to null and list is empty , its time to assign tail to null
        {
            delete tail;
            tail = NULL;
        }

        // memory cleanup of the previous node
        else
        {
            delete head->prev;
            head->prev = NULL;
        }


        return data;
    }

    T removeLast()
    {

        if (isEmpty())
            throw "Empty list";

        //  tail pointer backwards one node
        T data = tail->data;
        tail = tail->prev;
        --size;


        if (isEmpty())
        {
            delete head;
            head = NULL;
        }

        //  memory clean of the node that was just removed
        else
        {
            delete tail->next;
            tail->next = NULL;
        }


        return data;
    }

    T remove(Node<T>* node)
    {
        // If the node to remove is somewhere either at the
        // head or the tail handle those independently  (node provided here has already being searched and found and sent here just to remove
                                                         //and since its doubly linked list we have both prev and next info
        if (node->prev == NULL)
            return removeFirst();
        if (node->next == NULL)
            return removeLast();

        // Make the pointers of adjacent nodes skip over node
        node->next->prev = node->prev;
        node->prev->next = node->next;

        // Temporarily store the data we want to return
        T data = node->data;

        // Memory cleanup

        delete node;

        --size;


        return data;
    }


    T removeAt(int index)
    {
        // Make sure the index provided is valid
        if (index < 0 || index >= size)
        {
            throw "Illegal Argument";
        }

        int i;
        Node<T>* trav;

        // Search from the front of the list
        if (index < size / 2)
        {
            for (i = 0, trav = head; i != index; i++)
            {
                trav = trav->next;
            }
            // Search from the back of the list
        }
        else
            for (i = size - 1, trav = tail; i != index; i--)
            {
                trav = trav->prev;
            }

        return remove(trav);
    }

    bool remove(T data)
    {
        Node<T>* trav = head;

        // Support searching for null

        for (trav = head; trav != NULL; trav = trav->next)
        {
            if (data == trav->data)
            {
                remove(trav);
                return true;
            }
        }

        return false;
    }

    int indexOf(T data)
    {
        int index = 0;
        Node<T>* trav = head;

        // Support searching for null

        for (; trav != NULL; trav = trav->next, index++)
        {
            if (data == trav->data)

            {
                return index;
            }
        }

        return -1;
    }

     bool contains(T data)
    {
        return indexOf(data) != -1;
    }

    void print(){
        Node<T>* temp = head;
        while(temp != NULL){
            cout << temp->data << endl;
            temp = temp->next;
        }
    }

};


int main()
{
    DoublyLinkedList<int> d_linkedList;
    d_linkedList.add(1);
    d_linkedList.add(2);
    d_linkedList.add(3);
    d_linkedList.add(4);
    d_linkedList.add(5);
    d_linkedList.add(6);
    d_linkedList.print();
    if(!d_linkedList.remove(19))
        cout << "Item 19 not found" << endl;
    d_linkedList.remove(4);

    cout << "list after removing 4" << endl;
    d_linkedList.print();

    cout << "index of 5 is " << d_linkedList.indexOf(5) << endl;
//    cout << "Hello world!" << endl;
    return 0;
}
