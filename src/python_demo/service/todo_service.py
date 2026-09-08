import json
import os

def add_task(tasks, task):
    """向任务列表追加任务"""
    tasks.append(task)

def show_tasks(tasks):
    """展示全部任务"""
    if len(tasks) == 0:
        print("⚠️ 当前暂无任务")
        return
    print("\n===== 任务列表 =====")
    for idx, task in enumerate(tasks):
        print(f"{idx + 1}. {task}")
    print("====================\n")

def delete_task(tasks, index):
    """按列表原生下标（0开始）删除任务"""
    if 0 <= index < len(tasks):
        del tasks[index]
        print("✅ 任务删除成功")
    else:
        print("❌ 任务序号不存在，删除失败")

def update_task(tasks, index, new_task):
    """修改指定下标任务内容"""
    if 0 <= index < len(tasks):
        tasks[index] = new_task
        print("✅ 任务修改成功")
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
