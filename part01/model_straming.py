import os

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

# 通用的opanapi调用百炼模型 兼容用法
load_dotenv(override=True)

DASHSCOPE_API_KEY = os.getenv("DASHSCOPE_API_KEY")
DASHSCOPE_BASE_URL = os.getenv("DASHSCOPE_BASE_URL")

# qwen3.7-max 本身带思考功能，所以需要extra_body 关闭思考功能
qwen_chat = ChatOpenAI(
    model="qwen3.7-max",
    api_key=DASHSCOPE_API_KEY,
    base_url=DASHSCOPE_BASE_URL,
    extra_body={"enable_thinking": False}
)

for chunk in qwen_chat.stream("写一七言律诗,总结大模型的发展"):
    print(chunk.content, end="", flush=True)
