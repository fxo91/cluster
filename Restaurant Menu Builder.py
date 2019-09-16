
def readMenu(menu, filename):
    ifile = open(filename, 'r')
    for line in ifile:
        category,item,price = line.rstrip().split(',')
        price = round(float(price), 2)
        menu.append([category, item, price])

def displayMenu(menu, categs):
    print('==========================================='.center(49))
    print('Welcome to the Miami Favorites Meal Builder'.center(50))
    print('*******************************************\n'.center(49))
    print('Q to Quit'.rjust(13), 'N for New Meal'.rjust(31))
    print()
    print()

    i = 0
    for c in categs:
        print(c.center(50))
        print('=========='.center(50))
        print()
        for item in menu:
            if item[0] == c:
                i += 1
                print(str(i).ljust(8) + item[1].ljust(35) + '$ ' + str(item[2]))
        print()

def getMenuChoice():
    print('______________________________________________')
    print('Please insert item number to add to the order:')
    choice = input('>> ')
    print('______________________________________________')
    return choice

def displayTicket(ticket,tax,tip):
    subtotal = 0.0
    print()
    print('==================================================================')
    print('Summary of the order below:')
    print()
    for item in ticket:
        print(item[0].ljust(15), item[1].ljust(35), ' $',item[2])
        subtotal = subtotal + item[2]
    print('==================================================================')
    print('Subtotal = ${:.2f}'.format(subtotal).rjust(59))
    print('Tax = ${:.2f}'.format(subtotal*tax).rjust(59))
    print('Tip = ${:.2f}'.format(subtotal * tip).rjust(59))
    print('                                        ==========================')
    print('Total = ${:.2f}'.format(subtotal + subtotal*tax + subtotal*tip).rjust(59))
    print('                                        ==========================')

def main():
    filename = 'food.txt'
    menu = []
    categs = []
    readMenu(menu, filename)
    for item in menu:
        if item[0] not in categs:
            categs.append(item[0])
    displayMenu(menu, categs)

    choice = getMenuChoice()

    ticket = []
    taxRate = 0.07
    tipRate = .20
    while choice.upper() != 'Q':
        if choice.upper() != 'N':
            if int(choice) in range(len(menu) + 1):
                ticket.append(menu[int(choice) - 1])
                displayMenu(menu, categs)
                displayTicket(ticket, taxRate, tipRate)
                choice = getMenuChoice()
            else:
                print('Item entered is not in the menu, please re-enter:')
                choice = getMenuChoice()
        else:
            ticket.clear()
            displayMenu(menu, categs)
            choice = getMenuChoice()

if __name__ == ('__main__'):
    main()