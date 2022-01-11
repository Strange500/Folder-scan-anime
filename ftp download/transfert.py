import os, uuid,shutil,subprocess

main_dir="C:/Users/benja/Videos/testftp/"
uu="uuid/"
animee="ready/"
command=["ftp",'-s:"F:/convertcache/uiojsrnfdr.txt"', "mafreebox.freebox.fr"]
put_command=["put","file"]




dir=str(uuid.uuid4())
os.makedirs(main_dir+uu,exist_ok=True)
for i in range(len(os.listdir(main_dir+"ready"))):
    os.makedirs(main_dir+uu+dir,exist_ok=True)
    dir=str(uuid.uuid4())

uuidlist=os.listdir(main_dir+uu)
list_to_move=os.listdir(main_dir+animee)

def put_in_dir(file,uuidlist):
    for UUID in uuidlist:
        if len(os.listdir(main_dir+uu+UUID))==0:
            return [main_dir+animee+file,main_dir+uu+UUID]
            #shutil.move(main_dir+animee+file,main_dir+uu+UUID)

def delet_to_do(file,char):
    nb_to_do=0
    for i in range(len(list(file))):
        if list(file)[i]==char:
            nb_to_do=nb_to_do+1

    return nb_to_do        
def sup_char(file,nb_to_do,nb_to_do1):
    file=list(file)
    if "[" in file:
        for i in range(nb_to_do):
            frome=file.index("[")

            to=file.index("]")
            n=to-frome


            for i in range(n+1):
            
                file.pop(frome)
    if "(" in file:
        for i in range(nb_to_do1):
            frome=file.index("(")

            to=file.index(")")
            n=to-frome


            for i in range(n+1):
            
                file.pop(frome)


    if file[0]==" ":
        file[0]=""
    renamed="".join(str(e) for e in file)
    
    
            
    
    return renamed 


def put_ftp(file,depht):
    #dir =os.listdir("F:/convertcache/Ready")
    put_command[1]='"'+file+'"'
    if ".m" in file:
        instructget=["freebox","Boubou1208",'cd "Disque 1/Download"' , "lcd "+"C:/Users/benja/Videos/testftp"," ".join(put_command),"quit"]
        instruct="\n".join(instructget)
        f= open(main_dir+"test.txt","w")
        f.write(instruct)
        f.close()
        print(3)
        subprocess.run(main_dir+"lauchftp.bat",shell=True)
    else:
        print(file)
        n=delet_to_do(file,"[")
        renamed=sup_char(file,n,0)
        print(sup_char(file,n,0))
        print(renamed)
        if "265" in file or "x265" in file or "h265" in file or "HEVC" in file and ".mp4" in file or ".mkv" in file:
            if ".mkv" in file or ".mp4" in file:
                renamed=renamed.split(".m"," ")
                renamed[0]=renamed[0]+" x265"
                renamed=".m".join(renamed)
        print(renamed)
        
        os.rename(file,renamed)
        file=renamed
        
        dir=file.split("/")[-1]
        if depht>1:
            for i in range(2,depht+1):
                dir=file.split("/")[-i]+"/"+dir
                print(dir+"&&&&&&&&&&&&&&&&&&&&&")
        dir=dir
        
        
        
        instructget=["freebox","Boubou1208",'cd "Disque 1/Download"',"mkdir "+'"/Disque 1/Download/'+dir+'"' ,"quit"]
        instruct="\n".join(instructget)
        f= open(main_dir+"test.txt","w")
        f.write(instruct)
        f.close()
        print(2)
        subprocess.run(main_dir+"lauchftp.bat",shell=True)
        dir=dir.replace('"',"")
        for files in os.listdir(file):
            print(file)
            put_command[1]='"'+files+'"'
            print(1)
            print(put_command)
            instructget=["freebox","Boubou1208",'cd "Disque 1/Download/'+dir+'"' ,"lcd "+'"'+file+'"'," ".join(put_command),"quit"]
            instruct="\n".join(instructget)
            f= open(main_dir+"test.txt","w")
            f.write(instruct)
            f.close()
            print(dir)
            subprocess.run(main_dir+"lauchftp.bat",shell=True)
        for files in os.listdir(file):
            
            if ".m" not in files:
                print(file+"/"+files)
                return put_ftp(file+"/"+files,depht+1)
            
    

for anime in list_to_move:

    loc=put_in_dir(anime,uuidlist)
    shutil.move(loc[0],loc[1])


n=0
for dir in os.listdir(main_dir+"uuid"):
    for file in os.listdir(main_dir+"uuid/"+dir):
        renamed=file
        if ".m" in file:
            print(file)
            n=delet_to_do(file,"[")
            renamed=sup_char(file,n,0)
            print(renamed)
            print(main_dir+"uuid/"+dir+"/"+file)
            print(main_dir+"uuid/"+dir+"/"+renamed)
            os.rename(main_dir+"uuid/"+dir+"/"+file,main_dir+"uuid/"+dir+"/"+renamed)
    
        put_ftp(main_dir+"uuid/"+dir+"/"+renamed,1)
        shutil.rmtree(main_dir+"uuid/"+dir)
        n=n+1

for file in os.listdir(main_dir+"ready"):
    shutil.rmtree(main_dir+"Ready"+file)
    print("yey")


n=delet_to_do("[Pikari-Teshima] Karakai Jouzu no Takagi-san 2nd Season - 02 VOSTFR  [BD 1920x1080 x.265 10bit FLAC].mkv","[")
print(sup_char("[Pikari-Teshima] Karakai Jouzu no Takagi-san 2nd Season - 02 VOSTFR  [BD 1920x1080 x.265 10bit FLAC].mkv",n,0))