# gui.py

import tkinter as tk
from tkinter import ttk, messagebox
from installer import run_installer

class PackageInstallerGUI:
    def __init__(self):
        self.packages = {
            "Wiz Tree": "https://diskanalyzer.com/files/wiztree_4_20_setup.exe",
            "Opera": "https://www.opera.com/computer/thanks?ni=stable&os=windows",
            "Godot": "https://github.com/godotengine/godot/releases/download/4.3-stable/Godot_v4.3-stable_win64.exe.zip",
            "Blender": "https://ftp.halifax.rwth-aachen.de/blender/release/Blender4.2/blender-4.2.1-windows-x64.msi",
            "Firefox": "https://download.mozilla.org/?product=firefox-latest&os=win64&lang=en-US",
            "Discord": "https://discord.com/api/downloads/distributions/app/installers/latest?channel=stable&platform=win&arch=x64",
            "TeamSpeak 5": "https://files.teamspeak-services.com/pre_releases/client/5.0.0-beta77/teamspeak-client.msi",
            "TeamSpeak 3.6.2": "https://files.teamspeak-services.com/releases/client/3.6.2/TeamSpeak3-Client-win64-3.6.2.exe",
            "7Zip": "https://7-zip.org/a/7z2408-x64.msi",
            "WinRar": "https://www.win-rar.com/postdownload.html?&L=0",
        }
        self.root = tk.Tk()
        self.root.title("Package Installer")
        self.root.geometry("700x450")
        
        self.package_vars = {}
        self.create_widgets()

    def create_widgets(self):
        title_label = tk.Label(self.root, text="Select Packages to Install", font=("Helvetica", 16, "bold"))
        title_label.grid(row=0, column=0, columnspan=2, pady=(10, 20))

        row = 1
        for package_name in self.packages:
            var = tk.BooleanVar()
            chk = tk.Checkbutton(self.root, text=package_name, variable=var, font=("Helvetica", 12))
            chk.grid(row=row, column=0, sticky='w', padx=20, pady=5)
            self.package_vars[package_name] = var
            row += 1

        install_button = tk.Button(self.root, text="Install Selected", command=self.install_selected_packages, font=("Helvetica", 12), bg="#4CAF50", fg="white")
        install_button.grid(row=row, column=0, pady=(20, 10))

        self.progress = ttk.Progressbar(self.root, orient="horizontal", length=300, mode="determinate")
        self.progress.grid(row=row + 1, column=0, columnspan=2, pady=(10, 20))

    def install_selected_packages(self):
        selected = [pkg for pkg, var in self.package_vars.items() if var.get()]
        if not selected:
            messagebox.showinfo("No selection", "Please select at least one package.")
            return

        total_packages = len(selected)
        self.progress["maximum"] = total_packages

        for i, package in enumerate(selected):
            url = self.packages[package]

            if run_installer(url, package): 
                messagebox.showinfo(f"{package} installed successfully!")
            else: 
                messagebox.showinfo(f"Failed to install {package}.")
                
            self.progress["value"] = i + 1
            self.root.update_idletasks()
        
        messagebox.showinfo("Done", "Selected packages have been installed or downloaded.")
        self.progress["value"] = 0  # Reset the progress bar

    def run(self):
        self.root.mainloop()
