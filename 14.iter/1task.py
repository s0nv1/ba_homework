# 1.1 Task

n = 10
generator_list = (str(num) for num in range(1, n + 1))

assert list(generator_list) == ['1', '2', '3', '4', '5', 
                                '6', '7', '8', '9', '10',
                                ]

# 1.2 Task

s = ['кит', 'кот', 'крот']
generator_list = (f'{i} {s[i]}' for i in range(len(s)))

def num_list(lis):
    for ind in range(len(lis)):
        yield f'{ind} {lis[ind]}'
        
assert list(num_list(s)) == ['0 кит', '1 кот', '2 крот']
assert list(generator_list) == ['0 кит', '1 кот', '2 крот']

# 1.3 Task

s = ['кит', 'кот', 'крот']
gen = (f'{i} {s[i]}' for i in range(len(s)) if len(s[i]) <= 3)

def gen_list_less_3(lis):
    n = 0
    for i in lis:
        if len(i) <= 3:
            yield f'{n} {i}'
            n += 1
            
assert list(gen_list_less_3(s)) == ['0 кит', '1 кот']
assert list(gen) == ['0 кит', '1 кот']

# 1.4 Task

lists = ['111', 'cat', 'got', 'ddd', '222']
gener_digit = (i for i in lists if all(n.isdigit() for n in i))

def gen_digit(lis):
    for st in lis:
        try:
            int(st)
            yield st
        except ValueError:
            pass

assert list(gen_digit(lists)) == ['111', '222']
assert list(gener_digit) == ['111', '222']

# 1.5 Task

gener_digit_index = (i for i in range(len(lists)) if all(n.isdigit() for n in lists[i]))

def gen_index_digit(lis):
    for i in range(len(lis)):
        try:
            int(lis[i])
            yield i
        except ValueError:
            pass

assert list(gen_index_digit(lists)) ==  [0, 4]
assert list(gener_digit_index) == [0, 4]

# 1.6 Task
gen_tuple_ind_dig = ((i, lists[i]) for i in range(len(lists)) if all(n.isdigit() for n in lists[i]))
def gen_tuple_ind_digit(lis):
    for i in range(len(lis)):
        try:
            int(lis[i])
            yield (i, lis[i])
        except ValueError:
            pass

assert list(gen_tuple_ind_digit(lists)) ==  [(0, '111'), (4, '222')]
assert list(gen_tuple_ind_dig) == [(0, '111'), (4, '222')]

# 1.7 Task

phones = ['044 225 73 39', '099 116 30 87', '094 129 81 69', 
        '094 127 04 85', '044 222 74 33', '044 353 55 31', 
        '097 921 27 09', '094 550 50 02', '044 362 96 00', 
        '097 853 55 81', '097 120 95 90', '099 752 22 97', 
        '050 761 49 45', '094 497 75 09', '094 498 89 53', 
        '094 496 13 91', '094 497 35 13', '094 497 75 69', 
        '050 063 52 97', '050 530 97 71', '044 227 16 63', 
        '056 785 55 19', '068 450 69 13', '097 001 42 67', 
        '096 097 58 16', '094 497 34 37', '094 097 12 17', 
        '094 497 75 69', '097 497 75 97', '094 497 34 85', 
        '094 496 52 54',
        ]

only_kiestar_n = (i for i in phones if i[:3] == '097')

assert list(only_kiestar_n) == ['097 921 27 09', '097 853 55 81', 
                                        '097 120 95 90', '097 001 42 67', 
                                        '097 497 75 97',
                                        ]

# 1.8 Task

only_kie_n = (i for i in phones if i[:3] in ('097', '050'))

assert list(only_kie_n) == ['097 921 27 09', '097 853 55 81', 
                                        '097 120 95 90', '050 761 49 45', 
                                        '050 063 52 97', '050 530 97 71', 
                                        '097 001 42 67', '097 497 75 97',
                                        ]

# 1.9 Task

only_kie_num_38 = (('+38' + i).replace(' ', '', len(i)) for i in phones \
                                                if i[:3] in ('097', '050'))

assert list(only_kie_num_38) == ['+380979212709', '+380978535581', 
                                            '+380971209590', '+380507614945', 
                                            '+380500635297', '+380505309771', 
                                            '+380970014267', '+380974977597',
                                            ]
                                            
