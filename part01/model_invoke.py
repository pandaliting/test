import os

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

# 通用的opanapi调用百炼模型 兼容用法
load_dotenv(override=True)

DASHSCOPE_API_KEY = os.getenv("DASHSCOPE_API_KEY")
DASHSCOPE_BASE_URL = os.getenv("DASHSCOPE_BASE_URL")

qwen_chat = ChatOpenAI(
    model="qwen3.7-max",
    api_key=DASHSCOPE_API_KEY,
    base_url=DASHSCOPE_BASE_URL
)

message = [
    {"role": "system", "content": "你是一个专业的数学家"},
    {"role": "user", "content": "解释一下什么叫等比数列"}
]
print(qwen_chat.invoke(message).content)
