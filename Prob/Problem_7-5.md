**Problem 7.5**  
A battery of emf $\mathcal{E}$ and internal resistance $r$ is hooked up to a variable “load” resistance, $R$. 

If you want to deliver the maximum possible power to the load, what resistance $R$ should you choose? 

(You can’t change $\mathcal{E}$ and $r$, of course.)

解：

$$
i = \frac{\mathcal{E}}{r+R}
$$

$$
P = i^2R = \frac{\mathcal{E}^2R}{(r+R)^2}
$$

$$
\frac{d}{dR}P = \frac{d}{dR} \left[\frac{\mathcal{E}^2R}{(r+R)^2}\right] 
$$

$$
=\frac{ \mathcal{E}^2 (r+R)^2 - 2\mathcal{E}^2R (r+R)}{(r+R)^4} =0
$$

看分子就可以
$$
(r+R)^2 - 2R (r+R) = 0
$$

$$
(r+R) - 2R = 0
$$

$$
R = r
$$

也就是說當外部電阻等於電源內阻時，有最大功率輸出