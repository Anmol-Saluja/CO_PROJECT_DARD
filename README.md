# RISC-V 32-bit Assembler & Simulator

## CO_PROJECT For CSE_112_2025 Course @ IIIT-D

## Introduction
This project consists of a RISC-V 32-bit assembler and a simulator, both implemented in Python using Object-Oriented Programming (OOPS) principles and Sys library.

- The **assembler** converts RISC-V assembly instructions into machine code (binary representation), supporting a subset of RISC-V instructions while effectively handling registers, labels, and immediate values.
- The **simulator** executes the binary instructions, simulating the behavior of a RISC-V processor by maintaining registers and memory states.

## Features
### Assembler:
- Converts RISC-V assembly instructions into binary machine code.
- Implements label handling for jump and branch instructions.
- Uses Python’s OOPS approach for structured and modular design.
- Supports basic arithmetic, logical, memory access, and control flow instructions.

### Simulator:
- Simulates the execution of machine code on a RISC-V processor.
- Maintains register values and memory state.
- Handles various instruction categories, including arithmetic, branching, memory operations, and jumps.
- Generates output files with register and memory states.

## Approach
### Assembler:
- **Class-based Design**: The `Assembler` class encapsulates instruction handling, register mapping, and label tracking.
- **Register Mapping**: A dictionary maps register names to their corresponding binary representations.
- **Instruction Handling**: Methods process instructions, identify operation types, and convert them into binary format.
- **Label Management**: Labels are stored in a dictionary and resolved during instruction translation.

### Simulator:
- **Instruction Decoding**: The simulator decodes binary instructions into their components.
- **Execution Unit**: Each instruction is executed using appropriate functions, modifying registers or memory accordingly.
- **Program Counter (PC) Management**: The PC tracks instruction execution, supporting jumps and branches.
- **Memory Management**: A dictionary represents memory locations, storing and retrieving values as needed.

## Supported Instructions
The assembler and simulator support the following RISC-V instructions:

| Category   | Instructions   |
|------------|---------------|
| Arithmetic | add, sub       |
| Logical    | and, or        |
| Shift      | srl           |
| Comparison | slt           |
| Immediate  | addi          |
| Load/Store | lw, sw        |
| Branching  | beq, bne      |
| Jump       | jal, jalr     |

## Team Members
| Name           | Roll No  | GitHub Username  |
|---------------|----------|------------------|
| Anmol Saluja  | 2024085  | Anmol-Saluja     |
| Disha Kukkal  | 2024197  | CreativeMuch     |
| Divij Yadav   | 2024199  | wolf-havoc       |
| Rishit Sansanwal | 2024468 | Rishit468       |

## Usage
1. **Clone the repository**
```bash
    git clone https://github.com/your-repo-name.git
    cd your-repo-name
```
2. **Run the assembler**
```bash
    python3 assembler.py input.asm output.bin
```
3. **Run the simulator**
```bash
    python simulator.py output.bin out1.txt out2.txt
```
4. **Output**:
   - `out1.txt`: Contains register values after execution.
   - `out2.txt`: Contains memory states and final register values in binary format.

## Future Improvements/Updates
- Expand instruction set coverage.
- Implement error handling for invalid instructions.
- Optimize label resolution and memory management.
- Integrate assembler and simulator for a seamless workflow.

## License
This project is open-source and available for educational and research purposes.

For any queries or contributions, feel free to raise an issue or a pull request on GitHub!

