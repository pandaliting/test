import torch
import chromadb
from sentence_transformers import SentenceTransformer

# 1. 初始化
client = chromadb.Client()
collection = client.create_collection("my_knowledge_base")
model = SentenceTransformer('BAAI/bge-large-zh-v1.5')

# 2. 准备文档
documents = [
    "机器学习是人工智能的一个分支，通过数据训练模型来进行预测",
    "深度学习使用多层神经网络来学习数据的复杂特征",
    "Python是最流行的编程语言之一，广泛用于数据科学",
    "RAG是检索增强生成，结合检索和生成模型的优势",
    "向量数据库用于存储和检索高维向量表示",
    "自然语言处理让计算机能够理解和生成人类语言",
]

# 3. 生成向量并入库
embeddings = model.encode(documents).tolist()
ids = [f"doc_{i}" for i in range(len(documents))]

collection.add(
    documents=documents,
    embeddings=embeddings,
    ids=ids,
    metadatas=[{"source": f"chunk_{i}"} for i in range(len(documents))]
)

print(f"已入库 {collection.count()} 条文档")