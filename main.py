import random
import os

def main():
    file = 'reverse.asm'
    file_o = 'reverse.o'
    eax(file)
    ebx(file)
    ecx(file)
    edx(file)

    os.system("nasm -f elf32 -o reverse.o reverse.asm && ld -m elf_i386 -o reverse reverse.o")

    commande = 'objdump -d reverse | grep "^ " | cut -f2 | awk \'{for(i=1;i<=NF;i++) printf "\\\\x%s",$i} END {print ""}\' >> result.txt'
    os.system(commande)

    print(os.system("cat result.txt"))


def eax (file):
    delete = '  xor eax, eax'
    eax = ['  xor eax, eax', '  shr eax, 31', '  sub eax, eax', '  mov eax, 0xFFFFFFFF\n  add eax, 1']
    new = eax
    modifier_fichier(file, delete, new)

def ebx(file):
    delete = '  xor ebx, ebx'
    ebx = ['  xor ebx, ebx', '  shr ebx, 31', '  sub ebx, eax', '  mov ebx, 0xFFFFFFFF\n  add ebx, 1']
    new = ebx
    modifier_fichier(file, delete, new)

def ecx(file):
    delete = '  xor ecx, ecx'
    ecx = ['  xor ecx, ecx', '  shr ecx, 31', '  sub ecx, ecx', '  mov ecx, 0xFFFFFFFF\n  add ecx, 1']
    new = ecx
    modifier_fichier(file, delete, new)

def edx(file):
    delete = '  xor edx, edx'
    edx = ['  xor edx, edx', '  shr edx, 31', '  sub edx, edx', '  mov edx, 0xFFFFFFFF\n  add edx, 1']
    new = edx
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
