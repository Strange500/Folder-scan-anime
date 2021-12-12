#! /usr/bin/python
import os, logging


logging.basicConfig(filename="/mnt/Disque-1/log_tri.log", level=logging.INFO)
no265='path to directory for non-converted show'  
listeanime=["show to scan for"]
dir_list = os.listdir("path to directrory to scan")
dir_list_of_anime="path to dir destination"
splited_dir_list=[]
dl_dir="path to main dir"
target_dir=dir_list_of_anime
target_dir_list=os.listdir(dir_list_of_anime)
list_season=["s","season 0","season ",'s0']
list_season_except=["(Mugen"]

def encode(file):
    if "265" in file or "x265" in file or "h265" in file or "HEVC" in file:

        return True
def Season_Find(file,anime,dir):

    lenght=len(file)
    original=" ".join(file)
    file=" ".join(file)
    file=file.replace("("," ")
    file=file.replace(")"," ")
    file=file.replace("E"," ")
    file=file.lower()

    for nb_of_format in range(len(list_season)):

        for nb_of_season in range(4):

            for n in range(lenght):
                
                detect=list_season[nb_of_format]+str(nb_of_season)

                if detect in file and n+1<=lenght:
                    
                    
                    #os.makedirs(dir+anime+"Season 0"+str(nb_of_season), exist_ok=True)

                    return "Season 0"+str(nb_of_season)+"/"


    print("---->GOING DEFAULT")
    logging.info("---->GOING DEFAULT")
    #os.makedirs(dir+anime+"Season 01", exist_ok=True)
    return "Season 01"+"/"

def target_dir_find(target_dir_list,anime):
    
    for dir in target_dir_list:
        
        dir=dir.split(" ")
        
        for nb in range(len(dir)):
            
            if anime in dir:

                return target_dir+"/"+" ".join(dir)
        
    print("---->ERROR NO DIRECTORY FOR ",anime,"FOUND")
    logging.error("---->ERROR NO DIRECTORY FOR "+anime+"FOUND")

    return ""


def find(target_dir,dl_dir,file,anime):
    """return process et target dans liste"""
    separator=" "
    if "." in separator.join(file):

        for i in range(len(file)):

            if file[i] in anime:

                index=anime.index(file[i])
                print("FOUND AT",file[i])
                logging.info("FOUND AT "+file[i])
                process=dl_dir+separator.join(file)
                print("---->SEARCHING FOR ENCODE")
                
                
                if encode(separator.join(file))==True:
                        
                    print("---->ENCODED IN X265")
                    logging.info("---->ENCODED IN X265")
                    print("---->SEARCHING FOR DIRECTORY")
                    logging.info("---->SEARCHING FOR DIRECTORY")
                    target=target_dir_find(target_dir_list,anime[index])+"/"+Season_Find(file,target_dir_find(target_dir_list,anime[index]),dir_list_of_anime)+separator.join(file)
                    return [True,process,target,265]

                target=target_dir+separator.join(file)
                print("---->NOT ENCODED IN X265 PUTING TO CONVERT")
                logging.info("---->NOT ENCODED IN X265 PUTING TO CONVERT")
                return [True,process,no265+separator.join(file),"NOT X265 OR no ENCODE MENTIONNED"]
                
    return [False]




for file in dir_list:

    splited_dir_list.append(file.split(" "))


      
for file in splited_dir_list:
    
    result=find(target_dir,dl_dir,file,listeanime)

    if result[0]==True:

        print("---->MOVING TO",result[2])
        logging.info("---->MOVING TO "+result[2])
        os.rename(result[1],result[2])
     
    





