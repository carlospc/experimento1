# STEP 1.1

from urllib.request import urlopen
txt = urlopen("https://raw.githubusercontent.com/carlospc/experimento1/master/txt/cien-anios-de-soledad.txt").read().decode("utf-8", errors="replace").split("\n")
print("Our dataset contains {} scripts".format(len(txt)))
# ADVANCED_CHANGEME -- You can change this to load any text file 
# You want it to be one line of plain text for every script.  Extra
# annotations like [John:] or *starts coughing* make learning more difficult.
everything = set([w for s in txt for w in s.split()])
print("and {} lexical types".format(len(everything)))
