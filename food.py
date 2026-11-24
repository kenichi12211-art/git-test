class Food:
    def __init__(self,name,price=0):
        self.name = name
        self.price = price
    def my_food(self):
        print(f"僕は{self.name}が、好きです")
        print(f"値段は{self.price}円です。")

    def food_price(self):
        print(f"{self.name}を3個{int(self.price)*3}")
kenichi = Food("うどん",500)
kenichi.my_food()

a = Food("おにぎり",180)
a.food_price()
