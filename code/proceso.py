# STEP 1.1

from urllib.request import urlopen
txt = urlopen("https://raw.githubusercontent.com/carlospc/experimento1/master/txt/cien-anios-de-soledad.txt").read().decode("utf-8", errors="replace").split("\n")
print("Our dataset contains {} scripts".format(len(txt)))
# ADVANCED_CHANGEME -- You can change this to load any text file 
# You want it to be one line of plain text for every script.  Extra
# annotations like [John:] or *starts coughing* make learning more difficult.
everything = set([w for s in txt for w in s.split()])
print("and {} lexical types".format(len(everything)))

# STEP 1.2

# 1. Import the tokenizer
import spacy
nlp = spacy.load("es", disable=["parser","tagger","ner","textcat"])

# 2. Tokenize
txt = [nlp(s) for s in txt]

# 3. Mark the beginning and end of each script 
txt = [ ["<s>"] + [str(w) for w in s] + ["</s>"] for s in txt]

# 4. Separate the data into training and validation
train = txt[:-5]
valid = txt[-5:]

# 5. Flatten the lists into one long string and remove extra whitespace
train = [w for s in train for w in s if not w.isspace()]
valid = [w for s in valid for w in s if not w.isspace()]

