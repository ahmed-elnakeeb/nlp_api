from fastapi import FastAPI,Path,Query
from typing import IO, Optional
import fastapi
from pydantic import BaseModel
from nltk.corpus import stopwords
from gensim.models.word2vec import Word2Vec
import gensim.downloader as api
app=FastAPI()


@app.get("/")
def home():
    return {"auther":"ahmedelnakeeb2016"}

@app.get("/compare")
def compare_between_text(text_A:str,text_B:str):
    min_word_count = 1   # Minimum word count   
    stop_words=stopwords.words('english')
    text_A_filterd_list=[]
    text_B_filterd_list=[]
    
    
    for i in  text_A.split():
        if i not in stop_words:
            text_A_filterd_list.append(i)       
    for i in text_B.split():
        if i not in stop_words:
            text_B_filterd_list.append(i)

    model = api.load("glove-wiki-gigaword-50")
    result=model.n_similarity(
        text_A_filterd_list,text_B_filterd_list)
    return {"result":str(result)}
    
