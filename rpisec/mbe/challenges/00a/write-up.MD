Gabriel Lowden

The "file" command gives us the following output:
crackme0x00a: ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), dynamically linked, interpreter /lib/ld-linux.so.2, for GNU/Linux 2.6.15, BuildID[sha1]=a01d6d16a59c7f0d7ec00ab5454eed2eb22bd20d, not stripped

Lets try running it...
./crackme0x00a

The executable prompts us for a password.

Lets continue investigating.

The "strings" command gives us the following o/p:
/lib/ld-linux.so.2
__gmon_start__
libc.so.6
_IO_stdin_used
__isoc99_scanf
puts
__stack_chk_fail
printf
strcmp
__libc_start_main
GLIBC_2.7
GLIBC_2.4
GLIBC_2.0
PTRh
D$,1
T$,e3
UWVS
[^_]
Enter password: 
Congrats!
Wrong!
;*2$"
g00dJ0B!
GCC: (Ubuntu/Linaro 4.6.1-9ubuntu3) 4.6.1
.symtab
.strtab
.shstrtab
.interp
.note.ABI-tag
.note.gnu.build-id
.gnu.hash
.dynsym
.dynstr
.gnu.version
.gnu.version_r
.rel.dyn
.rel.plt
.init
.text
.fini
.rodata
.eh_frame_hdr
.eh_frame
.ctors
.dtors
.jcr
.dynamic
.got
.got.plt
.data
.bss
.comment
crtstuff.c
__CTOR_LIST__
__DTOR_LIST__
__JCR_LIST__
__do_global_dtors_aux
completed.6086
dtor_idx.6088
frame_dummy
__CTOR_END__
__FRAME_END__
__JCR_END__
__do_global_ctors_aux
pass1.c
pass.1685
__init_array_end
_DYNAMIC
__init_array_start
_GLOBAL_OFFSET_TABLE_
__libc_csu_fini
strcmp@@GLIBC_2.0
__i686.get_pc_thunk.bx
data_start
printf@@GLIBC_2.0
_edata
_fini
__stack_chk_fail@@GLIBC_2.4
__DTOR_END__
__data_start
puts@@GLIBC_2.0
__gmon_start__
__dso_handle
_IO_stdin_used
__libc_start_main@@GLIBC_2.0
__libc_csu_init
_end
_start
_fp_hw
__bss_start
main
_Jv_RegisterClasses
__isoc99_scanf@@GLIBC_2.7
_init

Near the top you can see the string "g00dJ0B!" that we did not see earlier when running the executable. 

Lets try that as the password.
Congrats!

