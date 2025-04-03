import sys
registers = {f"x{i}": 0 for i in range(32)}
registers["x2"] = 380
PC = 4
memory_values = {
    "0x10000": 0,
    "0x10004": 0,
    "0x10008": 0,
    "0x1000C": 0,
    "0x10010": 0,
    "0x10014": 0,
    "0x10018": 0,
    "0x1001C": 0,
    "0x10020": 0,
    "0x10024": 0,
    "0x10028": 0,
    "0x1002C": 0,
    "0x10030": 0,
    "0x10034": 0,
    "0x10038": 0,
    "0x1003C": 0,
    "0x10040": 0,
    "0x10044": 0,
    "0x10048": 0,
    "0x1004C": 0,
    "0x10050": 0,
    "0x10054": 0,
    "0x10058": 0,
    "0x1005C": 0,
    "0x10060": 0,
    "0x10064": 0,
    "0x10068": 0,
    "0x1006c": 0,
    "0x10070": 0,
    "0x10074": 0,
    "0x10078": 0,
    "0x1007C": 0
}
def unsigned(val,bits=32):
    binary = val&((1<<bits)-1)
    return binary
    
def convert(n,bits=32):
    if n<0:
        n=(1<<bits)+n
    else:
        n=n&((1<<bits)-1)
    return format(n,f'0{bits}b')

def addi(rs1,rd,imm):
    global PC
    rs1=int(rs1,2)
    rd=int(rd,2)
    imm_dec=int(imm,2)

    if imm[0]=="1":
        imm_dec-=4096
    registers[f"x{rd}"]=registers[f"x{rs1}"]+imm_dec

def lw(rs1, rd, imm):
    global PC
    rs1 = int(rs1, 2)
    rd = int(rd, 2)
    imm_dec = int(imm, 2)

    if imm[0] == "1":
        imm_dec -= 4096

    address = registers[f"x{rs1}"] + imm_dec
    registers[f"x{rd}"] = memory_values.get(hex(address), 0)

def rtype(funct7, funct3, rs1, rs2, rd):
    global PC
    rs1 = int(rs1, 2)
    rd = int(rd, 2)
    rs2 = int(rs2, 2)
    if funct3 == "000":
        if funct7 == "0000000":
            registers[f"x{rd}"] = registers[f"x{rs1}"] + registers[f"x{rs2}"]
        elif funct7 == "0100000":
            registers[f"x{rd}"] = registers[f"x{rs1}"] - registers[f"x{rs2}"]
            if(registers[f"x{rd}"] < 0):
                registers[f"x{rd}"] = registers[f"x{rs1}"] + unsigned(-registers[f"x{rs2}"])
    elif funct3 == "010":
        if registers[f"x{rs1}"] < registers[f"x{rs2}"]:
            registers[f"x{rd}"] = 1
        else:
            registers[f"x{rd}"] = 0
    elif funct3 == "101":
        registers[f"x{rd}"] = registers[f"x{rs1}"] >> (registers[f"x{rs2}"] & 0x1F)
    elif funct3 == "110":
        registers[f"x{rd}"] = registers[f"x{rs1}"] | registers[f"x{rs2}"]
    elif funct3 == "111":
        registers[f"x{rd}"] = registers[f"x{rs1}"] & registers[f"x{rs2}"]
        
def jalr(rs1, rd, imm):
    global PC
    rs1 = int(rs1, 2)
    rd = int(rd, 2)
    imm_dec = int(imm, 2)
    if imm[0] == "1":
        imm_dec -= 4096
    target_address = (registers[f"x{rs1}"] + imm_dec)
    if rd != 0:
        registers[f"x{rd}"] = PC  
    PC = target_address

