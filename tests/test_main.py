import os
import json
import tempfile
from src.python_demo.service.todo_service import *

def test_add_task():
    tasks = []
    add_task(tasks, "写代码")
    assert len(tasks) == 1
    assert tasks[0] == "写代码"

def test_delete_task():
    tasks = ["任务1", "任务2"]
    delete_task(tasks, 0)
    assert tasks == ["任务2"]
    # 删除不存在下标，列表不变
    delete_task(tasks, 99)
    assert tasks == ["任务2"]

def test_update_task():
    tasks = ["任务1"]
    update_task(tasks, 0, "修改后的任务")
    assert tasks[0] == "修改后的任务"
    update_task(tasks, 99, "xxx")
    assert tasks[0] == "修改后的任务"

def test_save_and_load_tasks():
    # 创建临时json文件，测试读写，用完自动删除
    with tempfile.NamedTemporaryFile(mode="w", delete=False, encoding="utf-8") as f:
        temp_path = f.name
    try:
        origin_tasks = ["语文", "数学"]
        save_tasks(origin_tasks, temp_path)
        loaded = load_tasks(temp_path)
        assert loaded == origin_tasks
    finally:
        os.unlink(temp_path)

def test_load_file_not_exist():
    fake_path = "not_exist_xxx123.json"
    res = load_tasks(fake_path)
    assert res == []
