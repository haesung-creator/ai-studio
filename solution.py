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

def format_receipt(name, price):
	return f"[{name}]}]" 가격: {price:,}원"

print("\n2) format_receipt 테스트:")
print(format_receipt("라떼", 5500))
print(format_receipt("아메리카노", 4000))
