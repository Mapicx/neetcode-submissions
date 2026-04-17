class MinStack {
public:
    stack<int> st;       // Stack for all values
    stack<int> min_st;   // Stack for minimum values

    MinStack() {}

    void push(int val) {
        st.push(val);
        // Push to min_st if it's empty or val is the new minimum
        if (min_st.empty() || val <= min_st.top()) {
            min_st.push(val);
        }
    }
    
    void pop() {
        // If the top of both stacks is the same, pop min_st as well
        if (st.top() == min_st.top()) {
            min_st.pop();
        }
        st.pop();
    }
    
    int top() {
        return st.top();
    }
    
    int getMin() {
        return min_st.top();
    }
};