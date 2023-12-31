# MAC Address Changer

This is a Python script that allows you to change the MAC (Media Access Control) address of a network interface on a Linux system.

## Prerequisites

- This script requires Python to be installed on your system.
- The script utilizes the `ifconfig` command-line tool, which is typically available on Linux systems.

## Usage

1. Clone the repository or download the `mac_address_changer.py` file.

2. Open a terminal or command prompt and navigate to the directory where the `mac_address_changer.py` file is located.

3. Run the script by entering the following command:
   ```
   python mac_address_changer.py
   ```

4. The program will prompt you to enter the network interface for which you want to change the MAC address (e.g., wlan0).

5. The script will retrieve and display the current MAC address of the specified interface.

6. It will generate a random MAC address and display it as the new MAC address.

7. The program will attempt to change the MAC address of the specified interface to the new MAC address. It will display a success message if the MAC address is changed successfully or an error message if the change fails.
