## Question 1

Take a look at the file labeled `data/data2.txt`. Why might we have missing values or values that state "NO SIGNAL" in this dataset? While we are currently ignoring these values, what might be the risk of filtering these values out?

[NO Signal can mean the heart rate was not detected while reading or it was disconnected. These values can be important for people with irregular heart beat rythms with sudden stops.]

## Question 2

While the "averages.png" and "maximums.png" graphs visualize typical values in our time-series data of heart rates and subsequently describe similar trends, the "stdevs.png" graph visualizes the standard deviations, which results in a graph with less apparent trends. In the context of heart rate, what does the standard deviation describe?

[In the context of heart rates, it shows the range of heart rates. These values represent deviations and variance from your average heart rate. The spikes in standard deviations might indicate irregular heart rates changes within the interval(window size)]

## Question 3

Run your `main.py` module and look at the graph labeled "averages.png." Roughly speaking, where do you see the time series experience a significant difference in values along the x-axis? Point out all x-values where you notice a drastic difference in future values.

[5,10,20, and near 30s are drastic differences in future values. They are indicated by the sharp changes in y-values(heart rates)]

## Question 4

Do you also notice a corresponding difference in values in the "stdevs.png" graph? If so, do these differences align with the "averages.png" graph? 

[Yes, sharp changes in average graph should be reflected in standard deviation graphs because it is calculated by variance which is the change of values in a range of values(window_size)]
