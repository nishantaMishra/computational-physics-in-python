#### Downward Half Pyramid #####

n=int(input("Enter number of rows: "))
for i in range(n + 1, 0, -1): ## recall range(start_value, stop_value, step_value) nested reverse loop
    for j in range(0, i - 1):
        print("*", end=' ')    
    print(" ")
    
"""   
* * * * *  
* * * *  
* * *  
* *  
*
"""
