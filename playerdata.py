import csv
input1=open('Events_2010_comp.csv','r')
input2=open('Events_2011_comp.csv','r')
input3=open('Events_2012_comp.csv','r')
input4=open('Events_2013_comp.csv','r')
input5=open('Events_2014_comp.csv','r')
input6=open('Events_2015_comp.csv','r')
input7=open('Events_2016_comp.csv','r')
input8=open('Events_2017_comp.csv','r')
player = dict()
event_list=[input1,input2,input3,input4,input5,input6,input7,input8]
for event in event_list:
    for row in csv.reader(event):
        if row[9] in player:
            player[row[9]] += 1
        else:
            player.update({row[9]:1})
with open('player.csv', 'w') as csv_file:
    writer = csv.writer(csv_file)
    for key, value in player.items():
       writer.writerow([key, value])
input1.close()
input2.close()
input3.close()
input4.close()
input5.close()
input6.close()
input7.close()
input8.close()

    
