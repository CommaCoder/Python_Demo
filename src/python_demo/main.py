import json
import os


def add_task(tasks,task):
    """向任务列表追加任务"""
    tasks.append(task)

def show_tasks(tasks):
    """展示全部任务"""
    if len(tasks)==0:
        print("⚠️ 当前暂无任务")
        return 
    print("\n===== 任务列表 =====")
    for idx,task in enumerate(tasks):
        print(f"{idx + 1}. {task}")
    print("====================\n")

def delete_task(tasks,index):
    if 0<=index<len(tasks):
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


def save_tasks(tasks,file_path):
    with open(file_path,"w",encoding="utf-8") as f:
        json.dump(tasks,f, ensure_ascii=False, indent=2)

def load_tasks(file_path):
    """读取JSON文件,加载任务;文件不存在返回空列表"""
    if not os.path.exists(file_path):
        return []
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)


def main():
    
    json_file_path="tasks.json"
    tasks=load_tasks(json_file_path)

    while True:
        print("===== TodoList 主菜单 =====")
        print("1. 添加任务")
        print("2. 查看全部任务")
        print("3. 删除任务")
        print("4. 修改任务")
        print("5. 退出程序")
        choice = input("请输入功能序号(1~5):")

        if choice=="1":
            print("\n--- 添加任务（输入q结束添加）---")
            # 内层子循环：持续添加任务
            while True:
                user_input = input("请输入任务内容：")
                if user_input == "q":
                    break
                # 过滤空任务
                if user_input.strip() == "":
                    print("⚠️ 任务不能为空，请重新输入")
                    continue
                add_task(tasks, user_input)

        elif choice=="2":
            show_tasks(tasks)

        elif choice == "3":
            show_tasks(tasks)
            try:
                user_num=int(input("请输入要删除的任务序号："))
                real_index=user_num-1
                delete_task(tasks,real_index)
            except ValueError:
                print("❌ 输入不是有效数字！")

        elif choice == "4":
            show_tasks(tasks)
            try:
                user_num = int(input("请输入要修改的任务序号："))
                real_index = user_num - 1
                new_text = input("输入任务新内容：")
                update_task(tasks, real_index, new_text)
            except ValueError:
                print("❌ 输入不是有效数字！")

        elif choice == "5":

            save_tasks(tasks, json_file_path)
            print("💾 任务已保存到 tasks.json")
            print("👋 程序退出")
            break

        else:
            print("❌ 无效选项，请输入1-5之间数字")

if __name__=="__main__":
    main()

