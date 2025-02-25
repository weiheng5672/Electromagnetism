
(e)

proof

$$
\int_S \nabla T \times d\vec{a} = - \oint_P T \, d\vec{l}
$$

[Hint: Let $\vec{v} = \vec{c} \, T$ in Stokes’ theorem.]

可以看到題目中的 $T = T(x,y,z)$ 是純量場，不是常數

提示中的 $\vec{c}$ 是常數向量

也就是說，$\vec{v} = T(x,y,z) \, \vec{c}$

$$
\nabla \times \left( T \, \vec{c} \right) = \nabla T \times \vec{c} + T \nabla \times \vec{c}
$$

由於 $\vec{c}$ 是常數向量，$\nabla \times \vec{c} = \vec{0} $

兩邊同時對 $S$ 面積分

$$
\int_S \nabla \times \left( T \, \vec{c} \right) \cdot d\vec{a} =\int_S \nabla T \times \vec{c}\cdot d\vec{a} 
$$

等號左邊

$$
\int_S \nabla \times \left( T \, \vec{c} \right) \cdot d\vec{a} = \oint_P T \, \vec{c} \cdot d\vec{l} 
$$

$$
= \vec{c}  \cdot \oint_P T \, d\vec{l} 
$$

等號右邊

$$
\int_S \nabla T \times \vec{c}\cdot d\vec{a} = - \int_S \nabla T \times d\vec{a} \cdot  \vec{c}
$$

$$
= - \vec{c} \cdot \int_S \nabla T \times d\vec{a}
$$

綜上所述

$$
\int_S \nabla T \times d\vec{a} = - \oint_P T \, d\vec{l} 
$$