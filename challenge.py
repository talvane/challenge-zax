if __name__ == '__main__':

    motoboys = {
        1: { 'vlr': 2 },
        2: { 'vlr': 2 },
        3: { 'vlr': 2 },
        4: { 'vlr': 2 },
        5: { 'vlr': 3 }
    }
    lojas = {
        1: { 1: { 'vlr': 50, 'perc_extra': 5, 'mot': 4 },
             2: { 'vlr': 50, 'perc_extra': 5, 'mot': 1 },
             3: { 'vlr': 50, 'perc_extra': 5, 'mot': 2 } },

        2: { 1: { 'vlr': 50, 'perc_extra': 5, 'mot': 3 },
             2: { 'vlr': 50, 'perc_extra': 5, 'mot': 5 },
             3: { 'vlr': 50, 'perc_extra': 5, 'mot': 1 },
             4: { 'vlr': 50, 'perc_extra': 5, 'mot': 2 } },

        3: { 1: { 'vlr': 50, 'perc_extra': 15, 'mot': 3 },
             2: { 'vlr': 50, 'perc_extra': 15, 'mot': 5 },
             3: { 'vlr': 100, 'perc_extra': 15, 'mot': 1 } }
    }

    motxljs = {}
    index = 1
    
    for id, pedido in lojas.items():
        for item in pedido.values():
            motxljs[index] = { 
                                'lj': id,
                                'mot': item['mot'],
                                'vlrMot': motoboys[item['mot']]['vlr'],
                                'vlrExtra': ((item['vlr']*item['perc_extra'])/100) 
                            }
            index += 1
    
    motxresult = {}

    for value in motxljs.values():
        if motxresult.get(value['mot']):
            motxresult[value['mot']] = {
                                            'qtdPed': motxresult[value['mot']]['qtdPed'] + 1,
                                            'lojas': motxresult[value['mot']]['lojas'],                                            
                                            'total': motxresult[value['mot']]['total'] + (value['vlrMot'] + value['vlrExtra'])
                                        }
            motxresult[value['mot']]['lojas'].append(value['lj'])                          
        else:
            motxresult[value['mot']] = {
                                            'qtdPed': 1,
                                            'lojas': [value['lj']],
                                            'total': value['vlrMot'] + value['vlrExtra']
                                        }

    cod_motoboy = input('Digite o código do motoboy [1-5]')

    if cod_motoboy != '' and cod_motoboy < '1' or cod_motoboy > '5':
        print('Código inválido.')
    else:
        if cod_motoboy:
            print(motxresult[int(cod_motoboy)])
        else:
            print(motxresult)
