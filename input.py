import os
import pandas as pd


def file2text(file,path="./data/"):

    with open(path+file, "r", encoding="utf-8") as f:
        lines = f.readlines()

    texts = []
    for text in lines:
        #text = text.replace('\n', '')
        texts.append(text)

    return texts

def files2text(folder,path="./data/"):

    files = os.listdir(path+folder)

    with open(files)as f:
        lines = f.readlines()

    all_documents = []
    all_titles = []
    all_keys = []

    for i,fname in enumerate(files):
        with open(path+folder+fname) as f:
            lines = f.readlines()

        all_text = ''.join(lines)

    all_documents.append(all_text)


    return all_documents

