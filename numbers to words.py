number = eval(input('Enter number:'))
def towords(n):
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

    if n<20:
            if n in units.values():
                extract_units=[z[0] for z in units.items() if z[1]==n]
                fin_extract=''.join(extract_units)

    if n==20:            
            fin_extract = 'twenty'
    
    elif n>20 and n<100:
            n=str(n)
            extract_tens=[z[0] for z in tens.items() if z[1]==int(n[0])]
            extract_units=[z[0] for z in units.items() if z[1]==int(n[1])]
            fin_extract=''.join(extract_tens)+'-'*len(extract_units)+''.join(extract_units)
   
    elif n>99 and n<1000:
            n=str(n)
            extract_hundreds=[z[0] for z in hundreds.items() if z[1]==int(n[0])]
            add=int(n[1]+n[2])
            if add in first_tens.values():
                extract_first_tens=[z[0] for z in first_tens.items() if z[1]==add]
                fin_extract=''.join(extract_hundreds)+' '+'and'+' '+''.join(extract_first_tens)
            else:
                extract_tens=[z[0] for z in tens.items() if z[1]==int(n[1])]
                extract_units=[z[0] for z in units.items() if z[1]==int(n[2])]
                fin_extract=''.join(extract_hundreds)+' '+'and'*(((len(extract_units)+len(extract_tens))**2)%3)\
                +' '+''.join(extract_tens)+'-'*len(extract_units)*len(extract_tens)+''.join(extract_units)
   
    elif n>999 and n<10000:
            n=str(n)
            extract_thousands=[z[0] for z in thousands.items() if z[1]==int(n[0])]
            extract_hundreds=[z[0] for z in hundreds.items() if z[1]==int(n[1])]
            add=int(n[2]+n[3])
            if add in first_tens.values():
                extract_first_tens=[z[0] for z in first_tens.items() if z[1]==add]
                fin_extract=''.join(extract_thousands)+','*len(extract_hundreds)+''.join(extract_hundreds)+' '+'and'+' '+''.join(extract_first_tens)
            else:
                extract_tens=[z[0] for z in tens.items() if z[1]==int(n[2])]
                extract_units=[z[0] for z in units.items() if z[1]==int(n[3])]
                fin_extract=''.join(extract_thousands)+','*len(extract_hundreds)+''.join(extract_hundreds)\
                +' '+'and'*(((len(extract_units)+len(extract_tens))**2)%3)+' '+''.join(extract_tens)+'-'*len(extract_units)*len(extract_tens)+''.join(extract_units)
        
    elif n>9999 and n<100000:
            n=str(n)
            add1=int(n[0]+n[1])
            if add1 in ten_thousands.values():
                extract_ten_thousands=[z[0] for z in ten_thousands.items() if z[1]==add1]
            else:
                extract_ten_thousands=''.join([z[0] for z in tens.items() if z[1]==int(n[0])])+'-'+\
            ''.join([z[0] for z in thousands.items() if z[1]==int(n[1])])
            extract_hundreds=[z[0] for z in hundreds.items() if z[1]==int(n[2])]
            add=int(n[3]+n[4])

            if add in first_tens.values():
                extract_first_tens=[z[0] for z in first_tens.items() if z[1]==add]
                fin_extract=''.join(extract_ten_thousands)+','*len(extract_hundreds)\
                +''.join(extract_hundreds)+' '+'and'+' '+''.join(extract_first_tens)
            else:
                extract_tens=[z[0] for z in tens.items() if z[1]==int(n[3])]
                extract_units=[z[0] for z in units.items() if z[1]==int(n[4])]
                fin_extract=''.join(extract_ten_thousands)+','*len(extract_hundreds)+''.join(extract_hundreds)\
                +' '+'and'*(((len(extract_units)+len(extract_tens))**2)%3)+' '+\
                ''.join(extract_tens)+'-'*len(extract_units)*len(extract_tens)+''.join(extract_units)
        
    elif n>=100000 and n<1000000:
            n=str(n)
            add1=int(n[0]+n[1]+n[2])
            add2=int(n[1]+n[2])
            if add1 in hundred_thousands.values():
                extract_hundred_thousands=[z[0] for z in hundred_thousands.items() if z[1]==add1]

            elif add2 in ten_thousands.values():
                extract_hundred_thousands=''.join([z[0] for z in hundreds.items() if z[1]==int(n[0])])+' '+'and'+' '+\
                ''.join([z[0] for z in ten_thousands.items() if z[1]==add2])
            else:
                extract_hundred_thousands=''.join([z[0] for z in hundreds.items() if z[1]==int(n[0])])+' '+'and'+' '+\
                ''.join([z[0] for z in tens.items() if z[1]==int(n[1])])+'-'*len([z[0] for z in tens.items() if z[1]==int(n[1])])\
                +''.join([z[0] for z in thousands.items() if z[1]==int(n[2])])
            extract_hundreds=[z[0] for z in hundreds.items() if z[1]==int(n[3])]
            add=int(n[4]+n[5])

            if add in first_tens.values():
                extract_first_tens=[z[0] for z in first_tens.items() if z[1]==add]
                fin_extract=''.join(extract_hundred_thousands)+','*len(extract_hundreds)\
                +''.join(extract_hundreds)+' '+'and'+' '+''.join(extract_first_tens)
            else:
                extract_tens=[z[0] for z in tens.items() if z[1]==int(n[4])]
                extract_units=[z[0] for z in units.items() if z[1]==int(n[5])]
                fin_extract=''.join(extract_hundred_thousands)+','*len(extract_hundreds)+''.join(extract_hundreds)\
                +' '+'and'*(((len(extract_units)+len(extract_tens))**2)%3)+' '+\
                ''.join(extract_tens)+'-'*len(extract_units)*len(extract_tens)+''.join(extract_units)

    return fin_extract
    
print(towords(number))
