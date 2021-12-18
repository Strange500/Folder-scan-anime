#! /usr/bin/python
import os, logging, json, requests

is265=False
logging.basicConfig(filename="/mnt/Disque-1/log_tri.log", level=logging.INFO)
no265='/mnt/Disque-1/Download/to convert/'
listeanime=["Platinum End","Takt Op. Destiny","Ganbare, Douki-chan","Shiroi Suna no Aquatope","Demon Slayer",'Eighty Six',"Komi-san wa Komyushou Desu","My Senpai is Annoying","Jahy-sama wa Kujikenai!","Mushoku Tensei","Mieruko-chan","Saihate No Paladin","Black Clover","Erased","Blue Exorcist"]
readd=open("/mnt/Disque-1/Download/listeanime.txt","r")
listeanime= readd.read()
readd.close()
listeanime=listeanime.split("%")
dir_list = os.listdir("/mnt/Disque-1/Download")
dir_list_of_anime="/mnt/Disque-1/JellyFin/Anime/Airing"
splited_dir_list=[]
dl_dir="/mnt/Disque-1/Download/"
target_dir=dir_list_of_anime
target_dir_list=os.listdir(dir_list_of_anime)
list_season=["season 0",'s0']
list_season_except=["(Mugen"]
webhook_url="https://discord.com/api/webhooks/920359694520950795/JUsjTQwC6MIyHOmCs_CDxAdY0xO9e88Aj1QlebTqla3izEEm5H1RJduoeypybXDpmJ4t"


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
def Season_Find(file,anime,dir):

    original=file
    if "Demon Slayer" in file:
        return "Season 03/"
    file=file.replace("("," ")
    file=file.replace(")"," ")
    file=file.replace("E"," ")
    file=file.lower()
    
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

        for animee in anime:
            
            if animee in file:
                index=anime.index(animee)
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
            if "[" in file:
                nb_to_do=delet_to_do(file,"[")
                nb_to_do1=delet_to_do(file,"(")
                ori=sup_char(file,nb_to_do,nb_to_do1)
            if "_" in file:
                ori=ori.replace("_"," ") 
                os.rename(file,file.replace("_"," "))   
            discri=ori.split(" - ")
            discri=discri[0]
            
            
            listeanime.append(discri)
            
            listeanime2="%".join(listeanime)
            lsanime.write(listeanime2)
            lsanime.close()
            os.makedirs(dir_list_of_anime+discri,0,exist_ok=True)
            anime.append(discri)
            newlist=os.listdir(dir_list_of_anime)
            
            target=target_dir_find([discri],discri)+"/"+Season_Find(file,target_dir_find([discri],discri),dir_list_of_anime)
            os.makedirs(target,0,exist_ok=True)
            return find(target_dir,dl_dir,file,listeanime)
            
            
            

    return [False]


def send_webhook_request(webhook_url):
    dir=os.listdir(no265)
    list_fichier=[]
    n=0
    for fichier in dir:
        n=n+1
        list_fichier.append(fichier)

    fichier='\n'.join(map(str, list_fichier))
    content='yo il y a '+str(n)+' fichier à convertir : \n'+fichier
    data =  {'name' : 'Directory Seeker',
                'content': content}

    r= requests.post(webhook_url, data=json.dumps(data), headers={'Content-type': 'application/json'})



      
for file in dir_list:
    
    result=find(target_dir,dl_dir,file,listeanime)

    if result[0]==True:

        print("---->MOVING TO",result[2])
        logging.info("---->MOVING TO "+result[2])
        os.rename(result[1],result[2])
        if result[-1]==True:
            is265=True
     
    
if is265==True:
    send_webhook_request(webhook_url)


