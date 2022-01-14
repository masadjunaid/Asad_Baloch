# while lopps and for loops
    #while loops
# loops are doing something again and again iteratively

# x = 0
# while (x<=5):
#     print(x)
#     x=x+1
# yaha par x zero se start hoga or 5 tak jaiga or jab tak ye statment qaim rahega loop chalega or end me khatam


# # FOR LOOP

# for x in range(5,10):
#     print(x)

#ARRAY

days =["Mon", "Tue" , "Wed",  "Thu" , "Fri", "Sat" , "Sun"]

for d in days:
   # if (d=="Fri"):break # loop stop at this point
    if (d=="Fri"): continue #skips d
    print(d)
