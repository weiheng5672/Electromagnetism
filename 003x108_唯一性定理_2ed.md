
---

**Conductors and the Second Uniqueness Theorem**

- The simplest way to set the boundary conditions 
  - for an electrostatic problem 
  - is to specify the value of \(V\) 
  - on all surfaces surrounding the region of interest. 

- And this situation often occurs in practice: 
  - In the laboratory, we have conductors connected to batteries, 
  - which maintain a given potential, 
  - or to ground, which is the experimentalist’s word for \(V = 0\). 

- However, there are other circumstances 
  - in which we do not know the potential at the boundary, 
  - but rather the charges on various conducting surfaces. 

- Suppose I put charge \(Q_a\) on the first conductor, \(Q_b\) on the second, and so on—
  - I’m not telling you how the charge distributes itself over each conducting surface, 
  - because as soon as I put it on, it moves around in a way I do not control. 

- And for good measure, 
  - let’s say there is some specified charge density \(\rho\) 
  - in the region between the conductors.

- Is the electric field now uniquely determined? (Yes)
- Or are there perhaps a number of different ways 
  - the charges could arrange themselves 
  - on their respective conductors, each leading to a different field? (No)

**Second Uniqueness Theorem:**  

- In a volume \(V\) 
  - surrounded by conductors 
  - and containing a specified charge density \(\rho\), 
- the electric field is uniquely determined 
  - if the total charge on each conductor is given. 
  - (The region as a whole can be bounded by another conductor, or else unbounded.)

**Proof:**

- Suppose there are two fields satisfying the conditions of the problem. 
- Both obey Gauss’s law in differential form in the space between the conductors:  
\[
\nabla \cdot \mathbf{E_1} = \frac{1}{\epsilon_0} \rho \quad and\quad \nabla \cdot \mathbf{E_2} = \frac{1}{\epsilon_0} \rho
\]
- And both obey Gauss’s law in integral form 
  - for a Gaussian surface enclosing each conductor:  
\[
\oint_{\text{ith conducting surface}} \mathbf{E_1} \cdot d\mathbf{a} = \frac{1}{\epsilon_0} Q_i 
\]
\[
\oint_{\text{ith conducting surface}} \mathbf{E_2} \cdot d\mathbf{a} = \frac{1}{\epsilon_0} Q_i
\]

- Likewise, for the outer boundary 
  - (whether this is just inside an enclosing conductor or at infinity):  
\[
\oint_{\text{outer boundary}} \mathbf{E_1} \cdot d\mathbf{a} = \frac{1}{\epsilon_0} Q_{\text{tot}}, \quad \oint_{\text{outer boundary}} \mathbf{E_2} \cdot d\mathbf{a} = \frac{1}{\epsilon_0} Q_{\text{tot}}
\]

- As before, we examine the difference \(\mathbf{E_3} \equiv \mathbf{E_1} - \mathbf{E_2}\), which obeys  
\[
\nabla \cdot \mathbf{E_3} = 0 \quad (1)
\]
in the region between the conductors, and  
\[
\oint \mathbf{E_3} \cdot d\mathbf{a} = 0 \quad (2)
\]
over each boundary surface.

- Now there is one final piece of information we must exploit: 
  - Although we do not know 
    - how the charge \(Q_i\) distributes itself over the \(i\)-th conductor, 
  - we do know that 
    - each conductor is an equipotential, 
- and hence \(V_3\) is a constant 
    - (not necessarily the same constant) over each conducting surface. 
    - (It need not be zero, for the potentials \(V_1\) and \(V_2\) may not be equal—
    - all we know for sure is that 
    - both are constant over any given conductor.)

- Next comes a trick. 
  - Invoking product rule, we find that  
\[
\nabla \cdot (V_3 \mathbf{E_3}) = V_3 (\nabla \cdot \mathbf{E_3}) + \mathbf{E_3} \cdot (\nabla V_3) = -(\mathbf{E_3})^2
\]
  - Here I have used Eq.(1), and \(\mathbf{E_3} = -\nabla V_3\). 
  - Integrating this over \(V\), and applying the divergence theorem to the left side:  
\[
\int_V \nabla \cdot (V_3 \mathbf{E_3}) d\tau = \oint_S V_3 \mathbf{E_3} \cdot d\mathbf{a} = - \int_V (\mathbf{E_3})^2 d\tau
\]
- The surface integral covers all boundaries of the region in question—
  - the conductors and outer boundary. 
- Now \(V_3\) is a constant over each surface 
  - (if the outer boundary is infinity, \(V_3 = 0\) there), 
  - so it comes outside each integral, and what remains is zero, according to Eq.(2). Therefore,  
\[
\int_V (\mathbf{E_3})^2 d\tau = 0
\]

- But this integrand is never negative; 
  - the only way the integral can vanish is if \(\mathbf{E_3} = 0\) everywhere. 
  - Consequently, \(\mathbf{E_1} = \mathbf{E_2}\), and the theorem is proved.

- This proof was not easy, and there is a real danger that 
  - the theorem itself will seem more plausible to you than the proof. 
- In case you think the second uniqueness theorem is “obvious,” consider this example of Purcell’s: 
  - Figure 3.7 shows a simple electrostatic configuration, consisting of four conductors with charges \( \pm Q \), situated so that the pluses are near the minuses. 
  - It all looks very comfortable. 
  - Now, what happens if we join them in pairs, by tiny wires, as indicated in Fig. 3.8? 
  - Since the positive charges are very near negative charges (which is where they like to be) you might well guess that nothing will happen—the configuration looks stable. 
  - Well, that sounds reasonable, but it’s wrong. 
  - The configuration in Fig. 3.8 is impossible. 
  - For there are now effectively two conductors, and the total charge on each is zero. 
  - One possible way to distribute zero charge over these conductors is to have no accumulation of charge anywhere, and hence zero field everywhere (Fig. 3.9). 
  - By the second uniqueness theorem, this must be the solution: 
    - The charge will flow down the tiny wires, canceling itself off.

