#!/usr/bin/python
# filename: invit.py
def InvIteration(A,L,Lambda):
   """An implementation of the inverse iteration to calculate eigenvectors of near-by eigenvalues

   PARAMETERS
   __________
   A:  (nxn) is the matrix the eigenvectors have to be calculated for
   L:  (nxm) m<n: matrix of initial eigenvectors (can be random) which have to be calculated
   Lambda: (m) vector of near-by eigenvalues referring to the eigenvectors which are known

   """
   for i in range(len(L)):
      if np.linalg.cond(A)>10000:     #threshold can be changed; it is a unreasoned guess
	 continue
      A_1=np.linalg.inv(A)	      # this can be not that stable if cond(A) is big; than change the algorithm
      tmp=L[i]-L[i]
      loops=0
      #if eigenvalues are close to each other: increase theshold of loops
      while np.linalg.norm(tmp-L[i],ord=np.inf)>0.001 and loops<12: 
	 tmp=deepcopy(L[i])
	 L[i]=(A_1.dot(L[i].T).T/np.linalg.norm(A_1.dot(L[i].T)))[:].T
	 loops+=1
   return L

version=1.0

# End of invit.py
