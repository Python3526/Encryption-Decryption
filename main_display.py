import tkinter as tk
from tkinter import colorchooser
from colorama import Fore
import rsa

public_key, private_key = 0, 0

# GUI-settings
display1 = tk.Tk()
display1.geometry('500x500')
display1.title('Encryption & Decryption')
display1.resizable(False, False)
display1.config(bg="lightgreen")

# user_input
entry1_info = tk.Label(display1,
                       text="Enter your text ⬇️",
                       font=('Cascase', 12, "bold"),
                       bg="lightgreen")
entry1_info.place(x=10, y=0)

entry1 = tk.Text(display1)
entry1.place(x=10, y=25, height=300, width=220)

entry2_info = tk.Label(display1,
                       text="Output✔️",
                       font=('Cascase', 12, "bold"),
                       bg="lightgreen")
entry2_info.place(x=270, y=0)

entry2 = tk.Text(display1)
entry2.place(x=270, y=25, height=300, width=220)


def hashing():
    global public_key, private_key
    entry2.delete(0.0, tk.END)
    value = entry1.get(0.0, 'end')

    public_key, private_key = rsa.newkeys(512)

    # Encode the string to bytes
    byte_string = value.encode()

    # Encrypt the byte string with the public key
    encoded = rsa.encrypt(byte_string, public_key)

    entry2.insert(0.0, str(encoded))
    entry1.delete(0.0, tk.END)


def unhashing():
    global public_key, private_key
    entry2.delete(0.0, tk.END)
    value = entry1.get(0.0, 'end')

    # Encode the string to bytes
    byte_encrypt = eval(value)

    decoded_byte = rsa.decrypt(byte_encrypt, private_key)
    decoded = decoded_byte.decode()

    entry2.insert(0.0, str(decoded))
    entry1.delete(0.0, tk.END)


# buttons
locking = tk.Button(text="Encryption",
                    bg="green",
                    activebackground="blue",
                    command=hashing)
locking.place(x=20, y=350, height=30, width=200)

unlocking = tk.Button(text="Decryption",
                      bg="red",
                      activebackground="yellow",
                      command=unhashing)
unlocking.place(x=280, y=350, height=30, width=200)


def color_changing():
    chosen_color = str(colorchooser.askcolor()[1])
    display1.config(bg=chosen_color)
    entry1_info.config(bg=chosen_color)
    entry2_info.config(bg=chosen_color)
    # entry1.config(bg=chosen_color)
    # entry2.config(bg=chosen_color)


color_button = tk.Button(text="button to change the color of display",
                         command=color_changing,
                         bg="white",
                         fg="black",
                         activebackground="yellow", )
color_button.place(x=-2, y=480, height=22, width=502)

quit_button = tk.Button(text="Quit",
                        command=display1.quit,
                        bg="white",
                        fg="black",
                        activebackground="red", )
quit_button.place(x=175, y=400, height=50, width=150)

display1.mainloop()

print(Fore.MAGENTA + "Come back, again🫡" + Fore.RESET)
