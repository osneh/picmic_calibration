
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import socket
import os
import time,collections,os, platform , pathlib
import argparse
import sys
VREFN_TH = 45

def read_ppreg(row,col):

    msg="#1 LOAD_PICMIC_I2C_REG -add 61 -val {}\n".format(row)
    s.send(msg)
    data = s.recv(1024)
    msg="#1 LOAD_PICMIC_I2C_REG -add 62 -val {}\n".format(col)
    s.send(msg)
    data = s.recv(1024)
    msg="#1 READ_PICMIC_I2C_REG -add 63 ?\n"
    s.send(msg)
    data = s.recv(1024)
    response = data.decode('utf-8').strip()   
    ppreg = response.split('=')[-1].strip()     
    print('----->> Used PPREG value '+str(ppreg)+ ' ~~ for ['+str(row)+','+str(col)+'] <<------' )
    return ppreg

def set_ppreg(row,col,new_ppreg):
    
    msg="#1 LOAD_PICMIC_I2C_REG -add 61 -val {}\n".format(row)
    s.send(msg)
    data = s.recv(1024)
    msg="#1 LOAD_PICMIC_I2C_REG -add 62 -val {}\n".format(col)
    s.send(msg)
    data = s.recv(1024)
    msg="#1 LOAD_PICMIC_I2C_REG -add 63 -val {}\n".format(new_ppreg)
    s.send(msg)
    data = s.recv(1024)
    response = data.decode('utf-8').strip()   
    ppreg = response.split('=')[-1].strip()     
    print('----->> Set new PPREG value '+str(ppreg)+ ' ~~ for ['+str(row)+','+str(col)+'] <<------' )


