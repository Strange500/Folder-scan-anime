import os , logging, shutil
logging.basicConfig(filename="/mnt/Disque-1/log_tri.log", level=logging.INFO,filemode='a')


main_dir="/mnt/Disque-1/Download"
dir_watch=os.listdir(main_dir)

list_season=["Season 0","Saison 0","Season ","Saison ","S0","S","s0","s","1st Season","2nd Season","3th Season"]

x=0
dir_watch.pop(dir_watch.index("Ready"))
dir_watch.pop(dir_watch.index("to convert"))
dir_watch.pop(dir_watch.index("tri"))


print(dir_watch)

def sup_prob_season(file):
    if "1st Season" in file:
        file=file.replace("1st Season","S01")
    if "2nd Season" in file:
        file=file.replace("2nd Season","S02")   
    if "3th Season" in file:
        file=file.replace("3th Season","S03")
    
    return file
def encode(file):
    if "265" in file or "x265" in file or "h265" in file or "HEVC" in file:

        return True

def Season_Find(file,list_season):

    for nb_of_format in range(len(list_season)):
        for nb_of_season in range(20):
            if list_season[nb_of_format]=="1st Season":
                if list_season[nb_of_format] in file:
                     
                    return "Season 01"
            if list_season[nb_of_format]=="2nd Season":
                if list_season[nb_of_format] in file:
                    

                    return "Season 02"
            if list_season[nb_of_format]=="3th Season":
                if list_season[nb_of_format] in file:
                    
                    return "Season 03"
                
            if list_season[nb_of_format]+str(nb_of_season) in file :
                    
                return list_season[nb_of_format]+str(nb_of_season) 
    if "Bonus" in  file or "spécial" in file or "special" in file or "bonus" in file or "oav" in file or "OAV" in file or "EXTRA" in file or "extra" in file or "movie" in file or "Movie" in file or "MOVIE" in file:
        return "Season 00"   
    return None

#print(encode("[Judas] Boku Dake ga Inai Machi (Erased) (Season 1) [BD 1080p][HEVC x265 10bit][Dual-Audio][Eng-Subs]"))


for anime in dir_watch:
    print(anime)
    
    isx265=encode(anime)

    if ".m" not in anime and "convert" not in anime and "Ready" not in anime and "tri" not in anime and ".p" not in anime and ".b" not in anime and ".t" not in anime :
        sub_dir=os.listdir(main_dir+"/"+anime)
        main_season=Season_Find(anime,list_season)
        
        logging.info("EXTRACTING "+anime)
        for season in sub_dir:
            print(season)
            if "." not in season:
                #print(anime)
                #print(season)
                dir_season=Season_Find(season,list_season)
                
                seasonn=os.listdir(main_dir+"/"+anime+"/"+season)
                #print(season)
                
                for file in seasonn:
                    
                    if dir_season != None  and dir_season!="Season 00":
                        
                        if "mp4" in file or "mkv" in file:
                            print("i have find some ep")
                            renamed=file.split(".")
                            if encode(file) or encode(anime)==True:
                                renamed[0]=renamed[0]+" x265 "
                            renamed[0]=renamed[0]+dir_season
                            renamed=".".join(renamed)
                            
                            #file_list=os.listdir(main_dir+"/"+dir+"/"+anime+"/"+dir_season)
                            renamed=sup_prob_season(renamed)
                            os.rename(main_dir+"/"+anime+"/"+season+"/"+file,main_dir+"/"+renamed)
                            

                    elif dir_season=="Season 00" and "mp4" in file or "mkv" in file:
                        print("i have find some ep")
                        renamed=renamed.split(".")
                        if encode(file) or encode(anime)==True:
                            renamed[0]=renamed[0]+" x265 "
                        renamed[0]=renamed[0]+dir_season
                        renamed=".".join(renamed)
                            
                            #file_list=os.listdir(main_dir+"/"+dir+"/"+anime+"/"+dir_season)
                        renamed=sup_prob_season(renamed)
                        os.rename(main_dir+"/"+anime+"/"+season+"/"+file,main_dir+"/"+renamed)

                            
                
            if ".mkv" in season or ".mp4" in season:
                renamed=season.split(".m")
                if "." in renamed[0]:
                    renamed[0]=renamed[0].replace("."," ")
                
                if encode(anime)==True:
                    renamed[0]=renamed[0]+" x265 "
                    
                    if Season_Find(season,list_season)!=None:
                        print("seaon in file")
                    elif main_season != None:
                        renamed[0]=renamed[0]+main_season
                    else:
                        renamed[0]=renamed[0]+"Season 01"
                    renamed=".m".join(renamed)
                    print(main_dir+"/"+renamed)
                    renamed=sup_prob_season(renamed)
                    
                    os.rename(main_dir+"/"+anime+"/"+season,main_dir+"/"+renamed)
                else:
                    if Season_Find(season,list_season)!=None:
                        print("mentioned in file")
                    elif main_season != None:
                        renamed[0]=renamed[0]+main_season
                    else:
                        renamed[0]=renamed[0]+"Season 01"
                    renamed=".m".join(renamed)
                    print(main_dir+"/"+renamed)
                    renamed=sup_prob_season(renamed)
                    os.rename(main_dir+"/"+anime+"/"+season,main_dir+"/"+renamed)
        logging.info("EXTRACTION OF "+anime+" COMPLETE OR NO FILE INSIDE")
        #shutil.rmtree(main_dir+"/"+anime)



for filee in os.listdir(main_dir):
    print(filee)
    if ".m" in filee:
        filee_renamed=sup_prob_season(filee)
        os.rename(main_dir+"/"+filee,main_dir+"/"+filee_renamed)



                  
                                        
                    

