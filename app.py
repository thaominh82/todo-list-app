# app.py
tasks = []

def add_task(task_name):
    tasks.append({'name': task_name, 'completed': False})

def complete_task(task_index):
    if 0 <= task_index < len(tasks):
        tasks[task_index]['completed'] = True
        print(f"Đã đánh dấu hoàn thành: {tasks[task_index]['name']}")
    else:
        print("Chỉ số công việc không hợp lệ.")

def list_tasks():
    if not tasks:
        print("Danh sách công việc trống.")
    else:
        print("Danh sách công việc:")
        for i, task in enumerate(tasks, 1):
            status = "[x]" if task['completed'] else "[ ]"
            print(f"{i}. {status} {task['name']}")

if __name__ == "__main__":
    add_task("Học bài Git")
    add_task("Làm bài tập Python")
    complete_task(0)
    list_tasks()
