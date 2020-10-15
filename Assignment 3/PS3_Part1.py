scores = [95, 66, 87, 90, 73, 82, 65, 77, 81, 86]
#print(scores)
total_number_of_scores = 0
score_total = 0
for i in scores: 
    #print(i)
    total_number_of_scores += 1;
    score_total += i
mean = score_total/total_number_of_scores
#print(total_number_of_scores)
print("The mean is:",mean)

variance_scores = [0] *10
#print(variance_scores)
inc = 0
for i in variance_scores:
    variance_scores[inc] = scores[inc]-mean
    inc = inc + 1
#print(variance_scores) 
inc = 0
variance_total = 0
for i in variance_scores:
    variance_total += variance_scores[inc]**2
    inc = inc + 1
#print(variance_total)
variance = variance_total/total_number_of_scores
print("The variance is:",variance)
standard_deviation = variance**.5
print("The standard deviation is:",standard_deviation)
