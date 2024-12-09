from collections import deque
from tkinter import Tk
from order_number import create_order_number_content, order_queue

class Order:
    def __init__(self, order_id):
        self.order_id = order_id
        self.status = "Waiting"

    def update_status(self, new_status):
        self.status = new_status

class OrderQueue:
    def __init__(self):
        self.queue = deque()

    def add_order(self, order):
        self.queue.append(order)
        print(f"Order {order.order_id} added to the queue.")

    def update_order_status(self, order_id, new_status):
        for order in self.queue:
            if order.order_id == order_id:
                order.update_status(new_status)
                print(f"Order {order_id} status updated to '{new_status}'.")
                return
        print(f"Order {order_id} not found in the queue.")

    def retrieve_next_order(self):
        if self.queue:
            order = self.queue.popleft()
            print(f"Order {order.order_id} retrieved from the queue.")
            return order
        else:
            print("No orders in the queue.")
            return None

    def get_order_status(self, order_id):
        for order in self.queue:
            if order.order_id == order_id:
                return order.status
        return "Order not found."

    def get_next_order_number(self):
        if self.queue:
            return self.queue[0].order_id
        else:
            return None

def create_main_window():
    window = Tk()
    window.geometry("507x782")
    window.configure(bg="#FFFFFF")
    next_order_number = order_queue.get_next_order_number()
    if next_order_number:
        create_order_number_content(window, next_order_number)
    else:
        print("No orders to display.")
    window.resizable(False, False)
    window.mainloop()

# Example usage:
if __name__ == "__main__":
    order_queue = OrderQueue()

    # Add orders to the queue
    order_queue.add_order(Order(1))
    order_queue.add_order(Order(2))

    # Update order statuses
    order_queue.update_order_status(1, "Preparing")
    order_queue.update_order_status(2, "Ready for Pickup")

    # Retrieve orders in sequence
    order = order_queue.retrieve_next_order()
    if order:
        print(f"Processing Order {order.order_id}: Status - {order.status}")

    order = order_queue.retrieve_next_order()
    if order:
        print(f"Processing Order {order.order_id}: Status - {order.status}")

    next_order_number = order_queue.get_next_order_number()
    if next_order_number: