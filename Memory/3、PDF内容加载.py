from langchain_community.document_loaders import PyMuPDFLoader

# 加载绝对路径
file_path = "/Users/zhouhaijun/Desktop/AI_Learning/langchain_1.2/asset/load/04-sample.pdf"
docx = PyMuPDFLoader(file_path).load()

for doc in docx:
    print(doc)
