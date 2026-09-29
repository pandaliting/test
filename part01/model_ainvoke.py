import asyncio
import os
import time
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
async def demo_async_invoke():
    print("计算异步任务")
    start_time = time.perf_counter()  # 计算开始时间
    print("程序开始")
    # 执行第一个任务
    asyncio.create_task(qwen_chat.ainvoke("用一句话解释人工智能"))
    # 执行第二个任务
    print("模型已在后台运行，执行第二个任务")
    
