import os
import winreg as reg
import ctypes
import sys

def is_admin():
    """Check if the script is running with administrator privileges."""
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def run_as_admin():
    """Restart the script with administrator privileges if not already elevated."""
    if not is_admin():
        print("Requesting administrator privileges...")
        ctypes.windll.shell32.ShellExecuteW(
            None, "runas", sys.executable, __file__, None, 1
        )
        sys.exit()

def remove_context_menu():
    try:
        # Define the registry key path for the context menu
        key_path = r"Directory\Background\shell\Resize"

        # Delete the "command" subkey
        reg.DeleteKey(reg.HKEY_CLASSES_ROOT, key_path + r"\command")

        # Delete the main "Resize" key
        reg.DeleteKey(reg.HKEY_CLASSES_ROOT, key_path)

        print("Context menu 'Resize' removed successfully!")

    except FileNotFoundError:
        print("Error: 'Resize' context menu does not exist.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    run_as_admin()  # Ensure the script runs with admin privileges
    remove_context_menu()