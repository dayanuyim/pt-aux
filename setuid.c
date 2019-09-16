#include <sys/types.h>
#include <unistd.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <errno.h>

int main(int argc, char *argv[])
{
    int id = (argc == 2)? atoi(argv[1]): 0;

    if(setgid(id) == -1)
        fprintf(stderr, "[+] setgid(%d): error: %s\n", id, strerror(errno));
    else
        fprintf(stderr, "[+] setgid(%d): ok\n", id);


    if(setuid(id) == -1)
        fprintf(stderr, "[+] setuid(%d): error: %s\n", id, strerror(errno));
    else
        fprintf(stderr, "[+] setuid(%d): ok\n", id);

    if(execl("/bin/sh", "sh", 0) == -1)
        fprintf(stderr, "[+] exec /bin/sh: error: %s\n", strerror(errno));

    return 0;
}
