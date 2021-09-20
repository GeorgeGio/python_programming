offense = False
defense = False
rule_changes = False

offense_new = None
defense_new = None
rule_changes_new = None

def get_offense():
    global offense_new


    offense_new = True
    print("We have offense:", offense_new)
    return offense_new


def get_defense():
    global defense_new
    defense_new = True
    print("We have defense:", defense_new)
    return defense_new

def get_rule_changes():



    rule_changes_new = True
    print("We have some rule changes:", rule_changes_new)

if offense_new and defense_new and rule_changes_new:

    print("We're going to the Super Bowl!")
else:
    print("We have defense:", defense)
    print("I can't predict the future, but no, the Jaguars will never win the Super Bowl.")






print("How are the Jags doing?\n")


get_offense()
get_defense()
get_rule_changes()
