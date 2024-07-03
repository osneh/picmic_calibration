# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import socket
import os
import time,collections,os, platform , pathlib
import argparse
import sys

# Fonction pour etablir une connexion TCP avec un serveur.
'''
def connect_to_server(server, port):
    try:
        # Tentative de connexion au serveur specifie par l adresse et le port.
        print(f"Tentative de connexion au serveur {server}:{port}")
        ##print("Tentative de connexion au serveur " +str(server)+":"+str(port))
        # Creation d'un objet socket avec IPv4 et TCP.
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
            # Connexion effective au serveur
            client.connect((server, port))
            print("Connexion etablie avec le serveur.")
            # Initialisation du numero de commande a 4.
            command_number = 3

            # Fonction interne pour verifier si la reponse du serveur correspond a l'accuse de reception attendu.
            def check_acknowledgement(command_desc, expected_ack, data):
                # Decodage de la reponse du serveur et affichage pour debogage.
                actual_data = data.decode('utf-8').strip()
                print(f"DEBUG: Reponse reçue pour {command_desc}: '{actual_data}'")
                ##print("DEBUG: Reponse reçue pour "+str(command_desc)+ ':'+ str(actual_data))
                # Verification que la reponse contient l'accuse de reception attendu.
                if expected_ack not in actual_data:
                    raise Exception(f"Accuse de reception attendu '{expected_ack}' non reçu.")
                    ##raise Exception("Accuse de reception attendu "+str(expected_ack)+" non reçu.")

            # Liste des commandes a envoyer au serveur avec leur description et l'accuse attendu.
            commands = [
                #(b"#1 ENABLE_DATA_TX_TO_TCP_CLIENT\n", "ENABLE_DATA_TX_TO_TCP_CLIENT", "#1 ENABLE_DATA_TX_TO_TCP_CLIENT #EXECUTED OK"),
                ##(b"#2 LOAD_SETUP -FROM .\\Setup\\Setup_K_24_04.dat \n", "Chargement de la configuration", "#2 LOAD_SETUP #EXECUTED OK"),
                ##(b"#2 LOAD_SETUP -FROM k:\\config\\Setup_06Jun24_V3514.dat\n", "LOAD_SETUP", "#2 LOAD_SETUP #EXECUTED OK"),
                (b"#1 LOAD_SETUP -FROM .\\Setup\\Setup_26Jun24_V3520.dat \n", "LOAD_SETUP", "#1 LOAD_SETUP #EXECUTED OK"),
                ##(b"#3 LOAD_PICMIC_CONFIG_FILE -FROM k:\\config\\myTest.txt\n", "LOAD_PICMIC_CONFIG_FILE", "#3 LOAD_PICMIC_CONFIG_FILE #EXECUTED OK"),
                (b"#2 LOAD_PICMIC_CONFIG_FILE -FROM .\\PICMIC_ConfigFiles\\picmic_cfg_all_columns_row3.txt \n", "Chargement du fichier de configuration PICMIC", "#2 LOAD_PICMIC_CONFIG_FILE #EXECUTED OK"),
                #(b"#3 LOAD_PICMIC_CONFIG_FILE -FROM k:\\config\\picmic_cfg_all_columns_row3.txt\n", "LOAD_PICMIC_CONFIG_FILE", "#3 LOAD_PICMIC_CONFIG_FILE #EXECUTED OK"),
                #(b"#4 LOAD_PICMIC_CONFIG_FILE -FROM k:\\config\\myTest.txt\n", "LOAD_PICMIC_CONFIG_FILE", "#4 LOAD_PICMIC_CONFIG_FILE #EXECUTED OK"),
            ]

            # Envoi de chaque commande et attente/controle de l'accuse de reception.
            for cmd, desc, ack in commands:
                client.sendall(cmd)
                data = client.recv(1024)
                check_acknowledgement(desc, ack, data)
                
            line3 = 'LOAD_PICMIC_I2C_REG -add 39 -val '
            line4 = 'START_RUN -TIME 1 -SAVETO '
            line5 = 'STOP_RUN '
            directory = "K:\\RUNDATA\\TCP_IP5"
            os.makedirs(directory, exist_ok=True)

            #client.sendall(b"#{command_number} LOAD_PICMIC_I2C_REG --add 61 --val \n".encode('utf-8'))

            # Boucle pour la creation des dossiers specifiques a chaque operation et envoi des commandes correspondantes pour une boucle en VrefN. 
            for VrefN in range(50, 66):
                folder_name = f"run{VrefN}"
                ##folder_path = os.path.join(directory, folder_name)
                folder_path = directory +"\\"+ folder_name
                ##os.makedirs(folder_path, exist_ok=True)
                print(f"Repertoire cree avec succes : {folder_path}")

                if (platform.system()=="Linux") :
                    linuxDir='/group/picmic'+pathlib.PureWindowsPath(folder_path).as_posix().strip('K:')
                    os.makedirs(linuxDir, exist_ok=True)
                    os.system("chmod -R g+w "+linuxDir)
                    print(f"Repertoire LINUX cree avec succes : {linuxDir}")
                else:
                    os.makedirs(folder_path, exist_ok=True)
                print(f"Repertoire cree avec succes : {folder_path}")
                time.sleep(0.1)

                current_command = f"#{command_number} {line3}{VrefN}\n"
                client.sendall(current_command.encode('utf-8'))
                try :
                    timeout = client.gettimeout()
                    client.settimeout(10.0)
                    data = client.recv(1024)
                    client.settimeout(timeout)
                    check_acknowledgement(f"{line3}{VrefN}", f"#{command_number} LOAD_PICMIC_I2C_REG #EXECUTED OK", data)
                except socket.timeout:
                    print('TIMEOUT')
                
                command_number += 1

                current_command = f"#{command_number} {line4}{folder_path}\n"
                client.sendall(current_command.encode('utf-8'))
                data = client.recv(1024)
                check_acknowledgement(f"{line4}{folder_path}", f"#{command_number} START_RUN #EXECUTED OK", data)
                skip_next_response = False
                command_number += 1

                if skip_next_response:
                    print(f"DEBUG: Reponse ignoree pour la commande #{command_number}")
                    client.recv(1024)
                    skip_next_response = False

                current_command = f"#{command_number} STOP_RUN\n"
                client.sendall(current_command.encode('utf-8'))

                data = client.recv(1024)
                check_acknowledgement(f"{line5}", f"#{command_number} STOP_RUN #EXECUTED OK", data)
                skip_next_response = True
                command_number += 1

                if skip_next_response:
                    print(f"DEBUG: Reponse ignoree pour la commande #{command_number}")
                    client.recv(1024)
                    skip_next_response = False

            # Envoi de la commande pour arrêter les scripts sur le serveur.
            client.sendall(b"#{command_number} STOP_SCRIPT\n")
            print(f"Commande envoyee #{command_number}: STOP_SCRIPT")

            # Boucle pour la gestion des commandes utilisateur en temps reel.
            while True:
                command = input("Envoyez une commande (tapez 'disconnect' pour sortir) : ")
                if command.lower() == "disconnect":
                    print("Deconnexion...")
                    break

                if command == "":
                    raise ValueError("La commande ne peut pas être nulle ou vide")

                client.sendall(f"#{command_number} {command}\n".encode("utf-8"))
                print(f"Commande envoyee #{command_number}: {command}")
                command_number += 1
                
    except Exception as e:
        print(f"Erreur: {e}")
'''
# ----------------------------------------------------------
def connect_to_server(server, port):
    try:
        # Tentative de connexion au serveur specifie par l adresse et le port.
        print(f"Tentative de connexion au serveur {server}:{port}")
        # Creation d'un objet socket avec IPv4 et TCP.
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
            # Connexion effective au serveur
            client.connect((server, port))
            #client.settimeout(1.0)
            print("Connexion etablie avec le serveur.")
            # Initialisation du numero de commande a 4.
            command_number = 3

            # Fonction interne pour verifier si la reponse du serveur correspond a l'accuse de reception attendu.
            def check_acknowledgement(command_desc, expected_ack, data):
                # Decodage de la reponse du serveur et affichage pour debogage.
                actual_data = data.decode('utf-8').strip()
                print(f"DEBUG: Response received for {command_desc}: '{actual_data}'")
                # Verification que la reponse contient l'accuse de reception attendu.
                if expected_ack not in actual_data:
                    raise Exception(f"Acknowledgment expected '{expected_ack}' NOT RECEIVED.")

            # Liste des commandes a envoyer au serveur avec leur description et l'accuse attendu.
            commands = [
                #(b"#1 ENABLE_DATA_TX_TO_TCP_CLIENT\n", "ENABLE_DATA_TX_TO_TCP_CLIENT", "#1 ENABLE_DATA_TX_TO_TCP_CLIENT #EXECUTED OK"),
                #(b"#2 LOAD_SETUP -FROM .\\Setup\\Setup_K_24_04.dat \n", "Chargement de la configuration", "#2 LOAD_SETUP #EXECUTED OK"),
                (b"#1 LOAD_SETUP -FROM .\\Setup\\Setup_26Jun24_V3520.dat\n", "LOAD_SETUP", "#1 LOAD_SETUP #EXECUTED OK"),
                ##(b"#2 LOAD_SETUP -FROM .\\Setup\\Setup_06Jun24_V3514.dat \n", "LOAD_SETUP", "#2 LOAD_SETUP #EXECUTED OK"),
                ##(b"#3 LOAD_PICMIC_CONFIG_FILE -FROM k:\\config\\myTest.txt\n", "LOAD_PICMIC_CONFIG_FILE", "#3 LOAD_PICMIC_CONFIG_FILE #EXECUTED OK"),
                (b"#2 LOAD_PICMIC_CONFIG_FILE -FROM .\\PICMIC_ConfigFiles\\picmic_cfg_all_columns_row3.txt \n", "Chargement du fichier de configuration PICMIC", "#2 LOAD_PICMIC_CONFIG_FILE #EXECUTED OK"),
                #(b"#3 LOAD_PICMIC_CONFIG_FILE -FROM k:\\config\\picmic_cfg_all_columns_row3.txt\n", "LOAD_PICMIC_CONFIG_FILE", "#3 LOAD_PICMIC_CONFIG_FILE #EXECUTED OK"),
                #(b"#4 LOAD_PICMIC_CONFIG_FILE -FROM k:\\config\\myTest.txt\n", "LOAD_PICMIC_CONFIG_FILE", "#4 LOAD_PICMIC_CONFIG_FILE #EXECUTED OK"),
            ]

            # Envoi de chaque commande et attente/controle de l'accuse de reception.
            for cmd, desc, ack in commands:
                client.sendall(cmd)
                data = client.recv(1024)
                check_acknowledgement(desc, ack, data)
                

            ##print('HELLO 00')
            line3 = 'LOAD_PICMIC_I2C_REG -add 39 -val '
            line4 = 'START_RUN -TIME 1 -SAVETO '
			      ##line5 = 'STOP_RUN '
            ##directory = "C:\\Users\\Karim\\TCP_IP\\04_25_2024"
            directory = "K:\\RUNDATA\\TCP_IP6"
            ##directory = "/group/picmic/RUNDATA"
            # Creation du repertoire racine une fois.
            os.makedirs(directory, exist_ok=True)
            ##print('HELLO 01')
            ##client.sendall(b"#{command_number} LOAD_PICMIC_I2C_REG --add 61 --val \n")
            ##client.sendall(b"#{command_number} LOAD_PICMIC_I2C_REG --add 61 --val \n".encode('utf-8'))

            # Boucle pour la creation des dossiers specifiques a chaque operation et envoi des commandes correspondantes pour une boucle en VrefN. 
            for VrefN in range(50, 66):
                folder_name = f"run{VrefN}"
