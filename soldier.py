import os
def soldier(path,mode):
    os.chdir(path)
    files = os.listdir(path)
    i = 1
    for file in files:
        if file.endswith(f'.{mode}'):
            os.rename(f"{file}", f"{i}.{mode}")
            i += 1
        else:
            os.rename(f"{file}", f"{file.capitalize()}")


