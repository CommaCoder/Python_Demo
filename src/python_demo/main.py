import os
from src.python_demo.service.todo_service import add_task,delete_task,update_task,show_tasks,save_tasks,load_tasks,toggle_task_status,set_task_priority

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
        print("6. 标记任务完成/未完成")
        print("7. 修改任务优先级")

        choice = input("请输入功能序号(1~7):")

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
                user_num=int(input("请输入要删除的任务ID："))
                delete_task(tasks,user_num)
            except ValueError:
                print("❌ 输入不是有效数字！")

        elif choice == "4":
            show_tasks(tasks)
            try:
                user_num = int(input("请输入要修改的任务序号："))
                new_text = input("输入任务新内容：")
                update_task(tasks, user_num, new_text)
            except ValueError:
                print("❌ 输入不是有效数字！")

        elif choice == "5":

            save_tasks(tasks, json_file_path)
            print("💾 任务已保存到 tasks.json")
            print("👋 程序退出")
            break

        elif choice == "6":
            show_tasks(tasks)

            try:
                task_id=int(input("请输入要切换状态的任务ID："))
                toggle_task_status(tasks,task_id)

            except ValueError:
                print("❌ 输入不是有效数字！")

        elif choice =="7":
            show_tasks(tasks)
            try:
                task_id = int(input("请输入要修改优先级的任务ID："))
                pri = int(input("请输入优先级(1高,2中,3低)："))
                set_task_priority(tasks, task_id, pri)
            except ValueError:
                print("❌ 输入不是有效数字！")
            
        else:
            print("❌ 无效选项，请输入1-6之间数字")

if __name__=="__main__":
    main()


