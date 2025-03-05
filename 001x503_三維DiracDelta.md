
### The Three-Dimensional Delta Function  

It is easy to generalize the delta function to three dimensions:  
$$
\delta^3 (\mathbf{r}) = \delta(x) \delta(y) \delta(z)
$$

(As always, $\mathbf{r} \equiv x \hat{\mathbf{x}} + y \hat{\mathbf{y}} + z \hat{\mathbf{z}}$ is the position vector, extending from the origin to the point $(x, y, z)$.) 

This three-dimensional delta function is zero everywhere except at $(0,0,0)$, where it blows up. 

Its volume integral is 1:
$$
\int_{\text{all space}} \delta^3 (\mathbf{r}) \, d\tau
$$

$$
=\int_{-\infty}^{\infty} \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} \delta(x) \delta(y) \delta(z) \,dx\,dy\,dz = 1
$$

And, generalizing Eq. (1.92),  
$$
\int_{\text{all space}} f(\mathbf{r}) \delta^3 (\mathbf{r} - \mathbf{a}) \, d\tau = f(\mathbf{a})
$$

As in the one-dimensional case, integration with $\delta$ picks out the value of the function $f$ at the location of the spike.  

We are now in a position to resolve the paradox introduced in Sect. 1.5.1. 

As you will recall, we found that the divergence of $\frac{\hat{\mathbf{r}}}{r^2}$ is zero everywhere except at the origin, and yet its integral over any volume containing the origin is a constant (to wit: $4\pi$). 

These are precisely the defining conditions for the Dirac delta function; evidently,
$$
\nabla \cdot \left( \frac{\hat{\mathbf{r}}}{r^2} \right) = 4\pi \delta^3 (\mathbf{r})
$$

More generally,
$$
\nabla \cdot \left( \frac{\hat{\gamma}}{\gamma^2} \right) = 4\pi \delta^3 (\vec{\gamma})
$$

where, as always, $\vec{\gamma}$ is the separation vector: 

$\vec{\gamma} = \mathbf{r} - \mathbf{r'} \quad \gamma = |\mathbf{r} - \mathbf{r'}|$

Note that differentiation here is with respect to $\mathbf{r}$, while $\mathbf{r'}$ is held constant. 

Incidentally, since
$$
\nabla \left( \frac{1}{r} \right) = -\frac{\hat{\mathbf{r}}}{r^2}
$$

(Prob. 1.13b), it follows that  
$$
\nabla^2 \frac{1}{r} = -4\pi \delta^3 (\mathbf{r})
$$
