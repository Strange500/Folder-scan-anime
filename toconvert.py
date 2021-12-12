
import subprocess, sys , os , logging , time
logging.basicConfig(filename="z:/log_tri.log", level=logging.INFO)




handbrake_command = ["C:/Users/benja/OneDrive/Documents/test/HandBrakeCLI.exe", "-v", "--preset-import-file", "Z:/Download/script265.json", "-i", "path", "-o", "path" ]



directory=os.listdir("z:/Download/to convert")



for file in directory:

    if "mp4" in file or "mkv" in file:
        
        handbrake_command[5]="Z:/Download/to convert"+"/"+file
        output_file=file.split(" ")
        output_file[-2]="x265"
        output_file=" ".join(output_file)
        handbrake_command[7]="Z:/Download/Ready"+"/"+output_file
        handbrake_command[7]= handbrake_command[7].replace(".mkv",".mp4")
        handbrake_command[7].replace(" "," x265 ",1)
        base_command='"'.join(handbrake_command)
        logging.info("ENCODING "+file)
        subprocess.run(handbrake_command, shell=True)
        logging.info("ENCODE COMPLETE FOR "+file)
        os.rename(handbrake_command[7],"Z:/Download/"+output_file)
        logging.info("REMOVING "+file+ " IN DIRECTORY /TOCONVERT AND MOVING "+file+ " FOR TRI.PY")
        os.remove(handbrake_command[5])
        
        
        
        






