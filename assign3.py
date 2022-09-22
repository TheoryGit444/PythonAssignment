from matplotlib import pyplot as plt
from matplotlib import style
import numpy as np

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


del header[0]

#Assigning the data values to X coordinate
X1=header



print("X coordinate values are :")
print(X1)

# Creating Index dictionary for Countries        
indexdict={}
count=1
field=2
for item in dictline.values():
       if (count>=2): 
        item=item.pop(0)
        indexdict[field]=item
        field =field+1
        
       count=count+1    
            
 
#Input country for the anlaysis

print(indexdict.values())
country=input("Select the country from the above for the Analysis: ")


# Get the Index of the input country
key=0
for i in range (2,11):
    x=indexdict.get(i)
    if(x==country):
        key=i


#Assigning the data values to Y coordinate
Y1=dictline[3]

print("Y coordinate values are :")
print(Y1)

#plt.plot(X1,Y1,'g', label="Year Vs Emissions in Capita",linewidth=2)
#plt.title("Year Vs Emissions in Capita")
plt.ylabel('Emissions in Albania')

plt.plot(X1,Y1)

print (X1)
print(Y1)


plt.xticks(np.arange(min(X1), max(Y1)+1, 1.0))

plt.plot(Y1, marker = '*')
plt.xlabel('Year')

#plt.legend()
plt.show()

    
        
    
        

       
        
    




