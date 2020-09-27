hm = {'00':'двенадцать','1':'один','2':'два','3':'три','4':'четыре','5':'пять','6':'шесть','7':'семь','8':'восемь','9':'девять','10':'десять','11':'одинадцать','12':'двенадцать','13':'тринадцать','14':'четырнадцать','15':'пятнадцать','16':'шестнадцать','17':'семнадцать','18':'восемнадцать','19':'девятнадцать'}
tens = {'2':'двадцать','3':'тридцать','4':'сорок','5':'пятьдесят'}
mins = {'1':'одна','2':'две','3':'три','4':'четыре'}
add1 = {'1':'первого','2':'второго','3':'третьего','4':'четвертого','5':'пятого','6':'шестого','7':'седьмого','8':'восьмого','9':'девятого','10':'десятого','11':'одинадцатого','12':'двенадцатого','13':'первого','14':'второго','15':'третьего','16':'четвертого','17':'пятого','18':'шестого','19':'седьмого','20':'восьмого','21':'девятого','22':'десятого','23':'одинадцатого','24':'двенадцатого'}
add2 ={'1':'час','2':'два','3':'три','4':'четыре','5':'пять','6':'шесть','7':'семь','08':'восемь','09':'девять','10':'десять','11':'одинадцать','12':'двенадцать','13':'час','14':'два','15':'три','16':'четыре','17':'пять','18':'шесть','19':'семь','20':'восемь','21':'девять','22':'десять','23':'одинадцать','24':'двенадцать'}
q = input("Введите время:")
o1 = q[0] + q[1]
o2 = q[2] + q[3]
if o1>'23' or o2>'59':
    print ('error')
elif o2 == '45':
    print ('без пятнадцати '+ add2[(str(int(o1) + 1))])
elif o2 == '50':
    print ('без десяти '+ add2[(str(int(o1) + 1))])
elif o2 == '40':
    print ('без двадцати '+ add2[(str(int(o1) + 1))])
elif o2 == '20':
    print ('двадцать минут '+ add1[(str(int(o1) + 1))])
elif o2 == '15':
    print ('пятнадцать минут '+ add1[(str(int(o1) + 1))])
elif o2 == '30':
    print ('пол '+ add1[(str(int(o1) + 1))])
elif o2 == '00':
    if o1 =="01":
        print (add2[(str(int(o1)))] + ' ровно')
    elif o1 in ('02','03','04','13','14','15','16'):
        print (add2[(str(int(o1)))] + ' часа ровно')
    else:
        print (add2[(str(int(o1)))] + ' часов ровно')
elif o2 == '55':
    print ('без пяти '+ add2[(str(int(o1) + 1))])
elif o2 == '05':
    print ('пять минут '+ add1[(str(int(o1) + 1))])
elif o1 == '00':
    if q[2] == '0':
        print ('двенадцать часов ' + mins[(q[3])] + ' минуты' )
    elif q[2] == '1':
        print ('двенадцать часов '+ hm[(o2)] + ' минут' )
    elif q[2] in ('2','3','4','5'):
        if q[3] == '1':
            print ('двенадцать часов ' + tens[(q[2])] + ' '+ mins[(q[3])] + ' минута' )
        elif q[3] in ('2','3','4'):
            print ('двенадцать часов ' + tens[(q[2])] + ' '+ mins[(q[3])] + ' минуты' )
        else:
            print ('двенадцать часов '+ tens[(q[2])] + ' '+ hm[(q[3])] + ' минут' )
