import numpy as np
def window_max(data: list, n: int) -> list:
    """
    Calculate maximum value of every "n"-size window

    Args:
        data (list[int]): list of integers representing heart rate samples
        n (int): The size of your window
    Returns:
        list[int]: list of maximums from each window (size should be len(data)//6)
    """
    oulst=[]

    size=len(data)

    for k in range(0,size,n):
        temp=data[k:k+n]
        oulst.append(max(temp))

    return oulst

def window_average(data: list, n: int) -> list:
    oulst=[]

    size=len(data)

    for k in range(0,size-(size%n),n):
        temp=data[k:k+n]
        oulst.append(round(sum(temp)/n,2))


    if(size%n >=1):
        temp_last=data[size-(size%n):size]
        temp_length=len(temp_last)
        oulst.append(round(sum(temp_last)/temp_length,2))
    
    return oulst


def window_stddev(data: list, n: int) -> list:
    """
    Calculate the standard deviation for non-overlapping windows of size `n`.
    If any window has fewer than 2 elements, return an empty list.
    
    :param data: List of numerical values.
    :param n: Size of each window.
    :return: List of standard deviations for each window or an empty list.
    """
    oulst = []
    size = len(data)
    
    # Ensure valid input
    if(size == 0 or n <= 1):
        return []
    
    # Loop over the data with step size `n` (non-overlapping windows)
    for k in range(0, size-size%n, n):
        window = data[k:k + n]
        
        # Calculate standard deviation for the window
        mean = sum(window) / len(window)
        sum_squared_diff = 0
        for x in window:
            sum_squared_diff += (x - mean) ** 2
        stddev = (sum_squared_diff / (len(window) - 1)) ** 0.5
        
        # Append rounded standard deviation to result list
        oulst.append(round(stddev, 2))
    
    #Find standard deviation for left over elements >1
    if((size%n)>1):
        left_over=(data[size-size%n:])
        left_over_std=(np.std(data[size-size%n:],ddof=1))
        oulst.append(round(left_over_std,2))

    return oulst
