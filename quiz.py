print ("Welcome to my compester quiz,")
playing = input ("Do you want to play?")
if  playing.lower()!= "yes":
    quit()
print("lets play:")
score = 0
answer = input ("What does cpu stand for? ")
if answer.lower ()  == "central processing unit":
   print ('correct!')
   score =+1
else:
  print ("Incorrect!")
answer = input ("What does Gpu stand For? ")
if answer.lower() == "graphics processing unit":
    print ('correctl')
    score =+ 1

else:
   print("Incorecl!.")

answer = input ("what does ram stand for? ")
if answer.lower() == " random acess momory":
   print ('correct!')
   score =+ 1
else:
   print("Incorrect ")
answer = input (" whatt does psu stand for? ") 
if answer.lower () == "power supply" :
    print ('correct')
    score =+ 1
else:
   print("Inconrect")
print ("yougt" + str(score)+ "questions correct ")
print ("yougot" + str((score /4) *100) + "% ")