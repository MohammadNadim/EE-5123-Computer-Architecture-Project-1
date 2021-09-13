"""
This is project 1 for EE-5123 computer architecture course.
Group 3:
1. Mohammad Nadim
2. Md. Musaddaqul Hasib
3. Md. Khairul Anam

"""

i = 0
j = 0
binary = []
string = []
MIPS_address = 496
function_output = []
end_list = False

# read input file.
file_name = raw_input("Please enter input text file name with extension: ")
file_open = open(file_name,'r')
#file_open = open('input.txt','r')



# read line from file
for line in file_open:
	string.append(line)
	binary.append(bin(int(string[i],2))[2:].zfill(32))
	i = i+1
length_binary = len(binary)


# convert binary to decimal
def binary_to_decimal(binary):
	decimal = int(binary,2)
	return decimal

# ADD, ADDU, SUB, SUBU instructions.
def ADD_SUB_UNSIGNED(data):
	function = binary_to_decimal(data[26:32])
	rs = 'R' + str(binary_to_decimal(data[6:11]))
	rt = 'R' + str(binary_to_decimal(data[11:16]))
	rd = 'R' + str(binary_to_decimal(data[16:21]))
	if function==32:
		op = 'ADD'
	elif function==33:
		op = 'ADDU'
	elif function==34:
		op = 'SUB'
	elif function==35:
		op = 'SUBU'

	answer = op +'	'+rd+', '+rs+', '+rt
	function_output.append(str(data)+'	'+str(MIPS_address)+'	'+answer)


# AND, OR, XOR, NOR, SLT instruction.
def LOGICAL(data):
	function = binary_to_decimal(data[26:32])
	if function==36:
		op = 'AND'
	elif function==37:
		op = 'OR'
	elif function==38:
		op = 'XOR'
	elif function==39:
		op = 'NOR'
	elif function==42:
		op = 'SLT'

	rs = 'R' + str(binary_to_decimal(data[6:11]))
	rt = 'R' + str(binary_to_decimal(data[11:16]))
	rd = 'R' + str(binary_to_decimal(data[16:21]))
	answer = op +'	'+rd+', '+rs+', '+rt
	function_output.append(str(data)+'	'+str(MIPS_address)+'	'+answer)


# SLL, SRL, SRA instructions.
def SHIFT(data):
	function = binary_to_decimal(data[26:32])
	if function==0:
		op = 'SLL'
	if function==2:
		op = 'SRL'
	elif function==3:
		op = 'SRA'

	rt = 'R' + str(binary_to_decimal(data[11:16]))
	rd = 'R' + str(binary_to_decimal(data[16:21]))
	shamt = 'R' + str(binary_to_decimal(data[21:26]))
	answer = op +'	'+rd+', '+rt+', '+shamt
	function_output.append(str(data)+'	'+str(MIPS_address)+'	'+answer)

# JR jump register instruction
def JUMP_REGISTER(data):
	op = 'JR'
	rs = 'R' + str(binary_to_decimal(data[6:11]))
	answer = op +'	'+rs
	function_output.append(str(data)+'	'+str(MIPS_address)+'	'+answer)



# BREAK, NOP instruction
def EXCEPTION(data):
	function = binary_to_decimal(data[26:32])
	if function==0:
		op = 'NOP'
	elif function==13:
		op = 'BREAK'

	answer = op
	function_output.append(str(data)+'	'+str(MIPS_address)+'	'+answer)



# r type instruction
def r_type_instruction(data):
	opcode = binary_to_decimal(data[0:6])
	function = binary_to_decimal(data[26:32])
	
	if function==32 or function==33 or function==34 or function==35:
		ADD_SUB_UNSIGNED(data)
	elif function==36 or function==37 or function==38 or function==39 or function==42:
		LOGICAL(data)
	elif function==0 or function==2 or function==3:
		SHIFT(data)
	elif function==8:
		JUMP_REGISTER(data)
	else:
		answer = 'Function not listed.'
		function_output.append(str(data)+'	'+str(MIPS_address)+'	'+answer)

		
# two's complement function
def twos_compliment(data):
	number = 0
	# positive number
	if int(data[0],2)==0:
		for i in range(len(data)):
			j = int(data[i],2)
			number+= j*(2**(len(data)-1-i))
	# negative number
	else:
		for i in range(len(data)):
			if int(data[i],2)==0:
				j = 1
				number+= j*(2**(len(data)-1-i))
			else:
				j = 0
				number+= j*(2**(len(data)-1-i))
		
		number = -1*(number+1)

	return number
	

