import tkinter as tk
import requests
from tkinter import colorchooser
from tkinter import *

def choose_color():
    color = colorchooser.askcolor()
    if color:
        color_code = color[1]
        color_entry.delete(0, tk.END)
        color_entry.insert(tk.END, color_code)

def send_webhook():
    webhook_url = webhook.get()

    color_code = color_entry.get()
    color_code = color_code.lstrip('#')  # Remove '#' symbol
    try:
        color_int = int(color_code, 16)
    except ValueError:
        print("Invalid color code format!")
        return

    embed = {
        "title": title_entry.get(),
        "description": desc_entry.get(),
        "url": url_entry.get(),
        "color": color_int,
        "footer": {"text": footer_entry.get()},
        "thumbnail": {"url": thumbnail_entry.get()},
        "image": {"url": image_entry.get()},
        "author": {"name": author_entry.get(), "icon_url": icon_entry.get()},
    }

    data = {"embeds": [embed]}
    response = requests.post(webhook_url, json=data)
    if response.status_code == 204:
        print("Embed sent successfully!")
    else:
        print(f"Failed to send embed. Status code: {response.status_code}")

root = tk.Tk()
root.title("Discord Webhook Embed Sender")
root.geometry("700x250")
root['background']='#313338'


tk.Label(root, text="Title:", bg='#313338', fg='#9a9a9a').grid(row=2, column=0)
title_entry = tk.Entry(root, bg='#4e5159', relief="flat")
title_entry.grid(row=2, column=1, padx=50, pady=5)

tk.Label(root, text="Description:", bg='#313338', fg='#9a9a9a').grid(row=2, column=3)
desc_entry = tk.Entry(root, bg='#4e5159', relief="flat")
desc_entry.grid(row=2, column=4, padx=50, pady=5)

tk.Label(root, text="Url:", bg='#313338', fg='#9a9a9a').grid(row=3, column=0)
url_entry = tk.Entry(root, bg='#4e5159', relief="flat")
url_entry.grid(row=3, column=1, padx=50, pady=5)

tk.Label(root, text="Color:", bg='#313338', fg='#9a9a9a').grid(row=3, column=3)
color_entry = tk.Entry(root, bg='#4e5159', relief="flat")
color_entry.grid(row=3, column=4, padx=50, pady=5)
color_pick_button = tk.Button(root, text="Pick Color", command=choose_color, bg='#313338', fg='#9a9a9a', relief="flat")
color_pick_button.grid(row=3, column=5)

tk.Label(root, text="Footer:", bg='#313338', fg='#9a9a9a').grid(row=4, column=0)
footer_entry = tk.Entry(root, bg='#4e5159', relief="flat")
footer_entry.grid(row=4, column=1, padx=50, pady=5)

tk.Label(root, text="Thumbnail:", bg='#313338', fg='#9a9a9a').grid(row=4, column=3)
thumbnail_entry = tk.Entry(root, bg='#4e5159', relief="flat")
thumbnail_entry.grid(row=4, column=4, padx=50, pady=5)

tk.Label(root, text="Image:", bg='#313338', fg='#9a9a9a').grid(row=5, column=0)
image_entry = tk.Entry(root, bg='#4e5159', relief="flat")
image_entry.grid(row=5, column=1, padx=50, pady=5)

tk.Label(root, text="Author:", bg='#313338', fg='#9a9a9a').grid(row=5, column=3)
author_entry = tk.Entry(root, bg='#4e5159', relief="flat")
author_entry.grid(row=5, column=4, padx=50, pady=5)

tk.Label(root, text="Icon:", bg='#313338', fg='#9a9a9a').grid(row=6, column=0)
icon_entry = tk.Entry(root, bg='#4e5159', relief="flat")
icon_entry.grid(row=6, column=1, padx=50, pady=5)

tk.Label(root, text="Inline:", bg='#313338', fg='#9a9a9a').grid(row=6, column=3)
inline_var = tk.Entry(root, bg='#4e5159', relief="flat")
inline_var.grid(row=6, column=4, padx=50, pady=5)

tk.Label(root, text="", bg='#313338', fg='#9a9a9a').grid(row=0, column=0)

webhook_label = tk.Label(root, text="Webhook:", bg='#313338', fg='#9a9a9a')
webhook_label.grid(row=0, column=0)
webhook_label.place(x=240, y=0)
webhook = tk.Entry(root, bg='#4e5159', relief="flat")
webhook.grid(row=0, column=1, padx=5, pady=5)
webhook.place(x=310, y=0)

separator = tk.Frame(root, height=1, width=400, bg="#9a9a9a")
separator.grid(row=1, columnspan=6, pady=5)

send_button = tk.Button(root, text="Send Embed", command=send_webhook, bg='#313338', fg='#9a9a9a', relief="flat")
send_button.grid(row=7, columnspan=6)
send_button.place(x=285,y=200)

root.mainloop()
