# EE-5123-Computer-Architecture-Project-1
In this project, you will develop a MIPS binary disassembler. Your program will read in a text file that contains MIPS binary code, and output another text file that has the corresponding MIPS assembly code. Please do not hardcode the input/output filenames in the program, so that your program can be tested with other input files.
<br />The input file (see fib_bin.txt for example) contains a sequence of 32-bit MIPS instructions which begins at address "496". The final instruction in the sequence of instructions is always BREAK. Following that is a sequence of 32-bit two’s complement signed integers up to the end of the file.
<br />The output file (see fib_out.txt for example) contains four columns of data with each column separated by one tab character:
<br />The binary string representing the 32-bit data word at that location.
<br />The address (in decimal) of that location, starting from “496”.
<br />The disassembled instruction opcode (if the current location is before the BREAK instruction), or signed decimal integer value (if the current location is after the BREAK instruction).
<br />If you are displaying an instruction, the fourth column should contain the remaining part of the instruction, with each argument separated by a comma and then a space. (“, “)
<br />The instructions and instruction arguments should be in capital letters. All integer values should be displayed in decimal. Immediate values should be proceeded by a “#” symbol. Please be careful that some instructions take signed immediate values while others take unsigned immediate values. Make sure that you properly display a signed or unsigned value depending on the context.
<br />Your disassembler needs to support the following 27 MIPS32 instructions (not just those in the fib example). The encoding details of these instructions can be found in the attached MIPS32 architecture manual.
<br />J, JR, BEQ, BNE, BGEZ, BGTZ, BLEZ, BLTZ
<br />ADD, ADDU, SUB, SUBU
<br />ADDI, ADDIU
<br />SLL, SRL, SRA
<br />AND, OR, XOR, NOR
<br />SLT, SLTI
<br />SW, LW
<br />BREAK
<br />NOP
<br />The Fibonacci example is provided: fib_bin.txt is the input file; fib_out.txt is the output file; fib_mips.txt is the real assembly code; fib_c.txt is the corresponding C code. The last two files are just for your reference.
<br />Finally, please mimic the sample output format as closely as possible, since I will use “diff” to compare your output versus mine. Also, your program will be tested with other examples, so please try to create your own sample input files to further test your program.
