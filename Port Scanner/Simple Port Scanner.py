import socket
from datetime import datetime

def port_scanner(target, start_port, end_port):
    print(f"\nScanning Target: {target}")
    print(f"Scanning Started at: {datetime.now()}\n")

    try:
        for port in range(start_port, end_port + 1):
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(1)  # Timeout of 1 second for each port
                result = s.connect_ex((target, port))  # Returns 0 if port is open
                if result == 0:
                    print(f"Port {port}: OPEN")
    except KeyboardInterrupt:
        print("\nScan interrupted by user.")
    except socket.gaierror:
        print("\nHostname could not be resolved.")
    except socket.error:
        print("\nCouldn't connect to server.")

if __name__ == "__main__":
    print("Simple Port Scanner")
    target = input("Enter the target IP or hostname: ").strip()
    start_port = int(input("Enter the starting port (e.g., 1): "))
    end_port = int(input("Enter the ending port (e.g., 65535): "))

    print("\nStarting scan...")
    port_scanner(target, start_port, end_port)
    print("\nScan complete.")
