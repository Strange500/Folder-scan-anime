import subprocess , os , logging, requests ,json,random,time
from datetime import datetime
main_dir=os.getcwd()

print(main_dir)
logging.basicConfig(filename="//Freebox_Server/disque 1/log_tri.txt", level=logging.INFO)
webhook_url="webhook_url"
get_command=["get","file"]
put_command=["put","file"]
instructput=["freebox","Boubou1208",'cd "Disque 1/Download/to convert"',"lcd "+"'"+main_dir+"'",'put "[KnK] Uma Musume Pretty Derby - 13 VOSTFR [BD 1080p FLAC 5Season 01.1 AAC 2.0].mkv"']
command=["ftp",'-s:'+'"'+main_dir+'/uiojsrnfdr.txt"', "mafreebox.freebox.fr"]
begin="On commence l'encodage de "
end="Encodage fini pour "
dir =os.listdir("//Freebox_Server/disque 1/Download/to convert")
list_waifu=[["Yotsuba Nakano","https://www.personality-database.com/profile_images/28026.png"],["Nino Nakano","https://images.genius.com/a079484288d88e56c70fcde49c3acc6c.500x500x1.jpg"],["Ichika Nakano","https://i.pinimg.com/originals/56/72/2b/56722bb5c7ab0277c8f0c19b201dc29d.jpg"],["Zero Two","https://i.redd.it/6ig4g7j355h61.jpg"],["Megumin","https://preview.redd.it/0iu4uzt1d2z41.jpg?auto=webp&s=10f9c7472e8c5bf963d13f3eb90c48f74fd2c8f8"],["Chizuru Ichinose","https://i.pinimg.com/originals/06/27/51/0627515d8bb8282b1c035bbcc8864792.jpg"],["Sumi Sakurasawa","https://www.nautiljon.com/images/perso/00/91/sakurasawa_sumi_19619.jpg"],["Ruka Sarashina","https://www.nautiljon.com/images/perso/00/85/sarashina_ruka_19558.jpg"],["Mami Nanami","https://wallpapercave.com/wp/wp7401783.jpg"],["Rem","https://i.pinimg.com/550x/42/77/93/427793ca16bf894a4101ae0d5bb5f2ad.jpg"],["Kitagawa Marin","https://i.pinimg.com/736x/98/4f/91/984f911b0d1b7a4497f98bf9b97b3cdd.jpg"],["Takagi","https://i.pinimg.com/originals/cf/db/be/cfdbbeca98709675f437b6f8481339a2.jpg"],["Nagatoro","https://i.pinimg.com/564x/97/bc/14/97bc14635c227ce9b4759b89e5c15e88.jpg"],["Douki-chan","https://thicc.mywaifulist.moe/waifus/40029/c79ac7706c5e050842eece4be73183af628da41328c6e6dd167c991ef99ce803_thumb.png"],["Guts","https://www.nautiljon.com/images/manga_persos/00/57/guts_175.jpg"],["Jahy-Sama","https://i.pinimg.com/236x/c7/fe/bf/c7febfbf541d472d13e371e82c3dd87b.jpg"],["Senko san","https://www.nautiljon.com/images/perso/00/34/senko_18443.jpg"],["シエスタ","https://i.pinimg.com/736x/26/d0/3e/26d03e45cfe45e228a3140eeeacc8907.jpg"],["Futaba Igurashi","https://i.pinimg.com/736x/88/cc/e6/88cce6ca3d27ff15cf14db79b104d62f.jpg"]]

###################Creating Directories ########################################

os.makedirs("Ready",exist_ok=True)
os.makedirs("toconvert",exist_ok=True)
cp_target='"'+main_dir+"/toconvert"


#####################Creating bat file ####################################
if "lauchftp.bat" not in os.listdir():
    open("lauchftp.txt","w").write('ftp -s:'+'"'+main_dir+"/"+"test.txt"+'"'+ ' mafreebox.freebox.fr')
    os.rename("lauchftp.txt","lauchftp.bat")


