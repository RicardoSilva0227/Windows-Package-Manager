import urllib.request
import os
import subprocess
from executables import returnInstallerName

def run_installer(url, file):
    try: 
        installerNameExe = returnInstallerName(file)
        urllib.request.urlretrieve(url, installerNameExe)
        
        if installerNameExe.endswith('.msi'):
            subprocess.check_call(['msiexec', '/i', installerNameExe, '/quiet', '/norestart'])
        else:
            subprocess.check_call([installerNameExe, '/S', '/verysilent', '/norestart'])
            
        os.remove(installerNameExe)
    except subprocess.CalledProcessError as error:
        print("Failed to install {package}", error)