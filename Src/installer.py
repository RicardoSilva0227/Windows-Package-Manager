import urllib.request
import os
import subprocess
import requests
import yaml

def run_installer(file):
    try: 
        packageInfo = getPackageInfo(file)

        if packageInfo:
            installerNameExe = packageInfo['SetupName']
            url = packageInfo['Url']
            instructions = packageInfo['Instructions']

        # urllib.request.urlretrieve(url, installerNameExe)
        download_file(url, installerNameExe)
        
        if installerNameExe.endswith('.msi'):
            subprocess.check_call(['msiexec', '/i', installerNameExe, '/quiet', '/norestart'])
        else:
            subprocess.check_call(installerNameExe + ' ' + instructions, shell=True)

        os.remove(packageInfo)
    except subprocess.CalledProcessError as error:
        print("Failed to install {package}", error)



def getPackageInfo(file):
    # Accesses the YAML file for the program info needed.
    try:
        os.chdir(os.path.dirname(os.path.abspath(__file__)))
        print(os.getcwd())
        with open('programsConfig.yaml', 'r') as programFile:
            programInfo = yaml.safe_load(programFile)
        
        return programInfo[file]
    except subprocess.CalledProcessError as error:
        print("Failed to install {package}", error)


def download_file(url, filename):
    # Download file making sure it was downloaded correctly.
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)