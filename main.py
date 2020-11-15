def hamiltonian( spins, H, D ) :
  energy = 0
  # Your code goes here
  
  return energy 
  
allup, alldown = 8*[1], 8*[-1]
print( "ENERGY FOR ALL SPIN UP", hamiltonian( allup, 1, 2 ) )
print( "ENERGY FOR ALL SPIN DOWN", hamiltonian( alldown, 1, 3 ) )
