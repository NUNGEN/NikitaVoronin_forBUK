def main():
    filename = "username.txt" 

    forbidden_symbols = "!@#$%^&*_()"

    try:
        with open(filename, 'r') as file:
            lines = file.readlines()

            for line in lines:
                username = line.strip()  
                is_valid = True  

                for symbol in forbidden_symbols:
                    if symbol in username:
                        is_valid = False
                        break

                if is_valid:
                    print(f"{username} – correct")
                else:
                    print(f"{username} – incorrect username")

    except FileNotFoundError:
        print(f"Error: File {filename} not found!")
    except Exception as e:
        print(f"Error: Something went wrong: {e}")
main()
