#! /usr/bin/python
import os, logging, json, requests, random,time

is265=False
logging.basicConfig(filename="/mnt/Disque-1/log_tri.log", level=logging.INFO)
no265='/mnt/Disque-1/Download/to convert/'
#readd=open("/mnt/Disque-1/Download/listeanime.txt","r")
#listeanime= readd.read()
#readd.close()
#listeanime=listeanime.split("%")

dir_list = os.listdir("/mnt/Disque-1/Download")
dir_list_of_anime="/mnt/Disque-1/JellyFin/Anime/Airing"
listeanime=os.listdir(dir_list_of_anime)
print(listeanime)
splited_dir_list=[]
dl_dir="/mnt/Disque-1/Download/"
target_dir=dir_list_of_anime
target_dir_list=os.listdir(dir_list_of_anime)
list_waifu=[["Yotsuba Nakano","https://www.personality-database.com/profile_images/28026.png"],["Nino Nakano","https://images.genius.com/a079484288d88e56c70fcde49c3acc6c.500x500x1.jpg"],["Ichika Nakano","https://i.pinimg.com/originals/56/72/2b/56722bb5c7ab0277c8f0c19b201dc29d.jpg"],["Zero Two","https://i.redd.it/6ig4g7j355h61.jpg"],["Megumin","https://preview.redd.it/0iu4uzt1d2z41.jpg?auto=webp&s=10f9c7472e8c5bf963d13f3eb90c48f74fd2c8f8"],["Chizuru Ichinose","https://i.pinimg.com/originals/06/27/51/0627515d8bb8282b1c035bbcc8864792.jpg"],["Sumi Sakurasawa","https://www.nautiljon.com/images/perso/00/91/sakurasawa_sumi_19619.jpg"],["Ruka Sarashina","https://www.nautiljon.com/images/perso/00/85/sarashina_ruka_19558.jpg"],["Mami Nanami","https://wallpapercave.com/wp/wp7401783.jpg"],["Rem","https://i.pinimg.com/550x/42/77/93/427793ca16bf894a4101ae0d5bb5f2ad.jpg"],["Kitagawa Marin","https://i.pinimg.com/736x/98/4f/91/984f911b0d1b7a4497f98bf9b97b3cdd.jpg"],["Takagi","https://i.pinimg.com/originals/cf/db/be/cfdbbeca98709675f437b6f8481339a2.jpg"],["Nagatoro","https://i.pinimg.com/564x/97/bc/14/97bc14635c227ce9b4759b89e5c15e88.jpg"],["Douki-chan","https://thicc.mywaifulist.moe/waifus/40029/c79ac7706c5e050842eece4be73183af628da41328c6e6dd167c991ef99ce803_thumb.png"],["Guts","https://www.nautiljon.com/images/manga_persos/00/57/guts_175.jpg"],["Jahy-Sama","https://i.pinimg.com/236x/c7/fe/bf/c7febfbf541d472d13e371e82c3dd87b.jpg"],["Senko san","https://www.nautiljon.com/images/perso/00/34/senko_18443.jpg"],["シエスタ","https://i.pinimg.com/736x/26/d0/3e/26d03e45cfe45e228a3140eeeacc8907.jpg"],["Futaba Igurashi","https://i.pinimg.com/736x/88/cc/e6/88cce6ca3d27ff15cf14db79b104d62f.jpg"]]
list_season=["season 0",'s0',"s","season "]
webhook_url="https://discord.com/api/webhooks/932239887279718480/JNRdpMiDFps215IN65tJ9pXQZjPU7t89yWu7Tmy6P0TeEMRhbMM7V-kntbvtfyD5Zlb7"
entier=["1","2","3","4","5","6","7","8","9"]

def is_loading(file):
    if "mkv" in file:
        txtfile=file.replace("mkv","txt")
    elif "mp4" in  file:
        txtfile=file.replace("mp4","txt")
    if txtfile in os.listdir("/mnt/Disque-1/Download"):
        return True
    else:
        return False
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



def encode(file):
    if "265" in file or "x265" in file or "h265" in file or "HEVC" in file:

        return True
    if "Shingeki no Kyojin" in file:
        return True
def Season_Find(file,anime,dir):
    if "Shingeki" in file:
        return "Season 04/"
    if "Kimetsu no Yaiba" in file:
        return "Season 03/"
    file=file.replace("("," ")
    file=file.replace(")"," ")
    file=file.replace("E"," ")
    file=file.lower()
    if "OAV" in  file:
        os.makedirs(anime+"/"+"Season 00",0, exist_ok=True)
        return "season 00/"
    for nb_of_format in range(len(list_season)):

        for nb_of_season in range(4):
                
            detect=list_season[nb_of_format]+str(nb_of_season)

            if detect in file :
                os.makedirs(anime+"/"+"Season 0"+str(nb_of_season),0, exist_ok=True)
                return "Season 0"+str(nb_of_season)+"/"
                    
                
    print("---->GOING DEFAULT")
    logging.info("---->GOING DEFAULT")
    os.makedirs(anime+"/"+"Season 01",0, exist_ok=True)
    return "Season 01"+"/"

