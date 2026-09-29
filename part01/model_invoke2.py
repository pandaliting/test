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
# 使用了assistant 带有记忆的内容 字典
message = [
    {"role": "system", "content": "AI助手"},
    {"role": "user", "content": "你好，我叫小猫"},
    {"role": "assistant", "content": "AI回复"},
]
print(qwen_chat.invoke(message).content)

message.append({"role": "user", "content": "我叫什么名字？"})
print(qwen_chat.invoke(message).content)
