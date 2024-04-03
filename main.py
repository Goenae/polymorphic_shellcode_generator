import random
import os

def main():
    os.system("cp template.asm reverse.asm")
    
    file = 'reverse.asm'
    file_o = 'reverse.o'
    
    rax(file)
    rbx(file)
    rcx(file)
    rdx(file)

    os.system("nasm -f elf64 -o %s %s && ld -o reverse %s" % (file_o, file, file_o))

    commande = 'objdump -d reverse | grep "^ " | cut -f2 | awk \'{for(i=1;i<=NF;i++) printf "\\\\x%s",$i} END {print ""}\' > result.txt'
    os.system(commande)

    print(os.system("cat result.txt"))


def rax (file):
    delete = '  xor rax, rax'
    rax = ['  xor rax, rax', '  shr rax, 63', '  sub rax, rax', '  mov rax, 0xFFFFFFFFFFFFFFFF\n  add rax, 1', '  sar rax, 63']
    new = rax
    modifier_fichier(file, delete, new)

def rbx(file):
    delete = '  xor rbx, rbx'
    rbx = ['  xor rbx, rbx', '  shr rbx, 63', '  sub rbx, rbx', '  mov rbx, 0xFFFFFFFFFFFFFFFF\n  add rbx, 1', '  sar rbx, 63']
    new = rbx
    modifier_fichier(file, delete, new)

def rcx(file):
    delete = '  xor rcx, rcx'
    rcx = ['  xor rcx, rcx', '  shr rcx, 63', '  sub rcx, rcx', '  mov rcx, 0xFFFFFFFFFFFFFFFF\n  add rcx, 1', '  sar rcx, 63']
    new = rcx
    modifier_fichier(file, delete, new)

def rdx(file):
    delete = '  xor rdx, rdx'
    rdx = ['  xor rdx, rdx', '  shr rdx, 63', '  sub rdx, rdx', '  mov rdx, 0xFFFFFFFFFFFFFFFF\n  add rdx, 1', '  sar rdx, 63']
    new = rdx
    modifier_fichier(file, delete, new)



def modifier_fichier(nom_fichier, ligne_a_supprimer, nouvelle_ligne):
    try:
        with open(nom_fichier, 'r') as fichier:
            lignes = fichier.readlines()

        # Recherche de toutes les occurrences de la ligne à supprimer
        indices_a_supprimer = [i for i, ligne in enumerate(lignes) if ligne.strip() == ligne_a_supprimer.strip()]

        # Modification de toutes les occurrences
        for indice in reversed(indices_a_supprimer):
            del lignes[indice]
            rand = random.randint(0, len(nouvelle_ligne)-1)
            lignes.insert(indice, nouvelle_ligne[rand] + '\n')

        # Écriture du fichier modifié
        with open(nom_fichier, 'w') as fichier:
            fichier.writelines(lignes)

        print("Modification du fichier réussie.")
    except FileNotFoundError:
        print(f"Le fichier '{nom_fichier}' n'a pas été trouvé.")
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")

if __name__ == '__main__':
    main()
