import subprocess
import re
import random

def get_current_mac(interface):
    """
    Retrieves the current MAC address of the specified interface.
    Returns the MAC address as a string.
    """
    ifconfig_result = subprocess.check_output(["ifconfig", interface]).decode()
    mac_address_search_result = re.search(r"(\w\w:\w\w:\w\w:\w\w:\w\w:\w\w)", ifconfig_result)

    if mac_address_search_result:
        return mac_address_search_result.group(0)
    else:
        return None

def change_mac(interface, new_mac):
    """
    Changes the MAC address of the specified interface to the given MAC address.
    Returns True if the MAC address is changed successfully, False otherwise.
    """
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

    # Verify if the MAC address is changed
    current_mac = get_current_mac(interface)
    if current_mac == new_mac:
        return True
    else:
        return False

def generate_random_mac():
    """
    Generates a random MAC address.
    Returns the MAC address as a string.
    """
    random_mac = [
        0x00,
        0x16,
        0x3e,
        random.randint(0x00, 0x7f),
        random.randint(0x00, 0xff),
        random.randint(0x00, 0xff)
    ]
    mac_address = ':'.join(map(lambda x: "%02x" % x, random_mac))
    return mac_address

def main():
    interface = input("Enter the interface (e.g., wlan0): ")

    current_mac = get_current_mac(interface)
    if current_mac:
        print(f"Current MAC address: {current_mac}")
    else:
        print("Failed to retrieve current MAC address. Please check the interface.")

    new_mac = generate_random_mac()
    print(f"New MAC address: {new_mac}")

    if change_mac(interface, new_mac):
        print(f"MAC address changed successfully to {new_mac}")
    else:
        print("Failed to change MAC address. Please check the interface.")

if __name__ == '__main__':
    main()