def btype(funct3, rs1, rs2, imm31_25, imm11_7):
    global PC
    imm_12 = imm31_25[0]
    imm_11 = imm11_7[-1]
    imm_10_5 = imm31_25[1:]
    imm_4_1 = imm11_7[:4]
    
    imm_binary = imm_12 + imm_11 + imm_10_5 + imm_4_1 + "0"
    imm = int(imm_binary, 2)
    if imm_binary[0] == "1":
        imm -= (8192)
    
    rs1_val = int(rs1, 2)
    rs2_val = int(rs2, 2)
    branch_taken = False
    if funct3 == "000":
        branch_taken = (registers[f"x{rs1_val}"] == registers[f"x{rs2_val}"])
    elif funct3 == "001":
        branch_taken = (registers[f"x{rs1_val}"] != registers[f"x{rs2_val}"])
    elif funct3 == "100":
        branch_taken = (registers[f"x{rs1_val}"] < registers[f"x{rs2_val}"])
    if branch_taken:
        PC += imm - 4 

def jtype(opcode, rd, imm31_12):
    global PC
    imm_20 = imm31_12[0]       
    imm_10_1 = imm31_12[1:11]  
    imm_11 = imm31_12[11]     
    imm_19_12 = imm31_12[12:20]  

    imm_binary = imm_20 + imm_19_12 + imm_11 + imm_10_1 + "0"
    imm = int(imm_binary, 2)
    if imm_binary[0] == "1":
        imm -= 2097152  #

    registers[f"x{int(rd, 2)}"] = PC  
    PC += imm  
    PC -= 4  
    
def execute(instruction_dict):
    global PC
    L1 = []
    L2 = []
    while PC in instruction_dict:
        bits = instruction_dict[PC]
        opcode = bits[-7:] 
        rd = bits[20:25]
        funct3 = bits[17:20]
        rs1 = bits[12:17]
        rs2 = bits[7:12]
        funct7 = bits[0:7]
        imm31_25 = bits[0:7]
        imm11_7 = bits[20:25]
        imm31_12 = bits[0:20]
        imm = bits[0:12]

        if opcode == "0010011":  
            addi(rs1, rd, imm)
        elif opcode == "0000011":  
            lw(rs1, rd, imm)
        elif opcode == "0110011":  
            rtype(funct7, funct3, rs1, rs2, rd)
        elif opcode == "1100011":  
            btype(funct3, rs1, rs2, imm31_25, imm11_7)
        elif opcode == "1101111":  
            jtype(opcode, rd, imm31_12)
        elif opcode == "1100111":
            jalr(rs1, rd, imm)
        elif opcode == "0100011":
            sw(funct3, rs1, rs2, imm31_25, imm11_7)
        reg_state1 = ""
        reg_state2 = ""
        reg_state1 += f"{PC}"
        reg_state2 += f"0b{convert(PC)}"
        for i in range(32):
            reg_state1 += f" {registers[f'x{i}']}"
            reg_state2 += f" 0b{convert(registers[f'x{i}'])}"
        L1.append(reg_state1)
        L2.append(reg_state2)
        PC += 4  
    return L1, L2

def main():
    if len(sys.argv) < 2:
        sys.exit(1)
    input_file = sys.argv[1]
    output_file1 = sys.argv[2] if len(sys.argv) > 2 else "out1.txt"
    output_file2 = sys.argv[3] if len(sys.argv) > 3 else "out2.txt"
    try:
        with open(input_file, "r") as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f"Error: Input file '{input_file}' not found")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading input file: {str(e)}")
        sys.exit(1)
    instruction_dict = {}
    addr=4
    for line in lines:
        instruction_dict[addr]=line.strip()
        addr += 4
    L1, L2 = execute(instruction_dict)
    try:
        with open(output_file1, "w") as f1:
            for i in L1:
                f1.write(i)
                f1.write("\n")
            f1.write(L1[-1])
            f1.write("\n")
            for i in memory_values:
                f1.write(f"{i[0:2]}000{i[2::]}:{memory_values[i]}")
                f1.write("\n")
                if i=="0x1007C":
                    break
        
        with open(output_file2, "w") as f2:
            for i in L2:
                f2.write(i)
                f2.write("\n")
            f2.write(L2[-1])
            f2.write("\n")
            for i in memory_values:
                f2.write(f"{i[0:2]}000{i[2::]}:0b{convert(memory_values[i])}")
                f2.write("\n")
                if i=="0x1007C":
                    break
            
        print(f"Successfully wrote output to '{output_file1}' and '{output_file2}'")
    except Exception as e:
        print(f"Error writing output files: {str(e)}")
        sys.exit(1)
main()
