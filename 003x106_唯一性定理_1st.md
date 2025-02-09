### Boundary Conditions and Uniqueness Theorems

- Laplace’s equation does not by itself determine \( V \); 
  - in addition, suitable boundary conditions must be supplied. 

- This raises a delicate question: 
  - What are appropriate boundary conditions, 
  - sufficient to determine the answer 
  - and yet not so strong as to generate inconsistencies? 

- The one-dimensional case is easy, 
  - for here the general solution \( V = mx + b \) contains two arbitrary constants, 
  - and we therefore require two boundary conditions. 
  - We might, for instance, specify the value of the function at each end, 
  - or we might give the value of the function and its derivative at one end, 
  - or the value at one end and the derivative at the other, and so on. 
  - But we **cannot** get away with just the value or just the derivative at one end—
    - this is insufficient information. 
  - **Nor** would it do to specify the derivatives at both ends—
    - this would either be redundant (if the two are equal) 
    - or inconsistent (if they are not).

- In two or three dimensions we are confronted by a partial differential equation, 
  - and it is not so obvious what would constitute acceptable boundary conditions. 
  - Is the shape of a taut rubber membrane, for instance, uniquely determined by the frame over which it is stretched, 
  - or, like a canning jar lid, can it snap from one stable configuration to another? 
  - The answer, as I think your intuition would suggest, is that \( V \) is uniquely determined by its value at the boundary 
    - (canning jars evidently do not obey Laplace’s equation). 
  - However, other boundary conditions can also be used (see Prob. 3.5).
 
- The proof that a proposed set of boundary conditions will suffice is usually presented in the form of a uniqueness theorem. 
- There are many such theorems for electrostatics, all sharing the same basic format—
- I’ll show you the two most useful ones.

**First uniqueness theorem**: 

- The solution to Laplace’s equation in some volume \( V \) is uniquely determined 
  - if \( V \) is specified on the boundary surface \( S \).

**Proof**: 

- Suppose there were two solutions to Laplace’s equation: 
  
\[ 
\nabla^2 V_1 = 0  \quad and \quad  \nabla^2 V_2 = 0 
\]

- both of which assume the specified value on the surface. 
- I want to prove that they must be equal. 
- The trick is to look at their difference:
 
\[ V_3 \equiv V_1 - V_2 \]

- This obeys Laplace’s equation, 

\[ \nabla^2 V_3 = \nabla^2 V_1 - \nabla^2 V_2 = 0 \]

- and it takes the value zero on all boundaries 
  - (since \( V_1 \) and \( V_2 \) are equal there). 
- But Laplace’s equation allows no local maxima or minima—
  - all extrema occur on the boundaries. 
- So the maximum and minimum of \( V_3 \) are both zero. 
- Therefore, \( V_3 \) must be zero everywhere, and hence 

\[ V_1 = V_2 \]