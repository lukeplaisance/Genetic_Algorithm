'''def biggest_number(num1, num2, num3):
    if num1 > num2 and num3:
        return num1
    if num2 > num1 and num3:
        return num2
    if num3 > num1 and num2:
        return num3

numbers = biggest_number(5, 2, 3)
a = 1'''

def common_numbers(listOne, listTwo):
    other_list = list()
    common_list = zip(listOne, listTwo)
    for item in common_list:
        if listOne[item] == listTwo[item]:
            other_list.append(listTwo[item])
            

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

common_numbers(a, b)
c = 2
                 