def target_dir_find(target_dir_list,anime):
    
    os.makedirs(target_dir+"/"+anime,0,exist_ok=True)
    for dir in target_dir_list:
 
        if anime in dir:
            
            return target_dir+"/"+dir
        
    print("---->ERROR NO DIRECTORY FOR ",anime,"FOUND")
    logging.error("---->ERROR NO DIRECTORY FOR "+anime+"FOUND")

    return ""


def find(target_dir,dl_dir,file,anime):
    """return process et target dans liste"""
    separator=" "
    target_dir_list=os.listdir(dir_list_of_anime)
    if ".mp4" in file or ".mkv" in  file:
        while is_loading(file)==True:
            time.sleep(10)


        for animee in anime:
            print(anime)
            if animee in file:
                print("FOUND FOR",file)
                logging.info("FOUND FOR "+file)
                process=dl_dir+file
                print("---->SEARCHING FOR ENCODE")
                
                
                if encode(file)==True:
                        
                    print("---->ENCODED IN X265")
                    logging.info("---->ENCODED IN X265")
                    print("---->SEARCHING FOR DIRECTORY")
                    logging.info("---->SEARCHING FOR DIRECTORY")
                    target=target_dir_find(target_dir_list,animee)+"/"+Season_Find(file,target_dir_find(target_dir_list,animee),dir_list_of_anime)
                    os.makedirs(target,0,exist_ok=True)
                    return [True,process,target+file,265]     


                target=target_dir+file
                
                print("---->NOT ENCODED IN X265 PUTING TO CONVERT")
                logging.info("---->NOT ENCODED IN X265 PUTING TO CONVERT")
                return [True,process,no265+file,"NOT X265 OR no ENCODE MENTIONNED",True]
          
        if " - " in  file or "_-_" in file:
            lsanime=open('listeanime.txt',"w")
            ori=file
            tkt=file
            if "[" in file:
                nb_to_do=delet_to_do(file,"[")
                nb_to_do1=delet_to_do(file,"(")
                ori=sup_char(file,nb_to_do,nb_to_do1)
            if "_" in file:
                ori=ori.replace("_"," ") 
                tkt=file.replace("_"," ")
                os.rename(dl_dir+file,dl_dir+tkt)   
            discri=ori.split(" - ")
            discri=discri[0]
            
            
            listeanime.append(discri)
            
            listeanime2="%".join(listeanime)
            lsanime.write(listeanime2)
            lsanime.close()
            os.makedirs(dir_list_of_anime+"/"+discri,0,exist_ok=True)
            anime.append(discri)
            newlist=os.listdir(dir_list_of_anime)
            
            target=target_dir_find([discri],discri)+"/"+Season_Find(file,target_dir_find([discri],discri),dir_list_of_anime)
            os.makedirs(target,0,exist_ok=True)
            return find(target_dir,dl_dir,tkt,listeanime)
        else:
            lsanime=open('listeanime.txt',"w")
            newwfile=file.split(" ")
            if "[" in newwfile[0]:
                newwfile=" ".join(newwfile)
                newwfile=newwfile.replace("]"," ")
                newwfile=newwfile.split(" ")
                if newwfile[1]!=" " and newwfile[1]!="":
                    anime=newwfile[1]

                else:
                    anime=newwfile[2]
                listeanime.append(anime)
                #listeanime2="%".join(listeanime)
                #lsanime.write(listeanime2)
                #lsanime.close()
                target=target_dir_find([anime],anime)+"/"+Season_Find(file,target_dir_find([anime],anime),dir_list_of_anime)
                os.makedirs(target,0,exist_ok=True)
                return find(target_dir,dl_dir,file,listeanime)
        
            if "S0" in file:
                anime=file.split("S0")[0]
            listeanime.append(anime)
            print(anime)
            #listeanime2="%".join(listeanime)
            #lsanime.write(listeanime2)
            #lsanime.close()
            target=target_dir_find([anime],anime)+"/"+Season_Find(file,target_dir_find([anime],anime),dir_list_of_anime)
            os.makedirs(target,0,exist_ok=True)
            return find(target_dir,dl_dir,file,listeanime)



            
            
           

    return [False]

def random_waifu(list_waifu=list_waifu):
    return random.choice(list_waifu)


    
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
    choice=random.choice(liste)
    return choice


def send_webhook_request(webhook_url=webhook_url,waifu=random_waifu()):
    dir=os.listdir(no265)
    fichier='\n'.join(map(str, dir))
    content='@admin'
    data =  {'name' : 'Directory Seeker',
                'content': content,
                
                'avatar_url': waifu[1],
                'username':waifu[0],
                'embeds':[
                    {
                        'color':1127128,
                        'footer':{
                            'text':'From jellyfin',
                            "icon_url":waifu[1]},
                        'title':'おはよう il y à '+str(len(dir))+' fichier à convertir : \n'+fichier,
                        "image":{"url":random_gif(waifu[0],16)}
                        }
                        ]
                        }
    r= requests.post(webhook_url, data=json.dumps(data), headers={'Content-type': 'application/json'})

      
for file in dir_list:
    
    result=find(target_dir,dl_dir,file,listeanime)

    if result[0]==True:

        print("---->MOVING TO",result[2])
        logging.info("---->MOVING TO "+result[2])
        print(result)
        
        os.rename(result[1],result[2])
        if result[-1]==True:
            is265=True
     
    
if is265==True:
    send_webhook_request()




