import os

from dotenv import load_dotenv
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_openai import ChatOpenAI

from rich import print as rprint

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
    HumanMessage(content="2 + 3 * 2 = ?"),
]
print(qwen_chat.invoke(message).content)
print("--------")

rprint(message)
