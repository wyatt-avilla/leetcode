// https://leetcode.com/problems/min-stack/

#include <climits>
#include <stack>

class MinStack {
  public:
    MinStack() { min_stack.push(INT_MAX); }

    void push(int val) {
        data_stack.push(val);

        if (val <= min_stack.top()) {
            min_stack.push(val);
        }
    }

    void pop() {
        if (data_stack.top() == min_stack.top()) {
            min_stack.pop();
        }
        data_stack.pop();
    }

    int top() { return data_stack.top(); }

    int getMin() { return min_stack.top(); }

    std::stack<int> data_stack;
    std::stack<int> min_stack;
};


int main(void) {

    MinStack minstack;
    minstack.push(1);
    minstack.push(2);
    minstack.push(3);

    return 0;
}