handbrake_command = ["HandBrakeCLI.exe", "-v", "--preset-import-file","script265.json", "-i", "path", "-o", "path" ]
def random_waifu(list_waifu=list_waifu):
    return random.choice(list_waifu)

def put_ftp(file):
    dir =os.listdir(main_dir+"\\Ready")
    put_command[1]='"'+file+'"'
    instructget=["freebox","Boubou1208",'cd "Disque 1/Download"' , "lcd "+"'"+main_dir+"/Ready"+"'"," ".join(put_command),"quit"]
    instruct="\n".join(instructget)
    #print(instruct)
    f= open("test.txt","w")
    f.write(instruct)
    f.close()
    subprocess.run('"'+main_dir+"/lauchftp.bat"+'"',shell=True)
    

def get_ftp(file):
    get_command[1]='"'+file+'"'
    instructget=["freebox","Boubou1208",'cd "Disque 1/Download/to convert"' , "lcd "+'"'+main_dir+"/toconvert"+'"'," ".join(get_command),"quit"]
    instruct="\n".join(instructget)
    #print(instruct)
    f= open("test.txt","w")
    f.write(instruct)
    f.close()
    subprocess.run('"'+main_dir+"/lauchftp.bat"+'"',shell=True)
    os.remove("//Freebox_Server/disque 1/Download/to convert/"+file)


def random_gif(search,lmt):
    apikey = "X90EVGHN8X7Z"  
    r = requests.get("https://g.tenor.com/v1/search?q=%s&key=%s&limit=%s" % (search, apikey, lmt))
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
    if liste==[]:
        return random_gif(search,lmt*2)
    choice=random.choice(liste)
    return choice

def send_webhook_request(webhook_url,statut,file,waifu):
    content=statut+file
    data =  {'name' : 'Directory Seeker',
                'avatar_url': waifu[1],
                'username':waifu[0],
                'content': "@admin",
                'embeds':[{
                    'color':1127128,
                    'footer':{
                        'text':'From Jellyfin',
                        'icon_url':waifu[1],
                        },

                    
                    'title':content,
                    "image":{"url":random_gif(waifu[0],16)}}]
                    


    }




                

    r= requests.post(webhook_url, data=json.dumps(data), headers={'Content-type': 'application/json'})


while True:
    directory=os.listdir(main_dir+"/toconvert")
    
    for file in directory:
       
        if "mp4" in file or "mkv" in file:
            #shutil.move("z:/Download/to convert/"+file,cp_target+"/"+file)
            handbrake_command[5]=main_dir+"/toconvert"+"/"+file
            if "x264" in file:
                orii=file
                output_file=file.replace("x264","x265")
            else:
                output_file=file.split(".")
                output_file[-2]=output_file[-2]+"x265"
                output_file=".".join(output_file)
            handbrake_command[7]=main_dir+"/Ready"+"/"+output_file
            handbrake_command[7]= handbrake_command[7].replace(".mkv",".mp4")
            handbrake_command[7].replace(" "," x265 ",1)
            base_command='"'.join(handbrake_command)
            logging.info("ENCODING "+file)
            send_webhook_request(webhook_url,begin,file,random_waifu())
            print(handbrake_command)
            subprocess.run(handbrake_command, shell=True)
            if len(os.listdir(main_dir+"/Ready"))!=0:
                send_webhook_request(webhook_url,end,file,random_waifu())
                logging.info("ENCODE COMPLETE FOR "+file)
                put_ftp(handbrake_command[7])
                os.remove(handbrake_command[7])
                
                
                
            os.remove(handbrake_command[5])
        

    print(datetime.now().strftime('%H:%M:%S')+": waiting for file")
    while len(os.listdir(main_dir+"/toconvert"))==0:
        dir=os.listdir("//Freebox_Server/disque 1/Download/to convert")
        
        if len(dir)!=0:
            
            get_ftp(dir[0])
            directory.append(dir[0])
        time.sleep(30)
    





