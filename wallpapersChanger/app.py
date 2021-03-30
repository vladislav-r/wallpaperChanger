import ctypes
from datetime import datetime
from os import listdir
import time
from glob import glob

from config import foldWithWallpapers, morning, day, evening, night


def getCurrentTime():
    return datetime.now().time().strftime('%H')

allWalpapers = listdir('D:\\Pictures\\wallpapers\\auto\\')

nightPic = glob(foldWithWallpapers +"*-night.*")
nightPicStr = ' '.join(map(str, nightPic))

eveningPic = glob(foldWithWallpapers +"*-evening.*")
eveningPicStr = ' '.join(map(str, eveningPic))

dayPic = glob(foldWithWallpapers +"*-day.*")
dayPicStr = ' '.join(map(str, dayPic))

morningPic = glob(foldWithWallpapers +"*-day.*")
morningPicStr = ' '.join(map(str, morningPic))
while True:
    current_time = getCurrentTime()
    if int(current_time) >= evening:
        ctypes.windll.user32.SystemParametersInfoW(20, 0, nightPicStr, 0)
    elif int(current_time) >= day:
        ctypes.windll.user32.SystemParametersInfoW(20, 0, eveningPicStr, 0) #eveningPicStr
    elif int(current_time) >= morning:
        ctypes.windll.user32.SystemParametersInfoW(20, 0, dayPicStr, 0)
    elif int(current_time) >= night:
        ctypes.windll.user32.SystemParametersInfoW(20, 0, morningPicStr, 0)
    
    print('no sleep')
    time.sleep(300)







