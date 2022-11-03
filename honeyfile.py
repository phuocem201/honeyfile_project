import psutil, os, subprocess

def list_dir_sand_link(dir, path):
    for file in os.listdir(dir):
        d = os.path.join(dir, file)
        if os.path.isdir(d):
            #print(d)
            # os.popen(" rm -rf " + d + "/raifile.txt")
            os.popen("ln -s '" + path + "' '" +   d + "/pass.txt'")
            list_dir_sand_link(d, path)
            
def delete_link(dir, path):
    for file in os.listdir(dir):
        d = os.path.join(dir, file)
        if os.path.isdir(d):
            #print(d)
            os.popen("sudo rm -rf " + d + "/pass.txt")
            delete_link(d, path)

tmp = open("/home/kali/Desktop/tmp.txt","w")
path = "/home/kali/Password.txt"
dir = '/home/kali/'

print("Creating Pipe ...")
os.mkfifo(path)

list_dir_sand_link(dir, path)

pid = psutil.Process().pid
print(str(pid))
whitelist = []
whitelist.append(str(pid))
blacklist = []
while True:
    print(whitelist)
    print(blacklist)
    print("Waiting...")
    f = open(path, "w")
    p = os.popen("sudo lsof | grep Password.txt ").readlines()
    for i in p:
        text = i.split()
        if (int(text[1]) == pid):
            continue
        elif(blacklist.count(text[0]) > 0):
            kill = psutil.Process(int(text[1]))
        elif(whitelist.count(text[1]) <= 0):
            print(i)
            print("Do you want kill process? [y/n]")
            z = input()
            if (z == "y"):
                blacklist.append(text[0])
                kill = psutil.Process(int(text[1]))
                kill.kill()
            elif(z == "n"):
                pid = text[1]
                whitelist.append(pid)
   
    print("Do you want to continue? [y/n]")
    s = input()
    if (s == "n"):
        f.close()
        delete_link(dir, path)
        print("Delete link....")
        os.system("sudo rm -rf " + path)
        print("Delete fifo....")
        print("End..")
        break