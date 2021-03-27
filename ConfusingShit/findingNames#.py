Names = ["Ben", "Thor", "Zoe", "Kate"]
PlayerName = ""
Max = 4
Current = 1
Found = False


print("What player are you looking for?: ")
PlayerName = input()

while((Found == False) and (Current <= Max)):
    if(Names[Current] == PlayerName):
        Found = True

    else:
        Current += 1

if(Found == True):
    print("Yes, they havea top score")

else:
    print("No, they do not have a top score")

    
    
