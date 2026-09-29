import os
from dotenv import load_dotenv
from langchain_community.chat_models import ChatTongyi

# 百炼的api-key 调用模型
load_dotenv(verbose=True)
DASHSCOPE_API_KEY = os.getenv("dashscope_api_key")

tongyi_chat = ChatTongyi(
    api_key=DASHSCOPE_API_KEY,
    model="qwen3.7-max"
)
# option + command + l
print(tongyi_chat.invoke("介绍下你自己"))
