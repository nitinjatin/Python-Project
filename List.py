list_1 = ["Bitcoin" , "Ethereum" , "Solana" , "Polygon" , "Binance"]
list_2 = [10 , 89 , 20 ,  76 , 67]
list_1.append("Avalanche")
list_2.sort()
list_2.reverse()
list_1.insert(2,"Tron") # insert a value at desired index 
pop_up = list_1.pop(2) # remove a value at desired index AND It stored into pop_up variable
remove_value = list_1.remove("Solana") # delted a desired value without mentioning index number 
print(list_1) 
print(list_2)
print(pop_up) # print the removed value
print(remove_value) # delete a desired value in list & It doesnot store deleted value in variable like POP()
'''
Use pop() when you know the index and want the removed value.
Use remove() when you know the value and don’t need the removed item
'''