print(type(4))
print(type(4.2))

a = 1
b = 3
c = 8
print(a + b + c)
print(a == b)

number = input()
if 100 >= int(number) >= 1:
    print("100以内的数字")
    print(number)
else:
    print("区间外的数字")

#单行注解：#，多行注解：''' '''


l = [1, 2, 3, 4]
for i in l:
    for j in l:
        for k in l:
            if(i != j) and (j != k) and (k != i):
                print(i,j,k)


a=[1, 2, 3, 4, 5]
print(a[::2])
print(a[-2:])


def filter_odd(number):
    return number % 2 == 0

print(list(filter(filter_odd,[1,2,7,12,45,56,66])))