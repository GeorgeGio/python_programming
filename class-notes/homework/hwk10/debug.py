offense = False
defense = False
rule_changes = False

def get_offense():


    offense = True
    print("We have offense:", offense)
    return offense

def get_defense():
    defense = True
    print("We have defense:", defense)

def get_rule_changes():


    rule_changes = True
    print("We have some rule changes:", rule_changes)

    if offense or defense or rule_changes:


        print("We're going to the Super Bowl!")
    else:
        print("We have defense:", defense)
        print("I can't predict the future, but no, the Jaguars will never win the Super Bowl.")






print("How are the Jags doing?\n")


get_offense()
get_defense()
get_rule_changes()
