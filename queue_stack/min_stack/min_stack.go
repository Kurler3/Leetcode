package minstack

import (
	"errors"
	"fmt"
)

type MinStack struct {
	stack []int
	mins  []int
	n      int
}

// Get min stack pointer
func GetMinStack() *MinStack {
	return &MinStack{
		stack: make([]int, 0),
		mins:  make([]int, 0),
		n: 0,
	}
}

// Push
func (this *MinStack) Push(val int) {
	this.stack = append(this.stack, val)
	if this.n == 0 || this.mins[this.n - 1] > val {
		this.mins = append(this.mins, val)
	} else {
		this.mins = append(this.mins, this.mins[this.n - 1])
	}
	this.n++
}

// Pop
func (this *MinStack) Pop() error {
	n := len(this.stack)
	if n == 0 { return errors.New("Stack is empty") }
	this.stack = this.stack[:n-1]
	this.mins = this.mins[:n-1]
	this.n--
	return nil
}

// Top
func (this *MinStack) Top() (int, error) {
	if this.n == 0 {
		return 0, errors.New("Empty stack")
	}
	return this.stack[this.n - 1], nil
}

// Get Min
func (this *MinStack) GetMin() (int, error) {
	if this.n == 0 {
		return 0, errors.New("Empty stack")
	} 
	return this.mins[this.n - 1], nil
}

func Init() {
	minStack := GetMinStack()
	minStack.Push(-2)
	fmt.Println(minStack)
	minStack.Push(0)
	fmt.Println(minStack)
	minStack.Push(-3)
	fmt.Println(minStack)
	min1, _ := minStack.GetMin()
	fmt.Println("MIN 1: ", min1) // -3
	minStack.Pop()
	fmt.Println(minStack)
	top, _ := minStack.Top()
	fmt.Println("TOP: ", top) //  0
	min2, _ := minStack.GetMin()
	fmt.Println("MIN 2: ", min2) // -2
}
