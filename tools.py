import os
from openai import OpenAI
from prompts import SCRIPT_PROMPT, TITLE_PROMPT, TAGS_PROMPT

# 大模型 API Key 和 Base URL 
API_KEY = "sk-b7830137861a47268a54ae139be82c5d"
BASE_URL = "https://dashscope.aliyuncs.com/compatible-mode/v1" 

client = OpenAI(api_key=API_KEY, base_url=BASE_URL)

def call_llm(prompt):
    response = client.chat.completions.create(
        #指定使用的模型qwen-turbo默认响应快
        model="qwen-turbo", 
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )
    return response.choices[0].message.content

def generate_script(topic): return call_llm(SCRIPT_PROMPT.format(topic=topic))
def generate_title(script): return call_llm(TITLE_PROMPT.format(script=script))
def generate_tags(script): return call_llm(TAGS_PROMPT.format(script=script))
