class  Calculate:
 def __init__(self, my_list, k):
  self.my_list = my_list
  self.k = k

 def calculate(self):
  total = 1
  sum = negative = positive = 0
  minn = min(self.my_list)
  maxx = max(self.my_list)
  index = self.my_list.index(maxx)
  for i in self.my_list:
   sum += i
   total *= i
   if i > 0:
    positive += 1
   elif i < 0:
    negative += 1
  return f"Sum: {sum} Multiply: {total} Max: {maxx} Min: {minn} Index: {index} Musbatlar: {positive} Manfiylar: {negative}"

 def sorted(self):
  self.my_list.sort()
  return self.my_list
 def reserve(self):
  self.my_list.reverse()
  return self.my_list

 def move(self):
  length = len(self.my_list)
  temp1 = []
  temp2 = []
  for i in range(0, length ):
   if i < length - self.k:
    temp1.append(self.my_list[i])
   else:
    temp2.append(self.my_list[i])
  temp2.extend(temp1)
  temp1.extend(temp2)
  return temp2 , temp1

# my_list = [98, -73, 23, -46 ,71, 14]
# print(my_list)
# a = Calculate(my_list)
# print(a.reserve())
# print(calc.calculate())
# print(calc.sorted())
# k = int(input("K: "))
# calc = Calculate(my_list, k)
# print(calc.move())


class Profit:
 def __init__(self, A, B):
  self.a = A
  self.b = B
 def calculate_profit(self):
  total_profit = 0
  for i in range(len(self.a)):
   profit = self.a[i] * self.b[i] / 100
   total_profit += profit
  return total_profit

A = [1000, 2000, 1500]
B = [5, 6, 4]
# money = Profit(A,B)
# print(money.calculate_profit())


class Market:
 def __init__(self, A, B, C):
  self.a = A
  self.b = B
  self.c = C

 def count(self):
  total_profit = 0
  for i in range(len(self.a)):
   profit = self.c[i] * self.b[i]
   total_profit += profit
   self.a[i] -= self.c[i]
  return f"Umumiy savdo: {total_profit}, qolgan tovarlar: {self.a}"

A = [20, 30, 15]
B = [10000, 20000, 25000]
C = [5, 12, 7]

obj = Market(A, B, C)
print(obj.count())








