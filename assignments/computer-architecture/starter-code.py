# Starter Code: Computer Architecture

# ── Task 1: Binary and Hexadecimal Conversion ──────────────────────────────

def convert_number(decimal_value):
    """Convert a decimal number to binary and hexadecimal."""
    # TODO: Return the binary and hex representations of decimal_value
    pass


def task1():
    user_input = input("Enter a decimal integer (0–65535): ")
    # TODO: Validate the input, call convert_number(), and print the results
    pass


# ── Task 2: Simple Register Machine ────────────────────────────────────────

REGISTERS = {"R0": 0, "R1": 0, "R2": 0, "R3": 0}

def execute_instruction(instruction):
    """Parse and execute a single register-machine instruction."""
    # TODO: Implement LOAD, ADD, SUB, and PRINT instructions
    pass


def task2():
    print("Register Machine — enter instructions (blank line to stop):")
    while True:
        line = input("> ").strip()
        if not line:
            break
        execute_instruction(line)


# ── Main ────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("=== Task 1: Number Conversion ===")
    task1()
    print("\n=== Task 2: Register Machine ===")
    task2()
