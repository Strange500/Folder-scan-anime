import subprocess , os , logging, requests ,json,random

logging.basicConfig(filename="z:/log_tri.log", level=logging.INFO)
webhook_url="https://discord.com/api/webhooks/927586895247069214/5z7tlhSnLG6qr8KC5KqDDjYLTzbm40gmyqnpawiYN_BV2JoqtjI8fK-BMXnoziFa9Jlj"
get_command=["get","file"]
put_command=["put","file"]
instructput=["freebox","Boubou1208",'cd "Disque 1/Download/to convert"',"lcd F:/convertcache",'put "[KnK] Uma Musume Pretty Derby - 13 VOSTFR [BD 1080p FLAC 5Season 01.1 AAC 2.0].mkv"']
command=["ftp",'-s:"F:/convertcache/uiojsrnfdr.txt"', "mafreebox.freebox.fr"]
begin="On commence l'encodage de "
end="Encodage fini pour "
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


def get_ftp(file):
    get_command[1]='"'+file+'"'
    instructget=["freebox","Boubou1208",'cd "Disque 1/Download/to convert"' , "lcd F:/convertcache"," ".join(get_command),"quit"]
    instruct="\n".join(instructget)
    #print(instruct)
    f= open("test.txt","w")
    f.write(instruct)
    f.close()
    subprocess.run("F:/convertcache/lauchftp.bat",shell=True)
    os.remove("//Freebox_Server/disque 1/Download/to convert/"+file)


def random_gif(search,lmt):
    apikey = "API_KEY_TENOR"  

    r = requests.get(
        "https://g.tenor.com/v1/search?q=%s&key=%s&limit=%s" % (search, apikey, lmt))

    if r.status_code == 200:
        
        top_8gifs = json.loads(r.content)
        
    else:
        top_8gifs = None


    

    liste=[]
    top_8gifs= str(top_8gifs).split(",")
    
    for gif in top_8gifs:
        
        if "{'url':" in gif and "nano" not in gif and "mp4" not in gif and "medium" not in gif and "webm" not in gif and "tiny" not in gif :
            
            
            link="https"+gif.split("https")[1].replace("'","")
            liste.append(link)

    
    choice=random.choice(liste)
    
    return choice

def send_webhook_request(webhook_url,statut,file):
    content=statut+file+" "+random_gif("FINISH",64)
    data =  {'name' : 'Directory Seeker',
                'content': content}

    r= requests.post(webhook_url, data=json.dumps(data), headers={'Content-type': 'application/json'})



directory=os.listdir("F:/convertcache")
for file in directory:

    if "mp4" in file or "mkv" in file:
        
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
        send_webhook_request(webhook_url,begin,file)
        subprocess.run(handbrake_command, shell=True)
        send_webhook_request(webhook_url,end,file)
        logging.info("ENCODE COMPLETE FOR "+file)
        put_ftp(handbrake_command[7])
        os.remove(handbrake_command[7])
        
        
        
        os.remove(handbrake_command[5])
        dir=os.listdir("//Freebox_Server/disque 1/Download/to convert")
        for fil in dir:
            get_ftp(fil)
            directory.append(fil)





