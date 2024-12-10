import tkinter as tk
import threading
import time
# ...existing code...

class QueueingScreen:
    def __init__(self):
        self.queue = []
        self.root = tk.Tk()
        self.root.title("Queueing Screen")
        self.root.geometry("600x400")  # Set the window size to 600x400

        self.queue_listbox = tk.Listbox(self.root)
        self.queue_listbox.pack(fill=tk.BOTH, expand=True)

        self.update_queue_display()

    def add_to_queue(self, order_id, stage="Preparing"):
        self.queue.append((order_id, stage, time.time()))
        print(f"Order {order_id} added to the queue at stage {stage}.")
        self.update_queue_display()
        threading.Thread(target=self.auto_update_status, args=(order_id,)).start()

    def auto_update_status(self, order_id):
        time.sleep(5)
        self.update_order_status(order_id, "Ready for Pickup")

    def update_order_status(self, order_id, new_stage):
        for i, (oid, stage, timestamp) in enumerate(self.queue):
            if oid == order_id:
                self.queue[i] = (oid, new_stage, timestamp)
                print(f"Order {order_id} updated to stage {new_stage}.")
                break
        else:
            print(f"Order {order_id} not found in the queue.")
        self.update_queue_display()

    def remove_from_queue(self, order_id):
        for order in self.queue:
            if order[0] == order_id:
                self.queue.remove(order)
                print(f"Order {order_id} removed from the queue.")
                break
        else:
            print(f"Order {order_id} not found in the queue.")
        self.update_queue_display()

    def display_queue(self):
        print("Current Queue:")
        for order_id, stage, timestamp in self.queue:
            print(f"{order_id}, Stage: {stage}")

    def update_queue_display(self):
        self.queue_listbox.delete(0, tk.END)
        for order_id, stage, timestamp in self.queue:
            self.queue_listbox.insert(tk.END, f"{order_id}, {stage}")

    def run(self):
        self.root.mainloop()

# ...existing code...

if __name__ == "__main__":
    queue_screen = QueueingScreen()
    queue_screen.add_to_queue(1)
    queue_screen.add_to_queue(2)
    queue_screen.run()
