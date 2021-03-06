import nashpy as nash
import numpy as np

#From Vince Knight's Youtube Tutorial
#A = np.array([[1,1,-1],[2,-1,0]])
#B = np.array([[1/2,-1,-1/2],[-1,3,2]])

#From Vince Knight's Nashpy git repo
#A = np.array([[1,2],[3,0]])
#B = np.array([[0,2],[3,1]])

#From Wikipedia's an example of 1st Coordination Game
#A = np.array([[4,1],[3,2]])
#B = np.array([[4,3],[1,2]])

#From Wikipedia's an example of 2nd Coordination Game
#A = np.array([[10,0],[0,10]])
#B = np.array([[10,0],[0,10]])

#From Wikipedia's an example of 1st Competition Game
#A = np.array([[0,2,2,2],[-2,1,3,3],[-2,-1,2,4],[-2,-1,0,3]])
#B = np.array([[0,-2,-2,-2],[2,1,-1,-1],[2,3,2,0],[2,3,4,3]])

#From Wikipedia's an example of 2nd Competition Game
#A = np.array([[0,25,5],[40,0,5],[10,15,10]])
#B = np.array([[0,40,10],[25,0,15],[5,5,10]])

#From MOEA's Result_VARs.txt
#1 (max U(S1)) - 305: 0,388.85,86.45,46.1
#2 (min U(S2)) - 1199: 6,342.25,280.1,110.6
#3 (min U(S3)) - 899: 6,301.45,167.4,242.6
## Game of U(S1) - U(S2) - #Winner: 1 - 2
#A = np.array([[388.85,388.85,388.85],[342.25,342.25,342.25],[301.45,301.45,301.45]]) #U(S1)
#B = np.array([[86.45,280.1,167.4],[86.45,280.1,167.4],[86.45,280.1,167.4]]) #U(S2)
## Game of U(S2) - U(S3) - #Winner: 2 - 3
#A = np.array([[86.45,86.45,86.45],[280.1,280.1,280.1],[167.4,167.4,167.4]]) #U(S2)
#B = np.array([[46.1,11.0,242.6],[46.1,11.0,242.6],[46.1,11.0,242.6]]) #U(S3)
## Game of U(S1) - U(S3) - #Winner: 1 - 3
#A = np.array([[388.85,388.85,388.85],[342.25,342.25,342.25],[301.45,301.45,301.45]]) #U(S1)
#B = np.array([[46.1,11.0,242.6],[46.1,11.0,242.6],[46.1,11.0,242.6]]) #U(S3)
## Game of B - U(S1) - #Winner: 2 - 1 & 3 - 1
#A = np.array([[0,0,0],[6,6,6],[6,6,6]]) #B
#B = np.array([[388.85,342.25,301.45],[388.85,342.25,301.45],[388.85,342.25,301.45]]) #U(S1)
## Game of B - U(S2) - #Winner: 2 - 2 & 3 - 2
#A = np.array([[0,0,0],[6,6,6],[6,6,6]]) #B
#B = np.array([[86.45,280.1,167.4],[86.45,280.1,167.4],[86.45,280.1,167.4]]) #U(S2)
## Game of B - U(S3) - #Winner: 2 - 3 & 3 - 3
A = np.array([[0,0,0],[6,6,6],[6,6,6]]) #B
B = np.array([[46.1,11.0,242.6],[46.1,11.0,242.6],[46.1,11.0,242.6]]) #U(S3)

game = nash.Game(A, B)

print(game)

eqs = game.support_enumeration()

for eq in eqs:
    print(eq)