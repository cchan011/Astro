from astroquery.jplhorizons import Horizons
from astropy.time import Time
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

AlbionPath = 'https://raw.githubusercontent.com/cchan011/Astro/main/final/albion.txt'
Albiondata = np.genfromtxt(AlbionPath, skip_header=61, skip_footer= 65, delimiter=',', names=['JDTDB','CalendarDate','X','Y','Z'])

ArrokothPath = 'https://raw.githubusercontent.com/cchan011/Astro/main/final/arrokoth.txt'
Arrokothdata = np.genfromtxt(ArrokothPath, skip_header=61, skip_footer= 65, delimiter=',', names=['JDTDB','CalendarDate','X','Y','Z'])

SilaPath = 'https://raw.githubusercontent.com/cchan011/Astro/main/final/sila-nunam.txt'
Siladata = np.genfromtxt(SilaPath, skip_header=61, skip_footer= 65, delimiter=',', names=['JDTDB','CalendarDate','X','Y','Z'])

tPath = 'https://raw.githubusercontent.com/cchan011/Astro/main/final/teharonhiawako.txt'
tdata = np.genfromtxt(tPath, skip_header=61, skip_footer= 65, delimiter=',', names=['JDTDB','CalendarDate','X','Y','Z'])

quaoarPath = 'https://raw.githubusercontent.com/cchan011/Astro/main/final/quaoar.txt'
quaoardata = np.genfromtxt(quaoarPath, skip_header=61, skip_footer= 65, delimiter=',', names=['JDTDB','CalendarDate','X','Y','Z'])

fig, ax = plt.subplots()

ax.plot(Albiondata['X'], Albiondata['Y'], marker ='',ms=3, c='blue', label='Albion')
ax.plot(Arrokothdata['X'], Arrokothdata['Y'], marker ='',ms=3, c='red', label='Arrokoth')
ax.plot(Siladata['X'], Siladata['Y'], marker ='',ms=3, c='green', label='Sila-Nunam')
ax.plot(tdata['X'], tdata['Y'], marker ='',ms=3, c='purple', label='Teharonhiawako')
ax.plot(quaoardata['X'], quaoardata['Y'], marker ='',ms=3, c='black', label='Quaoar')
ax.plot(0 ,0, marker='o',ms=10,c="yellow",label='Sun')
ax.set_xlabel('X [AU]')
ax.set_ylabel('Y [AU]')
ax.set_title("Selected cold KBO orbit")
ax.set_aspect('equal')
ax.grid()
fig.legend(loc = 2)

fig2 = plt.figure()
ax1 = plt.subplot()
ax1.plot(Albiondata['X'], Albiondata['Z'], marker ='',ms=3, c='blue', label='Albion')
ax1.plot(Arrokothdata['X'], Arrokothdata['Z'], marker ='',ms=3, c='red', label='Arrokoth')
ax1.plot(Siladata['X'], Siladata['Z'], marker ='',ms=3, c='green', label='Sila-Nunam')
ax1.plot(tdata['X'], tdata['Z'], marker ='',ms=3, c='purple', label='Teharonhiawako')
ax1.plot(quaoardata['X'], quaoardata['Z'], marker ='',ms=3, c='black', label='Quaoar')
ax1.plot(0 ,0, marker='o',ms=10,c="yellow",label='Sun')
ax1.set_xlabel('X [AU]')
ax1.set_ylabel('Z [AU]')
ax1.set_title("Selected cold KBO orbit")
ax1.set_aspect('equal')
ax1.grid()
fig2.legend(loc = 2)

plt.show()