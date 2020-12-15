def hamiltonian( spins, H, D ) :
  energy = 0
  # Your code goes here
  avspin = sum(spins) / len(spins) 
  for s in spins : energy = energy - (H+2*D*avspin)*s 
  return energy 
  
allup, alldown = 8*[1], 8*[-1]
print( "ENERGY FOR ALL SPIN UP", hamiltonian( allup, 1, 2 ) )
print( "ENERGY FOR ALL SPIN DOWN", hamiltonian( alldown, 1, 3 ) )
