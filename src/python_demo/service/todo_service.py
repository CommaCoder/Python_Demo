import json
import os



def show_tasks(tasks):
    """展示全部任务"""
    if len(tasks) == 0:
        print("⚠️ 当前暂无任务")
        return
    print("\n===== 任务列表 =====")
    for task in tasks:
        print(f"{task['id']}. {task['content']} {'[✓]' if task['done'] else '[]'}")
    print("====================\n")


def delete_task(tasks, task_id):
    """按列表原生下标（0开始）删除任务"""
    for task in tasks:
        if task["id"]==task_id:
            tasks.remove(task)
            print("✅ 任务删除成功")
            break
    else:
        print("❌ 任务序号不存在，删除失败")
            

def update_task(tasks, task_id, new_content):
    """修改指定下标任务内容"""
    for task in tasks:
        if task["id"]==task_id:
            task["content"]=new_content
            print("✅ 任务修改成功")
            break
    else:
        print("❌ 任务序号不存在，修改失败")


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
    task={"id":generate_next_id(tasks),"content":content,"done":False}
    tasks.append(task)


def toggle_task_status(tasks,task_id):
    for task in tasks:
        if task["id"]==task_id:
            task["done"]=not task["done"]
            print("✅ 任务状态切换成功")
            break
    else:
        print("❌ 任务ID不存在，切换失败")

