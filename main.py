# -*- coding: utf-8 -*-

import subprocess
from colorama import Fore,init
import zipfile
import sys

# intiziling colors
init()

# color list
colors = {
    "YELLOW":Fore.YELLOW,
    "GREEN":Fore.GREEN,
    "CYAN":Fore.CYAN,
    "MAGENTA":Fore.MAGENTA,
    "WHITE":Fore.WHITE,
    "RED":Fore.RED,
    "BLUE":Fore.BLUE,
}

def success_message(message):
    temp = ""
    temp += colors['CYAN']
    temp += '['
    temp += colors['WHITE']
    temp += '+'
    temp += colors['CYAN']
    temp += ']'
    temp += ' '
    temp += colors['GREEN']
    temp += message
    temp += colors['WHITE']
    
    print(temp)
    
def error_message(message):
    temp = ""
    temp += colors['RED']
    temp += '['
    temp += colors['WHITE']
    temp += '-'
    temp += colors['RED']
    temp += ']'
    temp += ' '
    temp += colors['YELLOW']
    temp += message
    temp += colors['WHITE']
    
    print(temp)

def info_message(message):
    temp = ""
    temp += colors['YELLOW']
    temp += '['
    temp += colors['WHITE']
    temp += '!'
    temp += colors['YELLOW']
    temp += ']'
    temp += ' '
    temp += colors['YELLOW']
    temp += message
    temp += colors['WHITE']
    
    print(temp)
    

def banner():
    author = "author: black dino"
    temp = f""" {colors['RED']}

                                                                                                                        
                                        ▓▓▒▒                                                                              
                                    ██▒▒  ▒▒██                                    
                                  ██▒▒▒▒  ▒▒▒▒██                                  
                                ██▒▒▒▒▒▒  ▒▒▒▒▒▒██                                
                            ████▒▒▒▒▒▒▒▒  ▒▒▒▒▒▒▒▒████                            
                          ██▒▒▒▒▒▒▒▒████  ████▒▒▒▒▒▒▒▒██                          
                        ██▒▒▒▒▒▒▒▒██▒▒▒▒  ▒▒▒▒██▒▒▒▒▒▒▒▒██                        
                      ██▒▒▒▒▒▒▒▒██████      ██████▒▒▒▒▒▒▒▒██                      
                      ██▒▒▒▒▒▒██▒▒▒▒▒▒██  ██▒▒▒▒▒▒██▒▒▒▒▒▒██                      
                        ██████▒▒▒▒▒▒▒▒██▒▒██▒▒▒▒▒▒▒▒██████                        
                            ██▒▒▒▒▒▒██▒▒▒▒▒▒██▒▒▒▒▒▒██                            
                          ██▒▒▒▒▒▒██▒▒▒▒▒▒▒▒▒▒██▒▒▒▒▒▒██                          
                          ██▒▒▒▒██▒▒▒▒▒▒██▒▒▒▒▒▒██▒▒▒▒██                          
                            ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██                            
                              ████▒▒▒▒██████▒▒▒▒████                              
                                  ████▒▒▒▒▒▒████                                  
                                ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒██                                
                              ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██                              
                            ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██                            
                            ██▒▒▒▒████▒▒▒▒▒▒████▒▒▒▒██                            
                            ██▒▒██    ██▒▒██    ██▒▒██                            
                            ██▒▒██  ██▒▒▒▒▒▒██  ██▒▒██                            
                            ██▒▒████▒▒▒▒▒▒▒▒▒▒████▒▒██                            
                            ██▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒▒██▒▒██                            
                            ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██                            
                            ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██                            
                              ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██                              
                                ████▒▒▒▒▒▒▒▒▒▒████                                
{colors['WHITE']}
----------------------------------------------------------------------------------------------
                        {colors['YELLOW']}+------------------------------+
                        +     {author}       +
                        +------------------------------+
{colors['WHITE']}----------------------------------------------------------------------------------------------
--hide    (hide file) usage: <png_file> <ziped_file> <new_file_name>
--unhide  (extract file) usage: <file_name>
--show    (show hide file) usage: <file_name>
                            

    """
    print(temp.encode('utf-8').decode('utf-8'),end='')

def hide_file(file_name,ziped_file,new_file_name):
    embed_file = f'{file_name}+{ziped_file}'
    subprocess.call(f'copy /b {embed_file} {new_file_name}', shell=True,stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    info_message(f'embed file: {new_file_name}')
    success_message('successfuly hide file...')
    
    
def extract_file(file_name):
    with zipfile.ZipFile(file_name,'r') as zip:
        zip.extractall()
    
    success_message('Successfully extracted file...')


def show_hiden_file(file_name):
    info_message('Hidden Files...')
    with zipfile.ZipFile(file_name,'r') as zip:
        zip.printdir()

def main():
    arguments = sys.argv[1:] # show after python main.py

    if len(arguments) == 0:
        banner()

    if '--hide' in arguments:
        arg_index = arguments.index('--hide')
        file_name = arguments[arg_index + 1]
        ziped_file = arguments[arg_index + 2]
        new_file_name = arguments[arg_index + 3]
        hide_file(file_name,ziped_file,new_file_name)

    if '--extract' in arguments:
        arg_index = arguments.index('--extract')
        file_name = arguments[arg_index + 1]
        extract_file(file_name)
        

    if '--show' in arguments:
        arg_index = arguments.index('--show')
        file_name = arguments[arg_index + 1]
        show_hiden_file(file_name)


if __name__ == '__main__':
    main()
