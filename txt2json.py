import os
from pandas.io import json
from tqdm import tqdm

filepath = "data/wiki.txt"
with open(filepath,'r',encoding='utf-8')as f:
    titles = []
    for line in f:
        line = line.strip()
        if line.endswith(":") and "," not in line and "." not in line:
            title = line[:-1]
            titles.append(title)
            print(title)
print(titles)

#        else:
#            with open("title.json","a",encoding="utf-8") as j:
#                j.:

txt = "Following the Nice Treaty, there was an attempt to reform the constitutional law of the European Union and make it more transparent; this would have also produced a single constitutional document. However, as a result of the referendum in France and the referendum in the Netherlands, the 2004 Treaty establishing a Constitution for Europe never came into force. Instead, the Lisbon Treaty was enacted. Its substance was very similar to the proposed constitutional treaty, but it was formally an amending treaty, and – though it significantly altered the existing treaties – it did not completely replace them."
print(len(txt))