import sqlite3
import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import Calendar
import datetime

# Database Setup
def setup_db():
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            amount REAL,
            category TEXT,
            description TEXT,
            date TEXT
        )
    """)
    conn.commit()
    conn.close()

# GUI Setup
class ExpenseTrackerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Expense Tracker")
        self.root.geometry("1200x500")  
        self.root.resizable(False, False)
        
        # Styling
        self.style = ttk.Style()
        self.style.configure("TButton", font=("Arial", 10), padding=5)
        self.style.configure("Treeview.Heading", font=("Arial", 11, "bold"))
        
        # Main Frame
        self.main_frame = ttk.Frame(root, padding=10)
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Input Frame
        self.input_frame = ttk.LabelFrame(self.main_frame, text="Add Expense", padding=10)
        self.input_frame.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        
        # Input Fields
        ttk.Label(self.input_frame, text="Amount:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.amount_entry = ttk.Entry(self.input_frame)
        self.amount_entry.grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Label(self.input_frame, text="Category:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.category_entry = ttk.Entry(self.input_frame)
        self.category_entry.grid(row=1, column=1, padx=5, pady=5)
        
        ttk.Label(self.input_frame, text="Description:").grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.description_entry = ttk.Entry(self.input_frame)
        self.description_entry.grid(row=2, column=1, padx=5, pady=5)
        
        ttk.Label(self.input_frame, text="Date:").grid(row=3, column=0, padx=5, pady=5, sticky="w")
        self.date_entry = ttk.Entry(self.input_frame)
        self.date_entry.grid(row=3, column=1, padx=5, pady=5)
        self.date_entry.bind("<Button-1>", self.show_calendar)
        
        # Buttons
        ttk.Button(self.input_frame, text="Add Expense", command=self.add_expense_gui).grid(row=4, column=0, columnspan=2, pady=5)
        
        # Table Frame
        self.table_frame = ttk.LabelFrame(self.main_frame, text="Expense Records", padding=10)
        self.table_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
        
        self.tree = ttk.Treeview(self.table_frame, columns=("ID", "Amount", "Category", "Description", "Date"), show='headings', height=10)
        self.tree.heading("ID", text="ID")
        self.tree.heading("Amount", text="Amount")
        self.tree.heading("Category", text="Category")
        self.tree.heading("Description", text="Description")
        self.tree.heading("Date", text="Date")
        self.tree.column("ID", width=30, anchor="center")
        
        self.tree.pack(fill=tk.BOTH, expand=True)
        
        # Action Buttons
        self.button_frame = ttk.Frame(self.main_frame)
        self.button_frame.grid(row=1, column=1, pady=10)
        
        ttk.Button(self.button_frame, text="View Expenses", command=self.view_expenses_gui).grid(row=0, column=0, padx=5)
        ttk.Button(self.button_frame, text="Delete Expense", command=self.delete_expense_gui).grid(row=0, column=1, padx=5)
        
    def show_calendar(self, event=None):
        """ Show a pop-up calendar for date selection """
        self.cal_window = tk.Toplevel(self.root)
        self.cal_window.title("Select Date")
        self.cal_window.geometry("250x250")
        self.cal_window.resizable(False, False)

        self.cal = Calendar(self.cal_window, date_pattern="dd/MM/yyyy", maxdate=datetime.date.today())
        self.cal.pack(pady=10)
        
        select_btn = ttk.Button(self.cal_window, text="Select Date", command=self.get_selected_date)
        select_btn.pack(pady=5)
    
    def get_selected_date(self):
        selected_date = self.cal.get_date()
        self.date_entry.delete(0, tk.END)
        self.date_entry.insert(0, selected_date)
        self.cal_window.destroy()
    
    def add_expense_gui(self):
        try:
            amount = float(self.amount_entry.get())
            category = self.category_entry.get()
            description = self.description_entry.get()
            date = self.date_entry.get()
            
            if not category or not description or not date:
                raise ValueError("All fields are required.")
            
            conn = sqlite3.connect("expenses.db")
            cursor = conn.cursor()
            cursor.execute("INSERT INTO expenses (amount, category, description, date) VALUES (?, ?, ?, ?)", (amount, category, description, date))
            conn.commit()
            conn.close()
            
            self.amount_entry.delete(0, tk.END)
            self.category_entry.delete(0, tk.END)
            self.description_entry.delete(0, tk.END)
            self.date_entry.delete(0, tk.END)
            
            messagebox.showinfo("Success", "Expense added successfully!")
            self.view_expenses_gui()
        except ValueError:
            messagebox.showerror("Error", "Invalid input! Please fill all fields correctly.")
    
    def view_expenses_gui(self):
        self.tree.delete(*self.tree.get_children())
        conn = sqlite3.connect("expenses.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM expenses")
        expenses = cursor.fetchall()
        conn.close()
        for exp in expenses:
            self.tree.insert("", tk.END, values=exp)
    
    def delete_expense_gui(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Warning", "Please select an expense to delete.")
            return
        item = self.tree.item(selected_item)
        expense_id = item['values'][0]
        conn = sqlite3.connect("expenses.db")
        cursor = conn.cursor()
        cursor.execute("DELETE FROM expenses WHERE id = ?", (expense_id,))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Expense deleted successfully!")
        self.view_expenses_gui()

if __name__ == "__main__":
    setup_db()
    root = tk.Tk()
    app = ExpenseTrackerApp(root)
    root.mainloop()