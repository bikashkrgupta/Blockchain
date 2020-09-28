# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 12:51:19 2020

@author: Kiit1705576
Demo of add blocks to Blockchain..next block contain previuous block 
"""
def add_list():
    print("add_list function started")
    print("Current Blockchain is = ")
    print( blockchain)
    element1=input("Give the element of the blockchain \n")
    
    blockchain.append([[blockchain[-1]],element1])
    print(blockchain)
    print("Element Added\n\n")
    

element1=input("Give the first element of the blockchain \n")
blockchain=[element1]
add_list()
add_list()
add_list()

print("Printing Blocks in Blockchain")
for i in range(len(blockchain)):
    print(blockchain[i])
