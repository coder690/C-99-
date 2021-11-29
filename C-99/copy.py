import os 
import shutil
path="C://Users//xpres//Desktop//C-99"
print("before Copy file")
print(os.listdir(path))
source="C://Users//xpres//Desktop//C-99//Text.txt"
destination="C://Users//xpres//Desktop//C-99//Text2.txt"
dest=shutil.copy(source,destination)
print("after coping file")
print(os.listdir(path))

