# Google Interview Question Find Best Block
Solving Google Interview Question : given Array of Block find the best blocks that have min distanse between requirements For Example:
blocks = [
        {'gym':True,'store':True,'school':True,'barber':False},
        {'gym':True,'store':False,'school':False,'barber':False},
        {'gym':False,'store':False,'school':False,'barber':False},
        {'gym':False,'store':False,'school':False,'barber':False},
        {'gym':False,'store':False,'school':True,'barber':False},
        {'gym':True,'store':True,'school':False,'barber':False},
        {'gym':False,'store':False,'school':False,'barber':True}
]

requirements = ['gym','stote','school','barber']

in this situation the block with the index of 5 is the best block because its have the min distanse between requirements.
