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
        # Use sys.argv[0] to reference the current script or executable
        ctypes.windll.shell32.ShellExecuteW(
            None, "runas", sys.executable if getattr(sys, 'frozen', False) else sys.argv[0], None, None, 1
        )
        sys.exit()

def add_context_menu():
    try:
        # Get the current directory where make_key.py or the executable is located
        current_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
        exe_path = os.path.join(current_dir, "resizer.exe")

        # Ensure the executable exists
        if not os.path.exists(exe_path):
            print(f"Error: {exe_path} does not exist. Make sure resizer.exe is in the same directory.")
            return

        # Define the registry key path for the context menu
        key_path = r"Directory\Background\shell\Resize"

        # Create the context menu entry
        with reg.CreateKey(reg.HKEY_CLASSES_ROOT, key_path) as key:
            reg.SetValue(key, "", reg.REG_SZ, "Resize")  # Set the menu name
            reg.SetValueEx(key, "Icon", 0, reg.REG_SZ, exe_path)  # Set the icon for the menu

        # Set the command to execute resizer.exe with the current directory as an argument
        command_path = key_path + r"\command"
        with reg.CreateKey(reg.HKEY_CLASSES_ROOT, command_path) as command_key:
            reg.SetValue(command_key, "", reg.REG_SZ, f'"{exe_path}" "%V"')  # Pass the current directory as an argument

        print("Context menu 'Resize' added successfully!")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    run_as_admin()  # Ensure the script runs with admin privileges
    add_context_menu()