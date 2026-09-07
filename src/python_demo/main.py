def add_task(tasks,task):
    tasks.append(task)

def main():
    tasks=[]

    
    

    while True:
        task=input("请输入一个任务(输入q结束):")
        
        if task=="q":
            break

        add_task(tasks,task)

        
    print("你的任务列表是")
    print(tasks)

if __name__=="__main__":
    main()

