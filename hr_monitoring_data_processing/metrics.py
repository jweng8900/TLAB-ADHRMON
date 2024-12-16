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


    if(len(data)==0):
     print("empty")
    else:
        for i in range(0,(size-(size%n)),n):
            for k in range(i,i+n):
                max=data[i]
                if(data[k]>=max):
                    max=data[k]
            oulst.append(max)   
    
        for l in range((size-(size%n)),size):
            oulst.append(data[l])
    return oulst


def window_average(data: list, n: int) -> list:
    pass


def window_stddev(data: list, n: int) -> list:
    pass
