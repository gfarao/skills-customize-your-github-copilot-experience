# 📘 Assignment: Computer Architecture

## 🎯 Objective

Explore the fundamental concepts of computer architecture by simulating basic CPU components and understanding how binary data is processed, stored, and retrieved in a computer system.

## 📝 Tasks

### 🛠️	Binary and Hexadecimal Conversion

#### Description
Write a Python program that converts numbers between decimal, binary, and hexadecimal representations. This will help you understand how computers store and process data at the lowest level.

#### Requirements
Completed program should:

- Accept a decimal integer as input from the user
- Display the binary representation of the number (using `bin()` or manual conversion)
- Display the hexadecimal representation of the number (using `hex()` or manual conversion)
- Handle invalid input gracefully with a helpful error message
- Support numbers in the range 0–65535 (16-bit unsigned integers)

### 🛠️	Simulate a Simple Register Machine

#### Description
Implement a simple register-based calculator that mimics how a CPU uses registers to perform arithmetic operations. Your program should support a small set of instructions to load values, perform operations, and display results.

#### Requirements
Completed program should:

- Define at least 4 registers (e.g., R0, R1, R2, R3) initialized to 0
- Support the following instructions:
  - `LOAD Rx, value` — load a value into a register
  - `ADD Rx, Ry` — add two registers and store the result in Rx
  - `SUB Rx, Ry` — subtract Ry from Rx and store the result in Rx
  - `PRINT Rx` — display the current value of a register
- Read a sequence of instructions from the user (or a hardcoded list) and execute them
- Display an error message for unrecognized instructions
