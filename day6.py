
path="C:/Users/Priyanka/PythonProject/Day1/Emissions1.txt"


file=open(path,"r")
lines=file.readlines()
totallines=len(lines)
file.close()

#Write content to new file
path2="C:/Users/Priyanka/PythonProject/Day6/Emissions_subset.csv"
f=open(path2,"w")

f.write(lines[0])
f.close()


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


countries=input("Enter the three countries to extract the data from the source file:")

listcountry=countries.split(",")
print(listcountry)

Range=len(listcountry)

#open file for append mode
path2="C:/Users/Priyanka/PythonProject/Day6/Emissions_subset.csv"
f=open(path2,"a")

for i in range (0,totallines):

    
    if (lines[i].startswith(listcountry[0])):
        
        f.write(lines[i])
    elif (lines[i].startswith(listcountry[1])):  
        f.write(lines[i])
        
    elif (lines[i].startswith(listcountry[2])):
        f.write(lines[i])

        
    
f.close()    
    


