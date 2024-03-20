from astroquery.jplhorizons import Horizons
from astropy.time import Time
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

t1 = '2023-07-05T10:00:00.00'
t2 = '2023-07-06T10:00:00.00'
Ducrosa = Horizons(id='A895 EC', location='500@10', epochs={'start': t1, 'stop': t2, 'step':'1d'})
Eph = Ducrosa.ephemerides()

t3 = '2021-12-05T10:00:00.00'
t4 = '2021-12-06T10:00:00.00'
Ducrosa2 = Horizons(id='A895 EC', location='500@10', epochs={'start': t3, 'stop': t4, 'step':'1d'})
Eph2 = Ducrosa2.ephemerides()

print(Eph['datetime_str','delta','delta_rate','true_anom'])
print(Eph2['datetime_str','delta','delta_rate','true_anom'])

B1 = 2*np.pi*2.81*(33.5795-33.3606)
h1 = 2.81
A1 = (1/2)*B1*h1

B2 = 3.08*(270.577-270.3941)*2*np.pi
h2 = 3.08
A2 = (1/2)*B2*h2

print('A1 = '+str(A1))
print('A2 = '+str(A2))

#they are about the same

EarthPath = 'https://raw.githubusercontent.com/cchan011/Astro/main/HW2/Earth.txt'
DucrosaPath = 'https://raw.githubusercontent.com/cchan011/Astro/main/HW2/Ducrosa.txt'
Edata = np.genfromtxt(EarthPath, skip_header=54, skip_footer= 68,delimiter=',', names=['JDTDB','CalendarDate','X','Y','Z','VX','VY','VZ'])
Ddata = np.genfromtxt(DucrosaPath, skip_header=61, skip_footer= 68, delimiter=',', names=['JDTDB','CalendarDate','X','Y','Z','VX','VY','VZ'])

fig, ax = plt.subplots()

ax.plot(Edata['X'], Edata['Y'], marker ='',ms=3, c='blue', label='Earth')
ax.plot(Ddata['X'], Ddata['Y'], marker ='',ms=3, c='red', label='400 Ducrosa')
ax.set_xlabel('X [km]')
ax.set_ylabel('Y [km]')
ax.set_title("Earth's orbit and 400 Ducrosa's orbit")
ax.set_aspect('equal')
ax.grid()
fig.legend(loc = 2)



#problem 3
IMPath = 'https://raw.githubusercontent.com/cchan011/Astro/main/HW2/IM-1.txt'
IMdata = np.genfromtxt(IMPath, skip_header=114, skip_footer= 68,delimiter=',', names=['JDTDB','CalendarDate','X','Y','Z','VX','VY','VZ'])
MoonPath = 'https://raw.githubusercontent.com/cchan011/Astro/main/HW2/Moon.txt'
Mdata = np.genfromtxt(MoonPath, skip_header=50, skip_footer= 68,delimiter=',', names=['JDTDB','CalendarDate','X','Y','Z','VX','VY','VZ'])

fig2 = plt.figure()
ax1 = plt.subplot()

ax1.plot(0, 0, 'bo', ms=1, label='Earth')
ax1.plot(Mdata['X'], Mdata['Y'], marker ='',ms=3, c='black', label='Moon')
ax1.plot(IMdata['X'], IMdata['Y'], marker ='',ms=3, c='purple', label='IM-1')
ax1.set_xlabel('X [km]')
ax1.set_ylabel('Y [km]')
ax1.set_title('IM-1 path from Earth to Moon')
ax1.set_aspect('equal')
ax1.grid()
fig2.legend(loc = 2)

fig3 = plt.figure()
ax2 = plt.subplot()

ax2.plot(0, 0, 'bo', ms=1, label='Earth')
ax2.plot(Mdata['X'], Mdata['Z'], marker ='',ms=3, c='black', label='Moon')
ax2.plot(IMdata['X'], IMdata['Z'], marker ='',ms=3, c='purple', label='IM-1')
ax2.set_xlabel('X [km]')
ax2.set_ylabel('Z [km]')
ax2.set_title('IM-1 path from Earth to Moon, XZ axes')
ax1.grid()
fig3.legend(loc = 2)

fig4 = plt.figure()
ax3 = plt.subplot()

speed = np.sqrt(IMdata['VX']**2+IMdata['VY']**2+IMdata['VZ']**2)

ax3.plot(0, 0, 'bo', ms=1, label='Earth')
ax3.plot(Mdata['X'], Mdata['Y'], marker ='',ms=3, c='black', label='Moon')
colorPlot = ax3.scatter(IMdata['X'], IMdata['Y'], marker ='.', s=4, c=speed,cmap = 'jet')
ax3.set_xlabel('X [km]')
ax3.set_ylabel('Y [km]')
ax3.set_title('IM-1 speed plot')
ax3.set_aspect('equal')
ax3.grid()


plt.colorbar(colorPlot)


plt.show()