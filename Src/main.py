from gui import PackageInstallerGUI


import subprocess
import urllib.request
import os

def main():
    app = PackageInstallerGUI()
    app.run()

if __name__ == "__main__":
    main()
