peso = int ( input( " insira o peso dos peixes"))
if peso <= 50: 
    print( "vai pagar multa nao ")
else:
        excesso= peso - 50 
        print( "kilos a mais: ",excesso)
        multa = excesso * 4 
        print( "essa é a multa", multa)