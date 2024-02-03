package validparenthesis

func IsValidParenthesis(s string) bool {
	stack := make([]rune, 0)
	for _, c := range s {
		switch c {
		case '(':
			stack = append(stack, ')')
			break
		case '{':
			stack = append(stack, '}')
			break
		case '[':
			stack = append(stack, ']')
			break
		default:
			n := len(stack)
			if n == 0 {
				return false
			}
			last := stack[n-1]
			stack = stack[:n-1]
			if last != c {
				return false
			}
		}
	}
	return len(stack) == 0
}

func main() {
	s := "()"
	IsValidParenthesis(s)

	s = "()[]{}"
	IsValidParenthesis(s)

	s = "(]"
	IsValidParenthesis(s)

	s = "([)]"
	IsValidParenthesis(s)

	s = "{[]}"
	IsValidParenthesis(s)
}