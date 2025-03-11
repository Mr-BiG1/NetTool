from scapy.all import *
import tkinter as tk
from tkinter import ttk, scrolledtext
import threading
import time
from collections import defaultdict


class NetworkMonitorGUI:
    def _init_(self,root):
        self.root = root
        self.root.title("Network Monitor")
        self.root.geometry("1000X700")


        # Monitoring COntrol

        self.monitoring = False
        self.ssh_threshold = 5
        self.portscan_threshold = 5
        


        # creating the GUI element 
        self.create_widgets()


        # installing statistics
        self.traffic_stats = defaultdict(int)
        self.alert = []
        self.update_interval = 2

        # starting perodic UI update 
        self.update_stats()

    def create_widgets(self):
        # control Panel
        control_frame = ttk.LabelFrame(self.root, text="Contents")
        control_frame.pack(pady=10, padx=10, fill="x")

        self.start_btn = ttk.Button(control_frame, text="Start Monitoring", command=self.toggle_monitoring)
        