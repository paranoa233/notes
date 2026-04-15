#### 3.2. Homogeneous equations

*Français : 3.2. Équations homogènes*

On appelle ainsi les équations différentielles qui peuvent s'exprimer en fonction de \( {y}^{\prime } \) et \( y/x \) .

> This is the name given to differential equations that can be expressed as a function of \( {y}^{\prime } \) and \( y/x \) .

Équations homogènes résolues : \( {y}^{\prime } = f\left( {y/x}\right) \) . On pose \( t = y/x \) , donc \( y = {tx} \) et \( f\left( t\right) {dx} = {dy} = {xdt} + {tdx} \) . On se ramène donc à \( \left\lbrack {f\left( t\right) - t}\right\rbrack {dx} = {xdt} \) , que l’on sait intégrer. Remarque 3. S’il existe \( {t}_{0} \) tel que \( f\left( {t}_{0}\right) = {t}_{0} \) , la fonction \( y = {t}_{0}x \) est solution.

> Solved homogeneous equations: \( {y}^{\prime } = f\left( {y/x}\right) \) . We set \( t = y/x \) , so \( y = {tx} \) and \( f\left( t\right) {dx} = {dy} = {xdt} + {tdx} \) . We thus reduce it to \( \left\lbrack {f\left( t\right) - t}\right\rbrack {dx} = {xdt} \) , which we know how to integrate. Remark 3. If there exists \( {t}_{0} \) such that \( f\left( {t}_{0}\right) = {t}_{0} \) , the function \( y = {t}_{0}x \) is a solution.

Équations homogènes non résolues : \( F\left( {y/x,{y}^{\prime }}\right) = 0 \) . On suppose connu un para-métrage \( t \mapsto \left( {u\left( t\right) , v\left( t\right) }\right) \) de \( \Gamma = \{ \left( {U, V}\right) \mid F\left( {U, V}\right) = 0\} \) , où \( u \) est de classe \( {\mathcal{C}}^{1} \) et \( v \) continue. On écrit \( y/x = u\left( t\right) \) et \( {y}^{\prime } = v\left( t\right) \) , donc

> Unsolved homogeneous equations: \( F\left( {y/x,{y}^{\prime }}\right) = 0 \) . We assume a parameterization \( t \mapsto \left( {u\left( t\right) , v\left( t\right) }\right) \) of \( \Gamma = \{ \left( {U, V}\right) \mid F\left( {U, V}\right) = 0\} \) is known, where \( u \) is of class \( {\mathcal{C}}^{1} \) and \( v \) is continuous. We write \( y/x = u\left( t\right) \) and \( {y}^{\prime } = v\left( t\right) \) , so

\[
{dy} = v\left( t\right) {dx} = {u}^{\prime }\left( t\right) {xdt} + u\left( t\right) {dx}\;\text{ d’où }\left\lbrack  {v\left( t\right)  - u\left( t\right) }\right\rbrack  {dx} = x{u}^{\prime }\left( t\right) {dt}.
\]

- Sur un intervalle où \( u - v \) ne s’annule pas, on écrit \( \frac{dx}{x} = \frac{{u}^{\prime }\left( t\right) }{v\left( t\right)  - u\left( t\right) }{dt} \) , puis on intègre ;

> - On an interval where \( u - v \) does not vanish, we write \( \frac{dx}{x} = \frac{{u}^{\prime }\left( t\right) }{v\left( t\right)  - u\left( t\right) }{dt} \) , then integrate;

- s’il existe \( {t}_{0} \) tel que \( u\left( {t}_{0}\right)  = v\left( {t}_{0}\right) \) , alors \( x \mapsto  u\left( {t}_{0}\right) x \) est solution.

> - if there exists \( {t}_{0} \) such that \( u\left( {t}_{0}\right)  = v\left( {t}_{0}\right) \) , then \( x \mapsto  u\left( {t}_{0}\right) x \) is a solution.
