import streamlit as st
from openai import OpenAI

# 设置页面的配置项
st.set_page_config(
    page_title="AI智能伴侣",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={}
)

# 大标题
st.title("AI智能伴侣")



# 系统提示词
system_prompt = "你是一名非常有魄力的AI助理，你的名字叫聪叔叔，请你使用霸气的语气回答用户的问题"

# 初始化客户端
client = OpenAI(
    api_key=st.secrets["DEEPSEEK_API_KEY"],
    base_url="https://api.deepseek.com/v1"
)

# 消息输入框
prompt = st.chat_input("请输入您要问的问题")

# 只有用户输入了内容，才执行下面的逻辑
if prompt:
    # 1. 显示用户消息
    st.chat_message("user").write(prompt)
    print("调用AI大模型，提示词: ", prompt)

    # 2. 调用AI大模型
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt},
        ],
        stream=False
    )

    # 3. 输出大模型返回的结果（控制台+页面）
    print("<---------- 大模型返回的结果: ", response.choices[0].message.content)
    with st.chat_message("assistant"):
        # 用st.text禁用Markdown，避免横线问题
        st.text(response.choices[0].message.content)
