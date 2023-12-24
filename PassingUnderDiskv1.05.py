# -*- coding: utf-8 -*-
"""
Created on Sun Dec 24 02:34:11 2023

@author: smith
"""
#PassingUnderDiskv1.05

# DPv1.05

import subprocess
import ctypes
import sys

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def elevate():
    if not is_admin():
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
        sys.exit()

def display_help():
    print("\nAvailable commands:")
    print("ACTIVE      - Mark the selected partition as active.")
    print("ADD         - Add a mirror to a simple volume.")
    print("ASSIGN      - Assign a drive letter or mount point to the selected volume.")
    print("ATTRIBUTES  - Manipulate volume or disk attributes.")
    print("ATTACH      - Attaches a virtual disk file.")
    print("AUTOMOUNT   - Enable and disable automatic mounting of basic volumes.")
    print("BREAK       - Break a mirror set.")
    print("CLEAN       - Clear the configuration information, or all information, off the disk.")
    print("COMPACT     - Attempts to reduce the physical size of the file.")
    print("CONVERT     - Convert between different disk formats.")
    print("CREATE      - Create a volume, partition or virtual disk.")
    print("DELETE      - Delete an object.")
    print("DETAIL      - Provide details about an object.")
    print("DETACH      - Detaches a virtual disk file.")
    print("EXIT        - Exit DiskPart.")
    print("EXTEND      - Extend a volume.")
    print("EXPAND      - Expands the maximum size available on a virtual disk.")
    print("FILESYSTEMS - Display current and supported file systems on the volume.")
    print("FORMAT      - Format the volume or partition.")
    print("GPT         - Assign attributes to the selected GPT partition.")
    print("HELP        - Display a list of commands.")
    print("IMPORT      - Import a disk group.")
    print("INACTIVE    - Mark the selected partition as inactive.")
    print("LIST        - Display a list of objects.")
    print("MERGE       - Merges a child disk with its parents.")
    print("ONLINE      - Online an object that is currently marked as offline.")
    print("OFFLINE     - Offline an object that is currently marked as online.")
    print("RECOVER     - Refreshes the state of all disks in the selected pack.")
    print("              Attempts recovery on disks in the invalid pack, and")
    print("              resynchronizes mirrored volumes and RAID5 volumes")
    print("              that have stale plex or parity data.")
    print("REM         - Does nothing. This is used to comment scripts.")
    print("REMOVE      - Remove a drive letter or mount point assignment.")
    print("REPAIR      - Repair a RAID-5 volume with a failed member.")
    print("RESCAN      - Rescan the computer looking for disks and volumes.")
    print("RETAIN      - Place a retained partition under a simple volume.")
    print("SAN         - Display or set the SAN policy for the currently booted OS.")
    print("SELECT      - Shift the focus to an object.")
    print("SETID       - Change the partition type.")
    print("SHRINK      - Reduce the size of the selected volume.")
    print("UNIQUEID    - Displays or sets the GUID partition table (GPT) identifier or")
    print("              master boot record (MBR) signature of a disk.")

def execute_command(command):
    try:
        subprocess.run(['diskpart', '/s', '-'], input=command, text=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error executing diskpart command: {e}")

if __name__ == "__main__":
    elevate()  # Elevate the script to run with administrator privileges

    while True:
        display_help()
        command = input("\nEnter a command (or 'exit' to quit): ").strip().upper()

        if command == 'EXIT':
            break
        else:
            execute_command(command)

