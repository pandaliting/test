from langchain_community.document_loaders import PyMuPDFLoader, TextLoader

# 加载绝对路径,加载PDF文本
file_path = "/Users/zhouhaijun/Desktop/AI_Learning/langchain_1.2/asset/load/04-sample.pdf"
docx = PyMuPDFLoader(file_path).load()
for doc in docx:
    print(doc)
# 加载txt
file_path1 = "/Users/zhouhaijun/Desktop/AI_Learning/langchain_1.2/asset/load/09-ai.txt"
docx1 = TextLoader(file_path1, encoding="utf-8").load()
for doc in docx1:
    print(doc)



