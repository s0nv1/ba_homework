# 2.1 Task
lists = ['111', 'cat', 'got', 'ddd', '222']


class GreatNumerator:
    
    def __init__(self, lis):
        self.lis = lis
        self.index = -1
        
    def __iter__(self):
        return self
    
    def __next__(self):
        self.index += 1
        if self.index > len(self.lis) - 1:
            raise StopIteration
        return f'{self.index} {self.lis[self.index]}'

assert list(GreatNumerator(lists)) == ['0 111','1 cat',
                                        '2 got','3 ddd',
                                        '4 222',
                                        ]

# 2.2 Task 1.7
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

class Phonefil:
    
    def __init__(self, lis):
        self.lis = list(i for i in lis if i[:3] == '097')
        self.ind = -1
        
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.ind == len(self.lis) - 1:
            raise StopIteration
        self.ind += 1
        return self.lis[self.ind]


assert list(Phonefil(phones)) == ['097 921 27 09', '097 853 55 81', 
                                '097 120 95 90', '097 001 42 67', 
                                '097 497 75 97',
                                ]

# 2.2 Task 1.8

class Phonefil:
    
    def __init__(self, lis):
        self.lis = list(i for i in lis if i[:3] in ['097', '050'])
        self.ind = -1
        
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.ind == len(self.lis) - 1:
            raise StopIteration
        self.ind += 1
        return self.lis[self.ind]

assert list(Phonefil(phones)) ==  ['097 921 27 09', '097 853 55 81', 
                                    '097 120 95 90', '050 761 49 45', 
                                    '050 063 52 97', '050 530 97 71', 
                                    '097 001 42 67', '097 497 75 97',
                                    ]

# 2.2 Task 1.9

class Phonefil:
    
    def __init__(self, lis):
        self.lis = list(('+38' + i).replace(' ', '', len(lis)) for i in lis \
                                                    if i[:3] in ['097', '050'])
        self.ind = -1
        
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.ind == len(self.lis) - 1:
            raise StopIteration
        self.ind += 1
        return self.lis[self.ind]

assert list(Phonefil(phones)) ==  ['+380979212709', '+380978535581', 
                                    '+380971209590', '+380507614945', 
                                    '+380500635297', '+380505309771', 
                                    '+380970014267', '+380974977597',
                                    ]
