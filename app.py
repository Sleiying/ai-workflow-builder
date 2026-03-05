import streamlit as st
from workflow import run_workflow

st.set_page_config(page_title="AI Workflow Builder", page_icon="🤖")
st.title("🤖 AI Workflow Builder")

task = st.text_input("请输入任务", "制作一款智能护眼台灯的抖音推广方案")

if st.button("🚀 开始执行工作流"):
    # 1. 使用 spinner 替代 status，解决嵌套冲突
    with st.spinner("Agent 正在规划并执行任务，请稍候..."):
        log = run_workflow(task)
        
    st.success("🎉 任务执行完毕！")
    
    # 2. 将结果平铺展示，作为产品经理/研发的 Demo 视觉效果更好
    for item in log:
        with st.expander(f"✅ {item['step']}", expanded=True):
            st.markdown(item["result"])
