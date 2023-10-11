
#initialize board size
rows, cols = (35,35)
tab = [[0 for i in range(cols)] for j in range(rows)]

#fix board boarders
for i in range(cols):
    tab[0][i]='_'
    tab[(rows-1)][i]='_'
for j in range(rows):
    tab[j][0]='_'
    tab[j][(cols-1)]='_'

# initialize start point for each players
startPointJ1=(17,1)
startPointJ2=(1,17)
startPointJ3=(17,rows-2)
startPointJ4=(cols-2,17)

#= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =

# function : print board in terminal
def affichage(tab):
    for i in range(cols):
        for j in range(rows):
            if tab[i][j]==0:
                print(". ",end="")
            else :
                print(str(tab[i][j])+" ",end="")
        print()

# function: check if the case are available, add a mouve markdown
def jouer(player,x,y,tab):
    if tab[x][y]==0 :
        tab[x][y]=player
        return True
    else:
        return False
    
def erase(player,tab):
    for i in range(rows):
        for j in range(cols):
            if tab[i][j]==player:
                tab[i][j]=0
    
    
#= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =

# print tab in terminal
affichage(tab)
