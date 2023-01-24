from replit import clear #You can call clear() to clear the output in the console.
from art import logo
#HINT: You can call clear() to clear the output in the console.
print(logo) #to print the gavel logo
print("Welcome to the blind auction Program")
no_bidders=False
bids={}

def find_highest_bid(bidding_record): #bidding record is the dictionary bid={"Kanmani": 123, "sam": 23}
    highest_bid=0 #assigning variable highest_bid 
    winner="" #name of the winner
    for bidder in bidding_record: # for loop in dictionary works with looping everytime through the key only.
        bid_amount=bidding_record[bidder] #bid_amount=bidding_record[kanmani]=123
        if bid_amount>highest_bid: #123>0, true, then highest bid will be assigned with the bid amount
            highest_bid=bid_amount
            winner=bidder #winner is the bidder(key) who has the value of highest amount 
    print(f"the winner is {winner} with  bid of {highest_bid}") #to print the winner and highest bid

while not no_bidders:
    name=input("What is your name?: ") #name of the bidder (key)
    bid=int(input("What is your bid?: $")) #amount by the bidder (value)
    bids[name]=bid #creating dictionary with name as key and bid as the value
    #print(bids)
    more_bidders=input("Are there any other bidders: Yes or No?:\n ") #to ask the bidder if there are any more bidders
    if more_bidders=='Yes': #yes means there are more bidders hence setting no_bidders as false as the loop runs until it s true
        clear()
        no_bidders=False
    else: #this is for no, means no more bidders hence setting it as true loop stops when there are no more bidders and calls the function to highest bid
        no_bidders=True 
        find_highest_bid(bids) #calling the function with the input bids (bidding record)
        
        
    


