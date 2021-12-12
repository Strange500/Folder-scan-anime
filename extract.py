import os , logging
logging.basicConfig(filename="z:/log_tri.log", level=logging.INFO,filemode='a')


main_dir="z:/Download"
dir_watch=os.listdir(main_dir)

list_season=["Season 0","Saison 0"]

x=0
dir_watch.pop(dir_watch.index("Ready"))



def Season_Find(file,list_season):

    for nb_of_format in range(len(list_season)):
        for nb_of_season in range(20):
                
            if list_season[nb_of_format]+str(nb_of_season) in file :
                    
                return "Season 0"+str(nb_of_season)    
    return None




for anime in dir_watch:
    if "." not in anime and "convert" not in anime and "Readdy" not in anime and "tri" not in anime:
        sub_dir=os.listdir(main_dir+"/"+anime)
        print(sub_dir)

        for season in sub_dir:
            if "." not in season:
                #print(anime)
                #print(season)
                dir_season=Season_Find(season,list_season)
                print(dir_season)
                seasonn=os.listdir(main_dir+"/"+anime+"/"+season)
                #print(season)
                for file in seasonn:
                    print(file)
                    if dir_season != None  :
                        if "mp4" in file or "mkv" in file:
                        
                            renamed=file.split(" ")
                            renamed.insert(-1,dir_season)
                            renamed=" ".join(renamed)
                            print(renamed)
                            #file_list=os.listdir(main_dir+"/"+dir+"/"+anime+"/"+dir_season)
                            print(main_dir+"/"+anime+"/"+season+"/"+file)
                            print(main_dir+renamed)
                            os.rename(main_dir+"/"+anime+"/"+season+"/"+file,main_dir+"/"+renamed)
                            
                            logging.info("REANAMING "+str(file)+" TO "+ renamed)

                                        
                    

