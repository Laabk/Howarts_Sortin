n = 10
def factorial(num):
    return 1 if (num == 1 or num == 0) else (num * factorial(num - 1))
print(factorial(n))

test_list = ['Gfg', 'is', 'best', 'for', 'Geeks']
rep = [sub.replace("G", "-").replace("e", "G").replace("-", "e") for sub in test_list]
print("the number in the list: " + str(test_list))
print("the number is: " + str(rep))

test_list = [4, 7, 8, 0, 8, 4, 2, 9, 4, 8, 4]
i, j = 4, 8
print("the number: " + str(test_list))
# time for the toggling process
for idx in range(len(test_list)):
    if int(test_list[idx]) == i:
        test_list[idx] = j
    elif int(test_list[idx]) == j:
        test_list[idx] = i
print("the number is: " + str(test_list))

test_list = [4, 7, 8, 0, 8, 4, 2, 9, 4, 8, 4]
def toggle(the_element, i, j):
    if the_element == i:
        return j
    elif the_element == j:
        return i
    return the_element
    i, j = 4, 8
res = [toggle(the_element, i, j) for the_element in test_list]
print("the alterd list: " + str(res))

str = 'geeks'
lst = ['for', 'ge', 'abc', 'ks', 'e', 'xyz']
from itertools import permutations
def checklist(str, lst):
    for i in range(2, len(lst) + 1):
        for perm in permutations(lst, i):
            if ''.join(perm) == str:
                return True
    return False
print(checklist(str,lst))

str = 'geeks'
lst = ['for', 'ge', 'abc', 'ks', 'e', 'xyz']
def checklist(str, lst):
    for i in lst:
        str = str.replace(i, "")
        if str == "":
            return True
    return False
print(checklist(str, lst))

