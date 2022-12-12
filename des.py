bits_48 = "101010101010101010101010101010101010101010101010"
InitialPermOrder = [58, 50, 42, 34, 26, 18, 10, 2,
 60, 52, 44, 36, 28, 20, 12, 4,
 62, 54, 46, 38, 30, 22, 14, 6,
 64, 56, 48, 40, 32, 24, 16, 8,
 57, 49, 41, 33, 25, 17, 9, 1,
 59, 51, 43, 35, 27, 19, 11, 3,
 61, 53, 45, 37, 29, 21, 13, 5,
 63, 55, 47, 39, 31, 23, 15, 7]
InitPermOrder = [x - 1 for x in InitialPermOrder]

InverseinitialPermOrder = [40, 8, 48, 16, 56, 24, 64, 32,
 39, 7, 47, 15, 55, 23, 63, 31,
 38, 6, 46, 14, 54, 22, 62, 30,
 37, 5, 45, 13, 53, 21, 61, 29,
 36, 4, 44, 12, 52, 20, 60, 28,
 35, 3, 43, 11, 51, 19, 59, 27,
 34, 2, 42, 10, 50, 18, 58, 26,
 33, 1, 41, 9, 49, 17, 57, 25]
InvInitPermOrder = [x - 1 for x in InverseinitialPermOrder]

E_TABLE = [32, 1, 2, 3, 4, 5, 4, 5, 6, 7, 8, 9, 8, 9, 10, 11, 12, 13, 12, 13, 14,
15, 16, 17,
 16, 17, 18, 19, 20, 21, 20, 21, 22, 23, 24, 25, 24, 25, 26, 27, 28, 29,
28, 29, 30, 31, 32, 1]

e_table = [x - 1 for x in E_TABLE]

P = [16, 7, 20, 21,
 29, 12, 28, 17,
 1, 15, 23, 26,
 5, 18, 31, 10,
 2, 8, 24, 14,
 32, 27, 3, 9,
 19, 13, 30, 6,
 22, 11, 4, 25]
Per = [x - 1 for x in P]

def Permutation(bitstr, permorderlist):
 permedbitstr = ''
 
 permedbitstr = [bitstr[b] for b in permorderlist]
 permedbitstr = "".join(permedbitstr)
 
 return permedbitstr

