# there was not enough time to complete this code. still alot to do compared to former function

import re 
def tointegers(n):
    units={'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9}
    first_tens={'ten':10,'eleven':11,'twelve':12,'thirteen':13,'fourteen':14,'fifteen':15,'sixteen':16,
            'seventeen':17,'eighteen':18,'nineteen':19}
    tens={'twenty':2,'thirty':3,'fourty':4,'fifty':5,'sixty':6,'seventy':7,'eighty':8,'ninety':9}
    hundreds={'one hundred':1,'two hundred':2,'three hundred':3,'four hundred':4,'five hundred':5,
          'six hundred':6,'seven hundred':7,'eight hundred':8,'nine hundred':9}
    thousands={'one thousand':1,'two thousand':2,'three thousand':3,'four thousand':4,
           'five thousand':5,'six thousand':6,'seven thousand':7,'eight thousand':8,'nine thousand':9}
    ten_thousands={'ten thousand':10,'eleven thousand':11,'twelve thousand':12,'thirteen thousand':13,
               'fourteen thousand':14,'fifteen thousand':15,'sixteen thousand':16,'seventeen thousand':17,
               'eighteen thousand':18, 'nineteen thousand':19,'twenty thousand':20,'thirty thousand':30,
               'fourty thousand':40,'fifty thousand':50,'sixty thousand':60,'seventy thousand':70,
               'eighty thousand':80,'ninety thousand':90}
    hundred_thousands={'one hundred thousand':100,'two hundred thousand':200,'three hundred thousand':300,
                    'four hundred thousand':400,'five hundred thousand':500,'six hundred thousand':600,
                    'seven hundred thousand':700,'eight hundred thousand':800,'nine hundred thousand':900}

    
    k = re.split(r'\sand\s',n) if 'and' in n else n.split()
    
    if len(k) == 1:
        if n in units.keys():
            extract_units= ''.join([str(z[1]) for z in units.items() if z[0]==n])
            fin_extract= extract_units

        if  n in first_tens.keys():
            extract_units= ''.join([str(z[1]) for z in first_tens.items() if z[0]==n])
            fin_extract= extract_units

    # if len(k) == 1:
        if n in tens.keys():
            extract_units= ''.join([str(z[1]) for z in tens.items() if z[0]==n])
            fin_extract= '{}{}'.format(extract_units,0)

        elif n in hundreds.keys():
            extract_units= ''.join([str(z[1]) for z in hundreds.items() if z[0]==n])
            fin_extract= '{}{}{}'.format(extract_units,0,0)

        elif n in thousands.keys():
            extract_units= ''.join([str(z[1]) for z in thousands.items() if z[0]==n])
            fin_extract= '{},{}{}{}'.format(extract_units,0,0,0)

        elif n in ten_thousands.keys():
            extract_units= ''.join([str(z[1]) for z in thousands.items() if z[0]==n])
            extract_units= ''.join([str(z[1]) for z in ten_thousands.items() if z[0]==n])
            fin_extract= '{},{}{}{}'.format(extract_units,0,0,0)


    if len(k) == 2:
        if k[0] in tens.keys() and k[1] in units.keys():
            extract_units= ''.join([str(z[1]) for z in units.items() if z[0]==k[1]])
            extract_tens= ''.join([str(z[1]) for z in tens.items() if z[0]==k[0]])
            fin_extract= '{}{}'.format(extract_tens,extract_units)
    
        if k[0] in hundreds.keys():
            if k[1] in units.keys():
                extract_units= ''.join([str(z[1]) for z in units.items() if z[0]==k[1]])
                extract_hundred= ''.join([str(z[1]) for z in hundreds.items() if z[0]==k[0]])
                fin_extract= '{}{}{}'.format(extract_hundred,0,extract_units)

            if k[1] in first_tens.keys():
                extract_units= ''.join([str(z[1]) for z in first_tens.items() if z[0]==k[1]])
                extract_hundred= ''.join([str(z[1]) for z in hundreds.items() if z[0]==k[0]])
                fin_extract= '{}{}'.format(extract_hundred,extract_units)

            if k[1] in tens.keys():
                extract_units= ''.join([str(z[1]) for z in tens.items() if z[0]==k[1]])
                extract_hundred= ''.join([str(z[1]) for z in hundreds.items() if z[0]==k[0]])
                fin_extract= '{}{}{}'.format(extract_hundred,extract_units,0)

            # if m[0] in tens.keys() and m[1] in units.keys():
            #     extract_units= ''.join([str(z[1]) for z in units.items() if z[0]==m[1]])
            #     extract_tens= ''.join([str(z[1]) for z in tens.items() if z[0]==m[0]])
            #     extract_hundred= ''.join([str(z[1]) for z in hundreds.items() if z[0]==k[0]])
            #     fin_extract= '{}{}{}'.format(extract_hundred,extract_tens,extract_units)
    
    if n == 'hundred':
        fin_extract = 100

    return fin_extract

print(tointegers('one hundred and eighty'))