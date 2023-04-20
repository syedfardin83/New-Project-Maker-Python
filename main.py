import subprocess
import os
from datetime import datetime


global coding_folder_path
home_directory = str(os.getcwd())
print('Home DIR '+home_directory)
coding_folder_path = "C:/Users/DELL/Desktop/Coding"

def open_vscode(path):
    subprocess.Popen(["code.exe",path])

def open_cmd(path):
    os.system(f"start cmd /K cd {path}")

def create_empty_file(path, name):
    os.chdir(path)
    f = open(name, 'w')
    f.close()

def enter_log(lang, path, files_created):
    os.chdir(home_directory)
    if (os.path.exists(home_directory+"\\"+"logs.txt"))==False:
        f = open('logs.txt','w')
        f.close()
    time = datetime.now()

    str = f"\n{time}\n{lang} Project\nProject Path: {path}\nFiles Created: {files_created}"

    f = open('logs.txt','r')
    initial = f.read()
    f.close()

    final = initial+"\n"+str
    f = open('logs.txt','w')
    f.write(final)
    f.close()

def create_python():
    files_created = []
    print("Enter project name:")
    project_name = str(input('> '))

    path = coding_folder_path+"/Python"
    os.chdir(path)
    os.mkdir(project_name)

    path = path+"/"+project_name
    os.chdir(path)

    create_empty_file(path, 'main.py')
    files_created.append("main.py")

    path = coding_folder_path+"/Python"+"/"+project_name
    open_cmd(path)
    open_vscode(path)

    print('\nSuccessfully created Python project '+path)
    print('Check logs.txt for more info.')
    enter_log("Python", path, files_created)

def create_HTML():
    print("Select the format: ")
    print("\t1. only HTML file")
    print("\t2. HTML + JavaScript file")
    print("\t3. HTML + JavaScript + CSS file")
    selected_format = str(input('> '))

    files_created = []
    if int(selected_format) == 1: files_created = ["index.html"]
    elif int(selected_format) == 2: files_created = ["index.html","script.js"]
    elif int(selected_format) == 3: files_created = ["index.html","script.js","style.css"]
    else:
        print('Invalid input, try again.')
        create_HTML()
    
    print("Enter project name: ")
    project_name = str(input('> '))

    path = coding_folder_path+"/Web development"
    os.chdir(path)
    os.mkdir(project_name)

    path = path+"/"+project_name
    os.chdir(path)

    for file in files_created:
        create_empty_file(path, file)

    open_cmd(path)

    open_vscode(path)

    print('\nSuccessfully created Python project '+path)
    print('Check logs.txt for more info.')
    enter_log("HTML",path, files_created)

    

list_of_languages = {
    "1":"HTML",
    "2":"Python",
    "3":"Java",
    "4":"MERN"
}

list_of_languages = [["1","HTML"],["2","Python"],["3","Java"],["4","MERN"]]

print('Which language project do you want to create?')
print('Enter a number from the below list: ')
for a in list_of_languages:
    print("\t"+a[0]+". "+a[1])

language_choice_number = int(input('> '))
selected_language = -1
for a in list_of_languages:
    if a[0] == str(language_choice_number): selected_language = a[1]

# print("Selected Language: "+str(selected_language)) Works

if selected_language == "Python" : create_python()
if selected_language == "HTML" : create_HTML()
else: print('This language is still under development!')