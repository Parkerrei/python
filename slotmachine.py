import random
def spin_row():
    symbols = ['😍','🤣','😁','😛','🥱','😴']
   
    return [random.choice(symbols)for _ in range(3)]
    # for symbols in range(3):
    #     result.append(random.choice(symbols))
    # return result
    
def print_row(row):
    print('------')
    print(' | '.join(row))
    print('------ ')
    
def get_payout(row,bet):
    if row[0] == row[1] == row[2]:
        if row[0] == '😍':
            return bet * 3
        elif row[0] == '🤣':
            return bet * 4
        elif row[0] == '😁':
            return bet * 5
        elif row[0] == '😛':
            return bet * 6
        elif row[0] == '🥱':
            return bet * 39
        elif row[0] == '😴':
            return bet * 3
    return 0

def main():
    balance = int(input('enter ur balance amount:'))
    print('.................')
    print('welcome to python slot machine //////')
    print('symbols ')
    print('.................')
    
    while balance > 0:
        print(f'current balance :${balance}')
        bet = input('place your bet : ')
         
        try:
            bet = int(bet)
        except ValueError as e:
            print(e)
            continue
        else:
            if bet > balance:
                print('insufficient balance') 
                continue 
            if bet <= 0:
                print('bet must be greater than 0') 
                continue
                
            balance -= bet 
            row = spin_row()
            print('spinning....\n')
            print_row(row)
            
            payout = get_payout(row,bet)
            if payout > 0:
                print(f'you won ${payout}') 
            else:
                print('sorry you lost this time ') 
                balance += payout
           
if __name__ == '__main__':
    main()


