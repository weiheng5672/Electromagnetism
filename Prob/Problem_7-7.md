
**Problem 7.7**  
A metal bar of mass $m$ slides frictionlessly on two parallel conducting rails a distance $l$ apart (Fig. 7.17). 

A resistor $R$ is connected across the rails, and a uniform magnetic field $B$, pointing into the page, fills the entire region.

![Figure 7.17](Figs/FIGURE%207.17.png)

(a) If the bar moves to the right at speed $v$, what is the current in the resistor? In what direction does it flow?  
(b) What is the magnetic force on the bar? In what direction?  
(c) If the bar starts out with speed $v_0$ at time $t = 0$, and is left to slide, what is its speed at a later time $t$?  
(d) The initial kinetic energy of the bar was, of course, $\frac{1}{2} m v_0^2$. Check that the energy delivered to the resistor is exactly $\frac{1}{2} m v_0^2$.

解：
(a)
根據右手定則，電流是逆時針方向

在電阻的部分是自上而下

$$
\mathcal{E} = vBl
$$

$$
i = \frac{vBl}{R}
$$

(b)
電流在bar的方向是向上，右手定則，磁力向左

$$
F_{\text{磁}} = ilB = \frac{vB^2l^2}{R}
$$

(c)
力是變力，電阻會讓電流會越來越小，力也會越來越小

但運動學公式依然是 $F=ma$

$$
-\frac{vB^2l^2}{R} = m \frac{dv}{dt}
$$

$$
-\frac{B^2l^2}{mR}dt = \frac{dv}{v}
$$

$$
ln(v) = -\frac{B^2l^2}{mR}t+C
$$

$$
v = Ae^{-\frac{B^2l^2}{mR}t}   
$$

$v(0) = v_0 = A$

$$
v = v_0e^{-\frac{B^2l^2}{mR}t}   
$$

(d)

$$
i = \frac{vBl}{R} = \frac{Bl}{R} v_0e^{-\frac{B^2l^2}{mR}t}
$$

$$
\int_{0}^{\infty} i^2R\,dt = \int_{0}^{\infty} \frac{B^2l^2}{R} v_0^2e^{-\frac{2B^2l^2}{mR}t}\,dt
$$

$$
= \frac{B^2l^2v_0^2}{R}\int_{0}^{\infty} e^{-\frac{2B^2l^2}{mR}t}\,dt
$$

$$
= \frac{B^2l^2v_0^2}{R} \left[ -\frac{mR}{2B^2l^2} e^{-\frac{2B^2l^2}{mR}t} \right]_{0}^{\infty} 
$$

$$
= \frac{mv_0^2}{2} \left[ - e^{-\frac{2B^2l^2}{mR}t} \right]_{0}^{\infty} 
$$

$$
= \frac{mv_0^2}{2} \left[ 0 - (-1) \right] = \frac{1}{2}mv_0^2
$$