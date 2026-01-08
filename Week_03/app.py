
import sys
import getpass
from database import create_user, verify_user, update_user, delete_user
from utils import validate_username, validate_password, passwords_match

def prompt_signup():
    print("\n=== Sign Up ===")
    username = input("Username (min 5 chars): ").strip()
    password = getpass.getpass("Password (min 8 chars): ")
    confirm = getpass.getpass("Confirm Password: ")

    valid, msg = validate_username(username)
    if not valid:
        print(f"Error: {msg}")
        return

    valid, msg = validate_password(password)
    if not valid:
        print(f"Error: {msg}")
        return

    valid, msg = passwords_match(password, confirm)
    if not valid:
        print(f"Error: {msg}")
        return

    success, msg = create_user(username, password)
    print(msg)

def prompt_login():
    print("\n=== Login ===")
    username = input("Username: ").strip()
    password = getpass.getpass("Password: ")

    success, msg = verify_user(username, password)
    print(msg)
    if success:
        user_session(username)

def user_session(username):
    print(f"\nWelcome, {username}!")
    while True:
        print("\nOptions: [1] Update Account  [2] Delete Account  [3] Logout")
        choice = input("Select: ").strip()
        if choice == '1':
            prompt_update(username)
            return
        elif choice == '2':
            prompt_delete(username)
            return
        elif choice == '3':
            print("Logged out.")
            return
        else:
            print("Invalid option. Try again.")

def prompt_update(old_username):
    print("\n=== Update Account ===")
    print("Options: 1) Username  2) Password  3) Both")
    opt = input("Choose option (1/2/3): ").strip()
    new_username = None
    new_password = None

    if opt == '1':
        new_username = input("New username: ").strip()
    elif opt == '2':
        new_password = getpass.getpass("New password: ")
        confirm = getpass.getpass("Confirm new password: ")
        valid, msg = validate_password(new_password)
        if not valid:
            print(f"Error: {msg}")
            return
        valid, msg = passwords_match(new_password, confirm)
        if not valid:
            print(f"Error: {msg}")
            return
    elif opt == '3':
        new_username = input("New username: ").strip()
        new_password = getpass.getpass("New password: ")
        confirm = getpass.getpass("Confirm new password: ")
        valid, msg = validate_username(new_username)
        if not valid:
            print(f"Error: {msg}")
            return
        valid, msg = validate_password(new_password)
        if not valid:
            print(f"Error: {msg}")
            return
        valid, msg = passwords_match(new_password, confirm)
        if not valid:
            print(f"Error: {msg}")
            return
    else:
        print("Invalid option.")
        return

    success, msg = update_user(old_username, new_username, new_password)
    print(msg)
    if success and new_username:
        print("Username changed — please log in again with the new username.")

def prompt_delete(username):
    print("\n=== Delete Account ===")
    confirm = input(f"Type DELETE to permanently remove account '{username}': ").strip()
    if confirm != "DELETE":
        print("Aborted. You must type DELETE to confirm.")
        return
    success, msg = delete_user(username)
    print(msg)

def main_menu():
    print("User Management (Console)")
    while True:
        print("\nMain Menu:")
        print("1) Login")
        print("2) Sign Up")
        print("3) Exit")
        choice = input("Choose (1/2/3): ").strip()
        if choice == '1':
            prompt_login()
        elif choice == '2':
            prompt_signup()
        elif choice == '3':
            print("Goodbye.")
            sys.exit(0)
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    try:
        main_menu()
    except KeyboardInterrupt:
        print("\nInterrupted. Exiting.")
        sys.exit(0) 