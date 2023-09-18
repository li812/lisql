import tkinter as tk
from tkinter import messagebox

# Initialize Lisql module
import lisql

# Define a global variable to store the connection
connection = None

# Function to establish connection
def connect_to_db():
    global connection
    host = host_entry.get()
    user = user_entry.get()
    password = password_entry.get()

    # Create a custom connection
    connection = lisql.create_connection(host, user, password)

    if connection:
        status_label.config(text="Connected", fg="green")
        clear_connection_fields()
    else:
        messagebox.showerror("Connection Error", "Failed to connect to the database.")

# Function to execute query
def execute_query():
    global connection
    query = query_entry.get()

    if connection:
        result = lisql.execute_query(connection, query, fetch=True)
        if result:
            result_text.config(state=tk.NORMAL)
            result_text.delete(1.0, tk.END)
            result_text.insert(tk.END, "\n".join(map(str, result)))
            result_text.config(state=tk.DISABLED)
            status_label.config(text="Query executed successfully", fg="green")
        else:
            result_text.config(state=tk.NORMAL)
            result_text.delete(1.0, tk.END)
            result_text.config(state=tk.DISABLED)
            status_label.config(text="No results", fg="blue")
    else:
        messagebox.showerror("Connection Error", "Not connected to the database.")

# Function to clear connection fields
def clear_connection_fields():
    host_entry.delete(0, tk.END)
    user_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)

# Function to clear query field and result
def clear_query_result():
    query_entry.delete(0, tk.END)
    result_text.config(state=tk.NORMAL)
    result_text.delete(1.0, tk.END)
    result_text.config(state=tk.DISABLED)
    status_label.config(text="", fg="black")

# Create the main window
root = tk.Tk()
root.title("LiSQL GUI")

# Connection Section
connection_frame = tk.LabelFrame(root, text="Connection")
connection_frame.pack(pady=10, padx=10)

host_label = tk.Label(connection_frame, text="Host:")
host_label.grid(row=0, column=0, padx=5, pady=5)
host_entry = tk.Entry(connection_frame)
host_entry.grid(row=0, column=1, padx=5, pady=5)

user_label = tk.Label(connection_frame, text="User:")
user_label.grid(row=1, column=0, padx=5, pady=5)
user_entry = tk.Entry(connection_frame)
user_entry.grid(row=1, column=1, padx=5, pady=5)

password_label = tk.Label(connection_frame, text="Password:")
password_label.grid(row=2, column=0, padx=5, pady=5)
password_entry = tk.Entry(connection_frame, show="*")
password_entry.grid(row=2, column=1, padx=5, pady=5)

connect_button = tk.Button(connection_frame, text="Connect", command=connect_to_db)
connect_button.grid(row=3, column=0, columnspan=2, pady=10)

clear_connection_button = tk.Button(connection_frame, text="Clear", command=clear_connection_fields)
clear_connection_button.grid(row=4, column=0, columnspan=2, pady=10)

# Query Section
query_frame = tk.LabelFrame(root, text="Query Execution")
query_frame.pack(pady=10, padx=10, fill="both", expand="yes")

query_label = tk.Label(query_frame, text="Enter Query:")
query_label.grid(row=0, column=0, padx=5, pady=5)
query_entry = tk.Entry(query_frame, width=50)
query_entry.grid(row=0, column=1, padx=5, pady=5)

execute_button = tk.Button(query_frame, text="Execute Query", command=execute_query)
execute_button.grid(row=1, column=0, pady=10)

clear_query_result_button = tk.Button(query_frame, text="Clear", command=clear_query_result)
clear_query_result_button.grid(row=1, column=1, pady=10)

result_text = tk.Text(query_frame, width=80, height=10, state=tk.DISABLED)
result_text.grid(row=2, columnspan=2, pady=10)

status_label = tk.Label(query_frame, text="", fg="black")
status_label.grid(row=3, columnspan=2)

root.mainloop()
