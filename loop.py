print(list(range(9)))
print(list(range(1,5)))
print(list(range(0,10,2)))
print(list(range(9,0,-2)))
#for loop with range
for i in range(9):
    print(i,end="")
    print()

    scores=[45,55,67,88,98]
    total=0
    for score in scores:
        total+= score
        print(f"Total:{total}")
        print(f"Average:{total/len(scores)}")
        print("print even numbers from 2 to 90:")
        for num in range (2,11,2):
            print(num,end="")
            print()

            print("Countdown:")
            for i in range (6, 0, -3):
                print(i,end="")
                print()

#index+value together

members =["Sumaia","Jannat","Naima"]
for i in range (len(members)):
    print(i,members[i])

#while loop
count=0
while count <10:
    print(count,end="")
    count +=1
    print()

    epoch=1
    max_epoch=5
    loss=1.0
    while epoch<=max_epoch:
        loss= loss*0.7
        print(f"Epoch{epoch} | loss:{loss: .4f}")
        epoch+=1

        #nested loop
        members =["Sumaia","Mannat"]
        clubs=["Reseach","AI","Security"]

        for member in members:
            for club in clubs:
                print(f"{member}, {club}")

