
Problem 1.49: 

Evaluate the integral  
$$
J = \int_V e^{-r} \nabla \cdot \left( \frac{\hat{r}}{r^2} \right) d\tau
$$
where $V$ is a sphere of radius $R$, centered at the origin, using two different methods.

(1)

$$
\int_V e^{-r} \nabla \cdot \left( \frac{\hat{r}}{r^2} \right) d\tau
$$

$$
= \int_V e^{-r} 4\pi \delta^3(\vec{r}) d\tau
$$

$$
= e^{-0} 4\pi \int_V  \delta^3(\vec{r}) d\tau = 4\pi
$$

(2)

$$
\nabla \cdot \left(e^{-r}\frac{\hat{r}}{r^2} \right)
$$

$$
= \nabla e^{-r} \cdot \left(\frac{\hat{r}}{r^2} \right) +  \left(e^{-r}\nabla \cdot\frac{\hat{r}}{r^2} \right)
$$

$$
\left(e^{-r}\nabla \cdot\frac{\hat{r}}{r^2} \right)
$$

$$
= \nabla \cdot \left(e^{-r}\frac{\hat{r}}{r^2} \right) - \nabla e^{-r} \cdot \left(\frac{\hat{r}}{r^2} \right)
$$

$$
\int_V e^{-r} \nabla \cdot \left( \frac{\hat{r}}{r^2} \right) d\tau
$$

$$
=\int_V \nabla \cdot \left(e^{-r}\frac{\hat{r}}{r^2} \right)d\tau - \int_V\nabla e^{-r} \cdot \left(\frac{\hat{r}}{r^2} \right) d\tau
$$

$$
=\oint_{\partial V} e^{-r}\frac{\hat{r}}{r^2} \cdot d\vec{a} - \int_V -e^{-r}\hat{r} \cdot \left(\frac{\hat{r}}{r^2} \right) d\tau
$$

$$
=\frac{e^{-R}}{R^2}  \oint_{\partial V} \hat{r} \cdot d\vec{a} + \int_V \frac{e^{-r}}{r^2}  d\tau
$$

$$
=\frac{e^{-R}}{R^2}\,4\pi R^2 + \int_{0}^{R} \frac{e^{-r}}{r^2}4\pi r^2dr
$$

$$
=4\pi e^{-R} + 4\pi \int_{0}^{R} e^{-r} dr
$$

$$
=4\pi e^{-R} + 4\pi \left[ -e^{-r} \right]_{0}^{R}
$$

$$
=4\pi e^{-R} + 4\pi \left[ -e^{-R} - (-1) \right]
$$

$$
=4\pi e^{-R} - 4\pi e^{-R} + 4\pi
$$

$$
=4\pi
$$