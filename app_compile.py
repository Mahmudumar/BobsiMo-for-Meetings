import os
import shutil

app_name = 'BobsiMo Minute Recorder'



#do the compilation

yo=f"""\
pyinstaller --onefile --noconsole \
--hidden-import=pyaudio --hidden-import=speech_recognition \
-n "{app_name}" -i "./BMT_logo.ico" test2.py
"""
print(yo)
os.system(yo)


#copy image into the app dist
shutil.copy(r'.\\BMT_logo.ico', '.\\dist\\')

print('done')