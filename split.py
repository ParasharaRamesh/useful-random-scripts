def split(costs, total):
    splits = dict()
    for cost in costs:
        txn, people = cost
        amount = txn / len(people)
        for person in people:
            if person in splits:
                splits[person] += amount
            else:
                splits[person] = amount
    return splits, (total == sum(splits.values()))



if __name__ == '__main__':
    total = 47.17
    costs = [
        (5.75, ["a", "s"]), #milk
        (2.95, ["p"]), #truffles
        (1.85, ["p"]), #juice
        (5.75, ["p"]), #milk
        (3.20, ["p", "a", "c"]),#veggies
        (2.27, ["a", "p"]), #ketchup
        (6.7, ["p"]), #ceral
        (6.7, ["s"]),#cereal
        (3.2, ["s"]), #oats
        (3, ["p"]), # banana muffin
        (2.8, ["a"]), #fruits cake
        (3, ["a", "p"]) #bread
    ]
    print(split(costs, total))
