# A mean field model
We will study the Ising model Hamiltonian that you have just learned to program in more detail in the exercises that follow.  Before we get on to that, however, we are going to learn an approximate Hamiltonian that we can use to study the behaviour of interacting Ising-like spins arranged on two or three dimensional, square lattices.  These higher-dimensionality lattices are obviously more interesting than the one-dimensional lattices that the spins were placed on in the previous exercise as they are closer to the structures found in real materials.

Recall that in our one-dimensional system each spin had two neighbours - one to the left on the ring and one to the right.  In two dimensions each spin, therefore, has four neighbours - one to the left, one to the right, one above and one below.  In three dimensions, by contrast, each spin has 6 neighbours, one left, one right, one above, one below, one in front and one behind.  In fact, and in general, in a D-dimensional space each spin has 2D neighbours.

In this exercise rather we are going to avoid working out which of our spins our neighbour by using the so-called mean-field approximation.  In this approximation, we assume that each of the neighbours of our spin has the average value for all the spins in the system.  In other words, the Hamiltonian for a system of N spins on a D dimensional lattice is:

![](https://render.githubusercontent.com/render/math?math=E=-\sum_{i=1}^N\left[\H%2B\frac{2D}{N}\sum_{j=1}^{N}s_j\right]s_i)

Modify the code in `main.py` so that the function called `hamiltonian` calculates the the quantity defined by the formula above.  Notice that this function takes a list called `spins`, which contains all the spin coordinates, a scalar variable called `H` that gives the magnetic field strength and a scalar variable called `D` that gives the dimension of the lattice.
