'''
-1=snake
0=water
1=gun

'''
#computer choice
import random
comp_num=random.choice([-1,0,1])

#user choice
user_str=input("Enter your choice(s,w,g):")
main_dict={"s":-1,"w":0,"g":1}
user_num=main_dict[user_str]  #to convert user choosen string to number for comparison

#to make it user freindly
rev_dict={-1:"SNAKE",0:"WATER",1:"GUN"}
print(f"You Choosed:{rev_dict[user_num]} \nComputer Choosed:{rev_dict[comp_num]}")

if(user_num==comp_num):
    print("It's a Draw!")
else:
    if(user_num==-1 and comp_num==0):
        print("---YOU WIN!---")

    elif(user_num==-1 and comp_num==1):
        print("---YOU LOOSE!---")

    elif(user_num==0 and comp_num==1):
        print("---YOU WIN!---")

    elif(user_num==0 and comp_num==-1):
        print("---YOU LOOSE!---")

    elif(user_num==1 and comp_num==0):
        print("---YOU LOOSE!---")

    elif(user_num==1 and comp_num==-1):
        print("---YOU WIN!---")

    else:
        print("---INVALID INPUT!---")