elif q[0] == '0':
    if q[1] == '1':
        if q[2] == '0':
            print (hm[(q[1])] + ' час'+ ' ' + hm[(q[3])] + ' минут' )
        elif q[2] == '1':
            print (hm[(q[1])] + ' час'+ ' ' + hm[(o2)] + ' минут' )
        elif q[2] in ('2','3','4','5'):
            if q[3] == '1':
                print (hm[(q[1])] + ' час'+ ' ' + tens[(q[2])] + ' '+ mins[(q[3])] + ' минута' )
            elif q[3] in ('2','3','4'):
                print (hm[(q[1])] + ' час'+ ' ' + tens[(q[2])] + ' '+ mins[(q[3])] + ' минуты' )            
            else:
                print (hm[(q[1])] + ' час'+ ' ' + tens[(q[2])] + ' '+ hm[(q[3])] + ' минут' )
    elif q[1] in ('2','3','4'):
        if q[2] == '0':
            print (hm[(q[1])] + ' часа'+ ' ' + hm[(q[3])] + ' минут' )
        elif q[2] == '1':
            print (hm[(q[1])] + ' часа'+ ' ' + hm[(o2)] + ' минут' )
        elif q[2] in ('2','3','4','5'):
            if q[3] == '1':
                print (hm[(q[1])] + ' часа'+ ' ' + tens[(q[2])] + ' '+ mins[(q[3])] + ' минута' )
            elif q[3] in ('2','3','4'):
                print (hm[(q[1])] + ' часа'+ ' ' + tens[(q[2])] + ' '+ mins[(q[3])] + ' минуты' )            
            else:
                print (hm[(q[1])] + ' часа'+ ' ' + tens[(q[2])] + ' '+ hm[(q[3])] + ' минут' )
    elif q[1] in ('5','6','7','8','9'):
        if q[2] == '0':
            print (hm[(q[1])] + ' часов'+ ' ' + hm[(q[3])] + ' минут' )
        elif q[2] == '1':
            print (hm[(q[1])] + ' часов'+ ' ' + hm[(o2)] + ' минут' )
        elif q[2] in ('2','3','4','5'):
            if q[3] == '1':
                print (hm[(q[1])] + ' часов'+ ' ' + tens[(q[2])] + ' '+ mins[(q[3])] + ' минута' )
            elif q[3] in ('2','3','4'):
                print (hm[(q[1])] + ' часов'+ ' ' + tens[(q[2])] + ' '+ mins[(q[3])] + ' минуты' )            
            else:
                print (hm[(q[1])] + ' часов'+ ' ' + tens[(q[2])] + ' '+ hm[(q[3])] + ' минут' )
elif q[0] == '1':
    if q[2] == '0':
        print (hm[(o1)] + ' часов'+ ' ' + hm[(q[3])] + ' минут' )
    elif q[2] == '1':
        print (hm[(o1)] + ' часов'+ ' ' + hm[(o2)] + ' минут' )
    elif q[2] in ('2','3','4','5'):
        if q[3] == '1':
            print (hm[(o1)] + ' часов'+ ' ' + tens[(q[2])] + ' '+ mins[(q[3])] + ' минута' )
        elif q[3] in ('2','3','4'):
            print (hm[(o1)] + ' часов'+ ' ' + tens[(q[2])] + ' '+ mins[(q[3])] + ' минуты' )            
        else:
            print (hm[(o1)] + ' часов'+ ' ' + tens[(q[2])] + ' '+ hm[(q[3])] + ' минут' )
elif o1 == '21':
    if q[2] == '0':
        print (tens[(q[0])] + ' '+ hm[(q[1])] +' час'+ ' ' + hm[(q[3])] + ' минут' )
    elif q[2] == '1':
        print (tens[(q[0])] + ' '+ hm[(q[1])] +' час'+ ' ' + hm[(o2)] + ' минут' )
    elif q[2] in ('2','3','4','5'):
        if q[3] == '1':
            print (tens[(q[0])] + ' '+ hm[(q[1])] +' час'+ ' ' + tens[(q[2])] + ' '+ mins[(q[3])] + ' минута' )
        elif q[3] in ('2','3','4'):
            print (tens[(q[0])] + ' '+ hm[(q[1])] +' час'+ ' ' + tens[(q[2])] + ' '+ mins[(q[3])] + ' минуты' )            
        else:
            print (tens[(q[0])] + ' '+ hm[(q[1])] +' час'+ ' ' + tens[(q[2])] + ' '+ hm[(q[3])] + ' минут' )
elif q[0] == '2':
    if q[2] == '0':
        print (tens[(q[0])] + ' '+ hm[(q[1])] +' часа'+ ' ' + hm[(q[3])] + ' минут' )
    elif q[2] == '1':
        print (tens[(q[0])] + ' '+ hm[(q[1])] +' часа'+ ' ' + hm[(o2)] + ' минут' )
    elif q[2] in ('2','3','4','5'):
        if q[3] == '1':
            print (tens[(q[0])] + ' '+ hm[(q[1])] +' часа'+ ' ' + tens[(q[2])] + ' '+ mins[(q[3])] + ' минута' )
        elif q[3] in ('2','3','4'):
            print (tens[(q[0])] + ' '+ hm[(q[1])] +' часа'+ ' ' + tens[(q[2])] + ' '+ mins[(q[3])] + ' минуты' )            
        else:
            print (tens[(q[0])] + ' '+ hm[(q[1])] +' часа'+ ' ' + tens[(q[2])] + ' '+ hm[(q[3])] + ' минут' )