	.file	"narnia0.c"
	.text
	.globl	main
	.align	16, 0x90
	.type	main,@function
main:                                   # @main
	.cfi_startproc
# BB#0:
	pushq	%rbp
.Ltmp2:
	.cfi_def_cfa_offset 16
.Ltmp3:
	.cfi_offset %rbp, -16
	movq	%rsp, %rbp
.Ltmp4:
	.cfi_def_cfa_register %rbp
	subq	$80, %rsp
	leaq	.L.str, %rdi
	movl	$0, -4(%rbp)
	movq	$1094795585, -16(%rbp)  # imm = 0x41414141
	movb	$0, %al
	callq	printf
	leaq	.L.str1, %rdi
	movl	%eax, -52(%rbp)         # 4-byte Spill
	movb	$0, %al
	callq	printf
	leaq	.L.str2, %rdi
	leaq	-48(%rbp), %rsi
	movl	%eax, -56(%rbp)         # 4-byte Spill
	movb	$0, %al
	callq	__isoc99_scanf
	leaq	.L.str3, %rdi
	leaq	-48(%rbp), %rsi
	movl	%eax, -60(%rbp)         # 4-byte Spill
	movb	$0, %al
	callq	printf
	leaq	.L.str4, %rdi
	movq	-16(%rbp), %rsi
	movl	%eax, -64(%rbp)         # 4-byte Spill
	movb	$0, %al
	callq	printf
	movabsq	$3735928559, %rsi       # imm = 0xDEADBEEF
	cmpq	%rsi, -16(%rbp)
	movl	%eax, -68(%rbp)         # 4-byte Spill
	jne	.LBB0_2
# BB#1:
	leaq	.L.str5, %rdi
	callq	system
	movl	%eax, -72(%rbp)         # 4-byte Spill
	jmp	.LBB0_3
.LBB0_2:
	leaq	.L.str6, %rdi
	movb	$0, %al
	callq	printf
	movl	$1, %edi
	movl	%eax, -76(%rbp)         # 4-byte Spill
	callq	exit
.LBB0_3:
	movl	$0, %eax
	addq	$80, %rsp
	popq	%rbp
	ret
.Ltmp5:
	.size	main, .Ltmp5-main
	.cfi_endproc

	.type	.L.str,@object          # @.str
	.section	.rodata.str1.1,"aMS",@progbits,1
.L.str:
	.asciz	 "Correct val's value from 0x41414141 -> 0xdeadbeef!\n"
	.size	.L.str, 52

	.type	.L.str1,@object         # @.str1
.L.str1:
	.asciz	 "Here is your chance: "
	.size	.L.str1, 22

	.type	.L.str2,@object         # @.str2
.L.str2:
	.asciz	 "%24s"
	.size	.L.str2, 5

	.type	.L.str3,@object         # @.str3
.L.str3:
	.asciz	 "buf: %s\n"
	.size	.L.str3, 9

	.type	.L.str4,@object         # @.str4
.L.str4:
	.asciz	 "val: 0x%08x\n"
	.size	.L.str4, 13

	.type	.L.str5,@object         # @.str5
.L.str5:
	.asciz	 "/bin/sh"
	.size	.L.str5, 8

	.type	.L.str6,@object         # @.str6
.L.str6:
	.asciz	 "WAY OFF!!!!\n"
	.size	.L.str6, 13


	.section	".note.GNU-stack","",@progbits
