# score1 =0 + score1 du joueur  =Score1    if score1 >100 score1=0    else if score1 <50   score1=0
# garder que le meilleur score if score0 < score0/ score = score0/     if score > score0/  score = score0 
# class player sert a savoir qui joue et a calculer le score final ainsi que le score total
# class player def score pour savoir le score de chaque personne sur chaque chanson
# class player deff pour savoir qui a gagné avec LE score le plus haut (calculer parmis tout les scores des joueurs le plus haut puis parmis cela le plus haut de tout les joueurs pour obtenir le gagnant) 
# class karaoke sert a recuperer les scores des chansons des joueurs 
# class karaoke recuperer tout les scores de chaque chanson puis calculer le meilleur score sur chaque chanson et dire qui a fait ce score
# savoir quelle joueur a fait le meilleur score sur chaque chanson (if score player1 > score player(len)...)
# savoir quelle joueur a était le plus constant (tout les chanson/par le nombre de chanson)
# qui a le meilleur score total
#  
#
#
#
#
#



scoretotal = 0
score = 0
Point0 = 0 # + score0
Point1 = 0 # + score1
Point2 = 0 # + score2
Point3 = 0 # + score3
Point4 = 0 # + score4


class Player:
    def __init__ (self,nom,song0,song1,song2,song3,song4,scorefinal,scoretotal):    
        self.nom = "name"
        self.song0 = "Point0"
        self.song1 = "Point1"
        self.song2 = "Point2"
        self.song3 = "Point3"
        self.song4 = "Point4"
        self.scorefinal = "Score"
        self.scoretotal = "Scoretotal"  

    def Score0(self):
        Point0+self.__score0
    def Score1(self):
        Point1+self.__score1
    def Score2(self):
        Point2+self.__score2
    def Score3(self):
        Point3+self.__score3
    def Score4(self):
        Point4+self.__score4                                

    def getScore(self):
        if Point0>Point1 & Point0>Point2 & Point0>Point3 & Point0>Point4 :
            score=Point0
        if Point1>Point0 & Point1>Point2 & Point1>Point3 & Point1>Point4 :
            score=Point1
        if Point2>Point0 & Point2>Point1 & Point2>Point3 & Point2>Point4 :
            score=Point2    
        if Point3>Point0 & Point3>Point1 & Point3>Point2 & Point3>Point4 :
            score=Point3
        if Point4>Point0 & Point4>Point1 & Point4>Point2 & Point4>Point3 :
            score=Point4        
    def getScoretotal(self):
        scoretotal== scoretotal + Point0 + Point1 + Point2 + Point3 + Point4




class Karaoke:
    def __init__ (self,score0,score1,score2,score3,score4,best0,best1,best2,best3,best4):
        self.score0 = "score0"
        self.score1 = "score1"
        self.score2 = "score2"
        self.score3 = "score3"
        self.score4 = "score4"
        best0="best0"
        best1="best1"
        best2="best2"
        best3="best3"
        best4="best4"
        
        
#        def best0():
#            if score0 Player1> score Player(len)
#                best0= Player1
#            if score0 Player2> score Player(len)
#                best0= Player2
#            if score0 Player3> score Player(len)
#                best0= Player3
#            if score0 Player4> score Player(len)
#                best0= Player4
#        def best1():
#            if score1 Player1> score Player(len)
#                best1= Player1
#            if score1 Player2> score Player(len)
#                best1= Player2
#            if score1 Player3> score Player(len)
#                best1= Player3
#            if score1 Player4> score Player(len)
#                best1= Player4      
#        def best2():
#            if score2 Player1> score Player(len)
#                best2= Player1
#            if score2 Player2> score Player(len)
#                best2= Player2
#            if score2 Player3> score Player(len)
#                best2= Player3
#            if score2 Player4> score Player(len)
#                best2= Player4    
#        def best3():
#            if score3 Player1> score Player(len)
#                best3= Player1
#            if score3 Player2> score Player(len)
#                best3= Player2
#            if score3 Player3> score Player(len)
#                best3= Player3
#            if score3 Player4> score Player(len)
#                best3= Player4
#        def best4():
#            if score4 Player1> score Player(len)
#                best4= Player1
#            if score4 Player2> score Player(len)
#                best4= Player2
#            if score4 Player3> score Player(len)
#                best4= Player3
#            if score4 Player4> score Player(len)
#                best4= Player4                                              




Robert=Player("Robert",0,0,0,0,0,0,0[Karaoke(60,57,94,68,76)])   
Roberta=Player("Roberta",0,0,0,0,0,0,0[Karaoke(59,73,64,85,78,)])
Roberto=Player("Roberto",0,0,0,0,0,0,0[Karaoke(94,64,70,97,53)])
Robertine=Player("Robertine",0,0,0,0,0,0,0[Karaoke(84,67,59,85,98)])
    