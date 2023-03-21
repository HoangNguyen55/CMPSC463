def main():
    companies = {
        "Google": ["Lisa", "Tom", "Sarah", "Bob", "Jane"],
        "Amazon": ["Sarah", "Tom", "Jane", "Lisa", "Bob"],
        "Meta": ["Jane", "Lisa", "Bob", "Tom", "Sarah"],
        "Apple": ["Jane", "Bob", "Tom", "Sarah", "Lisa"],
        "Microsoft": ["Bob", "Tom", "Sarah", "Lisa", "Jane"],
    }

    people = {
        "Lisa": ["Google", "Amazon", "Apple", "Meta", "Microsoft"],
        "Sarah": ["Amazon", "Apple", "Meta", "Google", "Microsoft"],
        "Bob": ["Microsoft", "Meta", "Google", "Apple", "Amazon"],
        "Tom": ["Meta", "Google", "Apple", "Amazon", "Microsoft"],
        "Jane": ["Apple", "Google", "Amazon", "Microsoft", "Meta"],
    }

    print("Company first")
    run_GS(proposers = companies, proposed = people)
    print("-"*20)
    print("People first")
    run_GS(proposers = people, proposed = companies)


def run_GS(proposers: dict[str, list], proposed: dict[str, list]):
    # list comprehensions for getting the name of all the proposer
    free_proposer: list[str] = [i for i in proposers]
    matched = {}

    # get the name of all the candiates and put them in a dictionary with a starting
    # state of None which is free
    for i in proposed:
        matched[i] = None

    while free_proposer:
        # get the proposer who are free and remove them from the
        # list of free proposer at the same time
        proposer = free_proposer.pop(0)

        # get the first person in the proposer's list
        # while also getting rid of them as potential
        # candidate again at the same time
        candidate: str = proposers[proposer].pop(0)

        # if the person being proposed to is already ocupied
        if matched[candidate]:
            # get the candidate's list and check if the proposer is higher priority
            if proposed[candidate].index(proposer) < proposed[candidate].index(matched[candidate]):
                # the person who matched to the candidate previously are now free
                free_proposer.insert(0, matched[candidate])
                # now the candidate and proposer are matched
                matched[candidate] = proposer
            else:
                # put the candidate back in the free list since they fail to get a new partner
                free_proposer.insert(0, proposer)
        else:
            # if they are not ocupied then they are instantly matched
            matched[candidate] = proposer

    for k, v in matched.items():
       print(f"{k} <-> {v}" )

if __name__ == "__main__":
    main()
