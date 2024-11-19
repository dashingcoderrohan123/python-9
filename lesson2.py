#Write a program to check whether the student can take an exam or not. Students will be allowed only in two conditions: If they have a medical cause (‘Y’ for yes and ‘N’ for no). If yes, then they will be allowed. If No, then check attendance If attendance is above 75, then allowed; otherwise, not allowed.

medical_cause=input("do you have medical cause Y or N ")
attendance=int(input("enter the attendance"))

if medical_cause=="Y":
    print("the student is allowed")

else:
    if attendance>=75:
        print("allowed")
    else:
        print("not allowed")            