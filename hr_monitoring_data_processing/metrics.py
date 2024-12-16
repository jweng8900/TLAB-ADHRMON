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
        oulst.append(sum(temp)/n)


    if(size%n >=1):
        temp_last=data[size-(size%n):size]
        temp_length=len(temp_last)
        oulst.append(sum(temp_last)/temp_length)
    
    return oulst


def window_stddev(data: list, n: int) -> list:
    oulst=[]
    top_num=[]

    size=len(data) 
    
    if(len(data)<=0 or n<=1):
        return []
    else:
        for k in range(0,size-(size%n),n):
            temp=data[k:k+n]
            mean=sum(temp)/n
            sum_squared_diff = 0
            for j in temp:
                sum_squared_diff += (j - mean) ** 2

            stddev = np.sqrt(sum_squared_diff / (n - 1))
            oulst.append(round(stddev, 2))

    if(size%n >=1):
        temp=data[size-(size%n):size]
        mean=sum(temp)/len(temp)
        sum_squared_diff =  (j - mean) ** 2
        stddev = np.sqrt(sum_squared_diff / (n - 1))
        oulst.append(round(stddev, 2))      
    
    return oulst