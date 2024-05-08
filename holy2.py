musica = """Jesus
És bem vindo neste lugar
Preparamos um altar
Podes vir
Jesus
Te convidamos para reinar
Preparamos um altar
Podes vir (yeah)
Não queremos só Tua visitação
Mas queremos que faça morada aqui
Pode vir
Pode vir, Jesus
Vem, vem
Vem, Tua noiva
Te espera
Com o coração em chamas
Vem
Oh, oh, vem
Não queremos só Tua visitação
Mas queremos que faça morada aqui
Podes vir, ó vem
Podes vir, Jesus, ô, ô, ô (Onde está a noiva do Cordeiro de Deus)
ô-uou
Vem, Tua noiva
Te espera
Com o coração em chamas
Vem
Tua noiva
Te espera
Com o coração em chamas
Vem (oh-oh-oh)
Jesus, vem, vem, o-o-ou
Jesus
Jesus, Te amo
Jesus
Nós Te amamos
Tua presença (ô, ô, ô)
Jesus
Jesus, Jesus, ô
Jesus
Amado noivo, yeah
Jesus
Nós Te amamos
Tua presença
Jesus
Jesus (Jesus)
Jesus, ô, ô
Jesus
Jesus
Nós Te amamos (amamos)
Amamos (Nós Te amamos) ô, ô
(Tua presença) Tua presença, yeah, yeah
Vem, vem
Vem, Tua noiva
Te espera
Com o coração em chamas
Vem (ôu)
Tua noiva
Te espera
Com o coração em chamas
Oh-oh-oh
Tua noiva, yeah, yeah
Te espera
(Te espera, Te espera) Meu coração em chamas
Vem, Tua noiva (Te espera, yeah, yeah)
Te espera (com um coração em chamas)
Com o coração
(Vamos falar esse Nome)
Jesus (amado meu)
Jesus
(Ninguém me toca como Tu)
Jesus
Te amo, Te amo
(Nós Te amamos)
(Tua presença) Jesus
Jesus (Jesus)
(Ninguém é como Tu, não)
(Jesus)
(Lindo, lindo és, Jesus)
(Jesus
Nós Te amamos
Tua presença)
(Jesus
Nós Te amamos
Tua presença)
(Jesus
Jesus
Jesus
Nós Te amamos
Tua presença)"""

# Substituir todas as quebras de linha por '\n'
musica = musica.replace('\r\n', '\n').replace('\r', '\n')

# Dividir a música em uma lista de versos
versos = musica.split('\n')

# Iniciar um contador para verificar a cada duas linhas
contador = 0

# Iterar através da lista de versos
with open('musica.txt', 'w') as arquivo:
    for verso in versos:
        # Verificar se o contador é par
        if contador % 2 == 0:
            # Se o contador for par, imprimir o verso e pular uma linha
            arquivo.write(verso+'\n')
            arquivo.write('\n')
            arquivo.write("##100\n")

        else:
            # Se o contador for ímpar, imprimir apenas o verso
            arquivo.write(verso+'\n')
        
        # Incrementar o contador
        contador += 1
