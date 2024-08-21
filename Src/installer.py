import urllib.request
import os
import subprocess
from executables import returnInstallerName

def run_installer(url, file):
    try: 
        installerNameExe = returnInstallerName(file)
        urllib.request.urlretrieve(url, installerNameExe)
        subprocess.check_call([installerNameExe, '-ms'])
        os.remove(installerNameExe)
    except subprocess.CalledProcessError:
        print("Failed to install {package}")