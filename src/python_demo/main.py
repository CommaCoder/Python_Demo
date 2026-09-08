import os
from src.python_demo.service.todo_service import *



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

