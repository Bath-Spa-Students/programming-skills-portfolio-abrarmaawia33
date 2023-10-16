#homogenous list
sports= ["football" , " basketball", "tabletennis"]
print(sports)
names= ["fatima" , "reyam" , "abrar"]
print(names)

#hetrogenous list
names=["abrar" ," 17" , "3.33"]
print(names)

#repitition operator*to repeat data
numbers=[1,2,3,4,5]
new_numbers=numbers*5
print(new_numbers)

#positive indexing
numbers=[9,7,5,0,3]
print(numbers[2])

#negative indexing starts from -1 , bc 0 is non-negative integer

numbers=[5,8,4,3,9]
print(numbers[-2])

#lens function 
numbers=[6,8,9,4,2,5,1,4]
print("number of elements in a list :" , len(numbers))

#mutability (changable)
numbers=[3,4,6,8,9]
numbers[0]=1
numbers[3]=7
print(numbers)

#concatenation
list_1=[2,7,4,8,3]
list_2=[4,6,8,2,1]
list_3=list_2+list_1
print(list_3)

#list slicing 

list=[1,2,31,4,35,6,7]
result= list[0:4]
print(result)

list=[1,4,6,3,8]
result=list[3:5]
print(result)

#find elemnts in list - if operator

new_list= [2,4,6,7,8]
if 5 in new_list:
    print("found")
else: 
    print("not found") 

new_list1=[5,6,3,8,4,7]
if 3 in new_list1:
     print("yes")
else:
    print("no")


list=[5,6,7,3,4]
list.remove(6)
print(list)

