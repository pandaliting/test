import os

from dotenv import load_dotenv
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
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
    SystemMessage(content="你是一个python专家"),
    HumanMessage(content="什么是生成器python"),
]
response = qwen_chat.invoke(message)
# print(response)
# 继续对话
message.append(AIMessage(content=response.content))
message.append(SystemMessage(content="能举个例子吗？"))
for chunk in qwen_chat.stream(message):
    print(chunk.content,end = "",flush=True)
