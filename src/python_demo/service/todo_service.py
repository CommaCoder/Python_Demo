import json
import os
from datetime import datetime


def show_tasks(tasks):
    """展示全部任务"""
    if len(tasks) == 0:
        print("⚠️ 当前暂无任务")
        return
    print("\n===== 任务列表 =====")
    for task in tasks:
        pri_text = {1:"[高]",2:"[中]",3:"[低]"}[task["priority"]]
        print(f"{task['id']}. {pri_text} {task['content']} {'[✓]' if task['done'] else '[]'}       创建时间:{task['create_time']}  更新时间:{task['update_time']}")
    print("====================\n")


def delete_task(tasks, task_id):
    """按列ID删除任务"""
    for task in tasks:
        if task["id"]==task_id:
            tasks.remove(task)
            print("✅ 任务删除成功")
            return True
    else:
        print("❌ 任务序号不存在，删除失败")
        return False
            

def update_task(tasks, task_id, new_content):
    """修改指定任务内容"""
    for task in tasks:
        if task["id"]==task_id:
            task["content"]=new_content
            task["update_time"]=get_now_str()
            print("✅ 任务修改成功")
            return True
    else:
        print("❌ 任务序号不存在，修改失败")
        return False


def save_tasks(tasks, file_path):
    """将任务列表保存到JSON文件"""
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(tasks, f, ensure_ascii=False, indent=2)

def load_tasks(file_path):
    """读取JSON文件，加载任务；文件不存在返回空列表"""
    if not os.path.exists(file_path):
        return []
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)

def generate_next_id(tasks):
    if not tasks:
        return 1
    
    max_id=max(task["id"] for task in tasks)
    return max_id+1

def add_task(tasks, content):
    """向任务列表追加任务"""
    now=get_now_str()
    task={"id":generate_next_id(tasks),
          "content":content,
          "done":False,
          "priority":2,
          "create_time":now,
          "update_time":now
        
          }
    tasks.append(task)


def toggle_task_status(tasks,task_id):
    for task in tasks:
        if task["id"]==task_id:
            task["done"]=not task["done"]
            task["update_time"]=get_now_str()
            print("✅ 任务状态切换成功")
            return True
    else:
        print("❌ 任务ID不存在，切换失败")
        return False

def set_task_priority(tasks, task_id, priority_level):
    """设置任务优先级，仅允许1/2/3"""
    # 先判断priority_level是不是合法
    if priority_level not in (1,2,3):
        print("❌ 优先级只能是1(高)、2(中)、3(低)")
        return False
    # 遍历查找task_id，找到就赋值task["priority"] = priority_level
    for task in tasks:
        if task["id"]==task_id:
            task["priority"]=priority_level
            task["update_time"]=get_now_str()
            print("✅ 任务优先级修改成功")
            return True
    else:
        print("❌ 任务ID不存在，修改优先级失败")
        return False



def get_now_str():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

