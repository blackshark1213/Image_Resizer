import cv2
import os 
from colorama import Fore as color


# Load the Dev. Logo
def logo():
    print(color.RED+'*+-------------------------------------------------------------------------+*'+color.WHITE)    
    print(color.BLUE+'''\tProgramed by Keshav raj.'''+color.BLUE+'''
         _    __   ______    _______    _      _          ___   __            __
        | |  / /  |  ____|  | ____  |  | |    | |        / ^ \  \ \          / /
        | | / /   | |       | |   |_|  | |    | |       / / \ \  \ \        / /
        | |/ /    | |____   | |_____   | |____| |      / /___\ \  \ \      / /
        | |\ \    |  ____|  |_____  |  |  ____  |     / _______ \  \ \    / /
        | | \ \   | |        _    | |  | |    | |    / /       \ \  \ \  / /
        | |  \ \  | |____   | |___| |  | |    | |   / /         \ \  \ \/ /
        |_|   \_\ |______|  |_______|  |_|    |_|  /_/           \_\  \__/  '''+color.GREEN+'. RAJ')
    print(color.RED+'*+-------------------------------------------------------------------------+*'+color.WHITE)  
    print('\n')     
    pass

if __name__=='__main__':
    logo()
    while True:
        filePath = input('Drag & Drop file here (done() for exit): ')
        if filePath == "done()":
            exit(0)
        elif '.' not in filePath:
            continue
        
        filePath = filePath.replace("'","")
        filePath = filePath.replace(" ","")
        
        
        #Load the image 
        image = cv2.imread(filePath)
        
        
        length = int(input(color.YELLOW+'Length of your new image : '+color.WHITE))
        breadth = int(input(color.YELLOW+'Breadth of your new image : '+color.WHITE))
        fileExtension = (input(color.YELLOW+'Go with default extension i.e (*.jpeg) Y/N :'+color.WHITE))
        if fileExtension =='N' or fileExtension =='n':
        	fileExtension = str(input(color.YELLOW+'Enter new Extensoion : '+color.WHITE))
        else:
        	fileExtension = 'jpeg'
     	
        # Resize to AxB pixels
        resized_image = cv2.resize(image, (length, breadth))

        # Save the resized image
        finalPath = str(filePath)+'_Resize_'+str(length)+'X'+str(breadth)+'_.'+str(fileExtension)
        cv2.imwrite(finalPath, resized_image)
        print(color.GREEN+' \t\tDone processing\t\n',color.WHITE)

        # __ = os.listdir('/home/{user}/Downloads/')
        # file =[]
        # for f in __:
        #     if f.endswith(".jpeg"):
        #         file.append(f)
        # print('\n'.join(file))
        
	
        os.system(f'ls -lh {finalPath} | lolcat')
        print('\n')

