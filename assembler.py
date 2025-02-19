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

    def inst_handle(self,inst,pc):
        inst=inst.strip()
        if ':' in inst:
            label,instr = inst.split(':')
            self.labels[label.strip()]=pc
            inst = instr.strip()
        if not inst:
            return None
        
        inst=inst.replace(',', ' ').replace('(', ' ').replace(')', ' ')
        inst=inst.strip()
        parts=inst.split(' ')
        parts=[p for p in parts if p]
        cmd=parts[0]

        if cmd=='add':
            funct7='0000000'
            funct3='000'
            opcode='0110011'
            rd=self.REGISTER_INST[parts[1]]
            rs1=self.REGISTER_INST[parts[2]]
            rs2=self.REGISTER_INST[parts[3]]
            return f"{funct7}{rs2}{rs1}{funct3}{rd}{opcode}"

        elif cmd=='sub':
            funct7='0100000'
            funct3='000'
            opcode='0110011'
            rd=self.REGISTER_INST[parts[1]]
            rs1=self.REGISTER_INST[parts[2]]
            rs2=self.REGISTER_INST[parts[3]]
            return f"{funct7}{rs2}{rs1}{funct3}{rd}{opcode}"

        elif cmd=='slt':
            pass

        elif cmd=='srl':
            pass

        elif cmd=='or':
            pass

        elif cmd=='and':
            pass

        elif cmd=='addi':
            pass

        elif cmd=='lw':
            pass

        elif cmd=='jalr':
            pass

        elif cmd=='sw':
            pass

        elif cmd in ['beq', 'bne']:
            pass

        elif cmd=='jal':
            pass

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
   pass

main()