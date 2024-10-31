import os
import shutil

app_name = 'BobsiMo Minute Recorder'



def make_app():#do the compilation

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


def app_installer_maker():
    # os.makedirs(f'./FINAL/{app_name}')
    #make an installer
    shutil.move('./dist/BobsiMo Minute Recorder.exe',f'./FINAL/{app_name}/BobsiMo Minute Recorder.exe')
    shutil.copy('./dist/BMT_logo.ico',f'./FINAL/{app_name}/BMT_logo.ico')
    shutil.copy(f'./FINAL/{app_name}/BMT_logo.ico', './FINAL')

# make_app()
app_installer_maker()