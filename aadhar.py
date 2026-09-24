def aadhar(card):
    card1="X"*4 +" "+"X"*4+" "+card[-4: ]
    print(f"After hiding sensitive data,aadhar no is {card1}")

card=input("Enter string: ")
if(card.isdigit() and len(card)==12):
    print(f'Before hiding sensitive data,aadhar no is {card[0:4]+" "+card[4:8]+" "+card[8:12]}')
    aadhar(card)
else:
    print("Invalid input")
