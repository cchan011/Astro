import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import requests


#question 1
Sun_link = "https://raw.githubusercontent.com/cchan011/Astro/main/HW4/latest_4096_HMII.jpg"
Sun = Image.open(requests.get(Sun_link, stream=True).raw) #grayscale mode 
SunData = np.array(Sun, dtype=int)
ExtratedLine = 2048

#print(Sun.mode)

#intensity
IntensityData = SunData[ExtratedLine,:] #doesnt have RGB values anymore, only 1 for grayscale
DataXAxis = np.linspace(start=0, stop=Sun.size[0], num=Sun.size[0])

fig = plt.figure(0)
ax = plt.subplot()
ax.plot(DataXAxis, IntensityData, color = 'black', label = 'data')
ax.set_xlim([0,4095]) #0 to 4095
ax.set_ylim([0,255])
ax.set_xlabel('Pixels')
ax.set_ylabel('Intensity')
ax.set_title('Intensity graphed, based on the image')

#for the function, I will add the two opposite pixels together, get an average, then get distance
#from the JPL database, Photosphere radius of the Sun = 696500 km
a = 2047
b = 2048
Avg = []
while a >= 0 and b <=4095:
    AvgNumber = (IntensityData[a] + IntensityData[b])/2
    Avg.append(AvgNumber)
    a -= 1
    b += 1

#in order to find the edges of the Sun in pixel numbers, use the following two lines of code:
#Zeros = [i for i, x in enumerate(IntensityData) if x == 0]
#print(Zeros) 
#using the zero array above, it shows that pixels 170 and 3927 are the edges.
#so the photosphere radius takes up 2047-170 = 1877 pixels.
scale = 696500 / 1877
DataXAxis2 = np.linspace(start=0, stop=len(Avg), num=len(Avg))
Distance = DataXAxis2 * scale

fig1 = plt.figure(1)
ax1 = plt.subplot()
ax1.plot(Distance, Avg, color = 'black', label = 'distance')
ax1.ticklabel_format(style='sci', axis='x', scilimits=(0,0))
ax1.set_xlim([0,7.5e5])
ax1.set_ylim([0,255])
ax1.set_xlabel('Distance from center (km)')
ax1.set_ylabel('Intensity')
ax1.set_title('Observed intensity graphed, based on distance from center')

#since the HMI observes the Sun at 6173 angstrom, we can't use Bohm-Vitense a_lambda or b_lambda constants, and thus can't solve exactly 
#the Eddington approximation is as follows:
#I(\theta)/I(0) = (2/5) + (3/5)cos(\theta)

angle = np.linspace(start=0, stop=np.pi/2, num=900)
IntensityTheoretical = (2/5) + (3/5)*np.cos(angle)
AngleAxis = angle*90/(np.pi/2)
#converting angles back to plane geometry distance
DistanceAxis = AngleAxis*696500/90

fig2 = plt.figure(2)
ax2 = plt.subplot()
ax2.plot(DistanceAxis, IntensityTheoretical, color = 'black', label = 'angle')
ax2.ticklabel_format(style='sci', axis='x', scilimits=(0,0))
ax2.set_xlim([0,7.5e5])
ax2.set_ylim([0,1])
ax2.set_xlabel('Distance from center (km)')
ax2.set_ylabel('Intensity function over intensity at zero angle')
ax2.set_title('Eddington approximation, based on distance from center')

#combined graph
#I(0) = 140, to match closer to observed intensity
fig3 = plt.figure(3)
ax3 = plt.subplot()
ax3.plot(Distance, Avg, color = 'red', label = 'Observed')
ax3.plot(DistanceAxis, IntensityTheoretical*140, color = 'green', label = 'Theoretical')
ax3.ticklabel_format(style='sci', axis='x', scilimits=(0,0))
ax3.set_xlim([0,7.5e5])
ax3.set_ylim([0,255])
ax3.set_xlabel('Distance from center (km)')
ax3.set_ylabel('Intensity')
ax3.set_title('Combined graph, with zero angle intensity = 140')
fig3.legend(loc = 2)



plt.show()