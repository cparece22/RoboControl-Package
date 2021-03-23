#Version Format: Month, Day, Major Version, Minor Version
#indev 10.8.0.1
#Nextup: Fix bugs

#IMPORTS========================================================================
import os
import sys
import time
import socket
import pygame
from pygame.locals import *
import concurrent.futures
import pickle

#FOR EXTENSIVE DIAGNOSTICS------------------------------------------------------
import linecache
import inspect
#-------------------------------------------------------------------------------
#===============================================================================

#VARIABLES======================================================================
e_d = True
server_port = 4242
maximum_clients = 10
clients = []

#FUNCTIONS======================================================================
def init():
    print_ed("Dostuff", get_line(), False)
    print("Interforth Server starting...")
    try:
        server_ip = '192.168.20.' + input("Please enter the last 3 digits of your Ip: ") #socket.gethostbyname(socket.gethostname())
    except:
        print_ed("ERROR! Failed to get host IP or Name", get_line(), True)
        sys.exit()
    try:
        network_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print_ed("Server initializing...", get_line(), False)
        network_socket.bind((server_ip, server_port))
        print_ed("Server IP and Port bound!", get_line(), False)
        network_socket.listen(maximum_clients)
        print("Server initialized, awaiting clients connections at: " + server_ip)
        client_count = 0
        register_connections(network_socket, client_count)
        print("Connection registered!")


    except Exception as error:
        print_ed("ERROR! Failed to create server!", get_line(), True)
        print("Error: " + str(error))
        sys.exit()
    pygame.init()
    return network_socket

def register_connections(ns, connection_count):
    clients.clear()
    connection, connected_address = ns.accept()
    wait_handshake_iterations = 10 #change this to change the number of checks for handshakes
    wait_handshake = wait_handshake_iterations
    while wait_handshake_iterations > 0:
        initial_handshake = connection.recv(4096)
        initial_handshake = initial_handshake.decode()
        if initial_handshake != '':
            wait_handshake_iterations = 0
        else:
            print_ed("No handshake received! " + str((wait_handshake + 1) - wait_handshake_iterations) + "/" + str(wait_handshake), get_line(), False)
            wait_handshake_iterations -= 1
            if wait_handshake_iterations == 0:
                print_ed("CRITICAL ERROR! No handshake received from clients!", get_line(), True)
    clients.append({"ID": connection_count, "Type": initial_handshake, "Address": connected_address, "Connection": connection})
    print_ed("clients Connected: " + str(clients[connection_count]), get_line(), False)

def check_and_input(input_int): #Changes inputs to integers
    try:
        return int(input_int)
    except ValueError:
        printED("Invalid Int detected!", get_line(), False)
        return(-1)

#EXTENSIVE DIAGNOSTICS----------------------------------------------------------
#Print statement
def print_ed(text, line, critical):
    if critical or e_d:
        print("ED | " + str(line) + " | " + str(text))

#Gets current line of code
def get_line():
    return inspect.currentframe().f_back.f_lineno
#-------------------------------------------------------------------------------
def numcounter():
	import random
	op = random.randint(0, 255)
	return op
#===============================================================================

#MAIN===========================================================================
if __name__ == '__main__':
    ns = init()
    x = 0
    running = True
    if clients[0]["Type"] == "motor_client":
        background_colour = (255,255,255)
        (width, height) = (500, 500)
        screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption('Motor clients Controls')
        screen.fill(background_colour)
        pygame.display.flip()
        print("Pygame Window Opened")
        while running:
            try:
                if x >= 7500:
                    x = 0
                    clients[0]["Connection"].sendall(b'None')
                    print("ping sent")
                else:
                    x += 1
                    #maybe put the for loop inside this? not sure...
                for event in pygame.event.get():
                    data = " "
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_w:
                            clients[0]["Connection"].send(b'w')
                        elif event.key == pygame.K_s:
                            clients[0]["Connection"].send(b's')
                        elif event.key == pygame.K_a:
                            clients[0]["Connection"].send(b'a')
                        elif event.key == pygame.K_d:
                            clients[0]["Connection"].send(b'd')
                        elif event.key == pygame.K_q:
                            clients[0]["Connection"].send(b'esc')
                            clients[0]["Connection"].close()
                            print("Closing successfully")
                            running = False
                            pygame.quit()
                            sys.exit()
                    elif event.type == pygame.KEYUP:
                            clients[0]["Connection"].send(b'0')
                    elif event.type == pygame.QUIT:
                        clients[0]["Connection"].send(b'esc')
                        clients[0]["Connection"].close()
                        print("Closing successfully")
                        running = False
                        pygame.quit()
                        sys.exit()
            except socket.error:
                recon = input("Connection Lost, attempt reconnect now? (Y/N)")
                if recon == 'Y':
                    clients[0]["Connection"].close()
                    register_connections(ns,0)
                elif recon == 'N':
                    clients[0]["Connection"].close()
                    print("Closing successfully")
                    running = False
                    pygame.quit()
                    sys.exit()
    else:
        print("Error, clients type not recognized")
# in Handler have it make sure the socket doesnt disconnect, and kill if it does, and here, iterate over all of the clients, and if it finds one closed, reconnect?
#===============================================================================
