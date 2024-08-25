import urllib.request
import os
import subprocess
import requests
import yaml

def run_installer(file):
    try: 
        packageInfo = getPackageInfo(file) # Grabs the file info
        if packageInfo:
            installerNameExe = packageInfo['SetupName']
            url = packageInfo['Url']
            instructions = packageInfo['Instructions']

        download_file(url, installerNameExe)
        
        if installerNameExe.endswith('.msi'):
            subprocess.check_call(['msiexec', '/i', installerNameExe, '/quiet', '/norestart']) # Uses the .MSI installer for the installation.
        else:
            subprocess.check_call(installerNameExe + ' ' + instructions, shell=True) # Downloads the app through CMD

        os.remove(packageInfo) # Removes the file after executions
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
    with requests.get(url, stream=True) as downloadObject: # Get Request the website hosting the download.
        downloadObject.raise_for_status() # Cheking the status (If its available, if not it will throw an exception.)
        with open(filename, 'wb') as file: # Opens the file in binary write mode
            for chunk in downloadObject.iter_content(chunk_size=8192): # iterates through the file in chuncks of 8 kbs.
                file.write(chunk) # Writes each chunk into the file.