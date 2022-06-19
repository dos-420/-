import time
a = int(input("请输入数字："))
b = int(input("请输入另一个数字："))
c = input("请输入计算方式：")
if c == '+':
    print(a + b)
    time.sleep(5)
elif c == '-':
    print (a - b)
    time.sleep(5)
elif c == '*':
    print(a * b)
    time.sleep(5)
else:
    print(a / b)
    time.sleep(5)