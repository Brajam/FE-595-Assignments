# -*- coding: utf-8 -*-
"""
Created on Sat Feb  2 16:31:09 2019

@author: ramra
"""

# Use NumPy and MatPlotLib to graph one period of sine and cosine on the same set of axes. 
#import numpy and matplotlib libraries used to generate the sin/cosite time and plot the graph
import numpy as np
import matplotlib.pyplot as plot
# Get x values of the graphs starting at 0 and ending at 2Pi.
time = np.linspace(0, 2*np.pi)
# Amplitude of the sine wave is sine of a variable like time
sin_amplitude = np.sin(time)
cos_amplitude = np.cos(time)
#Abraham's change Starts
#Adding calculation of the tangent
tan_amplitude = np.tan(time)
#As the tangent has Asymptote, Matplotlib is adding a vertical line
#an option for fixing the issue (based on:
#https://stackoverflow.com/questions/42837910/omit-joining-lines-in-matplotlib-plot-e-g-y-tanx)
#Using this approach, we will change the value Y in which the asymptote move from inf to -inf
tan_amplitude[:-1][np.diff(tan_amplitude) < 0] = np.nan
#Abraham's change ends

# Plot a sine wave using time and amplitude obtained for the sine wave
plot.plot(time, sin_amplitude,color="red",label="sine")
plot.plot(time, cos_amplitude,color="blue",label="cosine")
#Abraham's change Starts
#Adding tangent graph in green color
plot.plot(time, tan_amplitude,color="green",label="tangent")
#Abraham's change ends

# Give a title for the sine wave plot
#Abraham's change Starts
#Renaming the Graph Title
#plot.title('Sine and Cosine wave')
plot.title('Sine, Cosine and Tangent wave')
#Abraham's change ends

# Give x axis label for the sine wave plot
plot.xlabel('Time')
# Give y axis label for the sine wave plot
plot.ylabel('Amplitude')

plot.xticks((0,np.pi/2,np.pi,np.pi*3/2,np.pi*2),('0','π/2','π','3π/2','2π'))

#Abraham's change Starts
#Define the X axis limits
plot.xlim((0, 2 * np.pi))
#Define the Y axis limits
plot.ylim((-1,1))
# Removing the grid to have more clarity on the graphs
#plot.grid(True, which='both')
plot.grid(False, which='both')
#Abraham's change ends

plot.axhline(y=0, color='k')
# show the legend
plot.legend()

#Abraham's change Starts
#saving the graph to a file
plot.savefig('Assignment2.pdf')
#Abraham's change ends

# show the graph
plot.show()


