user = int(input("enter exam mark: "))
highest = 0
lowest = 100
marks = []

while user != -1:
    if user < 0 or user > 100:
        print("invalid mark try again")
    else:
        marks.append(user)
        if user > highest:
            highest = user
        if lowest > user:
            lowest = user
            
        
    user = int(input("enter exam mark: "))
        
if len(marks) > 0:
    print(f"valid marks: {marks}",end=" ")
    print(f"total marks is: {sum(marks)}", end=" ")
    print(f"average mark is : {round(sum(marks)/len(marks), 2)},", end=" ")
    print(f"highest mark is: {highest}")
    print(f"lowest mark is: {lowest}")