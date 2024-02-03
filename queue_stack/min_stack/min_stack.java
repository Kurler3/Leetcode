package queue_stack.min_stack;

import java.util.ArrayList;
import java.util.List;

class MinStack {

    private List<Integer> stack;
    private List<Integer> minStack;
    private int n;

    public MinStack() {
        stack = new ArrayList<>();
        minStack = new ArrayList<>();
        n = 0;
    }
    
    public void push(int val) {
        stack.add(val);
        if(n == 0 || val <= minStack.get(n - 1)) {
            minStack.add(val);
        } else {
            minStack.add(minStack.get(n - 1));
        }
        n++;
    }
    
    public void pop() {
        stack.remove(n - 1);
        minStack.remove(n - 1);
        n--;
        return;
    }
    
    public int top() {
        if(n == 0) return -1;
        return stack.get(n - 1);
    }
    
    public int getMin() {
        if(n == 0) return -1;
        return minStack.get(n - 1);
    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.push(val);
 * obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.getMin();
 */