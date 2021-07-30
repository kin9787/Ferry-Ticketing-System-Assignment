import time  # Time Module
import pickle  # For Keeping Data Permanently

ferry_list = ['Athena', 'Behemoth', 'Caerus', 'Delphin', 'Eiar', 'Fontus', 'Gelus', 'Harmonia',
              'Harmonia', 'Gelus', 'Fontus', 'Eiar', 'Delphian', 'Caerus', 'Behemoth', 'Athena']  # All Ferries ID
time_list = [1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1700, 1600, 1500, 1400, 1300, 1200, 1100, 1000]  # All Departure Time
b_amount = 10  # Seating Cap
e_amount = 40  # Seating Cap
real_time = time.asctime(time.localtime(time.time()))  # For Printing Out Real Time
v = []  # For Creating Seating List


# This Function Prints Out Main Menu
def main_menu():
    print('ferry ticketing system'.upper())
    print('--------main menu--------'.upper())
    print('Please select any option from below')
    print('P - to Purchase Ticket')
    print('V - to View Seating Arrangement')
    print('Q - to Quit The System')
    print('')


# This Function Prints Out Sub Menu
def submenu():
    
    print(' ')
    print('--------purchasing module--------'.upper())
    print('You have selected the purchasing option')
    print('Please select any option from below.')
    print('B - to purchase ticket for Business Class')
    print('E - to purchase ticket for Economy Class')
    print('M - to return to Main Menu')
    print('Q - to Quit')
    print(' ')


# This Function Prints Out Both Ferry ID and Time to be choose (From Penang to Langkawi)
def schedule_p2l():
    print('Ferry Schedule'.upper())
    print('-----------------------------------------------------------------')
    print('      Ferry ID     |  Departure Time   |       Destination       ')
    print('press 1 for ---  Athena      |       1000        |    Penang to Langkawi   ')
    print('press 2 for ---  Behemoth    |       1100        |    Penang to Langkawi   ')
    print('press 3 for ---  Caerus      |       1200        |    Penang to Langkawi   ')
    print('press 4 for ---  Delphin     |       1300        |    Penang to Langkawi   ')
    print('press 5 for ---  Eiar        |       1400        |    Penang to Langkawi   ')
    print('press 6 for ---  Fontus      |       1500        |    Penang to Langkawi   ')
    print('press 7 for ---  Gelus       |       1600        |    Penang to Langkawi   ')
    print('press 8 for ---  Harmonia    |       1700        |    Penang to Langkawi   ')
    print('-----------------------------------------------------------------')


# This Function Prints Out Both Ferry ID and Time to be choose (From Langkawi to Penang)
def schedule_l2p():
    print('Ferry Schedule'.upper())
    print('-----------------------------------------------------------------')
    print('      Ferry ID      |  Departure Time   |       Destination       ')
    print('press 9 for ---  Harmonia     |       1000        |    Langkawi to Penang   ')
    print('press 10 for ---  Gelus       |       1100        |    Langkawi to Penang   ')
    print('press 11 for ---  Fontus      |       1200        |    Langkawi to Penang   ')
    print('press 12 for ---  Eiar        |       1300        |    Langkawi to Penang   ')
    print('press 13 for ---  Delphin     |       1400        |    Langkawi to Penang   ')
    print('press 14 for ---  Caerus      |       1500        |    Langkawi to Penang   ')
    print('press 15 for ---  Behemoth    |       1600        |    Langkawi to Penang   ')
    print('press 16 for ---  Athena      |       1700        |    Langkawi to Penang   ')
    print('-----------------------------------------------------------------')


# This Function Let the User Choose their destination.
def destination():
    global selected_destination
    print(' ')
    print('Where would you like to go?')
    print('A--- Penang to Langkawi')
    print('B--- Langkawi to Penang')
    selected_destination = input('Your answer:').upper()
    if selected_destination == 'A':
        print('Penang to Langkawi'.upper())
    elif selected_destination == 'B':
        print('Langkawi to Penang'.upper())
    else:
        print('Sorry, you have input an invalid option.')
    print(' ')


