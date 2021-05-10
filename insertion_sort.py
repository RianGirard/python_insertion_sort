arr = [-98,55,-4,30,81,81,91,-50,1,-90,-84,-63,85,-8,44,42,-60,-97,66,45]
print(arr)
def insertion_sort(lis):
    for i in range(1, len(lis)):    # We start the first loop at position 1 because we are comparing "i" to the numbers to the left of it
        index = lis[i]              # Here is our marker
        for j in range(1, i+1):     # Our internal loop "j" starts at position 1 because of "i-j", so that we look at 1 to the left of i to begin with
            if index < lis[i-j]:    # if our index is less than the number to the left...
                lis[i-j], lis[i-j+1] = lis[i-j+1], lis[i-j]     # swap! 
            else:
                continue            # This "else" added for clarity, not required
    print(lis)
insertion_sort(arr)
