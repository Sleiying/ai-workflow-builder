from tools import call_llm, generate_script, generate_title, generate_tags
from prompts import PLANNER_PROMPT

def run_workflow(task):
    log = []
    
    plan = call_llm(PLANNER_PROMPT.format(task=task))
    log.append({"step": "1. 规划工作流", "result": plan})
    
    script = generate_script(task)
    log.append({"step": "2. 生成脚本", "result": script})
    
    title = generate_title(script)
    log.append({"step": "3. 提取标题", "result": title})
    
    tags = generate_tags(script)
    log.append({"step": "4. 输出标签", "result": tags})
    
    return log
