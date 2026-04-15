## 第一组参考题

1. 试用两种方法证明: 对于正数数列 \( \left\{  {a}_{n}\right\} \) ,必有

\[
\mathop{\lim }\limits_{{n \rightarrow  \infty }}\frac{{a}_{n}}{\left( {1 + {a}_{1}}\right) \left( {1 + {a}_{2}}\right) \cdots \left( {1 + {a}_{n}}\right) } = 0.
\]

2. (Abel-Pringsheim (普林斯海姆) 定理) 设正项级数 \( \sum {a}_{n} \) 的通项单调减少,且已知级数收敛,证明: \( \mathop{\lim }\limits_{{n \rightarrow  \infty }}n{a}_{n} = 0 \) . (举例说明,若通项非单调,则结论不成立.)

3. 设正项级数 \( \mathop{\sum }\limits_{{n = 1}}^{\infty }{a}_{n} \) 的通项单调减少,又已知级数 \( \mathop{\sum }\limits_{{n = 1}}^{\infty }\frac{{a}_{n}}{\sqrt{n}} \) 收敛,证明: 级数 \( \mathop{\sum }\limits_{{n = 1}}^{\infty }{a}_{n}^{2} \) 收敛.

4. 设正项级数 \( \mathop{\sum }\limits_{{n = 1}}^{\infty }{a}_{n} \) 的通项单调减少收敛于 0.1 (1 证明: 级数 \( \mathop{\sum }\limits_{{n = 1}}^{\infty }{a}_{n} \) 与级数 \( \mathop{\sum }\limits_{{n = 1}}^{\infty }n\left( {{a}_{n} - {a}_{n + 1}}\right) \) 同敛散，且在收敛时具有相同的和. (2) 对于通项不是单调减少的情况，试举例说明上述“同敛散”的结论不再成立.

5. 由于数列 \( \left\{  {a}_{n}\right\} \) 与无穷级数 \( \mathop{\sum }\limits_{{n = 1}}^{\infty }\left( {{a}_{n + 1} - {a}_{n}}\right) \) 具有相同的敛散性,试用级数理论讨论下列数列的敛散性:

(1) \( {a}_{n} = 1 + \frac{1}{2} + \cdots  + \frac{1}{n} - \ln n, n = 1,2,\cdots \)

(2) \( {a}_{n} = 1 + \frac{1}{\sqrt{2}} + \cdots  + \frac{1}{\sqrt{n}} - 2\sqrt{n}, n = 1,2,\cdots \)

(3) \( {a}_{n} = \frac{1}{2\ln 2} + \frac{1}{3\ln 3} + \cdots  + \frac{1}{n\ln n} - \ln \ln n, n = 2,3,\cdots \) .

(题 (1) 即上册 43 页命题 2.5.6, 题 (2) 见上册 56 页参考题 14. 又可以与上册 371 页参考题 10 作比较.)

6. 证明: (1) 若 \( f \) 是 \( \lbrack 1, + \infty ) \) 上的非负单调减少函数,则存在极限

\[
\mathop{\lim }\limits_{{n \rightarrow  \infty }}\left( {\mathop{\sum }\limits_{{k = 1}}^{n}f\left( k\right)  - {\int }_{1}^{n}f\left( x\right) \mathrm{d}x}\right)  = A,
\]

且 \( 0 \leq  A \leq  f\left( 1\right) ;\left( 2\right) \mathop{\lim }\limits_{{x \rightarrow   + \infty }}\mathop{\sum }\limits_{{n = 1}}^{\infty }\frac{x}{{x}^{2} + {n}^{2}} = \frac{\pi }{2} \) .

7. 若函数 \( f \) 在 \( \left\lbrack  {-1,1}\right\rbrack \) 上定义,且存在 \( {f}^{\prime \prime }\left( 0\right) \) ,证明: 级数 \( \mathop{\sum }\limits_{{n = 1}}^{\infty }f\left( \frac{1}{n}\right) \) 绝对收敛的充分必要条件是 \( f\left( 0\right)  = {f}^{\prime }\left( 0\right)  = 0 \) .

8. 设函数 \( f \) 在 \( \lbrack 1, + \infty ) \) 上单调增加且有极限 \( f\left( {+\infty }\right)  = A \) . 证明:

(1) \( \mathop{\sum }\limits_{{n = 1}}^{\infty }\left\lbrack  {f\left( {n + 1}\right)  - f\left( n\right) }\right\rbrack \) 收敛，并求其和；

(2)又若 \( f \) 在 \( \lbrack 1, + \infty ) \) 上二次可微,且 \( {f}^{\prime \prime }\left( x\right)  < 0 \) ,则 \( \mathop{\sum }\limits_{{n = 1}}^{\infty }{f}^{\prime }\left( n\right) \) 也收敛.

9. (二重正项级数的求和顺序交换定理) 设对每个正整数 \( n \) ,正项级数 \( \mathop{\sum }\limits_{{k = 1}}^{\infty }{a}_{n, k} \) 收敛，且其和为 \( {a}_{n} \) . 若级数 \( \mathop{\sum }\limits_{{n = 1}}^{\infty }{a}_{n} \) 收敛，证明:

\[
\mathop{\sum }\limits_{{n = 1}}^{\infty }{a}_{n} = \mathop{\sum }\limits_{{n = 1}}^{\infty }\mathop{\sum }\limits_{{k = 1}}^{\infty }{a}_{n, k} = \mathop{\sum }\limits_{{k = 1}}^{\infty }\mathop{\sum }\limits_{{n = 1}}^{\infty }{a}_{n, k}.
\]

