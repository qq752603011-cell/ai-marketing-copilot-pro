import streamlit as st

st.title("🚀 AI Prompt Studio")

industry = st.selectbox(
    "选择行业",
    ["电商", "教育", "房地产"]
)

task = st.selectbox(
    "选择任务",
    ["文案", "客服", "视频脚本"]
)

if st.button("生成 Prompt"):
    prompt = f"""
你是一位资深{industry}行业专家。

请帮助我完成{task}任务。

要求：
1. 专业
2. 清晰
3. 直接输出结果
"""

    st.code(prompt)