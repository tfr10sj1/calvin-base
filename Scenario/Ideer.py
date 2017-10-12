 just nu är det om en actor har full action kö (buffert) då shemaläggaren avbryter och börjar om och anropar shuffle som är inte så smart för att den byter till annan actor, men den vet inte om den nya actorn har full kö eller ej. 
 man vill göra är att kolla på alla actorer som är registrerade i ett program och se vilka som har tumma köer då väljer man de istället.
 
 En ide är att actorer kommunicerar med varandra via någonsårts kommunication utan att ta mycket tid och informera om hur mycket är kvar i sina buffert, 
 En annan ide är att varie actor kommunicerar med scemaläggaren och säga vad den har kvar i bufferten, schemaläggare håller koll på vilken actorskö kommer snart bli full och vilken som har den tum så kan sckeduler byta direkt.



csviz --script scenario2.calvin | dot -Tpdf >scenario2.pdf
evince scenario2.pdf