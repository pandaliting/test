import os
from dotenv import load_dotenv
from langchain_community.chat_models import ChatTongyi

# 1、创建模型的客户端
load_dotenv(verbose=True)
llm = ChatTongyi(
    api_key=os.getenv("CHAT_API_KEY"),
    model='qwen3.7-max',
)

# 定义历史对话
chat_history = []

# 第一次：用户自我介绍
user_message_1 = "我是一个AI老师。"
chat_history.append(("user", user_message_1))

# 拼接所有对话为上下文
context = "\n".join([f"{role}: {msg}" for role, msg in chat_history])
ai_reply_1 = llm.invoke(context).content
chat_history.append(("assistant", ai_reply_1))
print("第一次AI回复:", ai_reply_1)
# 记忆
# 第二次：带完整历史对话提问
user_message_2 = "我是谁"
chat_history.append(("user", user_message_2))  # ← 先加入历史

# 拼接完整上下文再调用
context = "\n".join([f"{role}: {msg}" for role, msg in chat_history])
ai_reply_2 = llm.invoke(context).content
chat_history.append(("assistant", ai_reply_2))
print("第二次AI回复:", ai_reply_2)

# 近期对话+摘要+关键信息 （构成完整的信息）
