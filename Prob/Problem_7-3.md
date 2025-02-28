**Problem 7.3**  

(a) Two metal objects are embedded in weakly conducting material of conductivity $\sigma$ (Fig. 7.6). Show that the resistance between them is related to the capacitance of the arrangement by  
$$
R = \frac{\epsilon_0}{\sigma C}
$$

(b) Suppose you connected a battery between 1 and 2, and charged them up to a potential difference $V_0$. If you then disconnect the battery, the charge will gradually leak off. Show that $V(t) = V_0 e^{-t / \tau}$, and find the time constant $\tau$ in terms of $\epsilon_0$ and $\sigma$.

解：
(a)
我沒有附圖，也不需要，只需要知道是相當一般性，任意的形狀

原則還是一樣，利用電荷守恆，電流 $I$ 必須總是相等

$$
I = \int_A \vec{J} \cdot d\vec{a} = \sigma\int_A \vec{E} \cdot d\vec{a}
$$

關鍵在於我的這個 $A$，要取包圍其中一個金屬物體的封閉曲面，此時根據高斯定律

$$
\int_A \vec{E} \cdot d\vec{a} = \frac{Q}{\varepsilon_0}
$$

$$
Q = \varepsilon_0 \int_A \vec{E} \cdot d\vec{a}
$$

$$
V = V_2 - V_1 = -\int_{1}^{2} \vec{E} \cdot d\vec{l}
$$

$$
R = \frac{V}{I} = \frac{ -\int_{1}^{2} \vec{E} \cdot d\vec{l}}{\sigma\int_A \vec{E} \cdot d\vec{a}}
$$

$$
C = \frac{Q}{V} =  \frac{\varepsilon_0 \int_A \vec{E} \cdot d\vec{a}}{-\int_{1}^{2} \vec{E} \cdot d\vec{l}}
$$

$$
RC = \frac{ -\int_{1}^{2} \vec{E} \cdot d\vec{l}}{\sigma\int_A \vec{E} \cdot d\vec{a}} \times\frac{\varepsilon_0 \int_A \vec{E} \cdot d\vec{a}}{-\int_{1}^{2} \vec{E} \cdot d\vec{l}} = \frac{\varepsilon_0}{\sigma}
$$

(b)
按題意，就只是個RC放電迴路，時間常數 
$$
\tau = RC = \frac{\varepsilon_0}{\sigma}
$$
