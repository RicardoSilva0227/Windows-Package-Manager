# Dictionary mapping installer names
INSTALLER_MAP = {
    'Opera': 'OperaSetup.exe',
    'Firefox': 'firefox_installer.exe',
    'Steam': 'SteamSetup.exe',
    'Discord': 'DiscordSetup.exe',
    'Blender': 'blender-4.2.1-windows-x64.msi',
    'TeamSpeak 5': 'teamspeak-client.msi',
    'TeamSpeak 3.6.2': 'TeamSpeak3-Client-win64-3.6.2.exe',
    '7Zip': '7z2408-x64.msi',
    'WinRar': 'winrar-x64-701.exe',
    'Wiz Tree': 'wiztree_4_20_setup.exe',
}

def returnInstallerName(installerName):
    return INSTALLER_MAP.get(installerName, None)