from external_api.covid import CovidData

value01 = 100
value02 = 250
value03 = 50
value04 = 150
value05 = 375
value06 = 300
value07 = 450

ratio = 20


def graph():

    val01 = '-' * int(value01 / ratio)
    val02 = '-' * int(value02 / ratio)
    val03 = '-' * int(value03 / ratio) 
    val04 = '-' * int(value04 / ratio)
    val05 = '-' * int(value05 / ratio)
    val06 = '-' * int(value06 / ratio)
    val07 = '-' * int(value07 / ratio)

    return f'''
        S : {val01} {value01}
        T : {val02} {value02}
        Q : {val03} {value03}
        Q : {val04} {value04}
        S : {val05} {value05}
        S : {val06} {value06}
        D : {val07} {value07}
    '''


n = CovidData().graph()
print(n)