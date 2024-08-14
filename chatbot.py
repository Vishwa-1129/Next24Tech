import tkinter as tk
from tkinter import scrolledtext

# Function to handle sending a message
def send_message():
    user_message = entry_message.get()
    if user_message.strip():
        chat_window.insert(tk.END, "You: " + user_message + "\n")
        entry_message.delete(0, tk.END)
        respond(user_message)

# Function to generate a response from the chatbot
def respond(user_message):
    # Simple response logic
    response = "Bot: " + get_bot_response(user_message) + "\n"
    chat_window.insert(tk.END, response)
    chat_window.see(tk.END)  # Scroll to the end of the chat window

# Function to get bot response (can be enhanced with more sophisticated logic)
def get_bot_response(user_message):
    # Simple keyword-based responses
    if "hello" in user_message.lower():
        return "Hello! How can I assist you today?"
    elif "how are you" in user_message.lower():
        return "I'm a bot, so I don't have feelings, but I'm here to help you!"
    elif "bye" in user_message.lower():
        return "Goodbye! Have a nice day!"
    else:
        return "I'm sorry, I don't understand that."

# Create the main application window
root = tk.Tk()
root.title("Chatbot")

# Create and place the chat window
chat_window = scrolledtext.ScrolledText(root, wrap=tk.WORD)
chat_window.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

# Create and place the message entry field
entry_message = tk.Entry(root, width=80)
entry_message.grid(row=1, column=0, padx=10, pady=10)

# Create and place the send button
send_button = tk.Button(root, text="Send", command=send_message)
send_button.grid(row=1, column=1, padx=10, pady=10)

# Bind the Enter key to send a message
root.bind('<Return>', lambda event: send_message())

# Run the application
root.mainloop()
