import dotenv
import os
from rich import print as rprint
from langchain.chat_models import init_chat_model
from openai import max_retries

dotenv.load_dotenv(override=True)
DASHSCOPE_API_KEY = os.getenv("DASHSCOPE_API_KEY")
DASHSCOPE_BASE_URL = os.getenv("DASHSCOPE_BASE_URL")

# temperature 从低到高 越大越随机
dashscope_chat = init_chat_model(
    model='openai:qwen3.7-max',
    api_key=DASHSCOPE_API_KEY,
    base_url=DASHSCOPE_BASE_URL,
    temperature=0,
    max_tokens=2000,
    max_retries=10
)
# 通过JSON初始化
message = [{"role": "system", "content": "你是一个善解人意的助手"},
           {"role": "assistant", "content": "你好，我能帮助你什么"},
           {"role": "user", "content": "什么是机器学习"}]
response = dashscope_chat.invoke(message)
print(response.content)
