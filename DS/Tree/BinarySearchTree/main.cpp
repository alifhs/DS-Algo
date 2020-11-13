#include <bits/stdc++.h>

using namespace std;


template <class T>
class BinarySearchTree
{

private:
    int nodeCount = 0;


    class Node
    {
        public:
        T data;
        Node* left;
        Node* right;

    public:
        Node(Node* left, Node* right, T elem)
        {
            this->data = elem;
            this->left = left;
            this->right = right;

        }

    };

    Node* root = NULL;


public:
    int size()
    {
        return nodeCount;
    }
    bool isEmpty()
    {
        return size() == 0;
    }

    bool add(T elem)
    {

        if(contains(elem))
        {
            return false;
        }
        else
        {
            root = add(root, elem);
            nodeCount++;
            return true;

        }

    }

private:
    Node* add(Node* node, T elem)
    {
        if(node == NULL)
        {
            node = new Node(NULL, NULL, elem);
        }
        else
        {
            if(elem < node->data)
            {
                node->left = add(node->left, elem);
            }
            else
            {
                node->right = add(node->right, elem);
            }
        }
        return node;

    }


public:
    bool remove(T elem)  //remove by element(not by pointer
    {
        if(contains(elem))
        {
            root = remove(root, elem);
            nodeCount--;
            return true;
        }
        return false;

    }

private:
    Node* remove(Node* node, T elem)
    {
        if(node == NULL) //this is never going to be null
            return NULL;

        if(elem  < node->data)
        {
            node->left = remove(node->left, elem);
        }
        else if(elem > node->data)
        {

            node->right = remove(node->right, elem);
        }
        else
        {

            if(node->left == NULL)
            {
                Node* rightChild = node->right;

                delete node;

                return rightChild;
            }
            else if(node->right == NULL)
            {

                Node* leftChild = node->left;
                delete node;

                return leftChild;
            }
            else
            {

                Node* temp = findMin(node->right); //find min from right sub tree/ find
                //find max from the left subtree

                node->data = temp->data;

                node->right = remove(node->right, temp->data);
            }
        }

        return node;


    }
    //finding leftMost node from right subtree
    Node* findMin(Node* node)
    {
        while(node->left != NULL)
            node = node->left;
                   return node;

    }

Node* findMax(Node* node)
    {
        while(node->right != NULL)
        {
            node = node->right;
        }
        return node;
    }

private:
    bool contains(Node* node, T elem)
    {
        if(node == NULL)
            return false;

        if(elem < node->data)
            return contains(node->left, elem);
        else if(elem > node->data)
            return contains(node->right, elem);

        else
            return true;

    }

public:
    bool contains(T elem)
    {
        return contains(root, elem);
    }



    public:
        int height()
        {
            return height(root);
        }



    private:
        int height(Node* node){
            if(node == NULL)
                return 0;
            return max(height(node->left), height(node->right))+1;
        }


        //traversal will be added

        void inOrder(Node* node){
            if(node==NULL)
                return;
            inOrder(node->left);
            cout <<(node->data)<<" ";
            inOrder(node->right);

        }

    public:
        void inOrder(){

            inOrder(root);
        }
};

int main()
{

    BinarySearchTree<int> bsTree;
    bsTree.add(4);
    bsTree.add(5);
    bsTree.add(1);
    bsTree.add(-23);
    bsTree.add(78);
    bsTree.add(45);
    bsTree.add(-12);
    bsTree.add(3);



    bsTree.inOrder();
    cout << "\n";

    bsTree.remove(1);

    bsTree.inOrder();



    return 0;
}
