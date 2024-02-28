import tkinter as tk
from tkinter import scrolledtext
from datetime import datetime
import requests

class CatGPTv0:
    def __init__(self, root):
        self.root = root
        self.root.geometry("600x500")  # Adjust the window size to 600x500
        self.root.resizable(False, False)  # Disable the maximize button
        self.root.title("CatGPTv0 - Chat Interface")

        # Text box for chat history
        self.chat_history = scrolledtext.ScrolledText(root, state='disabled', height=20, width=70)
        self.chat_history.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        # Entry widget for typing messages
        self.message_entry = tk.Entry(root, width=60)
        self.message_entry.pack(padx=10, pady=10, fill=tk.X)
        self.message_entry.bind("<Return>", self.on_enter)

    def on_enter(self, event):
        self.send_message()

    def send_message(self):
        message = self.message_entry.get()
        if message:
            self.display_message("You", message)
            response = self.generate_response(message)
            self.display_message("CatGPTv0", response)
            self.message_entry.delete(0, tk.END)

    def display_message(self, sender, message):
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        formatted_message = f"{timestamp} - {sender}: {message}\n"
        self.chat_history.configure(state='normal')
        self.chat_history.insert(tk.END, formatted_message)
        self.chat_history.configure(state='disabled')
        self.chat_history.see(tk.END)

    def generate_response(self, user_input):
        # URL of the local API endpoint
        api_url = "http://localhost:1234/generate"
        
        # Making a POST request to the API with the user input
        try:
            response = requests.post(api_url, json={"message": user_input})
            response_data = response.json()
            
            # Assuming the API returns a JSON with a field 'response' containing the generated message
            return response_data.get('response', "Sorry, I couldn't understand that.")
        
        except requests.exceptions.RequestException as e:
            # Handling request errors
            print(f"An error occurred: {e}")
            return "Sorry, there was a problem getting a response."

if __name__ == "__main__":
    root = tk.Tk()
    chat_interface = CatGPTv0(root)
    root.mainloop()

    ## [C] 1.0 Flames Co. 20XX
    #- ---  
