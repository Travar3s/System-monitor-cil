import psutil
import time

def show_cpu_usage():
    print(f"CPU Usage: {psutil.cpu_percent()}%")

def show_memory_usage():
    mem = psutil.virtual_memory()
    print(f"Memory Usage: {mem.percent}%")

def show_disk_usage():
    disk = psutil.disk_usage('/')
    print(f"Disk Usage: {disk.percent}%")

def show_network_io():
    net = psutil.net_io_counters()
    print(f"Bytes Sent: {net.bytes_sent}")
    print(f"Bytes Received: {net.bytes_recv}")

def show_uptime():
    boot_time = psutil.boot_time()
    uptime_seconds = time.time() - boot_time
    uptime_hours = uptime_seconds // 3600
    print(f"System Uptime: {int(uptime_hours)} hours")

def menu():
    while True:
        print("\nSystem Monitor Menu:")
        print("1. CPU Usage")
        print("2. Memory Usage")
        print("3. Disk Usage")
        print("4. Network I/O")
        print("5. System Uptime")
        print("6. Exit")
        choice = input("Enter choice (1–6): ")

        if choice == '1':
            show_cpu_usage()
        elif choice == '2':
            show_memory_usage()
        elif choice == '3':
            show_disk_usage()
        elif choice == '4':
            show_network_io()
        elif choice == '5':
            show_uptime()
        elif choice == '6':
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

menu()
