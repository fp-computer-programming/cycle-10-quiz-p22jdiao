# Author: JD 02/10/2022

prices = [30, 40, 25, 55, 60, 80, 65]
sales = [1, 3, 2, 5, 2, 1, 2]
items = [['tee-shirt','long-sleeved','tanktop'],['quarter-zip','pullover','full-zip','half-zip']]
#1
def average(lst):
    # The sum will sum up all the numbers in the list
    # the length will record the number of numbers within the list

    sum = 0
    length = len(lst)
    # The for loop will go through each individual element of the list and add them to the variable sum.

    for x in lst:
        sum += x
    # The variable average will then calculate the average of the numbers and be returned to the main function.
    average = sum / length

    return average
    

print(average(prices))

#2
def reduce_5(lst):
    # The function use a for loop to go throgh the enumerate of the list, and then moderate each element by reducing 5.

    for i,v in enumerate(lst):
        lst[i] = v - 5
    
    return lst

print(reduce_5(prices))

#3

def cal_sales(p,s):
    # The function uses a for loop of the enumerate of the prices list so it can keel track of the index that it is working on
    # The index will be the same for both list as they are matching with each other, so only one loop is needed
    # The variable amount will be used to sum the products of the sales and prices
    amount = 0
    for i,v in enumerate(p):
        amount += (p[i]*s[i])
    
    return amount
        
print(cal_sales(prices,sales))


#4
prices2 = [30, 40, 25, 55, 60, 80, 65]
def find_40(p):
    # This function uses a for loop of the enumerate of the prices, the loop will process through each element to check if the element is greater than 40
    # If it is greater than 40, the if conditional will be triggered, and the element will be reduced by 10

    for i,v in enumerate(p):
        if v > 40:
            p[i] = v - 10

    return p

print(find_40(prices2))


#5

prices3 = [30, 40, 25, 55, 60, 80, 65]

def matching(p,item):
    # Because the items list is a nested list, so there will be a nested for loop within another for loop.
    # The first loop will go through each element, and nested loop will go through each element of the nested loops.
    # A .append format is used here to add the newly generated string to the empty list that will be returned.

    new = []
    tracker = 0
    for i,v in enumerate(item):
        for i2,v2 in enumerate(v):

            new.append("{0} ${1}".format(v2,p[tracker]))
            tracker += 1
    return new

print(matching(prices3,items))

#6 

def count(mult,count_to):
    x = mult
    # Using a while loop to check if the current number(x) is greater than the count_to number.
    # x will be added by the multiple each loop.
    while x <= count_to:
        print(x)
        x += mult

# a and b variables will be edited by the input() function.
a = int(input("Enter the multiple: "))
b = int(input("Enter the number to count to: "))

count(a,b)
