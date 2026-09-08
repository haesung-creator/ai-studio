def calculator(a, b, op):
	if op == "+":
		return a + b
	elif op == "-":
		return a - b
	elif op == "*":
		return a * b
	elif op == "/":
		if b == 0:
			return "Error"
		return a / b
	return "Error"


# 최소 2가지 입력 테스트
print("1) calculator 테스트:")
print(calculator(10, 3, "/"))
print(calculator(5, 0, "/"))
