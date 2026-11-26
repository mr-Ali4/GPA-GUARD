# GPA Guard
print("hey, hi user welcome to gpa guard")
print("this website is designed to help you mantain your gpa and attendance")
# creating a loop to get user details and calculate gpa correctly
while True:
#  getting user details
 name=input("so let's start with your name first so what is your name? ")
 print("hey",name,"it's great to meet you")
 age=input("so tell me your age? ")
 print("okey so you are",age,"years old")
 university=input("so tell me you are from which university? ")
 print("it's great to know that you are fron",university)
 gpa=input("so tell me what is your current gpa? ")
 print("okey so your current gpa is",gpa)
 attendance=input("so tell me what is your current attendance percentage? ")
 print("okey so your current attendance is",attendance)
 print("so let's confirm your details: your name is",name,"your gpa is",gpa,"and your attendance percentage is",attendance)
#  confirming user details
 yes=input("is the above data correct? say in yes or no ")
 if yes.lower() =="yes":
    print("great to hear that now lets continue with our gpa calculation")
 else:
    print("okey try again then")
    continue
    # break
   #  creating a loop to get user semester details and calculate gpa
 while True:
#   getting user semester details
  semester=input("now tell me which semester are you in? ")
  print("so you are in",semester,"semester")
  subjects=input("now tell me how many subjects are there in your current semester? ")
  print("so you have",subjects,"subjects in your current semester")
  credits=input("now tell me how many credits are there in your current semester? ")
  print("so you have",credits,"credits in your current semester")
  print("so let's confirm your details: you are in",semester,"semester and you have",subjects,"subjects and you have",credits,"credits")
#   Confirming user semester details
  yes=input("is the above details correct? say in yes or no ")
  if yes.lower() =="yes":
     print("great to hear it let's start the calculation now")
  else:
     print("okey try again then")
     continue
  print("so to calculate your gpa we need you know the grades you got in your subjects")
#   getting marks in each subject and calculating gpa
  grades=[]
  for i in range(int(subjects)):
     grade = int(input("so tell me what grade you got in subject "+str(i+1)+"? "))
     grades.append(grade)
  print("the sum of your grades is:",sum(grades))
  total_marks=int(input("so now tell me what is the total marks of all of subjects "))
  print("the total marks for all subjects is:", total_marks)
  print("so you got",sum(grades),"marks out of",total_marks)
  percentage=(sum(grades)/total_marks)*100
  print("so your percentage is:", percentage)
  print("so you got the following grades in your subjects: ",grades)
  print("now we will calculate your gpa based on your grades and credits")
  grader=input("so now tell me what grade you got ").upper().strip()
  print("so you got " , grader.upper() ,"grade")
  try:
      grader_points={"A+":10,"A":9,"B":8,"C":7,"D":6,"F":0}
      if grader in grader_points:
       cgpa_value=grader_points[grader]
       print("your cgpa points are:",cgpa_value)
      else :
       cgpa_value=0
       print("invalid input")
  except:
    print("invalid entry")
  print(f"for an {grader} grade, your cgpa points are: {cgpa_value}")
  print("so you got",cgpa_value,"cgpa for your",grader,"grade")



