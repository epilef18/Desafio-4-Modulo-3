recordatorios = [['2021-01-01', "11:00", "Levantarse y ejercitar"],
 ['2021-05-01', "15:00", "No trabajar"],
 ['2021-07-15', "13:00", "No hacer nada es feriado"],
 ['2021-09-18', "16:00", "Ramadas"],
 ['2021-12-25', "00:00", "Navidad"]]


recordatorios[2] = ['2021-07-16', "13:00", "No hacer nada es feriado"]
recordatorios.pop(1)
recordatorios.insert(3,['2021-12-25', "22:00", "Cena de Navidad"])
recordatorios.insert(6,['2021-12-31', "22:00", "Cena de Año Nuevo"])
recordatorios.insert(1,['2021-02-02', "06:00", "Empezar el Año"])

# Output
print(recordatorios)
