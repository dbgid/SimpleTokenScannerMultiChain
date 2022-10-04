"""
FILE: multitoken.py
Author: Ajones AKA DBG ID
Description: Grab all available token in wallet by scan web explorer
"""
"""Require module"""
import requests as req
from bs4 import BeautifulSoup as DOM
import sys,os,argparse
from colorama import init, Style, Fore
"""Reset the term color while entering new line"""
init(autoreset=True)
"""Create the term color"""
class TermColor:
  RED=Fore.RED
  GREEN=Fore.GREEN
  YELLOW=Fore.YELLOW
  WHITE=Fore.WHITE
  BLUE=Fore.BLUE
  BRIGHT=Style.BRIGHT
class TokenGrabber(TermColor):
  def __init__(self):
    self.eth='https://etherscan.io/address/'
    self.bsc='https://bscscan.com/address/'
    self.polygon='https://polygonscan.com/address/'
    self.avax='https://snowtrace.io/address/'
    self.ftm='https://ftmscan.com/address/'
  def HttpBuilder(self,url):
    try:
      self.res=req.get(url,headers={'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','User-Agent': 'Mozilla/5.0 (Linux; Android 11; 21061110AG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.6 Mobile Safari/537.36'},timeout=30)
      if self.res.status_code==200:
        return self.res.content
      elif self.res.status_code==503:
        print(f"{self.BRIGHT}[!] Error: {self.YELLOW}Cloudflare detected...")
        sys.exit(1)
      else:
        raise Exception("Sorry the request are permitted status code <%s>" % self.res.status_code)
    except Exception as e:
      print("{}[!] Error: {}{}".format(self.BRIGHT,self.RED,e))
  def block(self):
    print(f"{self.BRIGHT}List of Block Chain Explorer:\n1\t ETH Blockchain\n2\t BSC Blockchain\n3\t Polygon Blockchain (error due this network behind Cloudflare)\n4\t Avax Blockchain\n5\tFantom Blockchain")
  def clear(self):
    with open('listoken.txt','w') as save:
      save.close()
    print(f"{self.GREEN}[√] listoken.txt has been cleaned")
  def masScan(self,cid,file):
    try:
      for i, wallet in enumerate(open(file,'r').readlines()):
        if '\n' in wallet:
          wallet=wallet.replace('\n','')
        else:
          pass
        print(f"{self.BRIGHT}{self.WHITE}[Proses] Running {self.GREEN}{i}{self.WHITE}/{self.RED}{len(open(file,'r').readlines())}")
        self.scanToken(cid,wallet)
    except Exception as e:
      print("{}[!] Error: {}{}".format(self.BRIGHT,self.RED,e))
  def scanToken(self,cid,wallet):
    try:
      if cid==1:
        print(f"{self.BRIGHT}{self.WHITE}[>>] {self.GREEN}Etherium Blockchain {self.WHITE}[<<]")
        self.url=self.eth
        self.mark='ETH'
      elif cid==2:
        print(f"{self.BRIGHT}{self.WHITE}[>>] {self.YELLOW}BSC Blockchain {self.WHITE}[<<]")
        self.url=self.bsc
        self.mark='BSC'
      elif cid==3:
        print(f"{self.BRIGHT}{self.WHITE}[>>] {self.BLUE}Polygon Blockchain {self.WHITE}[<<]")
        self.url=self.polygon
        self.mark='Polygon'
      elif cid==4:
        print(f"{self.BRIGHT}{self.WHITE}[>>] {self.RED}AVAX Blockchain {self.WHITE}[<<]")
        self.url=self.avax
        self.mark='AVAX'
      elif cid==5:
        print(f"{self.BRIGHT}{self.WHITE}[>>] {self.BLUE}Fantom Blockchain {self.WHITE}[<<]")
        self.url=self.ftm
        self.mark='Fantom'
      else:
        print(f"{self.BRIGHT}[!] Error: {self.RED}chain id no more than 5, you must choose 1-5. type {sys.argv[0]} --blockchain for more info")
        sys.exit(1)
      print(f"{self.BRIGHT}{self.WHITE}[INFO] Scanning wallet => {self.YELLOW}{wallet}")
      self.goto=self.HttpBuilder(self.url+wallet)
      self.sop=DOM(self.goto,'html.parser')
      self.token_element=self.sop.findAll('span',attrs={'class':'list-name hash-tag text-truncate'})
      self.token_amount=self.sop.findAll('span',attrs={'class':'list-amount link-hover__item hash-tag hash-tag--md text-truncate'})
      self.token_count=0
      self.token_result=''
      if len(self.token_element) < 1:
        print(f"{self.BRIGHT}[!] Error: {self.RED}this wallet not have token yet")
      else:
        for i, token in enumerate(self.token_element):
          self.token_count+=1
          self.token_result+=''.join(f"[{i}] {token.get_text()} {self.token_amount[i].get_text()}\n")
          if i==len(self.token_amount)-1:
            break
        print(f"{self.BRIGHT}[-] Total Token: {self.GREEN}{self.token_count}\n{self.WHITE}[>>] Token List [<<] \n{self.BLUE}{self.token_result}")
        self.delim='======================================='
        with open('listoken.txt','a') as save:
          save.write(f"{self.delim}\n[-] Wallet: {wallet} ({self.mark})\n[-] Total Token: {self.token_count}\n{self.token_result}\n{self.delim}\n")
          save.close()
    except Exception as e:
      print("{}[!] Error: {}{}".format(self.BRIGHT,self.RED,e))
if __name__=='__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('-f','--file',help='list of file wallet txt')
  parser.add_argument('-c','--chain',type=int,help='chain id of blockchain, see --blockchain for more info',default=2)
  parser.add_argument('--blockchain',action='store_true',help='Print help of chain id block explorer')
  parser.add_argument('--clear',action='store_true',help='clear listoken.txt file')
  args = parser.parse_args()
  txt=args.file
  chain=args.chain
  if args.blockchain:
    TokenGrabber().block()
  elif args.clear:
    TokenGrabber().clear()
  elif chain and txt:
    TokenGrabber().masScan(chain,txt)
  else:
    print('usage: %s -h for help' % sys.argv[0])
  