# This Function let Users to choose their Ferry and Time for Departure
def choosing_ticket():
    global ticket_choosing, open_ticket
    print(' ')
    ticket_choosing = int(input('Your choice:'))
    open_files()
    while True:
        if selected_destination == 'A':
            if ticket_choosing > 8 or ticket_choosing < 1:
                print('Please Pick a value within the range.')
                ticket_choosing = int(input('Your choice:'))
            else:
                print('Ferry_ID:', ferry_list[ticket_choosing - 1])
                print('Time of Departure:', time_list[ticket_choosing - 1])
                print(' ')
                return
        elif selected_destination == 'B':
            if ticket_choosing > 16 or ticket_choosing < 9:
                print('Please Pick a value within the range.')
                ticket_choosing = int(input('Your choice:'))
            else:
                print('Ferry_ID:', ferry_list[ticket_choosing - 1])
                print('Time of Departure:', time_list[ticket_choosing - 1])
                print(' ')
                return
        else:
            print('error')



# This Function Prints Out The Ticket
def ticket_type():
    global time, place, class_selected
    time = time.asctime(time.localtime(time.time()))
    print(' ')
    print('='*55)
    print('  \t\tBoarding Ticket')
    print('-'*55)
    print('Name\t\t\t:', name)
    if class_selected == 'B':
        print('Business Class')
    else:
        print('Economy Class')
    if selected_destination == 'A':
        place = 'Penang to Langkawi'
    elif selected_destination == 'B':
        place = 'Langkawi to Penang'
    print('Destination\t\t:', place)
    print('Departure time\t\t:', time_list[ticket_choosing - 1])
    print('Ferry ID\t\t:', ferry_list[ticket_choosing - 1])
    print('Seat Number Chosen :', seat_number)
    print('Please Arrive at Terminal 10 Minutes Before Departure.'.upper())
    print('='*55)
    print(' ')


# This Function Let The User to choose his/her seat (Business Class)
def business_seat():
    global seat_number, v, b_amount, ticket_choosing
    blist  = [v[0][0:5]]
    blist2 = [v[0][5:10]]
    print('     1  2  3  4  5')
    print('1 -', blist)
    print('2 -', blist2)
    while True:
        if b_amount == 0:
            print('Sorry but the ferry is fully booked.')
            break
        else:
            seat_number = int(input('Please Choose Your Seat(From 1 to 10):').upper())
            while True:
                if seat_number > 10 or seat_number < 1:
                    print('Sorry please choose seat between the given value.')
                    seat_number = int(input('Please Choose Your Seat(e.g.:1-10):'))
                else:
                    saving()
                    if v[0][seat_number - 1] == 1:
                        print('Sorry but the seat is booked.')
                        print('Please choose another seat.')
                        seat_number = int(input('Please Choose Your Seat(e.g.:1-10):'))
                    else:
                        v[0][seat_number - 1] = 1
                        print('Success!')
                        b_amount = b_amount - 1
                        saving()
                        return
    saving()


# This Function Let The User to choose his/her seat (Economy Class)
def economy_seat():
    global seat_number, v, ticket_choosing, e_amount
    elist  = [v[0][10:15]]
    elist2 = [v[0][15:20]]
    elist3 = [v[0][20:25]]
    elist4 = [v[0][25:30]]
    elist5 = [v[0][30:35]]
    elist6 = [v[0][35:40]]
    elist7 = [v[0][40:45]]
    elist8 = [v[0][45:50]]
    print('     1  2  3  4  5')
    print('1 -', elist)
    print('2 -', elist2)
    print('3 -', elist3)
    print('4 -', elist4)
    print('5 -', elist5)
    print('6 -', elist6)
    print('7 -', elist7)
    print('8 -', elist8)
    while True:
        seat_number = int(input('Please Choose Your Seat(e.g.:11-50):'))
        open_files()
        if seat_number > 51 or seat_number < 11:
            print('Sorry please choose seat between the given value.')
            seat_number = int(input('Please Choose Your Seat(e.g.:11-50):'))
        else:
            if v[0][seat_number - 1] == 'x':
                print('Sorry but the seat is booked.')
                print('Please choose another seat.')
            else:
                v[0][seat_number - 1] = 'x'
                print('Success!')
                e_amount = e_amount - 1
                saving()
                break
    saving()


# This Functions will take Users' name
def naming():
    global name
    name = input('Your name:')


