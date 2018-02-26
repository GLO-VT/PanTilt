import ephem
import math
from datetime import datetime

## Satellite Location (Lat,Long,Alt)
# satlat = 
# satlon = 
# satalt = 

## Blacksburg Observer Location (Lat,Long,Alt)
reflat = 37.229572
reflon = -80.413940

vatech = ephem.Observer()
vatech.lon = str(reflat)
vatech.lat = str(reflon)
vatech.elevation = 635
vatech.date = datetime.utcnow()

sun = ephem.Sun(vatech)

el = float(sun.alt)
az = float(sun.az)

## Observer Location (Cartesian)
## Unnecessary right now
# Rvt = 6371;
# xvt = Rvt*math.cos(math.radians(reflat))*math.cos(math.radians(reflon))
# yvt = Rvt*math.cos(math.radians(reflat))*math.sin(math.radians(reflon))
# zvt = Rvt*math.sin(math.radians(reflat))

## Sun Location (Cartesian)
Rsun = 149600000
xsun = Rsun*math.cos(el)*math.cos(az)
ysun = Rsun*math.cos(el)*math.sin(az)
zsun = Rsun*math.sin(el)

## Satellite Location (Cartesian)
# Rsat = 6371 + refalt;
# xsat = Rvt*math.cos(math.radians(satlat))*math.cos(math.radians(satlon))
# ysat = Rvt*math.cos(math.radians(satlat))*math.sin(math.radians(satlon))
# zsat = Rvt*math.sin(math.radians(satlat))

## Sat - Sun Vector
# xdir = xsun - xsat
# ydir = ysun - ysat
# zdir = zsun - zsat
# normvec = (xdir^2 + ydir^2 + zdir^2)**.5


