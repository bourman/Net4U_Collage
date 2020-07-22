import random
from time import sleep

print("Wellcome To Our Advertising Machine!!!")
sleep(1)
budget=int(input("What is you budget ($)?\n"))
sleep(1)
facebook=int(input("Enter how long your Facebook campaign:\n"))*100
instagram=int(input("Enter how long your Instagram campaign:\n"))*50
sum=facebook+instagram
print("It will cost you: "+str(facebook+instagram)+ "$\n")
sleep(1)
print("It will cost you: "+str((facebook+instagram)*3.5)+ "NIS")
sleep(1)
print("It will cost you: "+str((facebook+instagram)*1.17*3.5) + "NIS with tax\n")
sleep(1)

if(sum <= budget):
    print("Successful and you got another!" + str(budget-sum) + " $")
else:
    print("Unsuccessful and you have to add:" + str(sum-budget) + "$")
