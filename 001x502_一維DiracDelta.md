
### The One-Dimensional Dirac Delta Function  

The one-dimensional Dirac delta function, $\delta(x)$, can be pictured as an infinitely high, infinitesimally narrow “spike,” with area 1 (Fig. 1.45). 

![Figure 1.45](Figs/FIGURE%201.45.png)

That is to say:  
$$
\delta(x) =
\begin{cases} 
0, & \text{if } x \neq 0 \\ 
\infty, & \text{if } x = 0 
\end{cases}
$$
and
$$
\int_{-\infty}^{\infty} \delta(x) \, dx = 1.
$$

Technically, $\delta(x)$ is not a function at all, since its value is not finite at $x = 0$; in the mathematical literature, it is known as a generalized function or distribution. 

It is, if you like, the limit of a sequence of functions, such as rectangles $R_n(x)$, of height $n$ and width $1/n$, or isosceles triangles $T_n(x)$, of height $n$ and base $2/n$ (Fig. 1.46).  

![Figure 1.46](Figs/FIGURE%201.46.png)

If $f(x)$ is some “ordinary” function (that is, not another delta function—in fact, just to be on the safe side, let’s say that $f(x)$ is continuous), then the product $f(x) \delta(x)$ is zero everywhere except at $x = 0$. It follows that  
$$
f(x) \delta(x) = f(0) \delta(x) \tag{1.88}
$$

(This is the most important fact about the delta function, so make sure you understand why it is true: since the product is zero anyway except at $x = 0$, we may as well replace $f(x)$ by the value it assumes at the origin.) 

In particular,  
$$
\int_{-\infty}^{\infty} f(x) \delta(x) \, dx
$$

$$
= f(0) \int_{-\infty}^{\infty} \delta(x) \, dx = f(0) \tag{1.89}
$$

Under an integral, then, the delta function “picks out” the value of $f(x)$ at $x = 0$. 

(Here and below, the integral need not run from $-\infty$ to $+\infty$; it is sufficient that the domain extend across the delta function, and $-\epsilon$ to $+\epsilon$ would do as well.)  

Of course, we can shift the spike from $x = 0$ to some other point, $x = a$ (Fig. 1.47):  

![Figure 1.47](Figs/FIGURE%201.47.png)

$$
\delta(x - a) =
\begin{cases} 
0, & \text{if } x \neq a \\ 
\infty, & \text{if } x = a 
\end{cases}
$$
with  
$$
\int_{-\infty}^{\infty} \delta(x - a) \, dx = 1
$$

Equation (1.88) becomes  
$$
f(x) \delta(x - a) = f(a) \delta(x - a)
$$

and Eq. (1.89) generalizes to  
$$
\int_{-\infty}^{\infty} f(x) \delta(x - a) \, dx = f(a)
$$