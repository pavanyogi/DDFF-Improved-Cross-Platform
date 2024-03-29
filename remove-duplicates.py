#!/usr/bin/python3
#-*- coding: utf-8 -*-

# from os import path
import os, shutil, re
from colorama import Fore, Back, Style, init
import sys


# Initialize colorama
init()

if os.name == 'nt':  # Windows
    LINE_SEPERATOR = '\n'
else:
    LINE_SEPERATOR = os.linesep  # fallback to default line separator
print ('LINE_SEPERATOR', LINE_SEPERATOR)

def remove(path):
    """ param <path> could either be relative or absolute. """
    if os.path.isfile(path) or os.path.islink(path):
        os.remove(path)  # remove the file
    elif os.path.isdir(path):
        shutil.rmtree(path)  # remove dir and all contains
    else:
        raise ValueError("file {} is not a file or dir.".format(path))
    print('remove done')


if __name__ == "__main__":
    # Open a file: f1
    # f1 = open(r'test.txt',mode='r')
    # f1 = open(r'ddff-wip.txt',mode='r')
    f1 = open(r'ddff.txt', mode='r', encoding='utf-8')
     
    # read all lines at once
    file_content = f1.read()
     
    # close the file
    f1.close()

    # print('file_content', file_content)

    # item_list = file_content.split('\n\n')
    #item_list = file_content.split(LINE_SEPERATOR+LINE_SEPERATOR)
    if os.name == 'posix':  # Linux/Unix/MacOS
        item_list = file_content.split(LINE_SEPERATOR+LINE_SEPERATOR)
    elif os.name == 'nt':  # Windows
        # Join the list into a single string
        list_text = ''.join(file_content)
        item_list = re.split(r'\n\s*\n', list_text)

    # print('item_list', item_list)
    
    lines_to_skip = 0
    
    line_skip_count = 0
    item_list_skip_count = 0
    
    # Get the number of lines to skip from the command line argument
    if len(sys.argv) > 1 and sys.argv[1].isdigit():
        lines_to_skip = int(sys.argv[1])
    
    for item in item_list:
        #print(item)
        #print()
        # item_lines = item.split('\n')
        item_lines = item.split(LINE_SEPERATOR)
        #print('len(item_lines)', len(item_lines))
        
        if lines_to_skip > 0 and line_skip_count < lines_to_skip:
            line_skip_count += len(item_lines)
            
            # add 1 due to one blank line in between
            line_skip_count += 1
            item_list_skip_count += 1
            
    print('item_list_skip_count', item_list_skip_count)

    item_list_skip_count -= 2 
    if item_list_skip_count > 0:
        item_list = item_list[item_list_skip_count:]

    for item in item_list:
        # print(item)
        # print()
        # item_lines = item.split('\n')
        item_lines = item.split(LINE_SEPERATOR)
        # print('len(item_lines)', len(item_lines))
        tmp_list = []
        for line in item_lines:
            # print(line)
            if os.path.exists(line):
                # print(line)
                tmp_list.append(line)
            elif line.startswith('*'):
                # print(line)
                tmp_list.append(line)
        # print('len(tmp_list)', len(tmp_list))
        # print()
        your_input = -1
        if len(tmp_list) > 2:
            tmp_list2 = []
            for k in tmp_list:
                if tmp_list.index(k) != 0:
                    print(Fore.GREEN + str(tmp_list.index(k)), Fore.GREEN + str(k))
                else:
                    print(k)
                tmp_list2.append(tmp_list.index(k))
            user_input = input(Fore.RED + "keep index: ")
            print()
            if user_input.isdigit():
                user_input = int(user_input)
            if user_input != 0 and user_input in tmp_list2:
                your_input = user_input
            if your_input != -1:
                for l in tmp_list:
                    if tmp_list.index(l) != your_input and tmp_list.index(l) != 0:
                        print(Fore.RED + 'delete', Fore.RED + str(tmp_list.index(l)),  str(l))
                        if os.path.exists(l):
                            remove(l)
                    elif tmp_list.index(l) == 0:
                        print(Fore.GREEN + str(l))
                    else:
                        print(Fore.GREEN + 'keep', Fore.GREEN + str(tmp_list.index(l)), Fore.GREEN + str(l))
                print()
            input()
        
