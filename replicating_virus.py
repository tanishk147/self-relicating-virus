import shutil
import os
import random

current_script = os.path.abspath(__file__)

while True:
    rand=random.randint(1,1000000)
    replicated_script = f"{rand}.py"
    shutil.copyfile(current_script, replicated_script)

    print("Script replicated successfully as", replicated_script)



