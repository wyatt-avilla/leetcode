// https://leetcode.com/problems/design-linked-list/

#include <iostream>
#include <ostream>

class MyLinkedList {
  private:
    struct ListNode {
        int val;
        ListNode* next;
        ListNode* prev;

        ListNode(int x) : val(x), next(nullptr){};
    };

    int length;
    ListNode* head;
    ListNode* tail;

  public:
    friend std::ostream& operator<<(std::ostream& os,
                                    const MyLinkedList& list) {
        ListNode* cur = list.head;

        while (cur != nullptr) {
            os << "[" << cur->val << "]";
            if (cur->next != nullptr) {
                os << "->";
            }
            cur = cur->next;
        }
        return os;
    }

    MyLinkedList() {
        head = tail = nullptr;
        length = 0;
    }

    int get(int index) {
        if (index >= length) {
            return -1;
        }
        if (index == 0) {
            return head->val;
        }
        if (index == (length - 1)) {
            return tail->val;
        }

        ListNode* cur = head;
        for (int i = 0; i < index; ++i) {
            cur = cur->next;
        }
        return cur->val;
    }

    void addAtHead(int val) {
        if (length == 0) {
            head = tail = new ListNode(val);
            length += 1;
            return;
        }

        ListNode* temp = head;
        head = new ListNode(val);
        head->next = temp;
        temp->prev = head;

        length += 1;
    }

    void addAtTail(int val) {
        if (length == 0) {
            addAtHead(val);
            return;
        }

        ListNode* temp = tail;
        tail = new ListNode(val);
        tail->prev = temp;
        temp->next = tail;

        length += 1;
    }

    void addAtIndex(int index, int val) {
        if (index == 0) {
            addAtHead(val);
            return;
        }
        if (index == length) {
            addAtTail(val);
            return;
        }
        if (index > length) {
            return;
        }

        ListNode* cur = head;
        for (int i = 0; i < index - 1; ++i) {
            cur = cur->next;
        }

        ListNode* to_add = new ListNode(val);
        to_add->next = cur->next;
        to_add->prev = cur;

        cur->next = to_add;
        to_add->next->prev = to_add;

        length += 1;
    }

    void deleteAtIndex(int index) {
        if (index >= length) {
            return;
        }

        if (length == 1) {
            head = tail = nullptr;
            length -= 1;
            return;
        }
        if (index == 0) {
            head = head->next;
            head->prev = nullptr;
            length -= 1;
            return;
        }
        if (index == (length - 1)) {
            tail = tail->prev;
            tail->next = nullptr;
            length -= 1;
            return;
        }


        ListNode* cur = head;
        for (int i = 0; i < index; ++i) {
            cur = cur->next;
        }

        cur->prev->next = cur->next;
        cur->next->prev = cur->prev;

        length -= 1;
    }
};

int main(void) {
    MyLinkedList list = MyLinkedList();
    list.addAtHead(6);
    list.deleteAtIndex(0);


    std::cout << list << std::endl;

    return 0;
}
