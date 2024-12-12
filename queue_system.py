import heapq
import json
import os
from tkinter import Tk, Frame, LabelFrame, Button, Scrollbar
from tkinter import ttk

class OrderQueue:
    def __init__(self):
        self.queue = []
        self.counter = 0
        self.load_orders('orders.json')

    def load_orders(self, filepath):
        try:
            with open(filepath, 'r') as f:
                data = json.load(f)
            self.queue.clear()
            for order in data['orders']:
                # Create queue entry from order data
                self.queue.append((
                    order['queue_number'],
                    order['order_number'],
                    order['num_items'],
                    order['order_type'],
                    order.get('items', []),
                    order.get('addons', [])
                ))
        except (FileNotFoundError, json.JSONDecodeError):
            self.queue = []

    def save_orders(self, filepath):
        orders = [
            {
                'order_number': order[1],
                'queue_number': order[0],
                'num_items': order[2],
                'order_type': order[3],
                'items': order[4],
                'addons': order[5]
            } for order in self.queue
        ]
        with open(filepath, 'w') as f:
            json.dump({'orders': orders}, f, indent=2)

    def add_order(self, order_number, queue_number, num_items, order_type, items=None, addons=None):
        """Add an order to the queue with optional items and addons"""
        # Create order object
        order = {
            'order_number': order_number,
            'queue_number': queue_number,
            'num_items': num_items,
            'order_type': order_type,
            'items': items or [],
            'addons': addons or []
        }
        
        # Load existing orders (don't use self.load_orders to avoid duplicates)
        try:
            with open('orders.json', 'r') as f:
                data = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            data = {'orders': []}
            
        # Add new order
        data['orders'].append(order)
        
        # Save updated orders
        with open('orders.json', 'w') as f:
            json.dump(data, f, indent=2)
            
        # Update queue
        self.queue.append((
            queue_number, 
            order_number, 
            num_items, 
            order_type,
            items or [],
            addons or []
        ))

    def is_empty(self):
        return len(self.queue) == 0

    def pop_order(self):
        if not self.is_empty():
            return heapq.heappop(self.queue)
        return "Queue is empty"

    def get_categorized_orders(self):
        dine_in = [order for order in self.queue if order[3] == "Dine-In"]
        take_away = [order for order in self.queue if order[3] == "Take-away"]
        return {
            "Dine-In": sorted(dine_in, key=lambda x: x[0]),
            "Take-away": sorted(take_away, key=lambda x: x[0])
        }

    def reset_queue(self):
        """Reset the queue and save empty state to file"""
        self.queue.clear()
        self.counter = 0
        try:
            with open('orders.json', 'w') as f:
                json.dump({'orders': []}, f, indent=2)
                f.flush()
                os.fsync(f.fileno())
        except Exception as e:
            print(f"Error resetting queue: {e}")

    def get_last_order_number(self):
        if not self.queue:
            return 0
        return max(order[1] for order in self.queue)

# Initialize global variables
queue_window = None
orders_tree = None

# ...existing code...

def create_queue_system_window():
    global queue_window, orders_tree  # Only one tree now
    if queue_window is not None and queue_window.winfo_exists():
        update_queue_display()
        queue_window.lift()
        return
    
    queue_window = Tk()
    queue_window.geometry("1000x600")
    queue_window.minsize(1000, 600)
    queue_window.title("Order Queue")
    
    # Create main frame
    main_frame = Frame(queue_window)
    main_frame.pack(fill='both', expand=True, padx=10, pady=5)
    
    # Create single frame for all orders
    orders_frame = LabelFrame(main_frame, text="Order Queue", font=("Abril Fatface", 12))
    orders_frame.pack(fill='both', expand=True, padx=5)
    
    # Create headers
    headers = ["Queue #", "Order #", "Items", "Order Type", "Action"]
    
    # Style configuration
    style = ttk.Style()
    style.configure("Treeview", rowheight=50)
    
    # Create single treeview
    orders_tree = ttk.Treeview(orders_frame, columns=headers, show='headings', height=15, style="Treeview")
    
    # Configure columns
    orders_tree.column("Queue #", width=100, anchor='center')
    orders_tree.column("Order #", width=100, anchor='center')
    orders_tree.column("Items", width=100, anchor='center')
    orders_tree.column("Order Type", width=150, anchor='center')
    orders_tree.column("Action", width=150, anchor='center')
    
    for header in headers:
        orders_tree.heading(header, text=header)
    
    # Add scrollbar
    scrollbar = Scrollbar(orders_frame, orient="vertical", command=orders_tree.yview)
    orders_tree.configure(yscrollcommand=scrollbar.set)
    
    # Pack tree and scrollbar
    orders_tree.pack(side='left', fill='both', expand=True)
    scrollbar.pack(side='right', fill='y')
    
    # Initialize buttons dictionary
    orders_tree.buttons = {}
    
    update_queue_display()
    queue_window.protocol("WM_DELETE_WINDOW", on_queue_window_close)

