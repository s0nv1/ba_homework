# 3.1 
strings = ['111', 'cat', 'got', 'ddd', '222']

def GreatNumerator(lists):
    for s in range(len(lists)):
        yield f'{s} {lists[s]}'

assert list(GreatNumerator(strings)) == ['0 111','1 cat',
                                        '2 got','3 ddd',
                                        '4 222',
                                        ]

# 3.2---1.7 Task
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
        
def only_kiestar_num(lis):
    for tel in lis:
        if tel.startswith('097'):
            yield tel

assert list(only_kiestar_num(phones)) == ['097 921 27 09', '097 853 55 81', 
                                        '097 120 95 90', '097 001 42 67', 
                                        '097 497 75 97',
                                        ]

# 3.2----1.8 Task
def only_kie_num(lis):
    for tel in lis:
        if tel.startswith('097') or tel.startswith('050'):
            yield tel

assert list(only_kie_num(phones)) ==  ['097 921 27 09', '097 853 55 81', 
                                        '097 120 95 90', '050 761 49 45', 
                                        '050 063 52 97', '050 530 97 71', 
                                        '097 001 42 67', '097 497 75 97',
                                        ]

# 3.2---1.9 Task
def only_kie_num_380(lis):
    for tel in lis:
        if tel.startswith('097') or tel.startswith('050'):
            yield ('+38' + tel).replace(' ', '', len(tel))

assert list(only_kie_num_380(phones)) ==  ['+380979212709', '+380978535581', 
                                            '+380971209590', '+380507614945', 
                                            '+380500635297', '+380505309771', 
                                            '+380970014267', '+380974977597',
                                            ]
