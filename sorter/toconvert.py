
import subprocess , os , logging 
logging.basicConfig(filename="z:/log_tri.log", level=logging.INFO)


cp_target="C:/convert cache"

handbrake_command = ["C:/Users/benja/OneDrive/Documents/test/HandBrakeCLI.exe", "-v", "--preset-import-file", "Z:/Download/script265.json", "-i", "path", "-o", "path" ]










directory=os.listdir("F:/convertcache")



for file in directory:

    if "mp4" in file or "mkv" in file:
        #shutil.move("z:/Download/to convert/"+file,cp_target+"/"+file)
        handbrake_command[5]="F:/convertcache"+"/"+file
        output_file=file.split(" ")
        output_file[-2]="x265"
        output_file=" ".join(output_file)
        handbrake_command[7]="F:/convertcache/Ready"+"/"+output_file
        handbrake_command[7]= handbrake_command[7].replace(".mkv",".mp4")
        handbrake_command[7].replace(" "," x265 ",1)
        print(handbrake_command)
        base_command='"'.join(handbrake_command)
        logging.info("ENCODING "+file)
        subprocess.run(handbrake_command, shell=True)
        logging.info("ENCODE COMPLETE FOR "+file)
        
        
        
        #os.remove(handbrake_command[5])
        
        
        
        
        






