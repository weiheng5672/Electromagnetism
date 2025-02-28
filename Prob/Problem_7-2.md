**Problem 7.2**  
A capacitor $C$ has been charged up to potential $V_0$; at time $t = 0$, it is connected to a resistor $R$, and begins to discharge.  

(a) Determine the charge on the capacitor as a function of time, $Q(t)$. What is the current through the resistor, $I(t)$?  

(b) What was the original energy stored in the capacitor? By integrating $i^2R$, confirm that the heat delivered to the resistor is equal to the energy lost by the capacitor.  

Now imagine charging up the capacitor, by connecting it (and the resistor) to a battery of voltage $V_0$, at time $t = 0$ .  

(c) Again, determine $Q(t)$ and $I(t)$.  

(d) Find the total energy output of the battery $\int V_0 I \, dt$. Determine the heat delivered to the resistor. What is the final energy stored in the capacitor? What fraction of the work done by the battery shows up as energy in the capacitor? [Notice that the answer is independent of $R$!]

解:

克西荷夫電壓定律

$$
v_C(t) + v_R(t) = 0
$$

電容公式有
$$
Q(t) = C\,v_C(t)
$$

$$
I(t) = \frac{dQ}{dt}= C\frac{dv_C}{dt}
$$

只有一個迴路，電流都一樣，$I(t)$ 不須下標註明，帶入克西荷夫電壓定律中的 $v_R = I(t)R$

$$
v_C(t) + RC\frac{dv_C}{dt} = 0
$$

令 $v_C(t)=v(t)=v$ 簡化符號的使用

$$
v(t) + RC\frac{dv}{dt} = 0
$$

變數分離

$$
\frac{dv}{v} = -\frac{dt}{RC}
$$

$$
\mathrm{ln}(v) = \frac{-t}{RC} + A
$$

$$
v(t) = B\mathrm{e}^{-t/RC}
$$

帶入初始條件，$v(0)=V_0$
$$
v(0) = B = V_0
$$

$$
v(t) = V_0\mathrm{e}^{-t/RC}
$$

$$
Q(t) = C\,v(t) = CV_0\mathrm{e}^{-t/RC}
$$

$$
I(t) = \frac{v(t)}{R}= \frac{V_0}{R}\mathrm{e}^{-t/RC} \tag{a}
$$

對Q微分得到的電流會差個負號，只是表示電流是流出電容而已

電容初始電壓為，$V_0$，能量為
$$
\frac{1}{2}CV_0
$$

電阻消耗掉的總能量
$$
\int_{0}^{\infty} I^2R\,dt = \int_{0}^{\infty} \frac{V_0^2}{R}\mathrm{e}^{-2t/RC} dt
$$

$$
=\frac{V_0^2}{R}\int_{0}^{\infty}\mathrm{e}^{-2t/RC}dt
$$

$$
=\frac{V_0^2}{R}  \left[ \frac{-RC}{2} \mathrm{e}^{-2t/RC} \right]_{0}^{\infty}
$$

$$
=\frac{V_0^2}{R}  \left[ 0-\frac{-RC}{2}  \right] = \frac{1}{2}CV_0 \tag{b}
$$

接下來想像上述的RC電路中，串連一個定電壓 $V_0$，並且電容從零開始充電，令電容電壓為，$v(t)=v$

$$
v(t) + RC\frac{dv}{dt} = V_0
$$

$$
\frac{dv}{v-V_0} = -\frac{dt}{RC}
$$

$$
\mathrm{ln}(v-V_0) = \frac{-t}{RC} + A
$$

$$
v(t) = V_0 + B\mathrm{e}^{-t/RC}
$$

帶入初始條件，$v(0) = V_0 + B =0$
$$
B = -V_0
$$

$$
v(t) = V_0\left[ 1 - \mathrm{e}^{-t/RC} \right]  
$$

$$
Q(t) = C\,v(t) = CV_0\left[ 1 - \mathrm{e}^{-t/RC} \right] 
$$

$$
I(t) = \frac{dQ}{dt}= \frac{V_0}{R}\mathrm{e}^{-t/RC} \tag{c}
$$

電池做的總功

$$
\int_{0}^{\infty} V_0I \, dt = \int_{0}^{\infty} \frac{V_0^2}{R}\mathrm{e}^{-t/RC} dt
$$

$$
=\frac{V_0^2}{R}\int_{0}^{\infty}\mathrm{e}^{-t/RC}dt
$$

$$
=\frac{V_0^2}{R}  \left[ -RC \mathrm{e}^{-t/RC} \right]_{0}^{\infty}
$$

$$
=\frac{V_0^2}{R}  \left[ 0-(-RC)  \right] = CV_0 \tag{d}
$$

驗證下此時電阻消耗的總能量
$$
\int_{0}^{\infty} I^2R\,dt = \int_{0}^{\infty} \frac{V_0^2}{R}\mathrm{e}^{-2t/RC} dt
$$

$$
=\frac{V_0^2}{R}\int_{0}^{\infty}\mathrm{e}^{-2t/RC}dt
$$

$$
=\frac{V_0^2}{R}  \left[ \frac{-RC}{2} \mathrm{e}^{-2t/RC} \right]_{0}^{\infty}
$$

$$
=\frac{V_0^2}{R}  \left[ 0-\frac{-RC}{2}  \right] = \frac{1}{2}CV_0
$$

和(b)一樣，畢竟電流都一樣，但我之所以重複，是因為儘管電流在兩種情況下電流曲線數學上相同，但能量的來源和去向不同

第一種是電容 $C$ 初始電壓 $V_0$，對 $R$ 放電

第二種是電容 $C$ 初始電壓 $0$，定電壓 $V_0$ 對 $RC$ 串聯電路充電

在第二種狀況，電池提供的能量 $CV_0^2$，其中一半儲存在電容中，另一半被電阻消耗掉。

充電過程總會損失一半的能量，而這個結果與 $R$ 無關。  

充電過程中，電流從最大值 $I_0 = V_0 / R$ 開始，隨時間衰減。

理想無電阻情況，電流無限大，電容瞬間充電，不會有能量損失。  

實際電路中，若要減少充電損耗，通常會使用電感輔助（如LC振盪電路），以便能量在電場與磁場間轉換，而非直接轉化為熱。