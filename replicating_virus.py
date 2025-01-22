import shutil
import os
import random

current_script = os.path.abspath(__file__)

## to replicate for specific number
#replication_limit = 10
#replication_count = 0
#
#while replication_count < replication_limit:
#    rand = random.randint(1, 1000000)
#    replicated_script = f"{rand}.py"
#    shutil.copyfile(current_script, replicated_script)
#    replication_count += 1
#
#    print(f"Script replicated successfully as {replicated_script} ({replication_count}/{replication_limit})")
#
#print("Replication complete!")

while True:
    rand=random.randint(1,10)
    replicated_script = f"{rand}.py"
    shutil.copyfile(current_script, replicated_script)

    print("Script replicated successfully as", replicated_script)