def update_queue_display(sort_by="queue", reverse=False):
    if queue_window is None or not queue_window.winfo_exists():
        return
        
    order_queue = OrderQueue()
    order_queue.load_orders('orders.json')
    
    # Clear existing entries and buttons
    if hasattr(orders_tree, 'buttons'):
        for button in orders_tree.buttons.values():
            button.destroy()
        orders_tree.buttons.clear()
    
    for item in orders_tree.get_children():
        orders_tree.delete(item)
    
    orders = list(order_queue.queue)
    if sort_by == "queue":
        orders.sort(key=lambda x: x[0], reverse=reverse)
    elif sort_by == "order":
        orders.sort(key=lambda x: x[1], reverse=reverse)
    elif sort_by == "items":
        orders.sort(key=lambda x: x[2], reverse=reverse)
    
    def create_process_button(item_id, queue_num):
        bbox = orders_tree.bbox(item_id, "Action")
        if bbox:
            process_button = Button(
                orders_tree,
                text="Process",
                bg="#4CAF50",
                fg="white",
                relief="raised",
                font=("Arial", 10, "bold"),
                command=lambda: process_order(queue_num)
            )
            
            x = bbox[0] + (bbox[2] - bbox[0] - 80) // 2  # Center the button
            y = bbox[1] + 10
            process_button.place(x=x, y=y, width=80, height=30)
            orders_tree.buttons[item_id] = process_button
    
    for order in orders:
        item_id = orders_tree.insert('', 'end', values=(
            f"#{order[0]}", 
            f"#{order[1]}", 
            order[2],
            order[3],  # Order Type
            ""  # Empty space for button
        ))
        orders_tree.update()
        create_process_button(item_id, order[0])

def on_treeview_click(event):
    region = event.widget.identify("region", event.x, event.y)
    if region == "cell":
        column = event.widget.identify_column(event.x)
        if column == "#4":  # "Action" column
            item_id = event.widget.identify_row(event.y)
            item = event.widget.item(item_id)
            queue_num_str = item['values'][0]
            queue_num = int(queue_num_str.strip('#'))
            # Call the process_order function
            process_order(queue_num)

def process_order(queue_num):
    # Remove the order from orders.json
    with open('orders.json', 'r+') as f:
        data = json.load(f)
        data['orders'] = [o for o in data['orders'] if o['queue_number'] != queue_num]
        f.seek(0)
        f.truncate()
        json.dump(data, f, indent=2)
    
    # Reset order number in database.json
    with open('database.json', 'r+') as f:
        data = json.load(f)
        data['order_number'] = 0
        f.seek(0)
        f.truncate()
        json.dump(data, f, indent=2)
    
    update_queue_display()  # Refresh display after processing

def create_order_number():
    with open('orders.json', 'r+') as f:
        data = json.load(f)
        if data['orders']:
            last_order = max(data['orders'], key=lambda x: x['order_number'])
            return last_order['order_number'] + 1
        else:
            return 1

def on_queue_window_close():
    global queue_window
    queue_window.destroy()
    queue_window = None

def sort_and_display(sort_by):
    current_sort = getattr(queue_window, 'current_sort', {"column": "queue", "reverse": False})
    reverse = False if sort_by != current_sort["column"] else not current_sort["reverse"]
    queue_window.current_sort = {"column": sort_by, "reverse": reverse}
    update_queue_display(sort_by, reverse)

# ...existing code...