import os

this_directory = os.path.abspath(os.path.dirname(__file__))
file = open(this_directory + "/cancer.cancer", "r")
cancers = file.readlines()
file.close()
file = open(this_directory + "/symptoms.txt", "r")
temp = file.readlines()
symptoms = []
for i in temp:
    if i not in symptoms:
        symptoms.append(i.lower().rstrip('\r\n'))
symptoms = list(set(symptoms))
symptoms.sort()
