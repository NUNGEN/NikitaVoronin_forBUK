def calculate_result(num1, num2, operation):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        if num2 == 0:
            return "Error: Divided by zero!"
        return num1 / num2
    else:
        return "Error: unsupported opperation"

def main():
    try:
        with open('Numbers.txt', 'r') as file:
            lines = file.readlines()
            if len(lines) < 2:
                print("Error: File must contain two strokes")
                return

            numbers = lines[0].strip().split()
            if len(numbers) != 2:
                print("Error: First stroke must contain two numbers")
                return

            try:
                num1 = float(numbers[0])
                num2 = float(numbers[1])
            except ValueError:
                print("Error: incorrect numbers format")
                return

            operation = lines[1].strip()
            result = calculate_result(num1, num2, operation)

            if isinstance(result, str) and result.startswith("Error"):
                print(result)
            else:
                print(f"Result is: {result}")

    except FileNotFoundError:
        print("Error: File Number.txt is not found")
    except Exception as e:
        print(f"Error: {e}")


main()