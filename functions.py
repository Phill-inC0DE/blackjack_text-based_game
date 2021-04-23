# Useful functions.

def check_for_int(command):
    try:
        if command <= amount_in_pot:
            int(command)
            return command
        else:
            print("You do not have enough funds.")
    except ValueError:
        print("Type in a number.")
        return 0


    #print("You do not have enough funds.")
    #while True:
        #confirm_max = input("Would you like to add the maximum avaliable? Y/N\n")
        #if confirm_max.upper() == "Y":
            #bet_prompt = amount_in_pot
            #return bet_prompt
        #elif comfirm_max.upper() == "N":
            #command = input("How much would you like to bet?\n")
            #return int(command)