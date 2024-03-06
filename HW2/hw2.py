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

B1 = 2.81*(33.5795-33.3606)
h1 = 2.81
A1 = (1/2)*B1*h1

B2 = 3.08*(270.577-270.3941)
h2 = 3.08
A2 = (1/2)*B2*h2

print('A1 = '+str(A1))
print('A2 = '+str(A2))

#they are about the same

EarthPath = 'https://raw.githubusercontent.com/cchan011/Astro/main/HW2/Earth.txt'
DucrosaPath = 'https://raw.githubusercontent.com/cchan011/Astro/main/HW2/Ducrosa.txt'
Edata = np.genfromtxt(EarthPath, skip_header=55, skip_footer= 68,delimiter=',', names=['JDTDB','CalendarDate','X','Y','Z','VX','VY','VZ'])
Ddata = np.genfromtxt(DucrosaPath, skip_header=61, skip_footer= 68, delimiter=',', names=['JDTDB','CalendarDate','X','Y','Z','VX','VY','VZ'])

fig, ax = plt.subplots()

ax.plot(Edata['X'], Edata['Y'], marker ='',ms=3, c='blue')
ax.set_xlabel('X [km]')
ax.set_ylabel('Y [km]')
ax.set_title("Earth's Orbit")
ax.set_aspect('equal')
ax.grid()
plt.show()