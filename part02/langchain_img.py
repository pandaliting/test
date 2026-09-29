import os
import base64
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage

load_dotenv(override=True)

qwen_chat = ChatOpenAI(
    model="qwen-3.7-max",                                        # ← 视觉模型
    api_key=os.getenv("DASHSCOPE_API_KEY"),
    base_url=os.getenv("DASHSCOPE_BASE_URL"),
)

def encode_image(img_path):
    with open(img_path, "rb") as f:
        b64 = base64.b64encode(f.read()).decode("utf-8")
    ext = img_path.rsplit(".", 1)[-1]                           # 自动识别 png/jpg
    return f"data:image/{ext};base64,{b64}"

response = qwen_chat.invoke([
    HumanMessage(content_blocks=[
        {"type": "text", "text": "这张图里有什么？"},
        {"type": "image_url", "image_url": {"url": encode_image("img.png")}},
    ])
])
print(response.content)
