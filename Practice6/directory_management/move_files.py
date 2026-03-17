import shutil
shutil.move("test.txt", "x/test.txt")

import os
print(os.path.exists("test.txt"))

from pathlib import Path
file = Path("test.txt")
print(file.exists())
print(file.name)