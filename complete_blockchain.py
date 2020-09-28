# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 13:12:15 2020

@author: Kiit1705576
"""
blockchain=[]

def get_last_value():
    return(blockchain[-1])
    
def add_value(transaction_amount,last_transaction=blockchain[-1]):
    blockchain.append([[last_transaction],transaction_amount])
    
    
def get_transaction_value():
    user_value=float(input('Enter your transaction Amount'))
    return user_value

def get_user_choice():
    user_input=input("Please give your choice here:")
    return user_input

def print_block():
    index=0
    for block in blockchain:
        index=index+1
        print("Printing Block Number:"+str(index)+",Value="+str(block))
        
    print("Complete Blockchain is = ")
    print(blockchain)
    

def verify_chain():
    
    index = 0
    
    valid=True
    
    for block in blockchain:
        if index==0:
            index+=1
            continue
        
        elif block[0]==[blockchain[index-1]]:
            valid = True
        else:
            valid=False
            
            break
        
        index+=1
        
    return valid

while True:
    print("Choose an option")
    
    print('Chose 1 for adding a new transaction')
    
    print('Choose 2 for printing the blockchain')
    
    print('Choose 3 if you want to manipulate the data')
    
    print('Chose anything else if you want to quit')
    
    
    user_choice=int(get_user_choice())
    print(user_choice)
    
    if user_choice==1:
        tx_amount=get_transaction_value()
        add_value(tx_amount,get_last_value())
        
    elif user_choice==2:
        print_block()
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
        
    
    
    