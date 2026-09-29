# 演示大语言模型的无状态性
# 对话的记忆管理

import os
from dotenv import load_dotenv
from langchain_community.chat_models import ChatTongyi

# 1、创建模型的客户端
load_dotenv(verbose=True)
llm = ChatTongyi(
    api_key=os.getenv("CHAT_API_KEY"),
    model='qwen3.7-max',
)

# 记录第一次对话
user_query = '你好，我是一个AI老师'
ai_response = llm.invoke(user_query)
print("AI第一次回复：", ai_response)
# 记录第二次对话
user_query2 = '我是谁？'
ai_response = llm.invoke(user_query2)
print("Ai第二次回复：", ai_response)
