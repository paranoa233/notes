## 第二十三章 含参变量积分 参考题提示

## 参考题 (306 页)

3. (1) \( \varphi \left( x\right)  =  - {\left. 2\sqrt{x - t}f\left( t\right) \right| }_{0}^{x} + 2{\int }_{0}^{x}\sqrt{x - t}{f}^{\prime }\left( t\right) \mathrm{d}t \) ,(2) 利用 (1),然后将积分交换次序.

4. \( {\int }_{0}^{A}f\left( x\right) \frac{\sin {\alpha x}}{x}\mathrm{\;d}x = {\int }_{0}^{\alpha A}f\left( \frac{y}{\alpha }\right) \frac{\sin y}{y}\mathrm{\;d}y = {\int }_{0}^{+\infty }f\left( \frac{y}{\alpha }\right) \frac{\sin y}{y}\mathrm{\;d}y \) (将 \( f \) 零延拓),利用广义积分对 \( \alpha \) 一致收敛取极限.

5. \( F\left( t\right)  = {\int }_{0}^{+\infty }{\mathrm{e}}^{-y}f\left( \frac{y}{t}\right) \mathrm{d}y \) ,利用广义积分对 \( t \) 一致收敛取极限.

6. (1) 固定 \( t \) ,由 Schwarz 不等式得

\[
{\left\lbrack  {\int }_{A}^{B}f\left( t + u\right) f\left( u\right) \mathrm{d}u\right\rbrack  }^{2} \leq  {\int }_{A}^{B}{f}^{2}\left( {t + u}\right) \mathrm{d}u{\int }_{A}^{B}{f}^{2}\left( u\right) \mathrm{d}u
\]

\[
= {\int }_{A + t}^{B + t}{f}^{2}\left( u\right) \mathrm{d}u{\int }_{A}^{B}{f}^{2}\left( u\right) \mathrm{d}u
\]

其中 \( A, B \) 充分大或充分小,则 \( {\int }_{-\infty }^{+\infty }f\left( {t + u}\right) f\left( u\right) \mathrm{d}u \) 对每一个 \( t \) 都存在,且对 \( t \) 一致收敛. (2) \( \frac{1}{2\sqrt{\varepsilon \pi }}{\int }_{-\infty }^{+\infty }{\mathrm{e}}^{-{t}^{2}/{4\varepsilon }}g\left( t\right) \mathrm{d}t = \frac{1}{\sqrt{\pi }}{\int }_{-\infty }^{+\infty }{\mathrm{e}}^{-{x}^{2}}g\left( {2\sqrt{\varepsilon }x}\right) \mathrm{d}x \) ,由 \( g \) 有界知后面的广义积分对 \( \varepsilon \) 一致收敛.

7. (1) 注意 \( f\left( \alpha \right)  = \mathop{\sum }\limits_{{k = 0}}^{\infty }{\int }_{k\pi }^{\left( {k + 1}\right) \pi }\frac{{\mathrm{e}}^{-t}}{{\left| \sin t\right| }^{\alpha }}\mathrm{d}t = \frac{1}{1 - {\mathrm{e}}^{-\pi }}{\int }_{0}^{\pi }\frac{{\mathrm{e}}^{-t}}{{\left| \sin t\right| }^{\alpha }}\mathrm{d}t \)

(2)由于 \( f \) 不一定是连续函数,故要用定义证 \( g \) 的连续性.

8. 用柱坐标变换和余元公式,或用球坐标变换,体积为 \( \frac{\sqrt{2}}{3}\pi \) .

9. \( \bar{x} = \frac{3a}{4} \cdot  \frac{\Gamma \left( {2n}\right) \Gamma \left( {3n}\right) }{\Gamma \left( n\right) \Gamma \left( {4n}\right) } \) .

10. 惯性矩 \( I = 4{\iint }_{D}{y}^{2}\mathrm{\;d}x\mathrm{\;d}y = \frac{21}{{2}^{9}}\pi {R}^{4} \) .

11. 与第 5 题的方法类似.

13. \( {\int }_{0}^{+\infty }\cos {x}^{p}\mathrm{\;d}x = \frac{1}{p}{\int }_{0}^{+\infty }{y}^{\frac{1}{p} - 1}\cos y\mathrm{\;d}y \) ,利用 \( {y}^{\frac{1}{p} - 1} = \frac{1}{\Gamma \left( {1 - \frac{1}{p}}\right) }{\int }_{0}^{+\infty }{t}^{-\frac{1}{p}}{\mathrm{e}}^{-{yt}}\mathrm{\;d}t \) ,交换积分次序得 \( {\int }_{0}^{+\infty }\cos {x}^{p}\mathrm{\;d}x = \frac{1}{p}\Gamma \left( \frac{1}{p}\right) \cos \frac{\pi }{2p} \) .

14. 用余元公式,结果为 \( \ln \sqrt{2\pi } \) .

15. 利用 \( \frac{1}{{a}^{2} + {x}^{2}} = \mathop{\lim }\limits_{{\varepsilon  \rightarrow  {0}^{ + }}}{\int }_{\varepsilon }^{+\infty }{\mathrm{e}}^{-t\left( {{a}^{2} + {x}^{2}}\right) }\mathrm{d}t \) ,交换积分次序得

\[
{I}_{1} = \frac{\pi }{2a}{\mathrm{e}}^{-{ab}},{I}_{k + 1} =  - \frac{1}{2ak} \cdot  \frac{\partial {I}_{k}}{\partial a},{J}_{k} =  - \frac{\partial {I}_{k}}{\partial b}.
\]

16. 考虑 \( \ln \Gamma \left( x\right) \) 的导数.

17. (1) \( 1 + x + \cdots  + {x}^{n - 1} = \frac{{x}^{n} - 1}{x - 1} \) ; (2) 令 \( x \rightarrow  1 \) ; (3) 利用余元公式.
