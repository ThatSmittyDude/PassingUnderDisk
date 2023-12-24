# -*- coding: utf-8 -*-
"""
Created on Sun Dec 24 02:34:11 2023

@author: smith
"""
#PassingUnderDisk1.0
import psutil
import os

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

def allocate_space(disk_name, size):
    # Add logic to allocate space on the selected disk
    print(f"Allocating {size} on Disk {disk_name}.")

def main():
    while True:
        print("\nDiskpart-like Commands:")
        print("  list disk              - List available disks")
        print("  select disk [name]     - Select a disk by name")
        print("  allocate [size]        - Allocate space on the selected disk")
        print("  exit                   - Quit the program")

        command = input("\nEnter a command: ").strip()

        if command.lower() == 'exit':
            break
        elif command.lower() == 'list disk':
            list_disks()
        elif command.lower().startswith('select disk'):
            _, disk_name = command.split(' ')
            select_disk(disk_name)
        elif command.lower().startswith('allocate'):
            _, size = command.split(' ')
            allocate_space("C:", size)  # Assume Disk C: for demonstration, modify as needed
        else:
            print("Invalid command. Enter 'help' for a list of commands.")

if __name__ == "__main__":
    main()

