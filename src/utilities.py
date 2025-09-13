import decimal
import sys
import copy


d = decimal.Decimal(100.25)
ac = 100.25
print(d)
print(sys.getsizeof(d))
print(ac)
print(sys.getsizeof(ac))

a = True
b = False

match a:                   #то же, что и switch case
    case True:
        print("A:", a)
    case False:
        print(b)
    case _:
        print("Default")
d = ()
print(type(d))

arr = [1, 2, 3]
arr1 = copy.deepcopy(arr)  #полная копия списка