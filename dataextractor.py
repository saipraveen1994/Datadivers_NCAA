import csv
input1=open('Events_2010.csv','r')
output=open('Events_2010-edit.csv','w')
writer=csv.writer(output)
for row in csv.reader(input1):
    if row[6]!="0" and row[7]!="0":
        writer.writerow(row)
input1.close()
output.close()
        
