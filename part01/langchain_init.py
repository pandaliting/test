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
response = dashscope_chat.invoke(
    "张三，男，30岁，拥有8年编程开发经验，目前在某互联网大厂担任技术专家。帮我从上文中提取数据，返回JSON格式")
# response.pretty_print()
rprint(response)
