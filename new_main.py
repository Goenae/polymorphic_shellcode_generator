import random

def main():
    nom_fichier = 'reverse.asm'
    ligne_a_supprimer = '  xor eax, eax'
    eax = ['  shr eax, 31', '  shl eax, 31\n  bswap eax\n  sub al, 0x80', '  sub eax, eax', '  mov eax, 0xFFFFFFFF\n  add eax, 1']
    rand = random.randint(0, len(eax))
    nouvelle_ligne = eax[rand]
    modifier_fichier(nom_fichier, ligne_a_supprimer, nouvelle_ligne)

    ligne_a_supprimer1 = '  xor ebx, ebx'
    ebx = ['  shr ebx, 31', '  shl ebx, 31\n  bswap ebx\n  sub bl, 0x80', '  sub ebx, eax', '  mov ebx, 0xFFFFFFFF\n  add ebx, 1']
    rand1 = random.randint(0, len(eax))
    nouvelle_ligne1 = ebx[rand1]
    modifier_fichier(nom_fichier, ligne_a_supprimer1, nouvelle_ligne1)

    ligne_a_supprimer2 = '  xor ecx, ecx'
    ecx = ['  shr ecx, 31', '  shl ecx, 31\n  bswap ecx\n  sub cl, 0x80', '  sub ecx, ecx', '  mov ecx, 0xFFFFFFFF\n  add ecx, 1']
    rand2 = random.randint(0, len(eax))
    nouvelle_ligne2 = ecx[rand2]
    modifier_fichier(nom_fichier, ligne_a_supprimer2, nouvelle_ligne2)

    ligne_a_supprimer3 = '  xor edx, edx'
    edx = ['  shr edx, 31', '  shl edx, 31\n  bswap edx\n  sub dl, 0x80', '  sub edx, edx', '  mov edx, 0xFFFFFFFF\n  add edx, 1']
    rand3 = random.randint(0, len(eax))
    nouvelle_ligne3 = ebx[rand3]
    modifier_fichier(nom_fichier, ligne_a_supprimer3, nouvelle_ligne3)

def modifier_fichier(nom_fichier, ligne_a_supprimer, nouvelle_ligne):
    try:
        with open(nom_fichier, 'r') as fichier:
            lignes = fichier.readlines()

        # Recherche de toutes les occurrences de la ligne à supprimer
        indices_a_supprimer = [i for i, ligne in enumerate(lignes) if ligne.strip() == ligne_a_supprimer.strip()]

        # Modification de toutes les occurrences
        for indice in reversed(indices_a_supprimer):
            del lignes[indice]
            lignes.insert(indice, nouvelle_ligne + '\n')

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