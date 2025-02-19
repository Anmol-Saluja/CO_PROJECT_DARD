# CO_PROJECT
# RISC-V 32-bit Assembler

## Introduction
This project is a RISC-V 32-bit assembler implemented in Python using Object-Oriented Programming (OOP) principles. The assembler takes RISC-V assembly instructions as input and converts them into machine code (binary representation). It supports a subset of RISC-V instructions, handling registers, labels, and immediate values effectively.

## Features
- Converts RISC-V assembly instructions into binary machine code.
- Implements label handling for jump and branch instructions.
- Uses Python’s OOP approach for structured and modular design.
- Supports basic arithmetic, logical, memory access, and control flow instructions.

## Approach
The assembler follows a structured OOP-based approach:
1. **Class-based Design:** The `Assembler` class encapsulates instruction handling, register mapping, and label tracking.
2. **Register Mapping:** A dictionary is used to map register names to their corresponding binary representations.
3. **Instruction Handling:** A method processes each instruction, identifying operation types and converting them into binary format.
4. **Label Management:** Labels are stored in a dictionary and resolved during instruction translation.

## Supported Instructions
The assembler currently supports the following RISC-V instructions:

| Category       | Instructions      |
|---------------|------------------|
| Arithmetic    | `add`, `sub`      |
| Logical       | `and`, `or`       |
| Shift         | `srl`             |
| Comparison    | `slt`             |
| Immediate     | `addi`            |
| Load/Store   | `lw`, `sw`        |
| Branching    | `beq`, `bne`      |
| Jump         | `jal`, `jalr`     |

Future updates will expand support for more instructions and optimizations.

## Team Members
| Name            | Roll No  | GitHub Username  | Contributions |
|----------------|---------|-----------------|---------------|
| Anmol Saluja   | 2024085 | Anmol-Saluja    |               |
| Disha Kukkal   | 2024197 | CreativeMuch    |               |
| Divij Yadav    | 2024199 | wolf-havoc      |               |
| Rishit Sansanwal | 2024468 | Rishit468       |               |

(*The contributions column will be updated as work progresses.*)

## Usage
1. Clone the repository.
2. Run the assembler script with a set of RISC-V assembly instructions.
3. The output will be the binary representation of the given instructions.

## Future Improvements
- Expand instruction set coverage.
- Implement error handling for invalid instructions.
- Optimize label resolution and memory management.
- Add a user-friendly interface or command-line tool for ease of use.

## License
This project is open-source and available for educational and research purposes.

---
For any queries or contributions, feel free to raise an issue or a pull request on GitHub!

