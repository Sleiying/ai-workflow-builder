# AI Workflow Builder 自动工作流智能体

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.32.0-FF4B4B)
![LLM](https://img.shields.io/badge/LLM-OpenAI%20SDK%20%7C%20Qwen-000000)

## 背景

随着大模型能力的演进，AI 正在从“单次对话问答”向“复杂任务规划与执行（Agentic Workflow）”转变。本项目旨在通过极简的代码架构，探索并实现一个端到端的 AI 自动化工作流系统。

用户只需输入一个宏观任务（如“制作抖音电商推广方案”），系统即可自动完成：**任务理解与拆解 (Planning)** -> **工具链按序调用 (Tool Calling)** -> **结果流式输出 (Execution)**。

## 功能

1. **🧠 任务拆解 ：** 输入复杂任务后，Agent 自动将其拆解为逻辑连贯的标准化执行步骤。
2. **🛠️ 工具调用 ：** 基于大模型的上下文理解能力，按序触发不同职能的 Tool（如：脚本编导、文案优化、爆款标签提取）。
3. **👁️ 可视化交互：** 采用 Streamlit 构建响应式 UI，实时展示 Agent 的思考与执行状态，提供极佳的“呼吸感”产品体验。

## 界面
![网站_page-0001](https://github.com/user-attachments/assets/1e9a2984-5507-45b1-afa4-b87f65bcc6fa)
![网站_page-0002](https://github.com/user-attachments/assets/23987ce7-e85a-4793-b036-827aa66f9632)
![网站_page-0003](https://github.com/user-attachments/assets/2fd29c6d-428c-4b6d-9912-da6b7681ec8a)
![网站_page-0004](https://github.com/user-attachments/assets/002816b3-467b-45be-98ba-0080d27d0fdb)
![网站_page-0005](https://github.com/user-attachments/assets/3af8cd9c-291e-4fb2-8fcb-4078752cd44d)


## 系统架构

```text
User Input (复杂任务描述)
   │
   ▼
[ Task Analyzer & Planner ]  ──> 将任务拆解为 Step 1, 2, 3...
   │
   ▼
[ Tool Executor Pipeline ]
   ├─ Tool 1: 生成产品核心卖点/脚本
   ├─ Tool 2: 提炼高点击率文案/标题
   └─ Tool 3: 匹配高流量分发标签
   │
   ▼
Final Output (结构化方案输出)
```

## 🚀 快速开始 (Quick Start)

### 1. 环境准备
确保你的本地已安装 Python 3.9+，然后克隆本项目并安装依赖：

```bash
git clone [https://github.com/Sleiying/ai-workflow-builder.git](https://github.com/Sleiying/ai-workflow-builder.git)
cd ai-workflow-builder
pip install -r requirements.txt
```
## 2. 配置 API Key
本项目默认使用兼容 OpenAI SDK 的接口（如阿里云通义千问 Qwen）。
打开 tools.py，将其中的 API_KEY 替换为你自己的真实 Key。

## 3. 运行项目

```Bash
streamlit run app.py
浏览器将自动打开 http://localhost:8501，即可开始体验。
```
## Roadmap
目前的版本跑通了纯文本模态下的 Agent 核心工作流，未来的迭代将向更具挑战性的多模态与工程质量校验方向延伸：

[○] Phase 1: 基于 LLM 的文本任务规划与自动化执行引擎。

[ ] Phase 2: 跨模态扩展。在脚本生成节点后，自动对接视频生成 API，实现从文案到视频的完整生产链路。

[ ] Phase 3: 自动化质量评测机制。在生成流转中引入 FVD (Fréchet Video Distance) 指标，让 Agent 自动评估生成视频序列的连续性与质量；针对复杂空间旋转场景下的单体细节崩坏问题，计划探索利用 DUSt3R 提取三维空间特征，构建专属的“一致性视觉校验 Agent”，以保障最终输出的工业级可用性。

### 本项目为Demo，欢迎交流探讨。
