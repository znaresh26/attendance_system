import pandas as pd
z=pd.read_csv("details.csv")
students={}
for i in range(1,68):students[z.iloc[i,2].strip()]=[z.iloc[i,3],z.iloc[i,1],True]
#DAILY ATTENDANCE AND MAPS

rolls={"66":"AIML","67":"DS","62":"CS","33":"CSIT","12":"IT","04":"ECE","05":"CSE","02":"EEE","01":"CE","03":"ME","21":"AE"}
att={}
count=0

file = "day3_attendance_08_02-2023.txt"
fp=open(file,"w")

while True:
    z=input("ROLL NUMBER: ").upper().strip()
    if z=="DONE":fp.write('\nTodays Attendance: '+str(count)+"\n");print('\nTodays Attendance:',count);break
    try:
        if not(students["22951A"+z][2]):print("\nDUPLICATE RECORD FOUND\n");continue
        print("\nName:",students["22951A"+z][1].upper())
        print("Roll Number:","22951A"+z)
        print("Branch:",students["22951A"+z][0].upper())
        x=input("PRESS ANY KEY TO CONTINUE:").upper()
        
        if x=="N":continue
        students["22951A"+z][2]=False
        try:att[rolls[z[:2]]].append(z)
        except:att[rolls[z[:2]]]=[z]
        count+=1
        print("Total:",count)
        print("")
    except:print("\nInvalid Input\n")

print("\nBRANCH WISE ATTENDANCE: \n\n")
fp.write("\nBRANCH WISE ATTENDANCE: \n\n")
for i in att:
    att[i].sort()
    print(i+": ")
    fp.write(i+": "+"\n")
    for j in att[i]:fp.write("22951A"+j+"\n");print("22951A"+j)
    print("");fp.write("\n")
ab={}
for i in students:
    if students[i][2]:
        try:ab[rolls[i[-4:-2]]].append(i)
        except:ab[rolls[i[-4:-2]]]=[i]
fp.write("\nBRANCH WISE ABSENTEES:\n\n")
print("\nBRANCH WISE ABSENTEES:\n\n")
for i in ab:
    print(i+":")
    fp.write(i+":\n")
    ab[i].sort()
    for j in ab[i]:fp.write(j+"\n");print(j)
    print("");fp.write("\n")

fp.close()
