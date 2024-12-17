"""
The main Python mpdule that combines cleaner and metrics functions in order to
perform comprehensive analysis
"""

from metrics import window_max, window_average, window_stddev
from cleaner import filter_nondigits, filter_outliers

import matplotlib.pyplot as plt
import os.path

def run(filename: str) -> None:
    """
    Process heart rate data from the specified file, clean it, calculate metrics, 
    and save visualizations.

    Args:
        filename (str): The path to the data file (e.g., 'data/data1.txt').

    Steps:
        1. Read the file into a list of strings.
        2. Use `filter_nondigits` to clean the data and remove invalid entries.
        3. Use `filter_outliers` to remove unrealistic heart rate samples (<30 or >250).
        4. Calculate rolling maximums, averages, and standard deviations using functions from `metrics.py`.
        5. Save the plots to the `images/` folder:
            - Rolling maximums -> 'images/maximums.png'
            - Rolling averages -> 'images/averages.png'
            - Rolling standard deviations -> 'images/stdevs.png'

    Returns:
        list[int], list[int], list[int]: You will return the maximums, averages, and stdevs (in this order).
    """  
    data = []

    # open file and read into the `data` list
    file = open(filename)
    for line in file:
        data.append(line)

    #using the filter_nondigits to clean data
    data=filter_nondigits(data)
    
    #using the filter_outliers to clean data
    data=filter_outliers(data)
    print((data))

    #creating the images for maximums
    maximums = window_max(data, 6)
    fig, ax = plt.subplots()
    ax.plot(maximums)
    plt.savefig("images/maximums.png")

    #creating the images for averages
    averages = window_average(data, 6)
    fig,ax = plt.subplots()
    ax.plot(averages)
    plt.savefig("images/averages.png")

    #creating the images for stdevs
    stdevs = window_stddev(data, 6)
    fig,ax = plt.subplots()
    ax.plot(stdevs)
    plt.savefig("images/stdevs.png")
   
    if __name__ == "__main__":
        run("data/data1.txt")
    
    return maximums, averages, stdevs

    