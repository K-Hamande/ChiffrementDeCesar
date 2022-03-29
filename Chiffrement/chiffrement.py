def ChiffrementCesar(s, d):
    
     #recuperation des 26 lettres de l alphabet
     
    alphabet = " ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'.,"
    resultat = ""
    s = str.upper(s) 

    for lettre in s:
        
        if alphabet.find(lettre):
            
            #la position de chaque lettre du message a chiffré
            
            position = alphabet.find(lettre) 
            if position != 37 and position != 38 and position != 39:
                
                # addition de l'indice de chaque lettre du mots á chiffrer et de la clé de chiffrement 
                
                indice = position + d  

                if indice > 26 and indice < 30   :
                    indice = indice % 26 

                if indice >36    :
                    indice = indice % 36 + 26  
            else :
                indice = position 

            resultat += alphabet[indice] 
        else :
            resultat += ' ' 

    return resultat