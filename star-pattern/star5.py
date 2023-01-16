###  Full Downward Pyramid #####

n=int(input("Enter number of rows: "))
k = 0
for i in range(n, -1, -1):  #because step is -1 so we have written in order stop_value, start_value. 
    for j in range(k, 0, -1):
        print(end=" ")
    k = k + 1 #this k value defines preceding gaps.
    for j in range(0, i + 1):
        print("*", end=" ")
    print(" ") # this print function adds new line after the j loop ends. 
 """   
    * * * * * *  
     * * * * *  
      * * * *  
       * * *  
        * *  
         *  
"""
