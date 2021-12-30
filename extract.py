import os , logging
logging.basicConfig(filename="/mnt/Disque-1/log_tri.log", level=logging.INFO,filemode='a')


main_dir="/mnt/Disque-1/Download"
dir_watch=os.listdir(main_dir)

list_season=["Season 0","Saison 0","Season ","Saison ","S0","S"]

x=0
dir_watch.pop(dir_watch.index("Ready"))
dir_watch.pop(dir_watch.index("to convert"))
dir_watch.pop(dir_watch.index("tri"))


print(dir_watch)



def encode(file):
    if "265" in file or "x265" in file or "h265" in file or "HEVC" in file:

        return True

def Season_Find(file,list_season):

    for nb_of_format in range(len(list_season)):
        for nb_of_season in range(20):
                
            if list_season[nb_of_format]+str(nb_of_season) in file :
                    
                return "Season 0"+str(nb_of_season)    
    return None

#print(encode("[Judas] Boku Dake ga Inai Machi (Erased) (Season 1) [BD 1080p][HEVC x265 10bit][Dual-Audio][Eng-Subs]"))


for anime in dir_watch:
    print(anime)
    
    isx265=encode(anime)

    if "." not in anime and "convert" not in anime and "Ready" not in anime and "tri" not in anime:
        sub_dir=os.listdir(main_dir+"/"+anime)
        main_season=Season_Find(anime,list_season)
        

        for season in sub_dir:
            print(season)
            if "." not in season:
                #print(anime)
                #print(season)
                dir_season=Season_Find(season,list_season)
                
                seasonn=os.listdir(main_dir+"/"+anime+"/"+season)
                #print(season)
                for file in seasonn:
                    
                    if dir_season != None  :
                        logging.info("EXTRACTING "+anime)
                        if "mp4" in file or "mkv" in file:
                            print("i have find some ep")
                            renamed=file.split(".")
                            if encode(file) or encode(anime)==True:
                                renamed[0]=renamed[0]+" x265 "
                            renamed[0]=renamed[0]+dir_season
                            renamed=".".join(renamed)
                            
                            #file_list=os.listdir(main_dir+"/"+dir+"/"+anime+"/"+dir_season)
                            
                            os.rename(main_dir+"/"+anime+"/"+season+"/"+file,main_dir+"/"+renamed)
                            os
                            
                            logging.info("--->REANAMING "+str(file)+" TO "+ renamed)
                
            if ".mkv" in season or ".mp4" in season:
                renamed=season.split(".")
                logging.info("EXTRACTING "+anime)
                if encode(anime)==True:
                    renamed[0]=renamed[0]+" x265 "
                    
                    if Season_Find(season,list_season)!=None:
                        print("seaon in file")
                    elif main_season != None:
                        renamed[0]=renamed[0]+main_season
                    else:
                        renamed[0]=renamed[0]+"Season 01"
                    renamed=".".join(renamed)
                    print(main_dir+"/"+renamed)
                    logging.info("--->MOVING "+season+" TO /DONLOAD")
                    os.rename(main_dir+"/"+anime+"/"+season,main_dir+"/"+renamed)
                else:
                    if Season_Find(season,list_season)!=None:
                        print("mentioned in file")
                    elif main_season != None:
                        renamed[0]=renamed[0]+main_season
                    else:
                        logging.info("--->NO SEASON FIND GOING DEFAULT FOR "+season)
                        renamed[0]=renamed[0]+"Season 01"
                    renamed=".".join(renamed)
                    print(main_dir+"/"+renamed)
                    logging.info("--->MOVING "+season+" TO /DONLOAD")
                    os.rename(main_dir+"/"+anime+"/"+season,main_dir+"/"+renamed)



                    
                  
                                        
                    

