
import os
import subprocess
import readline
import sys
from contextlib import redirect_stdout



#def __init__(self, cmd_output,dir= 'blank', dev='blank'):
#    if dir is 'blank':
#        print("Directory is blank")
#        self.dir=get_dir()
#    
#    if dev is 'blank':
#        print("Device is blank")
#        self.dev=self.get_dev()
#
#    if cmd_output is None:
#        print("Need cmd")
#
total_list= ['']
file_list= ['']
directory_list= ['']


def get_dir(dir_path):
    if dir_path is None:
        return input("Please enter the directory: ")
    else:
        return dir_path

def get_dev(dev_path):
    if dir_path is None:
        return input("Please enter the device: ")
    else:
        return dev_path

def list_directories(input):
    # make a list out of the input from running the ntfsls command
    #print(input)

    with open('out.log', 'w') as file:
        with redirect_stdout(file):
            print(input) 

    with open('out.log', 'r') as file:
        list = [line.rstrip('\n') for line in file]   
        
    #print(list)
   # 
    return list
    


def print_out_list(input_list):
    for line in input_list:
        print( str(input_list.index(line)) + " : " + line )

def get_file_path():
    return input("Enter the directory for the NTFS drive : ")

def select_option(input_list):
    print_out_list(input_list)
    cur_list = input_list
    option = input("Select your option: ")
    
    if option == 'back':
        return option

    if option == 'grab_all':
        return option 
    if option == 'grab_all_quiet':
        return option
        
    else:     
         try:
             return input_list[int(option)] 
         except Exception as e:
             print("Something happened %s /n Selection an option again: " % str(e))
             select_option(input_list)

def file_or_directory_curdir(input, f_list, d_list):
    
    for item in input:
        if '"' in item:
            input.remove(item)
        elif '.' in item:
            #print(item + " is a file")
            f_list.append(item)
            
        elif '.' not in item: 
            #print(item + " is a directory")
            d_list.append(item)
            
        else:
            print("Cannot determine if its a file or directory")

    return f_list, d_list, input

def run_ls(dev,path=''):   
    output = subprocess.getoutput("sudo ntfsls -f %s -p '%s'" % (dev, path))
    return output

def grab_file(file_path, file_name, device_path, auto_yes = 'no'):
    if auto_yes =='yes':
        print("Grabbing %s...." % file_path)
        subprocess.getoutput("sudo ntfscat -f %s %s | dd of='%s' " % (device_path, file_path, file_name))
 
    else: 
        response = input("""Do you want me to grab : """ + file_path + "[yes/no]? ")
        if response == 'yes' or response == 'y':
            print("Grabbing file.......")
            subprocess.getoutput("sudo ntfscat -f %s %s | dd of='%s' " % (device_path, file_path, file_name))

        else:
            print("Restarting.....")

def if_a_file(object):
    if "." in object:
        return True
    else:
        return False

def grab_all_file(input_list, device_path, directory_path , auto_yes = 'no'):
       
    for item in input_list:
        target = ("  '%s/%s'  " % (directory_path , item))
        grab_file(target,item,device_path, 'yes')

  

def run_main(device_path="", directory_path="" , last_directory="/"):

    stop = False


    while stop == False:
    
        total_list= ['']
        file_list= ['']
        directory_list= ['']
        
        current_selection = ''
        
        print(device_path)
        print(directory_path)
        print(last_directory)    
        raw_output = run_ls(device_path,directory_path)
        
        total_list =list_directories(raw_output)
     
        file_or_directory_curdir(total_list, file_list, directory_list) 
        
        #print(file_list)
    
        print("****")
        #print(directory_list)
    
        print("****")
        print("****")
        print("****")
           
        #print_out_list(total_list)
        selection_name = select_option(total_list)
        print("*******/n/n******")
        
        if selection_name == 'back':
            directory_path = last_directory
            run_main(device_path, directory_path)
        
        for item in file_list:
            if ' ' in item:
                file_list.remove(item)
            else:
                print("%s passed file" % item)
        
        result = directory_path+ '/'+ selection_name        
        
        if selection_name == 'grab_all':
            grab_all_file(file_list, device_path, directory_path)
            print("$$$$$$")
            run_main(device_path,directory_path)
        elif selection_name == 'grab_all_quiet':
            print("grabbing all files****!!@@@")
            grab_all_file(file_list, device_path, directory_path, 'yes')
            run_main(device_path, device_path)
            

        if if_a_file(result):
            print("%s is a file" % result)
            grab_file(result, selection_name, device_path)

        else:
            print("%s is a directory" % result)
            ans =  input("Do you want me to open [yes/no/back]? ") 
            if ans == 'yes' or ans =='y':
                last_directory = directory_path
                directory_path = result
                
                run_main(device_path,directory_path)
            elif ans == 'back':
                print("Running again....")
                run_main(device_path,directory_path)
            else:
                print("Unknow option running again...")
                run_main(device_path, directory_path)
                    
                        
        
        quit = input("Continue running [Yes/No]: ")
        if quit == 'no' or quit == 'n':
                stop = True
        else:
            print("Run again.....")
    
if __name__ == "__main__":
    dir = input("Please enter the directory: ")
    if dir is '':
        print("DIR: /Users/Owner/Pictures")
    
    dev = input("Please enter the device (/dev/sda#): ")
    
    if dev is '':
        print("DIR: /dev/sdd4")
        dev = "/dev/sdd4"
    last_directory = "/"
    run_main(dev,dir, last_directory)