# ADDI, ADDIU. immediate instructions
def immediate(data):
	opcode = binary_to_decimal(data[0:6])
	rs = 'R' + str(binary_to_decimal(data[6:11]))
	rt = 'R' + str(binary_to_decimal(data[11:16]))
	imm = '#' + str(twos_compliment(data[16:32]))
	if opcode==8:
		op = 'ADDI'
	elif opcode==9:
		op = 'ADDIU'
		imm = '#' + str(binary_to_decimal(data[16:32]))
	elif opcode==10:
		op = 'SLTI'


	answer = op +'	'+rt+', '+rs+', '+imm
	function_output.append(str(data)+'	'+str(MIPS_address)+'	'+answer)
	

# Load-Store instructions. LW, SW
def LOAD_STORE(data):
	opcode = binary_to_decimal(data[0:6])
	if opcode==35:
		op = 'LW'
	elif opcode==43:
		op = 'SW'

	rs = 'R' + str(binary_to_decimal(data[6:11]))
	rt = 'R' + str(binary_to_decimal(data[11:16]))
	imm = str(twos_compliment(data[16:32]))
	answer = op +'	'+rt+', '+imm+'('+rs+')'
	function_output.append(str(data)+'	'+str(MIPS_address)+'	'+answer)

# Jump instructions. J
def JUMP(data):
	opcode = binary_to_decimal(data[0:6])
	if opcode==2:
		op = 'J'

	imm = '#' + str(twos_compliment(data[6:32]))
	answer = op +'	'+imm
	function_output.append(str(data)+'	'+str(MIPS_address)+'	'+answer)


# branch instructions. BEQ, BNE, BLEZ, BGTZ
def BRANCH(data):
	opcode = binary_to_decimal(data[0:6])
	if opcode==4:
		op = 'BEQ'
	elif opcode==5:
		op = 'BNE'

	rs = 'R' + str(binary_to_decimal(data[6:11]))
	rt = 'R' + str(binary_to_decimal(data[11:16]))
	imm = '#' + str(twos_compliment(data[16:32]))
	answer = op +'	'+rs+', '+rt+', '+imm
	function_output.append(str(data)+'	'+str(MIPS_address)+'	'+answer)


# another branch. BLTZ, BGEZ, BLEZ, BGTZ.
def BRANCH_2(data):
	opcode = binary_to_decimal(data[0:6])
	rt = 'R' + str(binary_to_decimal(data[11:16]))
	if opcode==1:
		if rt==0:
			op = 'BLTZ'
		elif rt==1:
			op = 'BGEZ'
	elif opcode==6:
		op = 'BLEZ'
	elif opcode==7:
		op = 'BGTZ'

	rs = 'R' + str(binary_to_decimal(data[6:11]))
	imm = '#' + str(twos_compliment(data[16:32]))
	answer = op +'	'+rs+', '+imm
	function_output.append(str(data)+'	'+str(MIPS_address)+'	'+answer)



# go through each line and create MIPS command
for i in range(length_binary):
	item = binary[i]
	opcode = binary_to_decimal(item[0:6])
	
	if binary_to_decimal(item[0:26])==0 and (binary_to_decimal(item[26:32])==0 or binary_to_decimal(item[26:32])==13):
		EXCEPTION(item)
		if binary_to_decimal(item[26:32])==13:
			end_list = True
			j = i+1
			break
	elif opcode==0:
		r_type_instruction(item)
	elif opcode in range(8,15):
		immediate(item)
	elif opcode in range(32,38) or opcode in range(40,44):
		LOAD_STORE(item)
	elif opcode==2 or opcode==3:
		JUMP(item)
	elif opcode in range(4,6):
		BRANCH(item)
	elif opcode==1 or opcode==6 or opcode==7:
		BRANCH_2(item)
	else:
		answer = 'Instruction not listed.'
		function_output.append(str(item)+'	'+str(MIPS_address)+'	'+answer)

	MIPS_address = MIPS_address+4


# Execute when there is BREAK
if end_list==True:
	for m in range(j, length_binary):
		MIPS_address = MIPS_address+4
		item = binary[m]
		twos_result = twos_compliment(item)
		function_output.append(str(item)+'	'+str(MIPS_address)+'	'+ str(twos_result))



# write data in output file
output_file = open('output.txt','w')
output_file.write('\n'.join(function_output))
output_file.close()
