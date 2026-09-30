# 文本向量化
import os
from langchain_classic.embeddings import init_embeddings
from langchain_community.embeddings import DashScopeEmbeddings
from langchain_openai import OpenAIEmbeddings

# 需要向量的文本
user_query = "特朗普上一次访华是什么时候？"
# 创建嵌入模型对象
embedding_model = DashScopeEmbeddings(model = "text-embedding-v1")
# 将文本向量化
vector = embedding_model.embed_query(user_query)
print(vector)
print(len(vector))