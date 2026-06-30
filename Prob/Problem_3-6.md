### 習題3-5

使用格林恆等式證明 靜電學第二唯一性定理

### 證

靜電學第二唯一性定理 是給定導體上的總帶電量已知

這些導體 扮演 邊界的角色

而他們的電位 不是已知條件


其實 格林恆等式 可以說是 微積分基本定理 的 進階形式

微積分基本定理 的內涵就是 

函數導數 對一個區域的積分結果 可以由 函數在邊界的值決定

一維

$$
\int_{a}^{b} \frac{df}{dx} dx = f(b) - f(a)
$$

三維
梯度 積分區域是線段 邊界是頭尾兩點

$$
\int_{\vec{a}}^{\vec{b}} \nabla V \cdot dl = V(\vec{b}) - V(\vec{a})
$$

散度 積分區域是體積 邊界是面積

$$
\int_V \nabla \cdot E dv = \oint_S E\cdot ds
$$

旋度 積分區域是面積 邊界是迴路

$$
\int_S \nabla \times E \cdot ds = \oint_L E\cdot dl
$$


格林定理 則是其中 散度基本定理的一個推廣
有兩個純量場 T U

$$
\nabla \cdot(T\nabla U )
$$

$$
= \nabla T \cdot \nabla U + T\nabla^2 U
$$



$$
\int_V \nabla \cdot(T\nabla U) dv = \int_V (\nabla T \cdot \nabla U + T\nabla^2 U) dv
$$

$$
\oint_S (T\nabla U) \cdot ds = \int_V (\nabla T \cdot \nabla U + T\nabla^2 U) dv
$$

這就是格林恆等式
注意 這裡的 東西 複雜 但核心還是
函數的導數 對一個區域的積分結果 可以由 函數在邊界的值決定

令 $U = T = V_{3}$

$$
\oint_S (V_{3}\nabla V_{3}) \cdot ds = \int_V (\nabla V_{3} \cdot \nabla V_{3} + V_{3}\nabla^2 V_{3}) dv
$$

$$
\nabla^2 V_{3} = 0
$$

$$
= \int_V \nabla V_{3} \cdot \nabla V_{3}  dv =  \int_V E_{3}^{2}  dv
$$

$$
-\oint_S (V_{3}E_{3}) \cdot ds =  \int_V E_{3}^{2}  dv
$$

後續和課文中一樣

這種方式好處就是 明確有個工具

課文中的方式 就是一種技巧性的作法 