# This function contain all procedure for booking seat (Business Class)
def business_seat_booking():
    global reply1
    destination()
    comfrim_destination = 0
    if selected_destination == 'A':
        comfrim_destination = 'Penang to Langkawi'
    elif selected_destination == 'B':
        comfrim_destination = 'Langkawi to Penang'
    else:
        print('Error.Code:bsb')
    print('Destination:', comfrim_destination)
    if selected_destination == 'A':
        schedule_p2l()
    elif selected_destination == 'B':
        schedule_l2p()
    else:
        print('Error.Code:bsb2')
    choosing_ticket()
    print('-------------------')
    instructions()
    business_seat()
    open_files()
    naming()
    ticket_type()
    print('Press Q to quit or press M to return to main menu.')
    answer = input('Your Answer:').upper()
    if answer == 'Q':
        reply1 = 'Q'
    elif answer == 'M':
        reply1 = 'M'
    else:
        print('Invalid')


# This function contain all procedure for booking seat (Economy Class)
def economy_seat_booking():
    global reply1
    destination()
    if selected_destination == 'A':
        comfrim_destination = 'Penang to Langkawi'
    elif selected_destination == 'B':
        comfrim_destination = 'Langkawi to Penang'
    else:
        print('Error.Code:esb')
    print('Destination:', comfrim_destination)
    if selected_destination == 'A':
        schedule_p2l()
    elif selected_destination == 'B':
        schedule_l2p()
    else:
        print('Error.Code:bsb')
    choosing_ticket()
    instructions()
    economy_seat()
    open_files()
    naming()
    ticket_type()
    print('Press Q to quit or press M to return to main menu.')
    answer = input('Your Answer:').upper()
    if answer == 'Q':
        reply1 = 'Q'
    elif answer == 'M':
        reply1 = 'M'
    else:
        print('Invalid')


# This Function will Print out the Seating Arrangement
def overall_seating():
    global ticket_choosing
    print('Overall Seating Arrangement')
    print('I will need to know where you are going :)')
    print('1 = Penang to Langkawi')
    print('2 = Langkawi to Penang')
    destination = int(input('Choose your destination:'))
    print(' ')
    if destination == 1:
        schedule_p2l()
    elif destination == 2:
        schedule_l2p()
    else:
        print('Error')
    answer = int(input('Choose your Ferry ID:'))
    print(' ')
    ticket_choosing = answer - 1
    print('Seating Arrangement for Ferry ID(', ferry_list[ticket_choosing - 1], ')')
    print('Time of Departure:', time_list[ticket_choosing - 1])
    with open(str(ticket_choosing), 'rb') as f:
        x = pickle.load(f)
        print('='*15)
        print('Business Class')
        print(x[0][0:5])
        print(x[0][5:10])
        print('-'*15)
        print('Economy Class')
        print(x[0][10:15])
        print(x[0][15:20])
        print(x[0][20:25])
        print(x[0][25:30])
        print(x[0][30:35])
        print(x[0][35:40])
        print(x[0][40:45])
        print(x[0][45:50])
        print('='*15)



# This Shows The Instruction for purchasing
def instructions():
    print(' ')
    if reply1 == 'B':
        print('Business Class')
    elif reply1 == 'E':
        print('Economy Class')
    else:
        print('Error!Code:instruc')
    print('Instructions:')
    print('0 = Available')
    print('x = Already Booked')
    print('')


# This Function create a list for seating plan
def open_files():
    global v
    try:
        file = open(str(ticket_choosing - 1), 'rb')
        v = pickle.load(file)
        file.close()
    except:
        v.append([0 for list in range(50)])


# This Function saves the data
def saving():
    global v
    file = open(str(ticket_choosing - 1), 'wb')
    pickle.dump(v, file)
    file.close()


# Core Function for everything to work
def main_function():
    global class_selected
    while True:
        global reply1
        while reply1 == 'M':
            main_menu()
            reply1 = input('Your choice:').upper()

        while reply1 == 'P':
            submenu()
            reply1 = input('Your choice:').upper()

        while reply1 == 'V':
            overall_seating()
            print('Press Q to quit or press M to return to main menu.')
            reply1 = input('Your choice:').upper()

        while reply1 == 'Q':
            print('Thank you')
            reply1 = 'Q', False
            if reply1 == 'Q':
                break
            return 0

        while reply1 == 'B':
            class_selected = 'B'
            business_seat_booking()

        while reply1 == 'E':
            class_selected = 'E'
            economy_seat_booking()


print('TIME:', real_time)  # Prints time
main_menu()
reply1 = input('Your choice:').upper()  # Reply From User
main_function()
