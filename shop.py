class Customer:
 def __init__(self, name, grade="basic"):
    self.name = name
    self.grade = grade
    self.points = 0
 def add_points(self, amount):
    self.points += int(amount * 0.05) #구매 금액의 5%를 포인트로 적립
 def get_discount_rate(self):
    if self.grade == "vip":
        return 0.1 # VIP 고객은 10% 할인
    return 0.03 # 일반 고객은 3% 할인
 def summary(self):
    return f"[{self.grade}] {self.name} (포인트: {self.points:,})"

class Order:
    def __init__(self, order_id, customer, items):
        self.order_id = order_id
        self.customer = customer     # Customer 인스턴스 참조
        self.items = items           # [(상품명, 가격), ...] 튜플의 리스트

    def add_item(self, name, price):
        # 상품 추가 시 (상품명, 가격) 튜플 형태로 리스트에 append
        self.items.append((name, price))

    def total_price(self):
        """주문 총액 (고객 등급 할인 적용 후 정수 반환)"""
        subtotal = sum(price for _, price in self.items)
        discount = self.customer.get_discount_rate()
        return int(subtotal * (1 - discount))

    def pay(self):
        """결제 완료 시 총액을 반환하고 고객에게 포인트 적립"""
        total = self.total_price()
        self.customer.add_points(total)  # 결제 금액에 따라 포인트 적립
        return total