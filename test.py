import psutil, os, subprocess

tmp = open("/home/kali/Desktop/TMP/tmp.txt", "w")
path = "/home/kali/Desktop/TMP/Password.txt"
print("Creating Pipe ...")
os.mkfifo(path)

while True:
    print("Waiting...")
    f = open(path, "w")
    p = os.popen("sudo lsof | grep Password.txt ").readlines()
    for i in p:
        print(i)
        text = i.split()
        print(text[0] + "\t" + text[1])
        tmp.writelines(text[0] + "\t" + text[1] + "\n")
    print("Do you want to continue? [y/n]")
    s = input()
    if s == "n":
        f.close()
        tmp.close()
        os.system("rm -rf " + path)
        print("End..")
        break
