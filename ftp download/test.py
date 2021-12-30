import subprocess , os , logging 
logging.basicConfig(filename="z:/log_tri.log", level=logging.INFO)

get_command=["get","file"]
put_command=["put","file"]
instructput=["freebox","Boubou1208",'cd "Disque 1/Download/to convert"',"lcd F:/convertcache",'put "[KnK] Uma Musume Pretty Derby - 13 VOSTFR [BD 1080p FLAC 5Season 01.1 AAC 2.0].mkv"']
command=["ftp",'-s:"F:/convertcache/uiojsrnfdr.txt"', "mafreebox.freebox.fr"]

dir =os.listdir("//Freebox_Server/disque 1/Download/to convert")

cp_target="C:/convert cache"

handbrake_command = ["C:/Users/benja/OneDrive/Documents/test/HandBrakeCLI.exe", "-v", "--preset-import-file", "F:/convertcache/script265.json", "-i", "path", "-o", "path" ]


def put_ftp(file):
    dir =os.listdir("F:/convertcache/Ready")
    print(file)
    put_command[1]='"'+file+'"'
    instructget=["freebox","Boubou1208",'cd "Disque 1/Download"' , "lcd F:/convertcache/Ready"," ".join(put_command),"quit"]
    instruct="\n".join(instructget)
    #print(instruct)
    f= open("test.txt","w")
    f.write(instruct)
    f.close()
    subprocess.run("F:/convertcache/lauchftp.bat",shell=True)
    

put_ftp("teste.txt")
#print(dir)

for file in dir:
    print(file)
    get_command[1]='"'+file+'"'
    instructget=["freebox","Boubou1208",'cd "Disque 1/Download/to convert"' , "lcd F:/convertcache"," ".join(get_command),"quit"]
    instruct="\n".join(instructget)
    #print(instruct)
    f= open("test.txt","w")
    f.write(instruct)
    f.close()
    subprocess.run("F:/convertcache/lauchftp.bat",shell=True)
    os.remove("//Freebox_Server/disque 1/Download/to convert/"+file)


directory=os.listdir("F:/convertcache")
for file in directory:

    if "mp4" in file or "mkv" in file:
        #shutil.move("z:/Download/to convert/"+file,cp_target+"/"+file)
        handbrake_command[5]="F:/convertcache"+"/"+file
        output_file=file.split(".")
        output_file[-2]=output_file[-2]+"x265"
        output_file=".".join(output_file)
        handbrake_command[7]="F:/convertcache/Ready"+"/"+output_file
        handbrake_command[7]= handbrake_command[7].replace(".mkv",".mp4")
        handbrake_command[7].replace(" "," x265 ",1)
        print(handbrake_command)
        base_command='"'.join(handbrake_command)
        logging.info("ENCODING "+file)
        print(handbrake_command[7])
        subprocess.run(handbrake_command, shell=True)
        logging.info("ENCODE COMPLETE FOR "+file)
        put_ftp(handbrake_command[7])
        os.remove(handbrake_command[7])
        
        
        
        os.remove(handbrake_command[5])




