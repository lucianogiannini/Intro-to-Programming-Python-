import random

##the students in the class
##the most popular names in 2020
students = \
["Oliver",\
"Liam",\
"Ethan",\
"Aiden",\
"Gabriel",\
"Caleb",\
"Elijah",\
"Theodore",\
"Declan",\
"Owen",\
"Elijah",\
"Charlotte",\
"Ava",\
"Amelia",\
"Olivia",\
"Aurora",\
"Violet",\
"Luna",\
"Hazel",\
"Cloe",\
"Aria"
 ]

##needed to build the test results
test_results = []
answers = ['a', 'b', 'c', 'd'] 
num_questions = 3  ##You may change the number for testing, a smaller number
                  ##will made testing the correctness of your code easier

##this code will build a dictionary of length 20 of 
##key - student name
##value - a list of num_questions length of randomly selected
##values from the list answers above
for student in students:
  result = []
  for i in range(num_questions):
    result.append(random.choice(answers))
  test = {}
  test[student] = result
  test_results.append(test)
print("Raw Data: ")
print(test_results)
visited = [False]*len(test_results)
print("Names and Answers of Each Student")
for i in range(0,len(test_results)):
    for key,value in test_results[i].items():
        print(key,value)
print("Names and Answers of Students Who Copied")
for i in range(0,len(test_results)):
    for key,value in test_results[i].items():
        for j in range(0,len(test_results)):
            for key2,value2 in test_results[j].items():
                if  value == value2 and visited[j] == False and key != key2:
                    print(key,value,"copied",key2,value2)
                    visited[j] = True; 
