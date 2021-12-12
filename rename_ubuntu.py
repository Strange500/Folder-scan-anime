import os , logging
logging.basicConfig(filename="/mnt/Disque-1/log_tri.log", level=logging.INFO,filemode='a')


main_dir="/mnt/Disque-1/JellyFin/Anime"
dir_watch=os.listdir(main_dir)

list_season=["Season 0"]

x=0

common_to_supp=["x265","h265","HEVC","VOSTFR", "MULTI","1080p","AAC","Bluray","10bits"]
print()



def Season_Find(file,list_season):

    for nb_of_format in range(len(list_season)):
        for nb_of_season in range(20):
                
            if list_season[nb_of_format]+str(nb_of_season) in file :
                    
                return "Season 0"+str(nb_of_season)+"/"    
    return None

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
    for to_sup in common_to_supp:
        if to_sup in renamed:
            renamed=renamed.replace(to_sup,"")
    
            
    
    return renamed 

    



for dir in dir_watch:
    sub_dir=os.listdir(main_dir+"/"+dir)
    #print(sub_dir)
    for anime in sub_dir:
        #print(anime)
        season=os.listdir(main_dir+"/"+dir+"/"+anime)
        #print(season)
        for sea in season:
            dir_season=Season_Find(sea,list_season)
            if dir_season != None:
                file_list=os.listdir(main_dir+"/"+dir+"/"+anime+"/"+dir_season)
                
                for file in file_list:
                    if "mp4" in file or "mkv" in file:
                        nb_to_do=delet_to_do(file,"[")
                        nb_to_do1=delet_to_do(file,"(")

                        renamed=sup_char(file,nb_to_do,nb_to_do1)
                        
                        if renamed != file:
                            logging.info("REANAMING "+str(file)+" TO "+ renamed)

                            os.rename(main_dir+"/"+dir+"/"+anime+"/"+dir_season+file,main_dir+"/"+dir+"/"+anime+"/"+dir_season+renamed)
            

