import tkinter as tk


def add_task():
    task = task_entry.get()
    if task:
        task_liststart.insert(tk.END, task)
        task_entry.delete(0, tk.END)

def delete_task():
    selected_task = task_liststart.curselection()
    if selected_task:
        task_liststart.delete(selected_task)

    selected_task = task_listbeing.curselection()
    if selected_task:
        task_listbeing.delete(selected_task)

    selected_task = task_listfinish.curselection()
    if selected_task:
        task_listfinish.delete(selected_task)

def mark_task():
    selected_task = task_liststart.curselection()
    if selected_task:
        task_liststart.itemconfig(selected_task, bg="#000")

    selected_task = task_listbeing.curselection()
    if selected_task:
        task_listbeing.itemconfig(selected_task, bg="#000")

    selected_task = task_listfinish.curselection()
    if selected_task:
        task_listfinish.itemconfig(selected_task, bg="#000")


def tostart_task():
    selected_task = task_listbeing.curselection()
    if selected_task:
        task_liststart.insert(tk.END, task_listbeing.get(selected_task))
        task_listbeing.delete(selected_task)

    selected_task = task_listfinish.curselection()
    if selected_task:
        task_liststart.insert(tk.END, task_listfinish.get(selected_task))
        task_listfinish.delete(selected_task)


def tobeing_task():
    selected_task = task_liststart.curselection()
    if selected_task:
        task_listbeing.insert(tk.END, task_liststart.get(selected_task))
        task_liststart.delete(selected_task)

    selected_task = task_listfinish.curselection()
    if selected_task:
        task_listbeing.insert(tk.END, task_listfinish.get(selected_task))
        task_listfinish.delete(selected_task)


def tofinish_task():
    selected_task = task_liststart.curselection()
    if selected_task:
        task_listfinish.insert(tk.END, task_liststart.get(selected_task))
        task_liststart.delete(selected_task)

    selected_task = task_listbeing.curselection()
    if selected_task:
        task_listfinish.insert(tk.END, task_listbeing.get(selected_task))
        task_listbeing.delete(selected_task)


root = tk.Tk()
root.title("Система управления задачами")
root.configure(background="#F0F0F5")

frame_panel = tk.Frame(root)
frame_panel.pack()

text_head = tk.Label(frame_panel, text="Введите вашу задачу:", fg="#333333")
text_head.pack(pady=5)

task_entry = tk.Entry(frame_panel, width=30, bg="#FFFFFF", font="sans-serif")
task_entry.pack(pady=10)

add_task_button = tk.Button(frame_panel, text="Добавить задачу", bg="#4CAF50", fg="#fff", command=add_task)
add_task_button.pack(pady=5)

delete_button = tk.Button(frame_panel, text="Удалить задачу", bg="#4CAF50", fg="#fff", command=delete_task)
delete_button.pack(pady=5)

mark_button = tk.Button(frame_panel, text="Отметить задачу", bg="#4CAF50", fg="#fff", command=mark_task)
mark_button.pack(pady=(5, 10))


frame_grid = tk.Frame(root)
frame_grid.pack()


liststart_button = tk.Button(frame_grid, text="Переместить в невыполненные", bg="#00f", fg="#fff", command=tostart_task)
liststart_button.grid(row=0, column=0)

text_liststart = tk.Label(frame_grid, text="Невыполненные:", fg="#333333")
text_liststart.grid(row=1, column=0)

task_liststart = tk.Listbox(frame_grid, height=10, width=50, bg="#00f", fg="#E0E0E0")
task_liststart.grid(row=2, column=0)


listbeing_button = tk.Button(frame_grid, text="Переместить в работу", bg="#f00", fg="#fff", command=tobeing_task)
listbeing_button.grid(row=0, column=1)

text_listbeing = tk.Label(frame_grid, text="В работе:", fg="#333333")
text_listbeing.grid(row=1, column=1)

task_listbeing = tk.Listbox(frame_grid, height=10, width=50, bg="#f00", fg="#E0E0E0")
task_listbeing.grid(row=2, column=1)


listfinish_button = tk.Button(frame_grid, text="Переместить в готово", bg="#060", fg="#fff", command=tofinish_task)
listfinish_button.grid(row=0, column=2)

text_listfinish = tk.Label(frame_grid, text="Готовые:", fg="#333333")
text_listfinish.grid(row=1, column=2)

task_listfinish = tk.Listbox(frame_grid, height=10, width=50, bg="#060", fg="#E0E0E0")
task_listfinish.grid(row=2, column=2)

root.mainloop()