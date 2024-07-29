salario = int( input( "quanto ganha por hora ? "))
horas= int( input( "quantas horas o mes trabalha ? "))
salario_bruto = float (salario * horas)
inss = 0.08 * salario_bruto
renda = 0.11 * salario_bruto
sindica = 0.05 * salario_bruto
liquido = salario_bruto - inss - renda - sindica
print ( " + Salário bruto: R$", salario_bruto)
print ("- IR(11%) : R$", renda)
print ( " - INSS (8%): R$", inss)
print ( "- Sindicato (5%): R$", sindica)
print ( "Salário líquido: R$ ", liquido)