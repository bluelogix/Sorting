# TO-DO: Complete the selection_sort() function below 

def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for j in range(cur_index, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j


        # TO-DO: swap
        temporary = arr[smallest_index]
        arr[smallest_index] = arr[cur_index]
        arr[cur_index] = temporary



    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    swap_occured = True
    while swap_occured:
        swap_occured = False
        for x in range(0, len(arr) - 1):
            if arr[x] > arr[x +1]:
                arr[x],arr[x +1] = arr[x + 1], arr[x]
                swap_occured = True
    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr