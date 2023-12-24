# -*- coding: utf-8 -*-
"""
Created on Sun Dec 24 02:34:11 2023

@author: smith
"""
#PassingUnderDisk1.02

import subprocess

def run_diskpart_command(command):
    try:
        result = subprocess.run(['diskpart', '/s', '-'], input=command, text=True, capture_output=True, check=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error executing diskpart command: {e.stderr}")

def list_disks():
    run_diskpart_command("list disk")

def select_disk(disk_number):
    run_diskpart_command(f"select disk {disk_number}")

def display_drive_specs(volume):
    run_diskpart_command(f"detail volume {volume}")

def allocate_partition(size, disk_number):
    run_diskpart_command(f"create partition primary size={size} disk={disk_number}")

def add_mirror(disk_number, mirror_disk_number):
    run_diskpart_command(f"add disk={disk_number} mirror disk={mirror_disk_number}")

def assign_drive_letter(volume, letter):
    run_diskpart_command(f"assign letter={letter} {volume}")

def format_volume(volume, filesystem="NTFS", label=""):
    run_diskpart_command(f"format fs={filesystem} label={label} {volume}")

def create_volume(size, filesystem="NTFS", label=""):
    run_diskpart_command(f"create volume simple size={size} fs={filesystem} label={label}")

def main():
    while True:
        print("\nDiskpart-like Commands:")
        print("  list disk                                          - List available disks")
        print("  select disk [number]                               - Select a disk by number")
        print("  display specs [volume]                             - Display specifications of the selected volume")
        print("  allocate [size] [disk_number]                      - Allocate a new partition on the selected disk")
        print("  add mirror [disk_number] [mirror_disk_number]      - Add a mirror to a simple volume")
        print("  assign letter [volume] [letter]                    - Assign a drive letter or mount point to the selected volume")
        print("  format [volume] [filesystem] [label]               - Format the volume or partition")
        print("  create volume [size] [filesystem] [label]          - Create a new volume")
        print("  exit                              - Exit DPv1.0")

        command = input("\nEnter a command: ").strip()

        if command.lower() == 'exit':
            break
        elif command.lower() == 'list disk':
            list_disks()
        elif command.lower().startswith('select disk'):
            _, disk_number = command.split(' ')
            select_disk(disk_number)
        elif command.lower().startswith('display specs'):
            _, volume = command.split(' ')
            display_drive_specs(volume)
        elif command.lower().startswith('allocate'):
            _, size, disk_number = command.split(' ')
            allocate_partition(size, disk_number)
        elif command.lower().startswith('add mirror'):
            _, disk_number, mirror_disk_number = command.split(' ')
            add_mirror(disk_number, mirror_disk_number)
        elif command.lower().startswith('assign letter'):
            _, volume, letter = command.split(' ')
            assign_drive_letter(volume, letter)
        elif command.lower().startswith('format'):
            _, volume, filesystem, label = command.split(' ')
            format_volume(volume, filesystem, label)
        elif command.lower().startswith('create volume'):
            _, size, filesystem, label = command.split(' ')
            create_volume(size, filesystem, label)
        else:
            print("Invalid command. Please enter a valid command or 'exit' to quit.")

if __name__ == "__main__":
    main()

