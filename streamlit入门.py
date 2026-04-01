import streamlit as st

# 大标题
st.title("Streamlit 入门演示")
st.header("Streamlit 一级标题")
st.subheader("Streamlit 二级标题")

# 段落文字
st.write("如果我是di，你会爱我吗")
st.write("请你不要再迷恋哥")
st.write("I'm nothing but a legend.")

# 图片
st.image("./resources/123.png")

# 视频
st.video("./resources/234.mp4")

# log
st.logo("./resources/cat.png")

# 表格
student_data = {
    "姓名": ["夜宵", "烧烤", "火锅"],
    "学号": ["1", "2", "3"]
}

st.table(student_data)

# 输入框
name = st.text_input("请输入姓名")
st.write(f"您输入的姓名为:{name}")

password = st.text_input("请输入密码", type="password")
st.write(f"您输入的姓名为:{password}")

# 单选按钮
st.radio("请输入您的性别", ["男", "女"], index=1)