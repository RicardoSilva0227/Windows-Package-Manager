# Dictionary mapping installer names
INSTALLER_MAP = {
    'Opera': 'OperaSetup.exe',
    'Firefox': 'firefox_installer.exe',
    'Steam': 'SteamSetup.exe',
}

def returnInstallerName(installerName):
    return INSTALLER_MAP.get(installerName, None)