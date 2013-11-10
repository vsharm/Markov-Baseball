import numpy
from numpy import linalg
singles = 28438
doubles = 8222
triples = 772
hr = 4661
plateAppearences = 184872
walks = 14640

pSingle = singles/float(plateAppearences)
pDouble = doubles/float(plateAppearences)
pTriple = triples/float(plateAppearences)
pHR = hr/float(plateAppearences)
pOut = 1 - ((singles+doubles+triples+hr + walks)/float(plateAppearences))
pWalk = walks/float(plateAppearences)
pWalkSingle = (walks+singles)/float(plateAppearences)

pWalkSingleR = float(pWalk + (pSingle/2))
pSingleR = float(pSingle)/2
pDoubleR = float(pDouble)/2
pSingleRi = float(pSingle)/4
pWalkSingleRi = pWalk + float(pSingle)/4
pSingleRii = (3*pSingle)/4



print("Stats", pSingle, pDouble, pTriple, pHR, pWalkSingle, pOut, pWalk, (pSingle + pDouble + pTriple + pHR + pWalkSingle + pOut + pWalk))


transition = numpy.matrix([
                           [pHR,pWalkSingle,pDouble,pTriple,0,0,0,0,pOut,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                           [pHR,0,0,pTriple,pWalkSingle,0,pDouble,0,0,pOut,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                           [pHR,pSingle,pDouble,pTriple,pWalk,0,0,0,0,0,pOut,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                           [pHR,pSingle,pDouble,pTriple,0,pWalk,0,0,0,0,0,pOut,0,0,0,0,0,0,0,0,0,0,0,0,0],
                           [pHR,0,0,pTriple,pSingle,0,pDouble,pWalk,0,0,0,0,pOut,0,0,0,0,0,0,0,0,0,0,0,0],
                           [pHR,0,0,pTriple,pSingle,0,pDouble,pWalk,0,0,0,0,0,pOut,0,0,0,0,0,0,0,0,0,0,0],
                           [pHR,pSingle,pDouble,pTriple,0,0,0,pWalk,0,0,0,0,0,0,pOut,0,0,0,0,0,0,0,0,0,0],
                           [pHR,0,0,pTriple,pSingle,0,pDouble,pWalk,0,0,0,0,0,0,0,pOut,0,0,0,0,0,0,0,0,0],
                           [0,0,0,0,0,0,0,0,pHR,pWalkSingle,pDouble,pTriple,0,0,0,0,pOut,0,0,0,0,0,0,0,0],
                           [0,0,0,0,0,0,0,0,pHR,0,0,pTriple,pWalkSingle,0,pDouble,0,0,pOut,0,0,0,0,0,0,0],
                           [0,0,0,0,0,0,0,0,pHR,pSingle,pDouble,pTriple,pWalk,0,0,0,0,0,pOut,0,0,0,0,0,0],
                           [0,0,0,0,0,0,0,0,pHR,pSingle,pDouble,pTriple,0,pWalk,0,0,0,0,0,pOut,0,0,0,0,0],
                           [0,0,0,0,0,0,0,0,pHR,0,0,pTriple,pSingle,0,pDouble,pWalk,0,0,0,0,pOut,0,0,0,0],
                           [0,0,0,0,0,0,0,0,pHR,0,0,pTriple,pSingle,0,pDouble,pWalk,0,0,0,0,0,pOut,0,0,0],
                           [0,0,0,0,0,0,0,0,pHR,pSingle,pDouble,pTriple,0,0,0,pWalk,0,0,0,0,0,0,pOut,0,0],
                           [0,0,0,0,0,0,0,0,pHR,0,0,pTriple,pSingle,0,pDouble,pWalk,0,0,0,0,0,0,0,pOut,0],
                           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,pHR,pWalkSingle,pDouble,pTriple,0,0,0,0,pOut],
                           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,pHR,0,0,pTriple,pWalkSingle,0,pDouble,0,pOut],
                           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,pHR,pSingle,pDouble,pTriple,pWalk,0,0,0,pOut],
                           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,pHR,pSingle,pDouble,pTriple,0,pWalk,0,0,pOut],
                           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,pHR,0,0,pTriple,pSingle,0,pDouble,pWalk,pOut],
                           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,pHR,0,0,pTriple,pSingle,0,pDouble,pWalk,pOut],
                           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,pHR,pSingle,pDouble,pTriple,0,0,0,pWalk,pOut],
                           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,pHR,0,0,pTriple,pSingle,0,pDouble,pWalk,pOut],
                           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]
                           ])

runVector  = numpy.matrix([
                           [pHR],
                           [2*pHR + pTriple],
                           [2*pHR + pSingle + pDouble + pTriple],
                           [2*pHR + pSingle + pDouble + pTriple],
                           [3*pHR + pSingle + pDouble + 2*pTriple],
                           [3*pHR + pSingle + pDouble + 2*pTriple],
                           [3*pHR + 2*pSingle + 2*pDouble + 2*pTriple],
                           [4*pHR + 2*pSingle + 2*pDouble + 3*pTriple + pWalk],
                           [pHR],
                           [2*pHR + pTriple],
                           [2*pHR + pSingle + pDouble + pTriple],
                           [2*pHR + pSingle + pDouble + pTriple],
                           [3*pHR + pSingle + pDouble + 2*pTriple],
                           [3*pHR + pSingle + pDouble + 2*pTriple],
                           [3*pHR + 2*pSingle + 2*pDouble + 2*pTriple],
                           [4*pHR + 2*pSingle + 2*pDouble + 3*pTriple + pWalk],
                           [pHR],
                           [2*pHR + pTriple],
                           [2*pHR + pSingle + pDouble + pTriple],
                           [2*pHR + pSingle + pDouble + pTriple],
                           [3*pHR + pSingle + pDouble + 2*pTriple],
                           [3*pHR + pSingle + pDouble + 2*pTriple],
                           [3*pHR + 2*pSingle + 2*pDouble + 2*pTriple],
                           [4*pHR + 2*pSingle + 2*pDouble + 3*pTriple + pWalk],
                           [0]
                           ])

resultMatrix = runVector
for z in  range(1,8):
    curentTransition = linalg.matrix_power(transition, z)
    tempMatrix = numpy.dot(curentTransition,runVector)
    resultMatrix = numpy.add(resultMatrix,tempMatrix)

print("resultMatrix")
print(resultMatrix)
