import os , shutil , time 

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = input("enter your path (use forward slash / while adding path ) : ")
to_dir = input("enter your destination path (use forward slash / while adding path ) : ")

dir_tree = { "Image_Files": ['.jpg', '.jpeg', '.png', '.gif', '.jfif'], 
            "Video_Files": ['.mpg', '.mp2', '.mpeg', '.mpe', '.mpv', '.mp4', '.m4p', '.m4v', '.avi', '.mov'], 
            "Document_Files": ['.ppt', '.xls', '.xlsx' ,'.csv', '.pdf', '.txt'], 
            "Setup_Files": ['.exe', '.bin', '.cmd', '.msi', '.dmg'] 
            }

class FileMovementHandler(FileSystemEventHandler):
    
    def on_created(self , event ):
        #print(event)
        name , ext = os.path.splitext(event.src_path)
        
        for key , value in dir_tree.items():
            if ext in value:
                filename = os.path.basename(event.src_path)
                
                print("FILE NAME IS " ,filename)
            
                path1= from_dir + "/" + filename
                path2 = to_dir + "/" + key 
                path3 = to_dir + "/" + key + "/" + filename
                
                if os.path.exists(path2) :
                    print("MOVING " + filename)
                    shutil.move (path1 , path3)
                    time.sleep(1)
                    
                else :
                    os.mkdir(path2)
                    print("MOVING " + filename)
                    shutil.move(path1 , path3)
                    time.sleep(1)
                
            
            
        
  
    
   
  
event_handler = FileMovementHandler()       
observer = Observer()
observer.schedule(event_handler , from_dir , recursive=True )
observer.start()

try:
    while True :
        time.sleep(2)
        print("Running")
        
except KeyboardInterrupt :
    print("STOPPED")
    observer.stop()
    

    
    
    