#                folder_path = os.path.join(directory, folder_name)
                folder_path = directory +"\\" + folder_name
                print(f"Repertoire a creer : {folder_path}")
                if (platform.system()=="Linux") :
                    linuxDir='/group/picmic'+pathlib.PureWindowsPath(folder_path).as_posix().strip('K:')
                    os.makedirs(linuxDir, exist_ok=True)
                    # print(f"chmod -R g+w {linuxDir}")
                    os.system("chmod -R g+w "+linuxDir)
                    print(f"Repertoire LINUX cree avec succes : {linuxDir}")
                else:
                    os.makedirs(folder_path, exist_ok=True)
                print(f"Repertoire cree avec succes : {folder_path}")
                time.sleep(0.1)

                current_command = f"#{command_number} {line3}{VrefN}\n"
                client.sendall(current_command.encode('utf-8'))
                try:
                    timeout=client.gettimeout()
                    client.settimeout(10.0)
                    data = client.recv(1024)
                    client.settimeout(timeout)
                    check_acknowledgement(f"{line3}{VrefN}", f"#{command_number} LOAD_PICMIC_I2C_REG #EXECUTED OK", data)
                except socket.timeout:
                    print('TIMOUTE')
                     
                command_number += 1

                current_command = f"#{command_number} {line4}{folder_path}\n"
                client.sendall(current_command.encode('utf-8'))
                data = client.recv(1024)
                print("ICIC0")
                print(data)
                check_acknowledgement(f"{line4}{folder_path}", f"#{command_number} START_RUN #EXECUTED OK", data)
                #time.sleep(1)
                #client.sendall(current_command.encode('utf-8'))
                data = client.recv(1024)
                print("ICI")
                print(data)
                check_acknowledgement(f"START_RUN", f"#{command_number} RUN_FINISHED", data)
                #time.sleep(1.0)
                #command_number += 1

                #current_command = f"#{command_number} STOP_RUN\n"
                #client.sendall(current_command.encode('utf-8'))
                #data = client.recv(1024)
                #check_acknowledgement(f"STOP_RUN", f"#{command_number} RUN_FINISHED", data)
                skip_next_response = False
                command_number += 1

                if skip_next_response:
                    print(f"DEBUG: Reponse ignoree pour la commande #{command_number}")
                    client.recv(1024)
                    skip_next_response = False

            # Envoi de la commande pour arrêter les scripts sur le serveur.
            client.sendall(b"#{command_number} STOP_SCRIPT\n")
            print(f"Commande envoyee #{command_number}: STOP_SCRIPT")

            # Boucle pour la gestion des commandes utilisateur en temps reel.
            while True:
                command = input("Envoyez une commande (tapez 'disconnect' ou Return (commande vide) pour sortir) : ")
                if command.lower() == "disconnect":
                    print("Deconnexion...")
                    break

                if command == "":
                    raise ValueError("La commande ne peut pas être nulle ou vide")

                client.sendall(f"#{command_number} {command}\n".encode("utf-8"))
                print(f"Commande envoyee #{command_number}: {command}")
                command_number += 1
                
    except Exception as e:
        print(f"Erreur: {e}")

# ################################################################################ #
def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("-host", "--host_ip" ,help="provide the server IP")
    parser.add_argument("-port", "--port_number" ,help="provide the port number")
    ##parser.add_argument("-sweeping","--RL",help="Sweeping Right(1) or Left(0)", action=argparse.BooleanOptionalAction, default=True)
    args = parser.parse_args()

    host = str(args.host_ip).strip()
    port = int(args.port_number)

    if ( (str(args.host_ip)=='None') & (str(args.port_number)=='None') ) :
        print("----------------------- >>>>>>>>>>>>>>>> Host && PortNumber-- Mandatory   <<<<<<<<<<<<<<<<<<<-------------------------")
        print('Script not executed')
        exit()

    host = str(args.host_ip).strip()
    ##host = str('\'')+str(args.host_ip)+str('\'')
    ##print('print host=',host)
    port = int(args.port_number)

    ##host = f'134.158.139.27'

    #port = 8266
    print(type(port))

    print('host=',host,',port=',port)

    

    connect_to_server(host, port)

    print('----- DONE ----------')
    exit()

# ################################################################################ #
if __name__ == "__main__":
    main()
