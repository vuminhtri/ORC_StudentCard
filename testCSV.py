import csv

result = [
    ([1,2,3],"Dương",3), 
    (4,5,6), 
    (7,8,9)
 ]

# opening the csv file in 'a+' mode
file = open('results.csv', 'a+', newline ='')

with file:
    write = csv.writer(file)
    write.writerows(result)