from astroquery.jplhorizons import Horizons
from astropy.time import Time
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

#problem 1
towerWidth = 10
towerHeight = 40
towerDistance = 100
towerTopAngle = np.arctan(towerHeight/towerDistance)*360/(2*np.pi)
towerSideAngle = np.arctan((towerWidth/2)/towerDistance)*360/(2*np.pi)

t = Time('2024-02-01T17:00:00.00', format='isot', scale='utc')
Huntsville = {'lon':-86.59, 'lat':34.73, 'elevation': 0} #assuming the field is at elevation 0, lon lat found at https://gammaray.nsstc.nasa.gov/events/5hgrbs/info/maps/al.html
Sun = Horizons('Sun', location=Huntsville, epochs=t.jd)
SunEph = Sun.ephemerides()
#print(SunEph['EL']) #checking if it works

fig, ax = plt.subplots()
ax.scatter(SunEph['AZ'], SunEph['EL'], s = 20, color='orange')
ax.set_xlabel('Azimuth [Deg]')
ax.set_ylabel('Elevation [Deg]')
ax.set_title("Solar position on "+t.isot+" UTC")
ax.set_xlim(0,360)
ax.set_ylim(0,90)
rect = patches.Rectangle((180-towerSideAngle, 0), towerSideAngle*2, towerTopAngle, linewidth=1, edgecolor='k', facecolor='gray')
ax.add_patch(rect)
ax.text(180, 0, 'S',
        verticalalignment='bottom', horizontalalignment='center',
        color='Red', fontsize=15)
ax.text(90, 0, 'E',
        verticalalignment='bottom', horizontalalignment='center',
        color='Red', fontsize=15)
ax.text(270, 0, 'W',
        verticalalignment='bottom', horizontalalignment='center',
        color='Red', fontsize=15)
ax.text(190, 20, 'Tower', color='black', fontsize=15)
ax.text(160, 40, 'Sun', color='black', fontsize=15)
ax.grid()

#problem 2
t2 = Time('1610-01-13T16:48:30.00', format='isot', scale='utc') #found on JPL Horizons that the Sunset (EL = 0) time was between 15:48 and 15:49 UTC on Jan 13th 1610. Assuming Sunset happened exactly at 15:48:30, so then first hour of night = 16:48:30
Padua = {'lon': 11.8768,'lat': 45.4064, 'elevation': 0} #assuming elevation is 0 again
Jupiter = Horizons(599, location=Padua, epochs=t2.jd)
Io = Horizons(501, location=Padua, epochs=t2.jd)
Europa = Horizons(502, location=Padua, epochs=t2.jd)
Ganymede = Horizons(503, location=Padua, epochs=t2.jd)
Callisto = Horizons(504, location=Padua, epochs=t2.jd)
JupiterEph = Jupiter.ephemerides()
IoEph = Io.ephemerides()
EuropaEph = Europa.ephemerides()
GanymedeEph = Ganymede.ephemerides()
CallistoEph = Callisto.ephemerides()
plt.figure(1)
fig, ax = plt.subplots()
ax.scatter(JupiterEph['AZ'], JupiterEph['EL'], s = 600, color='brown')
ax.scatter(IoEph['AZ'], IoEph['EL'], s = 20, color='red')
ax.scatter(EuropaEph['AZ'], EuropaEph['EL'], s = 20, color='orange')
ax.scatter(GanymedeEph['AZ'], GanymedeEph['EL'], s = 20, color='blue')
ax.scatter(CallistoEph['AZ'], CallistoEph['EL'], s = 20, color='green')
ax.set_xlabel('Azimuth [Deg]')
ax.set_ylabel('Elevation [Deg]')
ax.set_title("Jupiter and its 4 major moons' positions, \n on "+t2.isot+" UTC")
ax.set_xlim(99.9,100)
ax.set_ylim(40.5,40.75)
ax.text(JupiterEph['AZ']-0.01, JupiterEph['EL']+0.013, 'Jupiter', color='brown', fontsize=10)
ax.text(IoEph['AZ'], IoEph['EL']-0.011, 'Io', color='red', fontsize=10)
ax.text(EuropaEph['AZ']-0.01, EuropaEph['EL']+0.01, 'Europa', color='orange', fontsize=10)
ax.text(GanymedeEph['AZ']-0.015, GanymedeEph['EL']+0.01, 'Ganymede', color='blue', fontsize=10)
ax.text(CallistoEph['AZ']-0.011, CallistoEph['EL']+0.007, 'Callisto', color='green', fontsize=10)
ax.grid()

#problem 3
#i am choosing central park for the nyc place, and once again assuming elevation 0. TIme is 3pm = 15:00
CentralPark = {'lon':-73.966 ,'lat':40.782, 'elevation': 0}
SunCentralPark = Horizons('Sun', location=CentralPark, epochs={'start': '2024-01-01 20:00:00','stop': '2024-02-13 20:00:00','step':'1d'})
SunCentralParkEph = SunCentralPark.ephemerides()
plt.figure(2)
fig, ax = plt.subplots()
ax.scatter(SunCentralParkEph['AZ'], SunCentralParkEph['EL'], s = 20, color='orange')
ax.set_xlabel('Azimuth [Deg]')
ax.set_ylabel('Elevation [Deg]')
ax.set_title("Solar position on 20:00:00 UTC at Central Park, NYC. \n Daily from 2024-01-01 to 2024-02-13")
ax.set_xlim(0,360)
ax.set_ylim(0,90)
ax.grid()
#print(SunCentralParkEph[0][12]) #to find start and end point
#print(SunCentralParkEph[43][12])
ax.text(230, 10, 'Jan 1st', color='black', fontsize=10)
ax.text(230, 26, 'Feb 13th', color='black', fontsize=10)

#my southern hemisphere choice would be Auckland, New Zealand. UTC + 13. Still 3pm. Same assumption on elevation.
Auckland = {'lon':174.763,'lat':-36.850,'elevation':0}
SunAuckland = Horizons('Sun', location=Auckland, epochs={'start': '2024-01-01 02:00:00','stop': '2024-02-13 02:00:00','step':'1d'})
SunAucklandEph = SunAuckland.ephemerides()
plt.figure(3)
fig, ax = plt.subplots()
ax.scatter(SunAucklandEph['AZ'], SunAucklandEph['EL'], s = 20, color='orange')
ax.set_xlabel('Azimuth [Deg]')
ax.set_ylabel('Elevation [Deg]')
ax.set_title("Solar position on 02:00:00 UTC at Auckland, New Zealand. \n Daily from 2024-01-01 to 2024-02-13")
ax.set_xlim(0,360)
ax.set_ylim(0,90)
ax.grid()
#print(SunAucklandEph[0][12])
#print(SunAucklandEph[43][12])
ax.text(280, 67, 'Jan 1st', color='black', fontsize=10)
ax.text(320, 55, 'Feb 13th', color='black', fontsize=10)





plt.show()