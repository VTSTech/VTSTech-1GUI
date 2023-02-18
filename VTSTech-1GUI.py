# Program: VTSTech-1GUI.py
# Version: 0.0.1 Revision 03
# Operating System: Kali Linux
# Description: Python script to run dnsrecon, nmap, sslscan, wpscan, urlscan. Output saved per tool/target.
# Author: Written by Veritas//VTSTech (veritas@vts-tech.org)
# GitHub: https://github.com/Veritas83
# Homepage: www.VTS-Tech.org
# Dependencies: dnsrecon, nmap, sslscan, wpscan, urlscan, wget
# apt-get install dnsrecon nmap wget wpscan sslscan urlscan
# OpenAI's ChatCPT wrote r00, I modified it from there to be r01. I basically tried to get it to re-write my 1CMD
# bash shell script with a prompt and then said. Ok now make it a GUI in Python.

import os
import random
import tkinter as tk
from tkinter import messagebox
from tkinter import *

class ApplicationForm(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        # Create label and grid for hyperlink
        self.link_label = tk.Label(self.master, text="www.VTS-Tech.org")
        self.link_label.grid(row=8, column=0, columnspan=2, pady=10)
        self.link_label.bind("<Button-1>", self.open_link)
        self.link_label.config(foreground="blue", cursor="hand2")
    
    def open_link(self, event):
        messagebox.showinfo("More Information", "Visit https://www.VTS-Tech.org to learn more.")
    
    def submit_form(self):
        # code for submitting form goes here
        pass
        
v="0.0.1-r03"
def run_stage1():
    target = entry.get()
    n1="sudo nmap -Pn --reason -T4 --top-ports 10 -vv -sS "
    if proxy_var.get():
        with open("prox.txt", "r") as f:
            proxies = f.read().splitlines()
        proxy = random.choice(proxies)
        n1 += f"--proxy=socks4://{proxy} -oN nmap1-{target}.txt {target}"
    else:
    	n1 += f"-oN nmap1-{target}.txt {target}"
    os.system(n1)
    messagebox.showinfo("Info", "nmap stage 1 completed!")
def run_stage2():
    target = entry.get()
    n2="sudo nmap -Pn --reason -T4 --top-ports 100 -vv -sSV "
    if proxy_var.get():
        with open("prox.txt", "r") as f:
            proxies = f.read().splitlines()
        proxy = random.choice(proxies)
        n2 += f"--proxy=socks4://{proxy} -oN nmap2-{target}.txt {target}"
    else:
    	n2 += f"-oN nmap2-{target}.txt {target}"    
    os.system(n2)
    messagebox.showinfo("Info", "nmap stage 2 completed!")
def run_stage3():
    target = entry.get()
    n3="sudo nmap -Pn --reason -T4 --top-ports 250 -vv -sSV -O --script default "
    if proxy_var.get():
        with open("prox.txt", "r") as f:
            proxies = f.read().splitlines()
        proxy = random.choice(proxies)
        n3 += f"--proxy=socks4://{proxy} -oN nmap3-{target}.txt {target}"
    else:
    	n3 += f"-oN nmap3-{target}.txt {target}" 
    os.system(n3)
    messagebox.showinfo("Info", "nmap stage 3 completed!")
def run_stage4():
    target = entry.get()
    n4="sudo nmap -Pn --reason -T4 --top-ports 500 -vv -sSV -O -A --script default,safe "
    if proxy_var.get():
        with open("prox.txt", "r") as f:
            proxies = f.read().splitlines()
        proxy = random.choice(proxies)
        n4 += f"--proxy=socks4://{proxy} -oN nmap4-{target}.txt {target}"
    else:
    	n4 += f"-oN nmap4-{target}.txt {target}" 
    os.system(n4)
    messagebox.showinfo("Info", "nmap stage 4 completed!")
def run_stage5():
    target = entry.get()
    n5="sudo nmap -Pn --reason -T4 --top-ports 999 -vv -sSV -O -A --script default,safe,vuln "
    if proxy_var.get():
        with open("prox.txt", "r") as f:
            proxies = f.read().splitlines()
        proxy = random.choice(proxies)
        n5 += f"--proxy=socks4://{proxy} -oN nmap5-{target}.txt {target}"
    else:
    	n5 += f"-oN nmap5-{target}.txt {target}" 
    os.system(n5)
    messagebox.showinfo("Info", "nmap stage 5 completed!")    
def run_dnsrecon():
    target = entry.get()
    dnscmd=f"sudo dnsrecon -t std,srv,zonewalk -n 8.8.8.8 -z -f --iw --threads 2 --lifetime 10 --xml dnsrecon-{target}.xml -d {target}"
    os.system(dnscmd)
    messagebox.showinfo("Info", "dnsrecon completed!")		
def run_dirb():
    target = entry.get()
    if proxy_var.get():
        with open("prox.txt", "r") as f:
            proxies = f.read().splitlines()
        proxy = random.choice(proxies)
        dirbcmd = f"dirb http://{target} -f -p {proxy} -z 500 -o dirb-{target}.txt"
    else:
        dirbcmd = f"dirb http://{target} -f -z 500 -o dirb-{target}.txt"
    os.system(dirbcmd)
    messagebox.showinfo("Info", "dirb completed!")		
def run_sslscan():
    target = entry.get()
    sslcmd=f"sudo sslscan --verbose --no-colour --show-certificate --xml=sslscan-{target}.txt {target}"
    os.system(sslcmd)
    messagebox.showinfo("Info", "sslscan completed!")		
def run_wpscan():
    target = entry.get()
    wpcmd=f"sudo wpscan -e p,t,tt,u1-20 -t 2 -v -f cli-no-color -o wpscan-{target}.txt --url {target}"
    os.system(wpcmd)
    messagebox.showinfo("Info", "wpscan completed!")		
def run_wgetscan():
    target = entry.get()
    wgetcmd=f"sudo wget -t 4 --content-on-error https://{target}/ -O wget-{target}.txt"
    os.system(wgetcmd)
    messagebox.showinfo("Info", "wget completed!")	
def run_urlscan():
    target = entry.get()
    urlcmd=f"sudo urlscan -c -n wget-{target}.txt | tee urlscan-{target}.txt"
    os.system(urlcmd)
    messagebox.showinfo("Info", "urlscan completed!")	    

root = tk.Tk()

window_width = 320
window_height = 320

# get the screen dimension
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# find the center point
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

# set the position of the window to the center of the screen
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
root.title("VTSTech-1GUI {}".format(v))

# Create the checkbox
proxy_var = BooleanVar()
proxy_cb = Checkbutton(root, text="Use proxy", variable=proxy_var)

# Add the checkbox to the window
proxy_cb.grid(row=0, column=0, sticky=tk.W)

label = tk.Label(root, text="Enter target (IP/Hostname):")
label.grid(row=1, column=0, pady=4, padx=2, sticky=tk.W)

entry = tk.Entry(root)
entry.insert(0,"scanme.nmap.org")
entry.grid(row=2, column=0, pady=4, padx=2, sticky=tk.W)

dnsrecon_button = tk.Button(root, text="dnsrecon", command=run_dnsrecon)
dnsrecon_button.grid(row=3, column=0, pady=4, padx=2, sticky=tk.W)

sslscan_button = tk.Button(root, text="sslscan", command=run_sslscan)
sslscan_button.grid(row=4, column=0, pady=4, padx=2, sticky=tk.W)

wpscan_button = tk.Button(root, text="wpscan", command=run_wpscan)
wpscan_button.grid(row=5, column=0, pady=4, padx=2, sticky=tk.W)

wgetscan_button = tk.Button(root, text="wget", command=run_wgetscan)
wgetscan_button.grid(row=6, column=0, pady=4, padx=2, sticky=tk.W)

urlscan_button = tk.Button(root, text="urlscan", command=run_urlscan)
urlscan_button.grid(row=7, column=0, pady=4, padx=2, sticky=tk.W)

dirb_button = tk.Button(root, text="dirb", command=run_dirb)
dirb_button.grid(row=8, column=0, pady=4, padx=2, sticky=tk.W)

stage1_button = tk.Button(root, text="nmap stage 1", command=run_stage1)
stage1_button.grid(row=3, column=1, pady=4, padx=2, sticky=tk.W)

stage2_button = tk.Button(root, text="nmap stage 2", command=run_stage2)
stage2_button.grid(row=4, column=1, pady=4, padx=2, sticky=tk.W)

stage3_button = tk.Button(root, text="nmap stage 3", command=run_stage3)
stage3_button.grid(row=5, column=1, pady=4, padx=2, sticky=tk.W)

stage4_button = tk.Button(root, text="nmap stage 4", command=run_stage4)
stage4_button.grid(row=6, column=1, pady=4, padx=2, sticky=tk.W)

stage5_button = tk.Button(root, text="nmap stage 5", command=run_stage5)
stage5_button.grid(row=7, column=1, pady=4, padx=2, sticky=tk.W)

app = ApplicationForm(master=root)
root.mainloop()