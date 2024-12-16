def filter_nondigits(data: list) -> list:
    """
    Filter all strings from list that are not integers

    Args:
        data (list[str]): list of strings representing heart rate samples.
            Might contain invalid or missing data.
    Returns:
        list[int]: list of integers, with all non-digit strings removed
    """
    number_list=[]

    if(len(data)==0):
        return []
    
    for k in data:
        k=k.strip()

        if (k.isdigit()):
            
            number_list.append(int(k))

    return number_list


def filter_outliers(data: list) -> list:
    filtered_nums=[]

    for k in data:
        if(k>30 and k<250):
            filtered_nums.append(k)

    return filtered_nums