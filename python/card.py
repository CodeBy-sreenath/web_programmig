def locate_card(cards,query):
    position=0 #initialize position
    
    #set a loop for iteration
    while True:
        #check if the position matches query
        if cards[position]==query:
            return position
        #inrement the position
        position+=1
        if position==len(cards):
            return -1
result=locate_card([3,5,1,2,3],2) 
print(result)       
        
    