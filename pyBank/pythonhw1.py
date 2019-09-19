import csv

with open("hw1.csv", newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader, None)
       
    #for row in csvreader:
    #row_count = sum(1 for row in csvreader)
    #print(row_count)
    
    
    #for row in csvreader:
        
        #total+= int(row[1])
        
    #print(total)  
    #for row in csvreader:
        #print(row)
    
    total_revenue = []
    total_months =[]
    rev_change= []
    date=[]
    
    for row in csvreader:

        total_revenue.append(int(row[1]))
        total_months.append(row[0])
        
    print("Financial Analysis")
    print("------------------------")
    print("Total Months:", len(total_months))
    print("Total Revenue: $",sum(total_revenue))
    
    #print(total_revenue)
    for i in range(1,len(total_revenue)):
        rev_change.append(total_revenue[i] - total_revenue[i-1])   
        avg_rev_change = sum(rev_change)/len(rev_change)
        
        max_rev_change = max(rev_change)

        min_rev_change = min(rev_change)

        max_rev_change_date = str(total_months[rev_change.index(max(rev_change))])
        min_rev_change_date = str(total_months[rev_change.index(min(rev_change))])
    
    print ("Average Change: $",round(avg_rev_change))
    #print(max_rev_change)
    #print(min_rev_change)
    
    
    print("Greatest Increase in profits:", max_rev_change_date, "($", max_rev_change,")")
    print("Greatest Decrease in profits:", min_rev_change_date, "($", min_rev_change,")")
    
            
    #csvreader.seek(0)    
    #data = list(csvreader)
    #data = [row for row in csvreader]
    #for row in data

    #print(row_count)    
    #print (data)
    #print(data[0][1])
    #print(data[1])
    #netamount = sum(data[1])
    #csvreader.seek(0)
    #total= sum(csvreader[1] for row in csvreader)
    #print(total)
    #for row in csvreader:
         #print(sum(csvreader[1]))
      
   
    
    
   #Months_total = len(csvreader)
   # print(Months_total)
    
    