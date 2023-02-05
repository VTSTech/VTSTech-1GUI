# Program: VTSTech-1GUI.py
# Version: 0.0.1 Revision 02
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
import tkinter as tk
from tkinter import messagebox
v="0.0.1-r02"
def run_stage1():
    target = entry.get()
    n1="sudo nmap -Pn --reason -T4 --top-ports 100 -vv -sS -oX nmap1-{}.xml --stylesheet https://svn.nmap.org/nmap/docs/nmap.xsl {}".format(target, target)
    os.system(n1)
    messagebox.showinfo("Info", "nmap stage 1 completed!")
def run_stage2():
    target = entry.get()
    n2="sudo nmap -Pn --reason -T4 --top-ports 250 -vv -sS -oX nmap2-{}.xml --stylesheet https://svn.nmap.org/nmap/docs/nmap.xsl {}".format(target, target)
    os.system(n2)
    messagebox.showinfo("Info", "nmap stage 2 completed!")
def run_stage3():
    target = entry.get()
    n3="sudo nmap -Pn --reason -T4 --top-ports 500 -vv -sSV -oX nmap3-{}.xml --stylesheet https://svn.nmap.org/nmap/docs/nmap.xsl {}".format(target, target)
    os.system(n3)
    messagebox.showinfo("Info", "nmap stage 3 completed!")
def run_stage4():
    target = entry.get()
    n4="sudo nmap -Pn --reason -T4 --top-ports 750 -vv -sSV -oX nmap4-{}.xml --stylesheet https://svn.nmap.org/nmap/docs/nmap.xsl {}".format(target, target)
    os.system(n4)
    messagebox.showinfo("Info", "nmap stage 4 completed!")
def run_stage5():
    target = entry.get()
    n5="sudo nmap -Pn --reason -T4 --top-ports 999 -vv -sSV -oX nmap5-{}.xml --stylesheet https://svn.nmap.org/nmap/docs/nmap.xsl {}".format(target, target)
    os.system(n5)
    messagebox.showinfo("Info", "nmap stage 5 completed!")    
def run_dnsrecon():
    target = entry.get()
    dnscmd="sudo dnsrecon -t std,srv,zonewalk -n 8.8.8.8 -z -f --iw --threads 2 --lifetime 10 --xml dnsrecon-{}.xml -d {}".format(target, target)
    os.system(dnscmd)
    messagebox.showinfo("Info", "dnsrecon completed!")		
def run_sslscan():
    target = entry.get()
    sslcmd="sudo sslscan --verbose --no-colour --show-certificate --xml=sslscan-{}.xml {}".format(target, target)
    os.system(sslcmd)
    messagebox.showinfo("Info", "sslscan completed!")		
def run_wpscan():
    target = entry.get()
    wpcmd="sudo wpscan -e p,t,tt,u1-20 -t 2 -v -f cli-no-color -o wpscan-{}.txt --url {}".format(target, target)
    os.system(wpcmd)
    messagebox.showinfo("Info", "wpscan completed!")		
def run_wgetscan():
    target = entry.get()
    wgetcmd="sudo wget -t 4 --content-on-error https://{}/ -O wget-{}.txt".format(target, target)
    os.system(wgetcmd)
    messagebox.showinfo("Info", "wget completed!")	
def run_urlscan():
    target = entry.get()
    urlcmd="sudo urlscan -c -n wget-{}.txt | tee urlscan-{}.txt".format(target, target)
    os.system(urlcmd)
    messagebox.showinfo("Info", "urlscan completed!")	    

root = tk.Tk()

window_width = 320
window_height = 420

# get the screen dimension
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# find the center point
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

# set the position of the window to the center of the screen
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
root.title("VTSTech-1GUI {}".format(v))

label = tk.Label(root, text="Enter target (IP/Hostname):")
label.pack(pady=4,padx=2,anchor=tk.W)

entry = tk.Entry(root)
entry.pack(pady=4,padx=2,anchor=tk.W)

dnsrecon_button = tk.Button(root, text="dnsrecon", command=run_dnsrecon)
dnsrecon_button.pack(padx=2,anchor=tk.W)

sslscan_button = tk.Button(root, text="sslscan", command=run_sslscan)
sslscan_button.pack(padx=2,anchor=tk.W)

wpscan_button = tk.Button(root, text="wpscan", command=run_wpscan)
wpscan_button.pack(padx=2,anchor=tk.W)

wgetscan_button = tk.Button(root, text="wget", command=run_wgetscan)
wgetscan_button.pack(padx=2,anchor=tk.W)

urlscan_button = tk.Button(root, text="urlscan", command=run_urlscan)
urlscan_button.pack(padx=2,anchor=tk.W)

stage1_button = tk.Button(root, text="nmap stage 1", command=run_stage1)
stage1_button.pack(padx=2,anchor=tk.W)

stage2_button = tk.Button(root, text="nmap stage 2", command=run_stage2)
stage2_button.pack(padx=2,anchor=tk.W)

stage3_button = tk.Button(root, text="nmap stage 3", command=run_stage3)
stage3_button.pack(padx=2,anchor=tk.W)

stage4_button = tk.Button(root, text="nmap stage 4", command=run_stage4)
stage4_button.pack(padx=2,anchor=tk.W)

stage5_button = tk.Button(root, text="nmap stage 5", command=run_stage5)
stage5_button.pack(padx=2,anchor=tk.W)

root.mainloop()
