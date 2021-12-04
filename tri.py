import os

no265="Téléchargements/to convert/"
listeanime=["Platinum","Takt","Douki-chan","Shiroi","Demon","Komi-san"]
dir_list = os.listdir("Téléchargements")
dir_list_of_anime="JellyFin/Anime/Airing/"

target_dir_list=os.listdir("JellyFin/Anime/Airing/")
list_season=["s","season 0","Season ",'s0',"(Mugen Ressha-hen)"]
#print(target_dir_list)
indice=0


def Season_Find(file,anime,dir):
    lenght=len(file)
    file=" ".join(file)
    file=file.replace("E"," ")
    file=file.lower()
    file=file.split(" ")
    print(file)
    for nb_of_format in range(len(list_season)):
        for nb_of_season in range(4):
            for n in range(lenght):
                
                if list_season[nb_of_format]+str(nb_of_season) in file and n+1<=lenght:
                    
                    return "Season 0"+str(nb_of_season)+"/"
    os.makedirs(dir+anime+"Season 01", exist_ok=True)
    
    return "Season 01"+"/"


def target_dir_find(target_dir_list,anime):
    indice=0
    for dir in target_dir_list:
        dir=dir.split(" ")
        for nb in range(len(dir)):
            if anime==dir[nb]:
                return target_dir+" ".join(dir)
        indice=indice+1
    print("ERROR NO DIRECTORY FOR ",anime,"FOUND")

def find(target_dir,dl_dir,file,anime):
    """return process et target dans liste"""
    
    separator=" "
    for i in range(len(file)):
        if file[i]==anime:
            
            print("FOUND AT",file[i])
            process=dl_dir+separator.join(file)
            print("SEARCHING FOR ENCODE")
            
            for n in range(len(file)):
                
                string=file[n]
                
                string=string.replace("["," ")
                string=string.replace("]"," ")
                string=string.split(" ")
                
                for elt in range(len(string)):
                    #print(string)
                    if string[elt]=="265"or string[elt]=="x265"or string[elt]=="h265"or string[elt]=="HEVC":
                        print("ENCODED IN X265")
                        target=target_dir_find(target_dir_list,anime)+"/"+Season_Find(file,target_dir_find(target_dir_list,anime),dir_list_of_anime)+separator.join(file)
                        return [True,process,target,265]
            target="target_dir"+separator.join(file)
            print("NOT ENCODED IN X265 PUTING TO CONVERT")
            return [True,process,no265+separator.join(file),"NOT X265 OR no ENCODE MENTIONNED"]
            
            
        
        #print("NOTHING FOUND AT",file[i]) 
            
    return [False]



#print(dir_list)
splited_dir_list=[]
for file in dir_list:
    splited_dir_list.append(file.split(" "))


    
n=0

dl_dir="Téléchargements/"
target_dir="JellyFin/Anime/Airing/"




#process=dl_dir+separator.join(splited_dir_list[7])
#target=target_dir+separator.join(splited_dir_list[5])
#print(process,target)
#os.rename(process, target)


for file in splited_dir_list:
    for file in splited_dir_list:
        #print(file)
        #print(separator.join(file))
        #essai=0
        
        result=find(target_dir,dl_dir,file,listeanime[indice])
        #print(len(splited_dir_list),indice)
    
        if result[0]==True and indice+1<=len(splited_dir_list):
            #print(result[1],result[2])
            
            os.rename(result[1],result[2])
        
    if indice+1<len(listeanime):
            indice=indice+1

        








