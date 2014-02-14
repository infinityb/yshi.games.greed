import random

_scoring_table = [
    ((1, 2, 3, 4, 5, 6), 1200),
    ((2, 2, 3, 3, 4, 4), 800),
    ((1,)*6, 8000),
    ((1,)*5, 4000),
    ((1,)*4, 2000),
    ((1,)*3, 1000),
    ((1,),    100),
    ((2,)*6, 1600),
    ((2,)*5,  800),
    ((2,)*4,  400),
    ((2,)*3,  200),
    ((3,)*6, 2400),
    ((3,)*5, 1200),
    ((3,)*4,  600),
    ((3,)*3,  300),
    ((4,)*6, 3200),
    ((4,)*5, 1600),
    ((4,)*4,  800),
    ((4,)*3,  400),
    ((5,)*6, 4000),
    ((5,)*5, 2000),
    ((5,)*4, 1000),
    ((5,)*3,  500),
    ((5,),     50),
    ((6,)*6, 4800),
    ((6,)*5, 2400),
    ((6,)*4, 1200),
    ((6,)*3,  600),
]

_score_by_group = dict(_scoring_table)


def is_prefix(prefix, data):
    if len(data) < len(prefix):
        return False
    for data_elem, pref_elem in zip(data, prefix):
        if data_elem != pref_elem:
            return False
    return True


def dice_roll(ndice=6, sides=6):
    out = list()
    for _ in xrange(ndice):
        out.append(random.randint(1, sides))
    return out


def group_roll(roll_result):
    roll_result = list(sorted(roll_result))
    unclaimed = list()
    groups = list()
    idx = 0
    while idx < len(roll_result):
        for dice, dscore in _scoring_table:
            if is_prefix(dice, roll_result[idx:]):
                groups.append((dice, dscore))
                idx += len(dice)
        if idx < len(roll_result):
            unclaimed.append(roll_result[idx:][0])
            idx += 1
    if unclaimed:
        groups.append((tuple(unclaimed), 0))
    return groups


def calculate_score(groups):
    return sum(map(calculate_score_group, groups))


def calculate_score_group(group):
    return _score_by_group.get(group, 0)
