from openai import OpenAI
import os, dotenv

dotenv.load_dotenv(override=True)

client = OpenAI(
    api_key=os.getenv("DASHSCOPE_API_KEY"),
    base_url=os.getenv("DASHSCOPE_BASE_URL"),
)

for m in client.models.list().data:
    print(m.id)