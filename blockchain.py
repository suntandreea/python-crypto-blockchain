# this is a single line comment

blockchain = []

def get_last_blockchain_value():
    """ Returns the last value of the current blockchain 
    or None, if the blockchain is empty.
    """
    
    if len(blockchain) < 1:
        return None
    return blockchain[-1]


def add_transaction(transaction_amount, last_transaction=[1]):
    """ Append new value and last value to blockchain.
    
    Arguments:
    :transaction_amount: The amount that should be added.
    :last_transaction: The last blockchain transaction (default [1]).
    """

    if last_transaction == None:
        last_transaction = [1]
    
    blockchain.append([last_transaction, transaction_amount])


def get_transaction_value():
    """ Gets a new transaction amount from user input and returns it as a float. """
    return float(input('Your transaction amount, please: '))


def get_user_choice():
    """ Gets and returns a string with the user choice. """
    return input('Your choice: ')


def print_blockchain_elements():
    """ Output the blockchain list to the console """
    for block in blockchain:
        print('Outputting block: ', block)


def verify_chain():
    block_index = 0
    is_valid = True
    for block in blockchain:
        
        if block_index == 0: 
            block_index += 1
            continue
        elif block[0] == blockchain[block_index - 1]:
            is_valid = True
        else: 
            is_valid = False
            break

        block_index += 1
    return is_valid    


while True:
    print('Please choose')
    print('1: Add a new transaction value')
    print('2: Output the blockchain blocks')
    print('h: Manipulate the chain')
    print('q: Quit')

    user_choice = get_user_choice()

    if user_choice == '1':
        add_transaction(get_transaction_value(), get_last_blockchain_value())
    elif user_choice == '2':
        print_blockchain_elements()
    elif user_choice == 'h':
        if len(blockchain) >= 1:    
            blockchain[0] = [2]
    elif user_choice == 'q':
        break
    else:
        print('Your input is invalid. Please pick a value from the list!')

    if not verify_chain():
        print('Invalid blockchain!')
        break
    
print ('Done!')