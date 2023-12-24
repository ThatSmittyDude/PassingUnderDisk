# -*- coding: utf-8 -*-
"""
Created on Sun Dec 24 02:34:11 2023

@author: smith
"""
#PassingUnderDisk1.01
import os
import subprocess
import psutil

def list_disks():
    print("Available disks:")
    for partition in psutil.disk_partitions():
        print(f"Disk {partition.device}")

def select_disk(disk_name):
    disk_path = disk_name
    if os.path.exists(disk_path):
        print(f"Disk {disk_name} selected.")
    else:
        print(f"Disk {disk_name} not found.")

def assign_drive_letter(volume, drive_letter):
    # Add logic to assign a drive letter to the selected volume
    print(f"Assigning drive letter {drive_letter} to {volume}.")

def format_volume(volume, filesystem):
    # Add logic to format the selected volume with the specified filesystem
    print(f"Formatting {volume} with {filesystem} filesystem.")

# Add more functions for the remaining commands...

def main():
    while True:
        print("\nDiskpart-like Commands:")
        print("  list disk              - List available disks")
        print("  select disk [name]     - Select a disk by name")
        print("  assign [volume] [letter]- Assign a drive letter to the selected volume")
        print("  format [volume] [fs]   - Format the selected volume with the specified filesystem")
        # Add more commands to the menu...

        command = input("\nEnter a command: ").strip()

        if command.lower() == 'exit':
            break
        elif command.lower() == 'list disk':
            list_disks()
        elif command.lower().startswith('select disk'):
            _, disk_name = command.split(' ')
            select_disk(disk_name)
        elif command.lower().startswith('assign'):
            _, volume, drive_letter = command.split(' ')
            assign_drive_letter(volume, drive_letter)
        elif command.lower().startswith('format'):
            _, volume, filesystem = command.split(' ')
            format_volume(volume, filesystem)
        # Add more command checks and calls here...

if __name__ == "__main__":
    main()

