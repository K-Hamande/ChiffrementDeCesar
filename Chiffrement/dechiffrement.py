def DechiffrementCesar(s, d):
    alphabet = " ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'.,"
    resultat = ""
    s = str.upper(s)

    for lettre in s:
        
        if alphabet.find(lettre):
            position = alphabet.find(lettre)

            if position != 37 and position != 38 and position != 39:
                indice = position + d 

                if indice < 0 :
                    indice = indice % 26 

                if indice < 27 and position > 26  :
                    indice = indice + 10 
            else :
                indice = position

            resultat += alphabet[indice] 
        else :
            resultat += ' ' 

    return resultat