---

證明很複雜，不容易理解。
定理本身可能很直觀，看起來顯而易見。
但如果不經過嚴格的證明，人們可能會憑直覺覺得定理是對的，而不去深究證明的合理性。
這是一種風險，因為數學和物理學不只是依賴直覺，而是要有嚴格的論證。

舉了一個乍看直觀，但有誤解風險的例子。
在這個例子中，原本有4個導體，但最後是2個。
即使只是透過導線連接兩個導體球，整個東西就是一個導體。

證明的複雜性之一是，
而這個例子中，不同的導體也許會有不同的等電位，
我們不需要知道他是多少，也不需要知道他們一不一樣，
我們只需要知道每個導體都是等電位

比方說，四個導體的電位
第一個解，也許是，1、2、3、4
第二個解，也許是，5、6、7、8

另一個複雜性就是那個把戲
他是怎麼知道要把電位和電場相乘再取散度
運用對應乘積微分法則
然後再對整個區域積分並且運用散度定理
只能說這是一開始想出這個方法的人的創造性
這個證明過程是相當數學的，而不是基於幾何和物理的圖像

# Deepseek

**第二唯一性定理的逐步解釋與證明解析**

**定理陳述：**  
在由導體包圍的體積\( V \)內，若已知各導體上的總電荷及內部電荷密度\( \rho \)，則電場\(\mathbf{E}\)被唯一確定。外部邊界可以是另一導體或無限遠。

**證明步驟解析：**

1. **假設存在兩個解：**  
   設\(\mathbf{E_1}\)和\(\mathbf{E_2}\)均滿足問題條件，即：
   - **微分形式高斯定律**：在導體間區域，\(\nabla \cdot \mathbf{E_1} = \nabla \cdot \mathbf{E_2} = \rho/\epsilon_0\)。
   - **積分形式高斯定律**：對每個導體表面，\(\oint \mathbf{E_1} \cdot d\mathbf{a} = \oint \mathbf{E_2} \cdot d\mathbf{a} = Q_i/\epsilon_0\)。
   - **外邊界條件**：無論外邊界是導體或無限遠，總通量滿足\(\oint \mathbf{E_1} \cdot d\mathbf{a} = \oint \mathbf{E_2} \cdot d\mathbf{a} = Q_{\text{tot}}/\epsilon_0\)。

2. **構造差異場\(\mathbf{E_3}\)：**  
   定義\(\mathbf{E_3} = \mathbf{E_1} - \mathbf{E_2}\)，則：
   - \(\nabla \cdot \mathbf{E_3} = 0\)（因兩場散度相同）。
   - 對任一導體表面或外邊界，\(\oint \mathbf{E_3} \cdot d\mathbf{a} = 0\)（因兩場通量相同）。

3. **利用導體的等勢性質：**  
   每個導體表面為等勢體，故電勢差\(V_3 = V_1 - V_2\)在每個導體表面為常數（不同導體可能不同）。  
   - 注意：\(V_3\)在單個導體表面為常數，但不同導體間\(V_3\)的常數值可能不同。

4. **應用乘積法則與散度定理：**  
   - 考慮\(\nabla \cdot (V_3 \mathbf{E_3})\)，利用乘積法則：  
     \[
     \nabla \cdot (V_3 \mathbf{E_3}) = V_3 (\nabla \cdot \mathbf{E_3}) + \mathbf{E_3} \cdot (\nabla V_3).
     \]
     由於\(\nabla \cdot \mathbf{E_3} = 0\)且\(\mathbf{E_3} = -\nabla V_3\)，得：
     \[
     \nabla \cdot (V_3 \mathbf{E_3}) = -|\mathbf{E_3}|^2.
     \]
   - 對整個體積\(V\)積分，並應用散度定理：  
     \[
     \int_V \nabla \cdot (V_3 \mathbf{E_3}) \, d\tau = \oint_S V_3 \mathbf{E_3} \cdot d\mathbf{a} = -\int_V |\mathbf{E_3}|^2 \, d\tau.
     \]

5. **處理表面積分：**  
   - **導體表面**：\(V_3\)為常數，可提出積分外，剩餘部分為\(\mathbf{E_3}\)的通量，由步驟2知為零。  
   - **外邊界**：若為無限遠，\(V_3 \to 0\)；若為導體，同理\(V_3\)為常數且通量為零。  
   - 因此，表面積分整體為零，得：  
     \[
     \int_V |\mathbf{E_3}|^2 \, d\tau = 0.
     \]

6. **唯一性結論：**  
   被積函數\(|\mathbf{E_3}|^2 \geq 0\)，積分為零當且僅當\(\mathbf{E_3} = 0\)處處成立。故\(\mathbf{E_1} = \mathbf{E_2}\)，電場唯一。

**關鍵點與物理意義：**  
- **導體等勢的關鍵作用**：即使不同導體的\(V_3\)常數不同，其差異在表面積分中被提取為常數，通量為零的條件迫使積分消失。
- **數學技巧的物理對應**：乘積法則與散度定理的應用將問題轉化為能量積分（\(|\mathbf{E_3}|^2\)），體現場的差異必須為零。
- **反直覺例子的啟示**：如四導體連接成兩導體後，總電荷為零的唯一解是電場處處為零，顯示定理的強大約束性。

**總結：**  
該定理的證明通過嚴謹的數學操作，將物理條件（高斯定律、導體等勢）轉化為積分約束，最終導出矛盾，確保電場唯一。儘管過程抽象，但凸顯了數學工具在物理理論中的核心地位。
