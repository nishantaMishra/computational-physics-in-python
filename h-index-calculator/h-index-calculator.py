def h_index(citations):
    citations = list(map(int, citations.split(',')))
    
    # Sort the citations in ascending order
    citations.sort()
    n = len(citations)
    for i in range(n):
        if n - i <= citations[i]:
            return n - i
    # If no h-index is found, return 0
    return 0

citations_input = input("Enter the array of citations separated by comma: ")

h_index_value = h_index(citations_input)
print("The researcher's h-index is:", h_index_value)

# this code will throw error if user entered non-integer values. Instead lets print a message that number of citations cannot be anything other than non-negative integers
