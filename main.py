import customtkinter
import tkinter
from time import sleep
import requests
from time import sleep

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("dark-blue")
     
class tokeninfo():
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.title("Token Info")
        self.root.geometry("300x200")
        self.root.resizable(False, False)
        self.root.iconbitmap("icon.ico")
        self.root.configure(bg="#856ff8")
        self.token = customtkinter.CTkEntry(self.root)
        self.token.pack()
        self.button = customtkinter.CTkButton(self.root, text="Enter", command=self.tokens)
        self.button.pack()
        self.root.mainloop()
        self.root.destroy()
    def tokens(self):
        self.root = tkinter.Tk()
        self.root.title("Token Info")
        self.root.geometry("300x200")
        self.root.resizable(False, False)
        self.root.iconbitmap("icon.ico")
        self.root.configure(bg="#856ff8")
        self.head = {'Authorization': str(self.token)}
        self.user = requests.get('https://discord.com/api/v9/users/@me', headers=self.head)
        self.user = self.user.json()
        self.username = self.user['username']
        self.userid = self.user['id']
        self.email = self.user['email']
        self.phone = self.user['phone']
        self.nitro = self.user['premium_type']
        self.locale = self.user['locale']
        self.verified = self.user['verified']
        if self.nitro == 1:
            self.nitro = "Nitro Classic"
        else:
            self.nitro = "Nitro Boost"
        self.label = customtkinter.CTkLabel(self.root, text="Username: " + self.username)
        self.label.pack()
        self.label = customtkinter.CTkLabel(self.root, text="User ID: " + self.userid)
        self.label.pack()
        self.label = customtkinter.CTkLabel(self.root, text="Email: " + self.email)
        self.label.pack()
        self.label = customtkinter.CTkLabel(self.root, text="Phone: " + self.phone)
        self.label.pack()
        self.label = customtkinter.CTkLabel(self.root, text="Nitro: " + self.nitro)
        self.label.pack()
        self.label = customtkinter.CTkLabel(self.root, text="Locale: " + self.locale)
        self.label.pack()
        self.label = customtkinter.CTkLabel(self.root, text="Verified: " + self.verified)
        self.label.pack()
        self.root.mainloop()

class ipinfo():
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.title("IP Lookup")
        self.root.geometry("300x200")
        self.root.resizable(False, False)
        self.root.iconbitmap("icon.ico")
        self.root.configure(bg="#856ff8")
        self.ip = customtkinter.CTkEntry(self.root)
        self.ip.pack()
        self.button = customtkinter.CTkButton(self.root, text="Enter", command=self.ipgrab)
        self.button.pack()
        self.root.mainloop()
    def ipgrab(self):
        getip = requests.get(url = f"https://geo.leadboxer.com/GeoIpEngine/{self.ip}?jsonp")
        data = getip.json()
        self.root.label = tkinter.Label(self.root, text=f"Country: {data['countryName']}")
        self.root.label.pack()
        self.root.label = tkinter.Label(self.root, text=f"Continent: {data['continent']}")
        self.root.label.pack()
        self.root.label = tkinter.Label(self.root, text=f"Postal Code: {data['postalCode']}")
        self.root.label.pack()
        self.root.label = tkinter.Label(self.root, text=f"Latitude: {data['latitude']}")
        self.root.label.pack()
        self.root.label = tkinter.Label(self.root, text=f"Longitude: {data['longitude']}")
        self.root.label.pack()
        self.root.label = tkinter.Label(self.root, text=f"City: {data['city']}")
        self.root.label.pack()

class login():
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.title("Menu")
        self.root.geometry("300x200")
        self.root.resizable(False, False)
        self.root.iconbitmap("icon.ico")
        self.root.configure(bg="#856ff8")
        self.label = customtkinter.CTkLabel(self.root, text="We Are Smash")
        self.label.pack()
        self.ipinfo = customtkinter.CTkButton(self.root, text="IP Lookup", command=ipinfo)
        self.ipinfo.pack()
        self.tokeninfo = customtkinter.CTkButton(self.root, text="Token Info", command=tokeninfo)
        self.tokeninfo.pack()
        self.root.mainloop()     
login()

