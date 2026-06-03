# 14.3.py
import tkinter as tk
from tkinter import messagebox

class IceCreamStandGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Кафе-мороженое")
        self.root.geometry("400x300")
        
        self.flavors = ["Ванильное", "Шоколадное", "Клубничное", "Фисташковое"]
        
        tk.Label(root, text="Наше мороженое", font=("Arial", 16)).pack(pady=10)
        
        self.listbox = tk.Listbox(root)
        self.listbox.pack(pady=10, fill=tk.BOTH, expand=True)
        self.update_listbox()
        
        entry_frame = tk.Frame(root)
        entry_frame.pack(pady=5)
        
        tk.Label(entry_frame, text="Новый сорт:").pack(side=tk.LEFT)
        self.entry = tk.Entry(entry_frame)
        self.entry.pack(side=tk.LEFT, padx=5)
        
        button_frame = tk.Frame(root)
        button_frame.pack(pady=5)
        
        tk.Button(button_frame, text="Добавить", command=self.add_flavor).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Удалить", command=self.remove_flavor).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Проверить", command=self.check_flavor).pack(side=tk.LEFT, padx=5)
    
    def update_listbox(self):
        self.listbox.delete(0, tk.END)
        for flavor in self.flavors:
            self.listbox.insert(tk.END, flavor)
    
    def add_flavor(self):
        new_flavor = self.entry.get().strip()
        if new_flavor:
            if new_flavor not in self.flavors:
                self.flavors.append(new_flavor)
                self.update_listbox()
                self.entry.delete(0, tk.END)
                messagebox.showinfo("Успех", f"Сорт '{new_flavor}' добавлен")
            else:
                messagebox.showwarning("Внимание", "Такой сорт уже есть")
        else:
            messagebox.showwarning("Ошибка", "Введите название сорта")
    
    def remove_flavor(self):
        selected = self.listbox.curselection()
        if selected:
            flavor = self.listbox.get(selected[0])
            self.flavors.remove(flavor)
            self.update_listbox()
            messagebox.showinfo("Успех", f"Сорт '{flavor}' удален")
        else:
            messagebox.showwarning("Ошибка", "Выберите сорт для удаления")
    
    def check_flavor(self):
        flavor = self.entry.get().strip()
        if flavor:
            if flavor in self.flavors:
                messagebox.showinfo("Результат", f"Сорт '{flavor}' есть в наличии")
            else:
                messagebox.showinfo("Результат", f"Сорта '{flavor}' нет в наличии")
        else:
            messagebox.showwarning("Ошибка", "Введите название сорта для проверки")

if __name__ == "__main__":
    root = tk.Tk()
    app = IceCreamStandGUI(root)
    root.mainloop()
