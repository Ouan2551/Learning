    // Linked list => node that connect together each node contain data and pointer
    // type of linked list
    // 1) singly liked list => only one address to next node
    // 2) doubly linked list => has 2 node that next and previous node
    // 3) circular liked list => first node (head) connect to last node (tail)

// after this is basic linked list
#include <iostream>

class Node {
public:
    int data;
    Node* next;

    // Constructor
    Node(int val) {
        data = val;
        next = nullptr;
    }
};

class LinkedList {
private:
    Node* head;

public:
    // Constructor
    LinkedList() {
        head = nullptr;
    }

    // Add node at the end
    void append(int val) {
        Node* newNode = new Node(val);
        if (head == nullptr) {
            head = newNode;
        } else {
            Node* temp = head;
            while (temp->next != nullptr) {
                temp = temp->next;
            }
            temp->next = newNode;
        }
    }

    // Print the list
    void printList() {
        Node* temp = head;
        while (temp != nullptr) {
            std::cout << temp->data << " -> ";
            temp = temp->next;
        }
        std::cout << "null" << std::endl;
    }

    // Destructor to free memory
    ~LinkedList() {
        Node* current = head;
        while (current != nullptr) {
            Node* next = current->next;
            delete current;
            current = next;
        }
    }
};

int main() {
    std::ios::sync_with_stdio(0);std::cin.tie(0);std::cout.tie(0);
    LinkedList list;

    list.append(3);
    list.append(5);
    list.append(13);
    list.append(2);

    list.printList();

    return 0;
}