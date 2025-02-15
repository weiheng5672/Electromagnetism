### 習題1-13

$$
\nabla\gamma = \nabla\sqrt{(x - x')^2 + (y - y')^2 + (z - z')^2}
$$

$$
\nabla\gamma =
\frac{\partial \gamma}{\partial x} \,\hat{\mathbf{x}} +
\frac{\partial \gamma}{\partial y} \,\hat{\mathbf{y}} +
\frac{\partial \gamma}{\partial z} \,\hat{\mathbf{z}} 
$$

$$
\frac{\partial \gamma}{\partial x} = \frac{1}{2} \cdot \frac{2(x - x')}{\sqrt{(x - x')^2 + (y - y')^2 + (z - z')^2}} 
$$

$$
= \frac{x - x'}{\sqrt{(x - x')^2 + (y - y')^2 + (z - z')^2}}
= \frac{x - x'}{\gamma}
$$

Similarly,  

$$
\frac{\partial \gamma}{\partial y} = 
\frac{y - y'}{\gamma}
\quad
\frac{\partial \gamma}{\partial z} = 
\frac{z - z'}{\gamma}
$$

Thus,
$$
\nabla \gamma =
\frac{x - x'}{\gamma} \hat{\mathbf{x}}+
\frac{y - y'}{\gamma} \hat{\mathbf{y}}+
\frac{z - z'}{\gamma} \hat{\mathbf{z}}
$$

$$
= \frac{\vec{\gamma}}{\gamma} = \hat{\gamma}
$$

(a)
$$
\nabla(\gamma^2) = \nabla \left[{(x - x')^2 + (y - y')^2 + (z - z')^2} \right]
$$

$$
\nabla(\gamma^2) =
\frac{\partial (\gamma^2)}{\partial x} \,\hat{\mathbf{x}} +
\frac{\partial (\gamma^2)}{\partial y} \,\hat{\mathbf{y}} +
\frac{\partial (\gamma^2)}{\partial z} \,\hat{\mathbf{z}} 
$$

$$
\frac{\partial (\gamma^2)}{\partial x} = 2(x - x')
$$

Similarly,  

$$
\frac{\partial (\gamma^2)}{\partial y} = 2(y - y')
\quad
\frac{\partial (\gamma^2)}{\partial z} = 2(z - z')
$$

Thus,
$$
\nabla (\gamma^2) =
2(x - x') \hat{\mathbf{x}}+
2(y - y') \hat{\mathbf{y}}+
2(z - z') \hat{\mathbf{z}}
$$

$$
= 2\vec{\gamma}
$$

或者，透過連鎖律

$$
\nabla(\gamma^2) = 2\gamma\,\nabla(\gamma)
$$

$$
= 2\gamma\,\hat{\gamma} = 2\vec{\gamma}
$$

(b)
$$
\nabla \left( \frac{1}{\gamma} \right) = \frac{-1}{\gamma^2}\,\nabla(\gamma) = \frac{-\hat{\gamma}}{\gamma^2}
$$

(c)
$$
\nabla \left( \gamma^n \right) = n\gamma^{n-1}\,\nabla(\gamma) = n\gamma^{n-1} \, \hat{\gamma}
$$

