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
    
    pass