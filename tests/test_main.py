import tempfile
import os
from src.python_demo.service.todo_service import add_task, delete_task, update_task, save_tasks, load_tasks,toggle_task_status,set_task_priority

def test_add_task():
    tasks = []
    add_task(tasks, "写Python代码")
    assert len(tasks) == 1
    task1 = tasks[0]
    assert task1["id"] == 1
    assert task1["content"] == "写Python代码"

    add_task(tasks, "学习pytest")
    assert len(tasks) == 2
    task2 = tasks[1]
    assert task2["id"] == 2
    assert task2["content"] == "学习pytest"


def test_delete_task():
    tasks = []
    add_task(tasks, "任务A")
    add_task(tasks, "任务B")
    # 删除id=1
    delete_task(tasks, 1)
    assert len(tasks) == 1
    assert tasks[0]["id"] == 2

    # 删除不存在id，列表保持不变
    delete_task(tasks, 999)
    assert len(tasks) == 1


def test_update_task():
    tasks = []
    add_task(tasks, "旧内容")
    update_task(tasks, 1, "新内容")
    assert tasks[0]["content"] == "新内容"
    assert tasks[0]["id"] == 1  # id不变

    # 修改不存在id，数据不变
    update_task(tasks, 999, "随便写")
    assert tasks[0]["content"] == "新内容"


def test_save_and_load_tasks():
    tasks = []
    add_task(tasks, "保存测试任务")
    with tempfile.NamedTemporaryFile(mode="w", delete=False, encoding="utf-8") as f:
        temp_path = f.name
    try:
        save_tasks(tasks, temp_path)
        loaded_tasks = load_tasks(temp_path)
        assert len(loaded_tasks) == 1
        assert loaded_tasks[0]["id"] == 1
        assert loaded_tasks[0]["content"] == "保存测试任务"
    finally:
        os.unlink(temp_path)


def test_load_file_not_exist():
    non_exist_path = "no_such_file_12345.json"
    tasks = load_tasks(non_exist_path)
    assert tasks == []


def test_toggle_task_status():
    tasks = []
    add_task(tasks, "测试切换状态")
    # 新建默认未完成
    assert tasks[0]["done"] is False
    # 第一次切换 → 变成True
    toggle_task_status(tasks, 1)
    assert tasks[0]["done"] is True
    # 第二次切换 → 变回False
    toggle_task_status(tasks, 1)
    assert tasks[0]["done"] is False

    # 切换不存在ID，列表无变化
    toggle_task_status(tasks, 999)
    assert tasks[0]["done"] is False

def test_set_task_priority():
    tasks = []
    add_task(tasks, "优先级测试任务")
    # 默认优先级=2（中）
    assert tasks[0]["priority"] == 2

    # 修改为高优先级1
    set_task_priority(tasks, 1, 1)
    assert tasks[0]["priority"] == 1
    # 修改为低优先级3
    set_task_priority(tasks, 1, 3)
    assert tasks[0]["priority"] == 3

    # 非法优先级，不改变
    set_task_priority(tasks,1,99)
    assert tasks[0]["priority"] == 3

    # 不存在ID，无变化
    set_task_priority(tasks,999,1)
    assert tasks[0]["priority"] ==3
