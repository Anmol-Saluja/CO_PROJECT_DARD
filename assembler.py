import sys

class Assembler:
    def __init__(self):
        self.REGISTER_INST = {"zero":"00000","ra":"00001","sp":"00010","gp":"00011","tp":"00100",
            "t0":"00101","t1":"00110","t2":"00111","s0":"01000","fp":"01000",
            "a0":"01010","a1":"01011","a2":"01100","a3":"01101","a4":"01110",
            "a5":"01111","a6":"10000","a7":"10001","s2":"10010","s3":"10011",
            "s4":"10100","s5":"10101","s6":"10110","s7":"10111","s8":"11000",
            "s9":"11001","s10":"11010","s11":"11011","t3":"11100","t4":"11101",
            "t5":"11110","t6":"11111","s1":"01001"}
        self.labels={}

    def checkreg(self,reg):
        if reg not in self.REGISTER_INST:
            raise ValueError(f"Unsupported register: {reg}")
        
    def inst_handle(self,inst,pc):
        inst=inst.strip()
        if ':' in inst:
            label,instr=inst.split(':')
            self.labels[label.strip()]=pc
            inst=instr.strip()
        if not inst:
            return None
        
        inst=inst.replace(',', ' ').replace('(', ' ').replace(')', ' ')
        inst=inst.strip()
        parts=inst.split(' ')
        parts=[p for p in parts if p]
        cmd=parts[0]
        Flag=0
        if cmd=='add':
            funct7='0000000'
            funct3='000'
            opcode='0110011'
            self.checkreg(parts[1])
            self.checkreg(parts[2])
            self.checkreg(parts[3])
            rd=self.REGISTER_INST[parts[1]]
            rs1=self.REGISTER_INST[parts[2]]
            rs2=self.REGISTER_INST[parts[3]]
            return f"{funct7}{rs2}{rs1}{funct3}{rd}{opcode}"

        elif cmd=='sub':
            funct7='0100000'
            funct3='000'
            opcode='0110011'
            self.checkreg(parts[1])
            self.checkreg(parts[2])
            self.checkreg(parts[3])
            rd=self.REGISTER_INST[parts[1]]
            rs1=self.REGISTER_INST[parts[2]]
            rs2=self.REGISTER_INST[parts[3]]
            return f"{funct7}{rs2}{rs1}{funct3}{rd}{opcode}"

        elif cmd=='slt':
            funct7='0000000'
            funct3='010'
            opcode='0110011'
            self.checkreg(parts[1])
            self.checkreg(parts[2])
            self.checkreg(parts[3])
            rd=self.REGISTER_INST[parts[1]]
            rs1=self.REGISTER_INST[parts[2]]
            rs2=self.REGISTER_INST[parts[3]]
            return f"{funct7}{rs2}{rs1}{funct3}{rd}{opcode}"

        elif cmd=='srl':
            funct7='0000000'
            funct3='101'
            opcode='0110011'
            self.checkreg(parts[1])
            self.checkreg(parts[2])
            self.checkreg(parts[3])
            rd=self.REGISTER_INST[parts[1]]
            rs1=self.REGISTER_INST[parts[2]]
            rs2=self.REGISTER_INST[parts[3]]
            return f"{funct7}{rs2}{rs1}{funct3}{rd}{opcode}"

        elif cmd=='or':
            funct7='0000000'
            funct3='110'
            opcode='0110011'
            self.checkreg(parts[1])
            self.checkreg(parts[2])
            self.checkreg(parts[3])
            rd=self.REGISTER_INST[parts[1]]
            rs1=self.REGISTER_INST[parts[2]]
            rs2=self.REGISTER_INST[parts[3]]
            return f"{funct7}{rs2}{rs1}{funct3}{rd}{opcode}"

        elif cmd=='and':
            funct7='0000000'
            funct3='111'
            opcode='0110011'
            self.checkreg(parts[1])
            self.checkreg(parts[2])
            self.checkreg(parts[3])
            rd=self.REGISTER_INST[parts[1]]
            rs1=self.REGISTER_INST[parts[2]]
            rs2=self.REGISTER_INST[parts[3]]
            return f"{funct7}{rs2}{rs1}{funct3}{rd}{opcode}"

        elif cmd=='addi':
            opcode='0010011'
            funct3='000'
            self.checkreg(parts[1])
            self.checkreg(parts[2])
            rd=self.REGISTER_INST[parts[1]]
            rs1=self.REGISTER_INST[parts[2]]
            imm=int(parts[3])
            if -2048<=imm and imm<=2047:
                imm_bin=format(imm&0xFFF,'012b')
                return f"{imm_bin}{rs1}{funct3}{rd}{opcode}"
                
            else:
                raise ValueError(f"Immediate value out of range: {imm}")

        elif cmd=='lw':
            funct3='010'
            opcode='0000011'
            self.checkreg(parts[1])
            self.checkreg(parts[3])
            rd=self.REGISTER_INST[parts[1]]
            rs1=self.REGISTER_INST[parts[3]]
            imm=int(parts[2])
            if -2048<=imm and imm<=2047:
                imm_bin=format(imm&0xFFF,'012b')
                return f"{imm_bin}{rs1}{funct3}{rd}{opcode}"
                
            else:
                raise ValueError(f"Immediate value out of range: {imm}")

        elif cmd=='jalr':
            funct3='000'
            opcode='1100111'
            self.checkreg(parts[1])
            self.checkreg(parts[2])
            rd=self.REGISTER_INST[parts[1]]
            rs1=self.REGISTER_INST[parts[2]]
            imm=int(parts[3])
            if -2048<=imm and imm<=2047:
                imm_bin=format(imm&0xFFF,'012b')
                return f"{imm_bin}{rs1}{funct3}{rd}{opcode}"
                
            else:
                raise ValueError(f"Immediate value out of range: {imm}")

        elif cmd=='sw':
            funct3='010'
            opcode='0100011'
            self.checkreg(parts[1])
            self.checkreg(parts[3])
            rs2=self.REGISTER_INST[parts[1]]
            rs1=self.REGISTER_INST[parts[3]]
            imm=int(parts[2])
            if -2048<=imm and imm<=2047:
                imm_bin=format(imm&0xFFF,'012b')
                return f"{imm_bin[0:7]}{rs2}{rs1}{funct3}{imm_bin[7:12]}{opcode}"
            else:
                raise ValueError(f"Immediate value out of range: {imm}")

        elif cmd in ['beq','bne']:
            opcode='1100011'
            self.checkreg(parts[1])
            self.checkreg(parts[2])
            rs1=self.REGISTER_INST[parts[1]]
            rs2=self.REGISTER_INST[parts[2]]
            offset=parts[3]
            if offset in self.labels:
                val=(self.labels[offset]-pc)
            else:
                val=int(offset)
            imm=val
            if -2048<=imm and imm<=2047:
                imm_12=(imm>>12)&0x1
                imm_11=(imm>>11)&0x1
                imm_10_5=(imm>>5)&0x3F
                imm_4_1=(imm>>1)&0xF
                if cmd=='beq':
                    funct3='000'
                else:
                    funct3='001'
                return f"{imm_12:01b}{imm_10_5:06b}{rs2}{rs1}{funct3}{imm_4_1:04b}{imm_11:01b}{opcode}" 
                
            else:
                raise ValueError(f"Immediate value out of range: {imm}")

        elif cmd=='jal':
            opcode='1101111'
            rd=self.REGISTER_INST[parts[1]]
            self.checkreg(parts[1])
            offset=parts[2]
            if offset in self.labels:
                val=(self.labels[offset]-pc)
            else:
                val=int(offset)
            imm=val
            if -524288<=imm and imm<=524287:
                imm_20=(imm>>20)&0x1
                imm_10_1=(imm>>1)&0x3FF
                imm_11=(imm>>11)&0x1
                imm_19_12=(imm>>12)&0xFF
                return f"{imm_20:01b}{imm_10_1:010b}{imm_11:01b}{imm_19_12:08b}{rd}{opcode}"
                
            else:
                raise ValueError(f"Immediate value out of range: {imm}")
        else:
            raise ValueError(f"Unsupported instruction: {cmd}")

    def result(self,inst):
        bin_output=[]
        pc=0
        ct=0
        for instr in inst:
            instr=instr.strip()
            if ':' in instr:
                ct+=1
                pc+=4
                if ct==1:
                    pc=0
                label=instr.split(':')[0].strip()
                self.labels[label]=pc
            else:
                if instr:
                    pc+=4
                    ct+=1
                    if ct==1:
                        pc=0
        pc=0
        for instr in inst:
            instr=instr.strip()
            if ':' in instr:
                instr=instr.split(':')[1].strip()
            if instr:
                bin_output.append(self.inst_handle(instr, pc))
                pc += 4
        return bin_output

def main():
    if len(sys.argv) < 3:
        sys.exit(1)
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    assembler = Assembler()
    try:
        with open(input_file, "r") as f:
            inst = f.readlines()
        if inst and inst[-1] == '\n':
            inst.pop()
        bin_output = assembler.result(inst)
        with open(output_file, "w") as f:
            for code in bin_output:
                if code:
                    f.write(f"{code}\n")
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found")
        sys.exit(1)
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)
if __name__ == "__main__":
    main()
