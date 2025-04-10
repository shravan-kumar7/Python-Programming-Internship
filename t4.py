import random
import tkinter as tk
from tkinter import messagebox

class CoinTossApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Virtual Coin Toss Simulator")
        self.root.geometry("400x600")

        # Historical results
        self.history = {"Heads": 0, "Tails": 0, "Total": 0}
        
        # GUI Elements
        self.label = tk.Label(root, text="Virtual Coin Toss Simulator", font=("Arial", 16))
        self.label.pack(pady=10)

        self.num_flips_label = tk.Label(root, text="Number of flips:")
        self.num_flips_label.pack()
        
        self.num_flips_entry = tk.Entry(root)
        self.num_flips_entry.pack(pady=5)
        
        self.flip_button = tk.Button(root, text="Flip Coin!", command=self.flip_coins)
        self.flip_button.pack(pady=10)
        
        self.result_text = tk.Text(root, height=10, width=40)
        self.result_text.pack(pady=10)
        
        self.current_stats_label = tk.Label(root, text="Current Session Stats:")
        self.current_stats_label.pack()
        
        self.current_stats = tk.Label(root, text="Heads: 0 (0%)\nTails: 0 (0%)")
        self.current_stats.pack(pady=5)
        
        self.history_label = tk.Label(root, text="All Sessions History:")
        self.history_label.pack()
        
        self.history_stats = tk.Label(root, text="Heads: 0 (0%)\nTails: 0 (0%)")
        self.history_stats.pack(pady=5)
        
        self.quit_button = tk.Button(root, text="Quit", command=root.quit)
        self.quit_button.pack(pady=10)

    def single_coin_toss(self):
        """Simulate a single coin toss"""
        return random.choice(["Heads", "Tails"])

    def update_display(self, result, heads_count, tails_count, total_flips):
        """Update the GUI with current results"""
        # Update result text
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, result)
        
        # Update current session stats
        if total_flips > 0:
            heads_pct = (heads_count / total_flips) * 100
            tails_pct = (tails_count / total_flips) * 100
            current_stats_text = f"Heads: {heads_count} ({heads_pct:.1f}%)\nTails: {tails_count} ({tails_pct:.1f}%)"
            self.current_stats.config(text=current_stats_text)
        
        # Update historical stats
        if self.history["Total"] > 0:
            heads_pct = (self.history["Heads"] / self.history["Total"]) * 100
            tails_pct = (self.history["Tails"] / self.history["Total"]) * 100
            history_text = f"Heads: {self.history["Heads"]} ({heads_pct:.1f}%)\nTails: {self.history["Tails"]} ({tails_pct:.1f}%)"
            self.history_stats.config(text=history_text)

    def flip_coins(self):
        """Handle coin flipping and update GUI"""
        try:
            num_flips = int(self.num_flips_entry.get())
            if num_flips < 0:
                messagebox.showerror("Error", "Please enter a non-negative number")
                return
                
            heads_count = 0
            tails_count = 0
            results = ""
            
            if num_flips == 0:
                results = "No flips performed.\n"
            else:
                for _ in range(num_flips):
                    result = self.single_coin_toss()
                    results += f"{result}\n"
                    if result == "Heads":
                        heads_count += 1
                        self.history["Heads"] += 1
                    else:
                        tails_count += 1
                        self.history["Tails"] += 1
                    self.history["Total"] += 1
            
            self.update_display(results, heads_count, tails_count, num_flips)
            
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number")

def main():
    root = tk.Tk()
    app = CoinTossApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
