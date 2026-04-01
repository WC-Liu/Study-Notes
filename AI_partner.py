import streamlit as st
from openai import OpenAI
import os

#布局设置
st.set_page_config(
    # 页面标题
    page_title="AI 智能伴侣",
    # 页面图标
    page_icon = "🤖",
    # 布局
    layout="wide",
    # 控制侧边栏状态
    initial_sidebar_state="expanded",
    # 菜单
    menu_items={}
)

# 大标题
st.title("AI 智能伴侣")

# logo
st.logo("resources/cat.png")

# 系统提示词
system_promt = "你是个智能助手，请你回答我的问题"

# 创建会话
if "message" not in st.session_state:
    st.session_state.message = []   #如果state中没有message，则创建一个message列表

# 展示聊天信息
for message in st.session_state.message:
    st.chat_message(message["role"]).write(message["content"])


# 调用本地模型
client = OpenAI(
    base_url="http://localhost:11434/v1",  # 本地接口地址
    api_key="not-needed"  # 本地模型不需要真实 key
)

# 聊天框
promt = st.chat_input("请输入你的问题")

# 用户输入
if promt:
    st.chat_message("user").write(promt)
    print("-----------> 调用AI大模型，提示词：", promt)

    # 保存用户输入
    st.session_state.message.append({"role": "user", "content":promt})

    # 调用模型
    resp = client.chat.completions.create(
        model="qwen2.5:7b",         # 你本地的模型名
        messages=[
            {"role": "system", "content": system_promt},
            *st.session_state.message # 将之前的所有会话内容传入模型
        ],

        temperature=0.7,  # 模型参数（均衡模式）
        stream=True  # 关闭流式输出
    )


    #-----------------非流式输出方式----------------
    # 输出结果
    # print("-----------> 模型返回结果：", resp.choices[0].message.content)
    # 保存结果
    # st.chat_message("assistant").write(resp.choices[0].message.content)



    #------------------流式输出---------------------
    response_message = st.empty()
    full_response = ""
    for chunk in resp:
        if chunk.choices[0].delta.content is not None:
            content = chunk.choices[0].delta.content
            full_response += content
            response_message.chat_message("assistant").write(full_response)

    # 保存大模型返回结果
    st.session_state.message.append({"role": "assistant", "content": full_response})