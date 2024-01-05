name = input("what is your name? ")
account_number = input("what is your account number? ")
bank_name = input("what is your bank name? ")
start_balance = 0
amount2 = input("Add money received to your wallet? ")
sender_account_number = input("what is the sender's account number? ")
sender_bank_name = input("what is receiver's bank name? ")

# amount = int(amount2)
amount = int(amount2)
sender = int(sender_account_number)
new_balance = start_balance + amount



def received():
    wallet_balance_after_receiving = new_balance + amount
    print("you received  " + str(amount) + " " + "from your " + sender_account_number + " " + sender_bank_name)
    print("your account balance before transaction was " + str(start_balance))
    print("your new balance is " + str(new_balance))


received()