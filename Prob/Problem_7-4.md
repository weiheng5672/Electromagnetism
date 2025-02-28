**Problem 7.4**  

Suppose the conductivity of the material separating the cylinders in Ex. 7.2 is not uniform; specifically, $\sigma(s) = \frac{k}{s}$, for some constant $k$. Find the resistance between the cylinders.  

**Hint:** Because $\sigma$ is a function of position, Eq. 7.5 does not hold, the charge density is not zero in the resistive medium, and $E$ does not go like $\frac{1}{s}$. But we do know that for steady currents, $I$ is the same across each cylindrical surface. Take it from there.

解:

在例題7-2中，作者是先根據高斯定律求出電場後，再利用歐姆定律。

提示中的公式7-5就是高斯定律求得的電場，這裡不再重複，因為這個習題中，導電度不再均勻，有淨電荷堆積，我們無法先用高斯定律求出電場。

但透過電荷守恆，電流 $I$ 必須總是一樣

$$
J = \frac{I}{2\pi sL} = \sigma E = \frac{k}{s} E
$$

$$
E = \frac{I}{2\pi kL}
$$

本習題刻意給定的不均勻導電度，剛好會使得電場是常數

$$
V = E(b-a) = \frac{I(b-a)}{2\pi kL}
$$

$$
R = \frac{V}{I} = \frac{b-a}{2\pi kL}
$$

這題給定不均勻導電度，看似讓問題變複雜，實際上由於給定的導電度是刻意設計過的，使得結果反而更簡單。