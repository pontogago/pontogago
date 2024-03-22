musica = """
I've always been the one to say the first goodbye
Had to love and lose a hundred million times
Had to get it wrong to know just what I like
Now I'm falling
You say my name like I have never heard before
I'm indecisive, but, this time, I know for sure
I hope I'm not the only one that feels it all
Are you falling?
Centre of attention
You know you can get whatever you want from me
Whenever you want it, baby
It's you in my reflection
I'm afraid of all the things you could do to me
If I would've known it, baby
I would've stayed at home
'Cause I was doing better alone
But when you said: Hello
I knew that was the end of it all
I should've stayed at home
'Cause now there ain't no letting you go
Am I falling in love with the one that could break my heart?
Oh no, I was doing better alone
But when you said: Hello
I knew that was the end of it all
I should've stayed at home
'Cause now there ain't no letting you go
Am I falling in love with the one that could break my heart?
I wonder, when you go, if I stay on your mind
Two can play that game, but you win me every time
Everyone before you was a waste of time
Yeah, you got me
Centre of attention
You know you can get whatever you want from me
Whenever you want it, baby
It's you in my reflection
I'm afraid of all the things you could do to me
If I would've known it, baby
I would've stayed at home
'Cause I was doing better alone
But when you said: Hello
I knew that was the end of it all
I should've stayed at home
'Cause now there ain't no letting you go
Am I falling in love with the one that could break my heart?
Oh no, I was doing better alone
But when you said: Hello
I knew that was the end of it all
I should've stayed at home
'Cause now there ain't no letting you go
Am I falling in love with the one that could break my heart?
Ooh, break my heart
Ooh, break my heart
Ooh
Am I falling in love with the one that could break my heart?
I would've stayed at home
'Cause I was doing better alone
But when you said: Hello
I knew that was the end of it all
I should've stayed at home (I would've stayed at home 'cause I–)
'Cause now there ain't no letting you go
Am I falling in love with the one that could break my heart?
Oh no (oh no), I was doing better alone
But when you said: Hello
I knew that was the end of it all
I should've stayed at home
'Cause now there ain't no letting you go
Am I falling in love with the one that could break my heart?"""

# Substituir todas as quebras de linha por '\n'
musica = musica.replace('\r\n', '\n').replace('\r', '\n')

# Dividir a música em uma lista de versos
versos = musica.split('\n')

# Iniciar um contador para verificar a cada duas linhas
contador = 0

# Iterar através da lista de versos
for verso in versos:
    # Verificar se o contador é par
    if contador % 2 == 0:
        # Se o contador for par, imprimir o verso e pular uma linha
        print(verso)
        print()
        print('##100')
    else:
        # Se o contador for ímpar, imprimir apenas o verso
        print(verso)
    
    # Incrementar o contador
    contador += 1