list6b = [bits_48[i:i + 6] for i in range(0, len(bits_48), 6)]
SBOX = [
 # Box-1
 [
 [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
 [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
 [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
 [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]
 ],
 # Box-2
 [
 [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
 [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
 [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
 [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]
 ],
 # Box-3
 [
 [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
 [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
 [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
 [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]
 ],
 # Box-4
 [
 [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
 [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
 [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
 [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]
 ],
 # Box-5
 [
 [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
 [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
 [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
 [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]
 ],
 # Box-6
 [
 [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
 [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
 [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
 [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]
 ],
 # Box-7
 [
 [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
 [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
 [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
 [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]
 ],
 # Box-8
 [
 [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
 [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
 [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
 [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]
 ]
]
DECtoBIN4 = {0: '0000',
 1: '0001',
 2: '0010',
 3: '0011',
 4: '0100',
 5: '0101',
 6: '0110',
 7: '0111',
 8: '1000',
 9: '1001',
 10: '1010',
 11: '1011',
 12: '1100',
 13: '1101',
 14: '1110',
 15: '1111'}


def sbox_lookup(input6bitstr, sboxindex):
 
 row = 0
 col = 0
 col = int(input6bitstr[1:5], base=2)
 row = int(input6bitstr[0] + input6bitstr[5], base=2)
 sbox_value = SBOX[sboxindex][row][col]
 
 # Decimal to binary conversion
 DECtoBIN4 = {0: '0000',
 1: '0001',
 2: '0010',
 3: '0011',
 4: '0100',
 5: '0101',
 6: '0110',
 7: '0111',
 8: '1000',
 9: '1001',
 10: '1010',
 11: '1011',
 12: '1100',
 13: '1101',
 14: '1110',
 15: '1111'}
 return DECtoBIN4[sbox_value]

def XORbits(bitstr1, bitstr2):
 
 xor_result = ""
 for index in range(len(bitstr1)):
 if bitstr1[index] == bitstr2[index]:
 xor_result += '0'
 else:
 xor_result += '1'
 
 return xor_result

def functionF(bitstr32, keybitstr48):
 
 outbitstr32 = ''
 expansionbits = Permutation(bitstr32, e_table)
 
 XOR = XORbits(expansionbits, keybitstr48)
 allbits6 = [XOR[i:i + 6] for i in range(0, len(bits_48), 6)]
 S_BOX = [(sbox_lookup(allbits6[i], i)) for i in range(0, len(SBOX))]
 S_BOX = "".join(S_BOX)
 outbitstr32 = Permutation(S_BOX, Per)
 
 return outbitstr32

PC1 = [57, 49, 41, 33, 25, 17, 9,
 1, 58, 50, 42, 34, 26, 18,
 10, 2, 59, 51, 43, 35, 27,
 19, 11, 3, 60, 52, 44, 36,
 63, 55, 47, 39, 31, 23, 15,
 7, 62, 54, 46, 38, 30, 22,
 14, 6, 61, 53, 45, 37, 29,
 21, 13, 5, 28, 20, 12, 4]
PC_1 = [x - 1 for x in PC1]

shift_table = [1, 1, 2, 2,
 2, 2, 2, 2,
 1, 2, 2, 2,
 2, 2, 2, 1]

key_comp = [14, 17, 11, 24, 1, 5,
 3, 28, 15, 6, 21, 10,
 23, 19, 12, 4, 26, 8,
 16, 7, 27, 20, 13, 2,
 41, 52, 31, 37, 47, 55,
 30, 40, 51, 45, 33, 48,
 44, 49, 39, 56, 34, 53,
 46, 42, 50, 36, 29, 32]

key_comp_1 = [x - 1 for x in key_comp]

def Permutation(bitstr, permorderlist):
 permedbitstr = ''
 
 permedbitstr = [bitstr[b] for b in permorderlist]
 permedbitstr = "".join(permedbitstr)
 
 return permedbitstr

Permutation("0001001100110100010101110111100110011011101111001101111111110001",
PC_1)

def circular_left_shift(bits, numberofbits):
 shiftedbits = bits[numberofbits:] + bits[:numberofbits]
 return shiftedbits

def des_keygen(C_inp, D_inp, roundindex):
 
 C_out = circular_left_shift(C_inp, shift_table[roundindex])
 D_out = circular_left_shift(D_inp, shift_table[roundindex])
 key48 = C_out + D_out
 
 key48 = Permutation(key48, key_comp_1)
 
 return key48, C_out, D_out

Permutation("0001001100110100010101110111100110011011101111001101111111110001",
InitPermOrder)
# print(IP)
#LE_inp32 = IP[:32]

def des_round(LE_inp32, RE_inp32, key48):
 LE_out = RE_inp32
 RE_out = XORbits(LE_inp32, functionF(RE_inp32, key48))
 
#This will return 32-bits of LE and RE
 return LE_out, RE_out

def bytetobin(byteseq):
 
 key_bits = [bin(int(b))[2:].zfill(8) for b in byteseq]
 
 key_bits=''.join(key_bits)
 
 return key_bits

def bitstring_to_bytes(s):
 return (int(s, 2).to_bytes(len(s) // 8, byteorder=‘big'))

def des_enc(inputblock, num_rounds, inputkey64):
 keyslist=list()
 # function will accept one block of plaintext and sent through each round of DES and return cipher

 inputkey64bit=bytetobin(inputkey64)
 
 PC_2 = Permutation(inputkey64bit, PC_1)
 
 C_inp, D_inp = PC_2[:28], PC_2[28:]
 for i in range(num_rounds):
 subkey = des_keygen(C_inp, D_inp, i)
 
 C_inp=subkey[1]
 
 D_inp=subkey[2]
 keyslist.append(subkey[0])
 
 Text_bits = bytetobin(inputblock)
 
 IP_Text=Permutation(Text_bits,InitPermOrder)
 LE_inp32 = IP_Text[:32]
 #print(LE_inp32)
 RE_inp32 = IP_Text[32:]
 #print(RE_inp32)
 for i in range(0,(num_rounds)):
 #print(i)
 LE_out,RE_out=des_round(LE_inp32,RE_inp32,keyslist[i])
 LE_inp32=LE_out
 RE_inp32=RE_out
 
 cipherblock=Permutation(RE_out+LE_out,InvInitPermOrder)
 
 cipherblock=bytes(int(cipherblock[i : i + 8], 2) for i in range(0,
len(cipherblock), 8))
 
 return cipherblock

def des_enc_test(input_fname, inputkey64, num_rounds, output_fname):
 
 
 finp = open(input_fname, 'rb')
 inpbyteseq = finp.read()
 
 finp.close()
 blocklist=[]
 
 if (len(inpbyteseq) % 8!= 0):
 for i in range(8 - len(inpbyteseq) % 8):
 inpbyteseq = inpbyteseq + b" "
 
 # this Loop over is to iterate over all the blocks and get the cipher block
 
 fout = open(output_fname, 'wb')
 
 for i in range(0,len(inpbyteseq),8):
 blocklist = inpbyteseq[i:i + 8]
 
 cipherbyteseq=des_enc(blocklist,num_rounds,inputkey64)
 
 fout.write(cipherbyteseq)
 
 fout.close()

def des_dec(inputblock, num_rounds, inputkey64):
 keyslist=[]
 # function will accept one block of ciphertext at a time and outputs plaintext
 inputkey64bit = bytetobin(inputkey64)
 PC_2 = Permutation(inputkey64bit, PC_1)
 C_inp, D_inp = PC_2[:28], PC_2[28:]
 for i in range(num_rounds):
 subkey = des_keygen(C_inp, D_inp, i)
 C_inp = subkey[1]
 D_inp = subkey[2]
 keyslist.append(subkey[0])
 inputblock=bytetobin(inputblock)
 inputblock=Permutation(inputblock,InitPermOrder)
 LE_inp32 = inputblock[:32]
 RE_inp32 = inputblock[32:]
 for i in range(num_rounds,0,-1):
 LE_out,RE_out=des_round(LE_inp32,RE_inp32,keyslist[i-1])
 LE_inp32 = LE_out
 RE_inp32 = RE_out
 plainblock = Permutation(RE_out + LE_out, InvInitPermOrder)
 plainblock=bytes(int(plainblock[i : i + 8], 2) for i in range(0,len(plainblock), 8))
 
 return plainblock

def des_dec_test(input_fname, inputkey64, num_rounds, output_fname):
 
 # This function will read the contents of file in byte sequence.
 cipherbyteseq=[]
 blocklist=[]
 finp = open(input_fname, 'rb')
 cipherbyteseq = finp.read()
 
 finp.close()
 if (len(cipherbyteseq) % 8!= 0):
 for i in range(8 - len(cipherbyteseq) % 8):
 cipherbyteseq = cipherbyteseq + b" "
 
 fout = open(output_fname, 'wb')
 for i in range(0,len(cipherbyteseq),8):
 blocklist = cipherbyteseq[i:i + 8]
 
 plainbyteseq=des_dec(blocklist,num_rounds,inputkey64)
 
 fout.write(plainbyteseq)
 
 fout.close()
