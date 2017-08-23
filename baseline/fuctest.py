import numpy as np
import copy
top10 = {
    '557579': ['1_6', 212 * 1],
    '558082': ['1_11', 168 * 1],
    '558788': ['1_6', 156 * 1],
    '557167': ['1_6', 134 * 1],
    '558910': ['1_1', 131 * 1],
    '556664': ['1_8', 122 * 1],
    '552472': ['1_2', 111 * 1],
    '555820': ['1_6', 106 * 1],
    '558077': ['1_5', 94 * 1],
    '557018': ['1_6', 92 * 1],
    '556700': ['1_1', 91 * 1],
    '558096': ['1_12', 91 * 1],
    '558498': ['1_11', 89 * 1],
    '558259': ['1_6', 88 * 1],
    '558768': ['1_1', 85 * 1],
    '558625': ['1_6', 78 * 1],
    '558871': ['1_1', 76 * 1],
    '558578': ['1_3', 73 * 1],
    '558331': ['1_3', 73 * 1],
    '552335': ['1_6', 73 * 1],
}

test = {
    1:{
    '1_2' : 55,
    '1_3' : 46,
    '1_1' : 22,
    '1_6' : 19,
    '1_11' : 9
    },
    2 :{
    '1_1' : 42 * 6,
    '1_2' : 1 * 5
    },

    3 : {
    '1_1' : 28 * 6,
    '1_6' : 25 * 5,
    '1_8' : 22 * 4,
    },

    4 : {
    '1_6' : 43 * 6,
    '1_11' : 18 * 5,
    '1_1' : 12 * 4
    },

    5 : {
    '1_1' : 24 * 6,
    '1_6' : 3 * 5,
    '1_2' : 9 * 4
    }
}

for user in test:
    top10copy = copy.deepcopy(top10)
    for i in top10copy:
        if top10copy[i][0] in test[user]:
            top10copy[i][1] *= test[user][top10copy[i][0]]

    top = sorted(top10copy.items(), key=lambda x:x[1][1],reverse=True)

    print(' '.join([x[0] for x in top[:5]]))
    print(top[:5])
