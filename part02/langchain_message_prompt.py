import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv(override=True)
DASHSCOPE_API_KEY = os.getenv("DASHSCOPE_API_KEY")
DASHSCOPE_BASE_URL = os.getenv("DASHSCOPE_BASE_URL")

MODEL_NAME = "qwen3.7-max"
MAX_PAIRS_HISTORY = 10
EXIT_WORD = "quit"

qwen_chat = ChatOpenAI(
    model=MODEL_NAME,
    api_key=DASHSCOPE_API_KEY,
    base_url=DASHSCOPE_BASE_URL,
    extra_body={"enable_thinking": False},  # 关闭思考，避免流式卡住
)

# 保留最近 N 对对话（system + 最近 N 轮 user/assistant）
def keep_recent_messages(msgs, max_pairs=10):
    system = [m for m in msgs if m["role"] == "system"]
    history = [m for m in msgs if m["role"] != "system"]
    # 每对 = user + assistant，保留最后 max_pairs*2 条
    return system + history[-(max_pairs * 2):]

messages = [{  # ← 改成 messages（复数）
    "role": "system",
    "content": "你是小谷姐姐，尚硅谷教育的数字员工，也是一名耐心、友好的智能助手。我会用自然、清晰的方式回答用户问题。"
}]

print(f"✨ 请输入问题，输入 {EXIT_WORD} 结束对话\n")

i = 1
while True:
    print("\n", "=" * 10, f'-> 第 {i} 轮对话开始 <-', "=" * 10, "\n")
    user_input = input("🙋 请输入：")

    # 退出判断（break 必须在 if 里面）
    if user_input.lower() == EXIT_WORD:
        print("🌙 对话已结束，欢迎下次再来！")
        break

    messages.append({"role": "user", "content": user_input})

    print("🧚 小谷姐姐：", end="", flush=True)
    reply_content = ""
    memory_messages = keep_recent_messages(messages, max_pairs=MAX_PAIRS_HISTORY)

    # 流式输出（缩进要对齐）
    for chunk in qwen_chat.stream(memory_messages):  # ← qwen_chat，不是 model
        if chunk.content:
            print(chunk.content, end="", flush=True)
            reply_content += chunk.content

    print("\n", "=" * 10, f'-> 第 {i} 轮对话结束 <-', "=" * 10, "\n")
    i += 1

    messages.append({"role": "assistant", "content": reply_content})
