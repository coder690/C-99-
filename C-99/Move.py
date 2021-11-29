import os 
import shutil
path="C://Users//xpres//Desktop//C-99"
print("before Moving")
print(os.listdir(path))
source="C://Users//xpres//Desktop//C-99//Text.txt"
destination="C://Users//xpres//Desktop//C-99//newfolder"
dest=shutil.move(source,destination)
print("after moving")
print(os.listdir(path))