# Fonction pour etablir une connexion TCP avec un serveur.
# ----------------------------------------------------------
def connect_to_server(server, port, vrefn, dirname="K:\\RUNDATA\\TCPdata"):
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
            command_number = 4

            # Fonction interne pour verifier si la reponse du serveur correspond a l'accuse de reception attendu.
            def check_acknowledgement(command_desc, expected_ack, data):
                # Decodage de la reponse du serveur et affichage pour debogage.
                actual_data = data.decode('utf-8').strip()
                #print(f"DEBUG: Response received for {command_desc}: '{actual_data}'")
                # Verification que la reponse contient l'accuse de reception attendu.
                if expected_ack not in actual_data:
                    raise Exception(f"Acknowledgment expected '{expected_ack}' NOT RECEIVED.")

            # Liste des commandes a envoyer au serveur avec leur description et l'accuse attendu.
            formated_string = f"#3 LOAD_PICMIC_I2C_REG -add 39 -val {vrefn} \n"
            byte_string=formated_string.encode('utf-8')
            commands = [
                ##(b"#1 LOAD_SETUP -FROM .\\Setup\\Setup_08Jul24_V3521.dat\n", "LOAD_SETUP", "#1 LOAD_SETUP #EXECUTED OK"),
                (b"#1 LOAD_SETUP -FROM .\\Setup\\Setup_26Jun24_V3520.dat\n", "LOAD_SETUP", "#1 LOAD_SETUP #EXECUTED OK"),
                (b"#2 LOAD_PICMIC_CONFIG_FILE -FROM .\\PICMIC_ConfigFiles\\picmic_cfg_all_columns_row3.txt \n", "Chargement du fichier de configuration PICMIC", "#2 LOAD_PICMIC_CONFIG_FILE #EXECUTED OK"),
                ##(b"#2 LOAD_PICMIC_CONFIG_FILE -FROM .\\PICMIC_ConfigFiles\\TEST2NN.txt \n", "Chargement du fichier de configuration PICMIC", "#2 LOAD_PICMIC_CONFIG_FILE #EXECUTED OK"),
                (byte_string, "LOAD_PICMIC_I2C_REG", "#3 LOAD_PICMIC_I2C_REG #EXECUTED OK"),
            ]

            # Envoi de chaque commande et attente/controle de l'accuse de reception.
            for cmd, desc, ack in commands:
                print(cmd)
                client.sendall(cmd)
                data = client.recv(1024)
                check_acknowledgement(desc, ack, data)
            
            line3 = 'LOAD_PICMIC_I2C_REG -add 38 -val '
            line4 = 'START_RUN -TIME 1 -SAVETO '
            
            directory = dirname
            
            os.makedirs(directory, exist_ok=True)

            # Boucle pour la creation des dossiers specifiques a chaque operation et envoi des commandes correspondantes pour une boucle en VrefN. 
            xlimit = [5,VREFN_TH-4]
            loop_dir = 1

            if ( vrefn-VREFN_TH > 0 ) :
                xlimit = [65,VREFN_TH+3]
                loop_dir = -1
            
            sweeping_flag = True

            while sweeping_flag :

                # for vrefp in range(xlimit[0],xlimit[1],loop_dir):
                ##for vrefp in range(40,61):
                for vrefp in range(50,52):
                    folder_name = f"run_vrefn{vrefn}_vrefp{vrefp}"
                    # folder_path = os.path.join(directory, folder_name)
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

                    current_command = f"#{command_number} {line3}{vrefp}\n"
                    client.sendall(current_command.encode('utf-8'))
                    try:
                        timeout=client.gettimeout()
                        client.settimeout(10.0)
                        data = client.recv(1024)
                        client.settimeout(timeout)
                        check_acknowledgement(f"{line3}{vrefp}", f"#{command_number} LOAD_PICMIC_I2C_REG #EXECUTED OK", data)
                    except socket.timeout:
                        print('TIMEOUT')
                        
                    command_number += 1

                    current_command = f"#{command_number} {line4}{folder_path}\n"
                    client.sendall(current_command.encode('utf-8'))
                    data = client.recv(1024)
                    check_acknowledgement(f"{line4}{folder_path}", f"#{command_number} START_RUN #EXECUTED OK", data)
                    #time.sleep(1)
                    #client.sendall(current_command.encode('utf-8'))
                    data = client.recv(1024)
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
                        #print(f"DEBUG: Reponse ignoree pour la commande #{command_number}")
                        client.recv(1024)
                        skip_next_response = False

                # Envoi de la commande pour arrêter les scripts sur le serveur.
                client.sendall(b"#{command_number} STOP_SCRIPT\n")
                #print(f"Commande envoyee #{command_number}: STOP_SCRIPT")

                # ########################################################## #
                #                data processing and analysis                #
                # ########################################################## #

                ## process data from binary to ascii
                os.system("/home/ilc/habreu/data_bin2ascii/readDataPicmic_bin2ascii_STANDARDBREAK_VREFP.py -f /group/picmic/RUNDATA/TCPdata/run_vrefn*_vrefp*/sampic_tcp_ru*/picmic_dat*/picmic_*.bin")

                ## merge decoded data
                os.system("python /home/ilc/habreu/data_bin2ascii/merger.py -f /group/picmic/RUNDATA/TCPdata/*txt")

                ## Sweeping --> count the pixels and change their PPReg value

                sweeping_flag = False
            # --- Henso Here
            exit()


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
    parser.add_argument("-vrefn", "--vrefn_val" ,help="provide the current vrefn value")
    parser.add_argument("-dirname", "--dir_name" ,help="provide the output directory value")
    ##parser.add_argument("-sweeping","--RL",help="Sweeping Right(1) or Left(0)", action=argparse.BooleanOptionalAction, default=True)
    args = parser.parse_args()

    host = str(args.host_ip).strip()
    port = int(args.port_number)
    ival = int(args.vrefn_val)
    this_dirname = str(args.dir_name).strip()

    if ( (str(args.host_ip)=='None') & (str(args.port_number)=='None') ) :
        print("----------------------- >>>>>>>>>>>>>>>> Host && PortNumber-- Mandatory   <<<<<<<<<<<<<<<<<<<-------------------------")
        print('Script not executed')
        exit()

    print('host=',host,',port=',port, ',vrefn=',ival, ',dir_name=',this_dirname)

    connect_to_server(host, port, ival,this_dirname)

    print('----- DONE ----------')
    exit()

# ################################################################################ #
if __name__ == "__main__":
    main()