10. 对正整数 \( m \geq  2 \) ,用 \( {s}_{m} \) 表示级数 \( \mathop{\sum }\limits_{{n = 2}}^{\infty }\frac{1}{{n}^{m}} \) 的和,证明: \( \mathop{\sum }\limits_{{m = 2}}^{\infty }{s}_{m} = 1 \) .

11. 设正项级数 \( \mathop{\sum }\limits_{{n = 1}}^{\infty }{a}_{n} \) 的通项单调减少趋于 0,且已知数列 \( \left\{  {\mathop{\sum }\limits_{{k = 1}}^{n}\left( {{a}_{k} - {a}_{n}}\right) }\right\} \) 有界, 证明: \( \mathop{\sum }\limits_{{n = 1}}^{\infty }{a}_{n} \) 收敛.

12. 设正项级数 \( \mathop{\sum }\limits_{{n = 1}}^{\infty }{a}_{n} \) 收敛,且数列 \( \left\{  {{a}_{n} - {a}_{n + 1}}\right\} \) 严格单调减少,证明:

\[
\mathop{\lim }\limits_{{n \rightarrow  \infty }}\left( {\frac{1}{{a}_{n + 1}} - \frac{1}{{a}_{n}}}\right)  =  + \infty .
\]

13. 设正项级数 \( \mathop{\sum }\limits_{{n = 1}}^{\infty }{a}_{n} \) 收敛,数列 \( \left\{  {n{a}_{n}}\right\} \) 单调,证明: \( \mathop{\lim }\limits_{{n \rightarrow  \infty }}n{a}_{n}\ln n = 0 \) .

14. 设 \( {a}_{1} = 1,{a}_{2} = 2,{a}_{n} = {a}_{n - 1} + {a}_{n - 2}, n = 3,4,\cdots \) ,证明: \( \mathop{\sum }\limits_{{n = 1}}^{\infty }\frac{1}{{a}_{n}} \) 收敛. (Fibonacci 数列的倒数所成级数收敛.)

15. 设 \( 0 < p < 1,{a}_{1} > 0,{a}_{n + 1} = \frac{{a}_{n}}{1 + {a}_{n}^{p}}, n = 1,2,\cdots \) ,证明: \( \mathop{\sum }\limits_{{n = 1}}^{\infty }{a}_{n} \) 收敛.

16. 设正项级数 \( \mathop{\sum }\limits_{{n = 1}}^{\infty }{a}_{n} \) 收敛,则对于 \( p > \frac{1}{2} \) ,证明: 级数 \( \mathop{\sum }\limits_{{n = 1}}^{\infty }\frac{\sqrt{{a}_{n}}}{{n}^{p}} \) 收敛. 举例说明 \( p = \frac{1}{2} \) 时级数 \( \mathop{\sum }\limits_{{n = 1}}^{\infty }\frac{\sqrt{{a}_{n}}}{{n}^{1/2}} \) 可能发散.

17. 证明下列两个级数发散: (1) \( \mathop{\sum }\limits_{{n = 1}}^{\infty }\sin n \) ; (2) \( \mathop{\sum }\limits_{{n = 1}}^{\infty }\sin {n}^{2} \) .

18. 设正项级数 \( \mathop{\sum }\limits_{{n = 1}}^{\infty }{a}_{n} \) 发散,讨论下列级数的敛散性: (1) \( \mathop{\sum }\limits_{{n = 1}}^{\infty }\frac{{a}_{n}}{1 + {n}^{2}{a}_{n}} \) ; (2) \( \mathop{\sum }\limits_{{n = 1}}^{\infty }\frac{{a}_{n}}{1 + n{a}_{n}};\left( 3\right) \mathop{\sum }\limits_{{n = 1}}^{\infty }\frac{{a}_{n}}{1 + {a}_{n}};\left( 4\right) \mathop{\sum }\limits_{{n = 1}}^{\infty }\frac{{a}_{n}}{1 + {a}_{n}^{2}}. \)

19. 设有收敛级数 \( \mathop{\sum }\limits_{{n = 1}}^{\infty }{a}_{n} = S \) ,证明: (1) \( \mathop{\lim }\limits_{{n \rightarrow  \infty }}\frac{{a}_{1} + 2{a}_{2} + \cdots  + n{a}_{n}}{n} = 0 \) ; (2) 级数 \( \mathop{\sum }\limits_{{n = 1}}^{\infty }\frac{{a}_{1} + 2{a}_{2} + \cdots  + n{a}_{n}}{n\left( {n + 1}\right) } \) 收敛,且其和也是 \( S \) .

20. 设级数 \( \mathop{\sum }\limits_{{n = 1}}^{\infty }{a}_{n} = s \) 为条件收敛， \( \mathop{\sum }\limits_{{n = 1}}^{\infty }{a}_{f\left( n\right) } = t \) 是 \( \mathop{\sum }\limits_{{n = 1}}^{\infty }{a}_{n} \) 的一个重排. 若 \( t \neq  s \) ， 证明: 对于任意 \( N \) ,存在 \( n \) ,使 \( \left| {n - f\left( n\right) }\right|  > N \) .

(这表明, 对于条件收敛级数作重排时, 如果每一项的新位置与原有位置之差不超过某个界限的话, 则级数的和不会改变.)
