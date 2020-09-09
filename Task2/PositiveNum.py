list1 = [12,-7,5,64,-14]
print("Input: list1 = ",list1)
for num1 in list1:
    if(num1>0): 
     print(num1 , end=", ")

list2=[12,14,-95,3] 
print('\n')    
print("Input: list2 = ",list2)
for num2 in list2:
	if(num2<0):
		list2.remove(num2)
print(list2)	
