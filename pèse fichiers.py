import os


def peser(path):
    try:
        total = 0
        for truc in os.listdir(path):
            total += peser(path+os.sep+truc)
        return total
    except NotADirectoryError:
        return os.path.getsize(path)


for chose in os.listdir(os.getcwd()):
    print("Le fichier", chose, "pèse", peser(os.getcwd()+os.sep+chose), "octets.")
input()