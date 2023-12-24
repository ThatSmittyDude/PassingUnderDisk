# -*- coding: utf-8 -*-
"""
Created on Sun Dec 24 02:34:11 2023

@author: smith
"""
#PassingUnderDisk0.9
import os

def list_disks():
    print("Available disks:")
    for root, dirs, files in os.walk("\\\\.\\PHYSICALDRIVE"):
        for dir in dirs:
            print(f"Disk {dir}")

def select_disk(disk_number):
    disk_path = f"\\\\.\\PHYSICALDRIVE{disk_number}"
    if os.path.exists(disk_path):
        print(f"Disk {disk_number} selected.")
    else:
        print(f"Disk {disk_number} not found.")

def allocate_space(disk_number, size):
    # Add logic to allocate space on the selected disk
    print(f"Allocating {size} on Disk {disk_number}.")

def main():
    while True:
        print("\nDiskpart-like Commands:")
        print("  list disk              - List available disks")
        print("  select disk [number]   - Select a disk by number")
        print("  allocate [size]        - Allocate space on the selected disk")
        print("  exit                   - Quit the program")

        command = input("\nEnter a command: ").strip()

        if command.lower() == 'exit':
            break
        elif command.lower() == 'list disk':
            list_disks()
        elif command.lower().startswith('select disk'):
            _, disk_number = command.split(' ')
            select_disk(disk_number)
        elif command.lower().startswith('allocate'):
            _, size = command.split(' ')
            allocate_space(1, size)  # Assume Disk 1 for demonstration, modify as needed
        else:
            print("Invalid command. Enter 'help' for a list of commands.")

if __name__ == "__main__":
    main()

