import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import requests
from matplotlib import colormaps

#image dimension 2048 x 1288
Img_link = "https://raw.githubusercontent.com/cchan011/Astro/main/HW5/DTEPD_026905_2610_027024_2610_A01.jpg"
Cone = Image.open(requests.get(Img_link, stream=True).raw).convert('L') #for some reason this is in RGB mode? convert to grayscale 
ConeData = np.array(Cone, dtype=int)

ScaleLine = 18 #by manual inspection, pixel 18 should have only the white line without interference from the caption
ExtractedLine = 630 #one of the lines that crosses the cone

ScaleData = ConeData[ScaleLine,:]
LineDataFullLine = ConeData[ExtractedLine,:] #full line profile
LineData = LineDataFullLine[100:1947] #trimmed left and right edge to dodge the sudden jump to 0

#print(LineData)

#find the pixels corresponding to the scale via the two lines below
#ScalePixel = [i for i, x in enumerate(ScaleData) if x == 255]
#print(ScalePixel)
#this shows that from pixel 1832 to 1956 is the white line, which corresponds to 1km in real distance.

ImageScale = 1000/(1956-1832)

#for verticle scale, the readme file states that the maximum elevation of the image is -4584.56m
#the minimum is -4996.51m. These two values correspond to the 0-255 grayscale.

HeightScale = (4996.51-4584.56)/255

PixelAxis = np.linspace(start=100, stop=Cone.size[0]-201, num=Cone.size[0]-201)
XAxis = PixelAxis*ImageScale
YAxis = (LineData*HeightScale)-4996.51
colors = YAxis+4996.51

fig = plt.figure(0)
ax = plt.subplot()
colorPlot = ax.scatter(XAxis, YAxis, marker =',', c = colors, cmap = 'jet')
ax.set_xlabel('Distance (m)')
ax.set_ylabel('Height (m)')
ax.set_title('Height graphed with color bar')
cbar = plt.colorbar(colorPlot)
cbar.ax.set_ylabel("Height (m)")

plt.show()