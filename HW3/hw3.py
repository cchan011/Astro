import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import requests
from scipy.signal import find_peaks
from scipy.optimize import fsolve

light_link = "https://github.com/cchan011/Astro/blob/main/HW3/astro%20hw3%20pics/light.jpg?raw=true"
gas_link = "https://github.com/cchan011/Astro/blob/main/HW3/astro%20hw3%20pics/gas.jpg?raw=true"
red_link = "https://github.com/cchan011/Astro/blob/main/HW3/astro%20hw3%20pics/red_led_spectrum.jpg?raw=true"
uv_link = "https://github.com/cchan011/Astro/blob/main/HW3/astro%20hw3%20pics/uv_led_spectrum.jpg?raw=true"

light = Image.open(requests.get(light_link, stream=True).raw)
gas = Image.open(requests.get(gas_link, stream=True).raw)
red = Image.open(requests.get(red_link, stream=True).raw)
uv = Image.open(requests.get(uv_link, stream=True).raw)

lightData = np.array(light, dtype=int)
gasData = np.array(gas, dtype=int)
redData = np.array(red, dtype=int)
uvData = np.array(uv, dtype=int)

#images already rotated as is. comment out the other plots then plt.show() if trying to look at a specific plot
#(spectrum row range, extract line) based on visual inspection

#full pic
'''
lightplot = plt.imshow(light) #1450 - 1750, 1600
gasplot = plt.imshow(gas) #1600 - 1800, 1700
redplot = plt.imshow(red) #1500 - 1700, 1600
uvplot = plt.imshow(uv) #1500 - 1630, 1600
'''

#trimmed dataset
lightData2 = lightData[1450:1750,:]
gasData2 = gasData[1600:1800,:]
redData2 = redData[1500:1700,:]
uvData2 = uvData[1500:1630,:]

#trimmed image
'''
lightplot2 = plt.imshow(lightData2) 
gasplot2 = plt.imshow(gasData2) 
redplot2 = plt.imshow(redData2) 
uvplot2 = plt.imshow(uvData2)
'''

#extracted line
lightLine = 1600
gasLine = 1700
redLine = 1600
uvLine = 1600

#rgb values
lightR = lightData[lightLine,:][:,0]
lightG = lightData[lightLine,:][:,1]
lightB = lightData[lightLine,:][:,2]
lightAvg = lightR + lightG + lightB

gasR = gasData[gasLine,:][:,0]
gasG = gasData[gasLine,:][:,1]
gasB = gasData[gasLine,:][:,2]
gasAvg = gasR + gasG + gasB

redR = redData[redLine,:][:,0]
redG = redData[redLine,:][:,1]
redB = redData[redLine,:][:,2]
redAvg = redR + redG + redB

uvR = uvData[uvLine,:][:,0]
uvG = uvData[uvLine,:][:,1]
uvB = uvData[uvLine,:][:,2]
uvAvg = uvR + uvG + uvB

#all pics have same x range (same phone camera)
x = np.linspace(start=1, stop=uv.size[0], num=uv.size[0])

#Calibration for the lightbulb and gas spectrum. The LED spectrums are NOT calibrated since I took those pictures at home.
'''
lightPeaks, _ = find_peaks(lightAvg, height = ??)

lightPurplePeak = lightPeaks.argmin()
lightRedPeak = lightPeaks.argmax()

def func(p):
    return [lightPurplePeak*p[0]+p[1]-436.594, lightRedPeak*p[0]+p[1]-610.788]

params = fsolve(func, [1, 1])
Wavelength = x*params[0]+params[1]

fig = plt.figure()
ax = plt.subplot()
ax.plot(Wavelength, lightAvg, color = 'black', label = 'light')
ax.set_xlabel('Wavelength [nm]')
ax.set_title('Calibrated CFB spectrum')

fig2 = plt.figure()
ax2 = plt.subplot()
ax2.plot(Wavelength, gasAvg, color = 'black', label = 'gas')
ax2.set_xlabel('Wavelength [nm]')
ax2.set_title('Calibrated Spectrum from mystery gas emission')
'''


fig = plt.figure()
ax = plt.subplot()
ax.plot(x, lightAvg, color='red', label = 'light')
ax.set_title('CFB light spectrum')

fig2 = plt.figure()
ax2 = plt.subplot()
ax2.plot(x, gasAvg, color='red', label = 'gas')
ax2.set_title('Mystery light spectrum')


fig3 = plt.figure()
ax3 = plt.subplot()
ax3.plot(x, redAvg, color='red', label = 'red')
ax3.set_title('Red LED light spectrum')

fig4 = plt.figure()
ax4 = plt.subplot()
ax4.plot(x, uvAvg, color='purple', label = 'UV')
ax4.set_title('UV LED light spectrum')

RedPeak = redAvg.argmax()
uvPeak = uvAvg.argmax()

print('Red LED peak: (' + str(RedPeak) + ',' + str(redAvg[RedPeak]))
print('UV LED peak: (' + str(uvPeak) + ',' + str(uvAvg[uvPeak]))

plt.show()
