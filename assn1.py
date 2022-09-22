
#Assignment 1
'''Read CSV File and store data in the dictionary.
Each key in the dictionary should be a string, as read from the CSV file. The value of that key will be a Python list. 
You will use this dictionary for the next three modules.'''


path="C:/Users/Priyanka/PythonProject/Day1/Emissions1.txt"


def readdata(dictline):
    
   file=open(path,"r")
   lines=file.readlines()
   file.close()

   totallines=len(lines)

   #print("total lines of the file are:" )
   #print(totallines)

   field=1
  
   for i in range(totallines):

      line=lines[i].split("|")
      dictline[field]=line
      field=field+1
       
   return(dictline)
    

dictline={}
dictline=readdata(dictline)
header=dictline[1]
#print("header of the file is ")
#print(header)
#print(dictline[195])
#print(dictline.keys())

indexdict={}

totalindex=len(header)
j=0
for i in range(1,totalindex):

    indexdict[i]=header[j]
    j=j+1

#print(indexdict) 

year=input("Select the Year to find the Statics(1997-2010): ") 

indexvalue = {i for i in indexdict if indexdict[i]==year}
print("index of the input year is ",indexvalue)

for x in indexvalue:
  index=x-1
  print("Index is :")
  print(index)

Listline=[]
#print(dictline[195])
for key in dictline:

    Listline.append(dictline[key])

lengthListline=len(Listline)

print("Total Lines in the file are :"+str(lengthListline))

sum=0

'''for i in range (1,196):
    print(Listline[i][0])
'''

for i in range (1,lengthListline):
    sum=float(Listline[i][index])+sum

avg=sum/195 
print("average CO2 Emission in the "+year+" is:" +str(avg))   

max=float(Listline[1][index])
min=float(Listline[1][index])
maxcountry=Listline[1][0]
mincountry=Listline[1][0]




for i in range (3,lengthListline):
    value=float(Listline[i][index])
    if (value>max):
        max=value
        maxcountry=Listline[i][0]
        
    
        
for i in range (3,lengthListline):
   # print("country"+mincountry)
   # print(min)
    value=float(Listline[i][index])
    if ( value<min):
        min=value
        mincountry=Listline[i][0]
 
        
print("country with maximum  co2 emission is:"+maxcountry)
print("country with minimum  co2 emission is:"+mincountry)
     
    







    
    
    
    

    
    
    
    
    



