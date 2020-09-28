# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 15:49:55 2020

@author: Kiit1705576
"""

import hashlib
import json
reward=10.0
genesis_block={     # initially 
        'previous_hash':'',
        'index':0,
        'transaction':[],
        'nonce':23
        
}
blockchain=[genesis_block]
print(blockchain)

open_transactions=[]
owner='Bikash'

def hash_block(block):
    return hashlib.sha256(json.dumps(block).encode()).hexdigest()

def valid_proof(transactions,last_hash,nonce):
    guess=(str(transactions)+str(last_hash)+str(nonce)).encode()
    guess_hash=hashlib.sha256(guess).hexdigest()
    print(guess_hash)
    return guess_hash[0:2]=='00'


def pow():
    last_block=blockchain[-1]
    last_hash=hash_block(last_block)
    nonce=0
    while not valid_proof(open_transactions,last_hash,nonce):
        nonce+=1
    return nonce
    
    
def get_last_value():
    """ extracting last element of blockchain list"""
    return(blockchain[-1])
    
def add_value(recipient,sender=owner,amount=1.0):
    transaction={'sender':sender,'recipient':recipient,'amount':amount}
    open_transactions.append(transaction)

def mine_block():
    last_block=blockchain[-1]
    hashed_block=blockchain(last_block)
    nonce=pow()
    reward_transaction={'sender':'MINING','recipient':owner,'amount':reward}
    open_transactions.append(reward_transaction)
    print(open_transactions)
    
    block={'previous_hash':hashed_block,'index':len(blockchain),'transaction':open_transactions,'nonce':nonce}
    blockchain.append(block)
    print("\n\n\nBLOCKCHAIN")
    print(blockchain)
    print("\n\n\n")
    
def get_transaction_value():
    tx_recipient=input('Enter the recipient of the transaction:')
    tx_amount=float(input('Enter your transaction amount'))
    return tx_recipient,tx_amount

def get_user_choice():
    user_input=input("Please give your choice here:")
    return user_input

def print_block():
    index=0
    for block in blockchain:
        index=index+1
        print("Printing Block Number:"+str(index))
        print(blockchain)
        print('\n\n')
        
        
while True:
    print("Choose an option")
    
    print('Chose 1 for adding a new transaction')
    
    print('Choose 2 for mining a  new block')
    
    print('Choose 3 for printing the blockchain')
    
    print('Chose anything else if you want to quit')
    
    
    user_choice=int(get_user_choice())
    print(user_choice)
    
    if user_choice==1:
        tx_data=get_transaction_value()
        recipient,amount=tx_data
        add_value(recipient,amount=amount)
        print(open_transactions)
        
    elif user_choice==2:
        mine_block()
        open_transactions=[]
        
    elif user_choice==3: 
        if len(blockchain)>=1:
            #blockchain[0]='A'  
            block_value=int(input('Enter Block Number for Manipulation'))
            transaction_value=float(input('Enter transaction amount for Manipulation'))
            #blockchain[1]=[12,34]
            blockchain_manipulate=[]
            print("Original blockchain="+str(blockchain(block_value)))
            blockchain_manipulate=blockchain[block_value]
            blockchain_manipulate[-1]=transaction_value
            
            print("Manipulated blockchain = "+str(blockchain_manipulate))
            blockchain[block_value]=blockchain_manipulate
            print(blockchain)
    else:
        print("else")
        break
    
    if not verify_chain():
        print(blockchain)
        print('Blockchain manipulate')
        break
        
    
    
    
        
