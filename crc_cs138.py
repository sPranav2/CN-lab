class CRC:
	
	def __init__(self):
		self.cdw = ''

	def xor(self,a,b):
		result = []
		for i in range(1,len(b)):
			if a[i] == b[i]:
				result.append('0')
			else:
				result.append('1')


		return  ''.join(result)



	def crc(self,message, key):
		pick = len(key)

		tmp = message[:pick]

		while pick < len(message):
			if tmp[0] == '1':
				tmp = self.xor(key,tmp)+message[pick]
			else:
				tmp = self.xor('0'*pick,tmp) + message[pick]

			pick+=1
            

		if tmp[0] == "1":
			tmp = self.xor(key,tmp)
		else:
			tmp = self.xor('0'*pick,tmp)

		checkword = tmp
		return checkword

	def encodedData(self,data,key):
		l_key = len(key)
		append_data = data + '0'*(l_key-1)
		remainder = self.crc(append_data,key)
		codeword = data+remainder
		self.cdw += codeword
		print("Remainder: " ,remainder)
		print("Dataword: " ,codeword)

	def reciverSide(self,data,key):
		r = self.crc(data,key)
		
		print('remainder: ',r)
		if r == '0'*16:
			print("No Error")
		else:
			print("Error")



data = input('enter data word: \n')
key = '10001000000100001'
beforeCrc=data+'0'*(len(key)-1)
print('data: ',data,'\n key: ',key,'\n ','\n dataword before crc: ',beforeCrc)
c = CRC()
c.encodedData(data,key)
ch=int(input('do you wish to add error? (1-yes, 0-no)'))
if(ch==1):
    print('current dataword: ',data)
    newWd=input('enter altered keyword')
    c.reciverSide(newWd+key,key)
else:
    c.reciverSide(c.cdw,key)
print('---------------')


    
