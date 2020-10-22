numberofscores= 0
score= 0
scorecount= 0
total= 0
average= 0

numberofscores= int(input(Enter the number of test score you want averaged"))
                          
while scorecount < numberofscores:
                          score=int(input("Please input a score:"))
                          total +=score
                          scorecount +=1
                          print("Score Received")
                          
average= total/numberofscores
                        
print("The average for the given test score is:",average)
