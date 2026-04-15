### 4. Problems

*Français : 4. Problèmes*

PROBLEME 1 (CRYPTOGRAPHIE : LE SYSTÉME DE CHIFFREMENT RSA). On se donne deux nombres premiers \( p \) et \( q \) distincts et on pose \( n = {pq} \) . Soient \( c, d \) deux entiers tels que \( {cd} \equiv 1\left( {\;\operatorname{mod}\;\varphi \left( n\right) }\right) \) où \( \varphi \) désigne l’indicateur d’Euler. Montrer que pour tout \( t \in \mathbb{Z} \) , on a \( {t}^{cd} \equiv t\left( {\;\operatorname{mod}\;n}\right) \) .

> PROBLEM 1 (CRYPTOGRAPHY: THE RSA ENCRYPTION SYSTEM). Let \( p \) and \( q \) be two distinct prime numbers and let \( n = {pq} \) . Let \( c, d \) be two integers such that \( {cd} \equiv 1\left( {\;\operatorname{mod}\;\varphi \left( n\right) }\right) \) where \( \varphi \) denotes Euler's totient function. Show that for all \( t \in \mathbb{Z} \) , we have \( {t}^{cd} \equiv t\left( {\;\operatorname{mod}\;n}\right) \) .

Solution. Les nombres \( p \) et \( q \) étant premiers et distincts, on a \( \varphi \left( n\right) = \left( {p - 1}\right) \left( {q - 1}\right) \) . Soit \( k \in \mathbb{Z} \) tel que \( {cd} = 1 + {k\varphi }\left( n\right) \) . Soit \( t \in \mathbb{Z} \) . Pour prouver que \( {t}^{cd} \equiv t\left( {\;\operatorname{mod}\;n}\right) \) , il suffit de prouver \( {t}^{cd} \equiv t\left( {\;\operatorname{mod}\;p}\right) \) et \( {t}^{cd} \equiv t\left( {\;\operatorname{mod}\;q}\right) \) (conséquence de l’isomorphisme de \( \mathbb{Z}/p\mathbb{Z} \times \mathbb{Z}/q\mathbb{Z} \) et \( \mathbb{Z}/{pq}\mathbb{Z} \) ). Prouvons par exemple \( {t}^{cd} \equiv t\left( {\;\operatorname{mod}\;p}\right) \) (le calcul modulo \( q \) est analogue).

> Solution. Since the numbers \( p \) and \( q \) are prime and distinct, we have \( \varphi \left( n\right) = \left( {p - 1}\right) \left( {q - 1}\right) \) . Let \( k \in \mathbb{Z} \) be such that \( {cd} = 1 + {k\varphi }\left( n\right) \) . Let \( t \in \mathbb{Z} \) . To prove that \( {t}^{cd} \equiv t\left( {\;\operatorname{mod}\;n}\right) \) , it suffices to prove \( {t}^{cd} \equiv t\left( {\;\operatorname{mod}\;p}\right) \) and \( {t}^{cd} \equiv t\left( {\;\operatorname{mod}\;q}\right) \) (a consequence of the isomorphism between \( \mathbb{Z}/p\mathbb{Z} \times \mathbb{Z}/q\mathbb{Z} \) and \( \mathbb{Z}/{pq}\mathbb{Z} \) ). Let us prove \( {t}^{cd} \equiv t\left( {\;\operatorname{mod}\;p}\right) \) for example (the calculation modulo \( q \) is analogous).

- Si \( t \land  p = 1 \) alors \( {t}^{p - 1} \equiv  1\left( {\;\operatorname{mod}\;p}\right) \) (théorème de Fermat) donc \( {t}^{cd} \equiv  {\left( {t}^{p - 1}\right) }^{k\left( {q - 1}\right) }t \equiv  t \; \left( {\;\operatorname{mod}\;p}\right) \) .

> - If \( t \land  p = 1 \) then \( {t}^{p - 1} \equiv  1\left( {\;\operatorname{mod}\;p}\right) \) (Fermat's Little Theorem) so \( {t}^{cd} \equiv  {\left( {t}^{p - 1}\right) }^{k\left( {q - 1}\right) }t \equiv  t \; \left( {\;\operatorname{mod}\;p}\right) \) .

- Si \( t \land  p \neq  1 \) , alors \( p \) divise \( t \) , et alors on a \( {t}^{cd} \equiv  t \equiv  0\left( {\;\operatorname{mod}\;p}\right) \) .

> - If \( t \land  p \neq  1 \) , then \( p \) divides \( t \) , and thus we have \( {t}^{cd} \equiv  t \equiv  0\left( {\;\operatorname{mod}\;p}\right) \) .

Remarque. L’application \( g : \mathbb{Z}/n\mathbb{Z} \rightarrow \mathbb{Z}/n\mathbb{Z}\;\dot{t} \mapsto {\dot{t}}^{c} \) s’appelle une fonction de chif-frement, \( f : \dot{t} \mapsto {\dot{t}}^{d} \) fonction de déchiffrement. L’exercice affirme que \( f \circ g\left( \dot{t}\right) = \dot{t} \) . On peut donc chiffrer un message (représenté par un élément \( \dot{t} \) de \( \mathbb{Z}/n\mathbb{Z} \) ) avec \( g \) , puis on le déchiffre avec \( f \) . Le couple \( \left( {n, c}\right) \) est appelé la clef publique, l’entier \( d \) la clef secrète. La sécurité de ce système repose sur le fait que connaissant la clef publique, il est très difficile de déterminer \( d \) : un moyen consiste par exemple à factoriser \( n \) pour trouver \( p \) et \( q \) , ce qui est encore impossible à réaliser lorsque \( p \) et \( q \) sont grands, typiquement (pour l'année 2020) de l'ordre de 150 à 200 chiffres (le record est la factorisation d'un nombre entier sans forme particulière de 250 chiffres, obtenue en 2020 après 2700 années de calcul distribué). Ainsi, tout le monde peut chiffrer mais seuls ceux connaissant la clef secrète peuvent déchiffrer. Ce système de chiffrement est apparu en 1976. Il est appelé RSA (du nom des inventeurs Rivest, Shamir et Adleman) et est couramment utilisé aujourd'hui car il est extrêmement robuste. Son apparition explique l'intérêt que l'on porte aujourd'hui aux algorithmes de factorisation et de primalité.

> Remark. The map \( g : \mathbb{Z}/n\mathbb{Z} \rightarrow \mathbb{Z}/n\mathbb{Z}\;\dot{t} \mapsto {\dot{t}}^{c} \) is called an encryption function, \( f : \dot{t} \mapsto {\dot{t}}^{d} \) a decryption function. The exercise states that \( f \circ g\left( \dot{t}\right) = \dot{t} \) . One can therefore encrypt a message (represented by an element \( \dot{t} \) of \( \mathbb{Z}/n\mathbb{Z} \) ) with \( g \) , then decrypt it with \( f \) . The pair \( \left( {n, c}\right) \) is called the public key, the integer \( d \) the secret key. The security of this system relies on the fact that knowing the public key, it is very difficult to determine \( d \) : one way, for example, is to factor \( n \) to find \( p \) and \( q \) , which is still impossible to achieve when \( p \) and \( q \) are large, typically (as of 2020) on the order of 150 to 200 digits (the record is the factorization of an integer without any particular form of 250 digits, obtained in 2020 after 2700 years of distributed computing). Thus, everyone can encrypt but only those who know the secret key can decrypt. This encryption system appeared in 1976. It is called RSA (named after the inventors Rivest, Shamir, and Adleman) and is commonly used today because it is extremely robust. Its appearance explains the interest currently shown in factorization and primality algorithms.

PROBLÉME 2 (NOMBRES PSEUDO-PREMIERS ET NOMBRES DE CARMICHAEL). Le théorème de Fermat affirme que si \( n \) est premier et si \( a \land n = 1 \) , alors \( {a}^{n - 1} \equiv 1\left( {\;\operatorname{mod}\;n}\right) \) . Le but du problème est d'étudier la réciproque.

> PROBLEM 2 (PSEUDOPRIME NUMBERS AND CARMICHAEL NUMBERS). Fermat's Little Theorem states that if \( n \) is prime and if \( a \land n = 1 \) , then \( {a}^{n - 1} \equiv 1\left( {\;\operatorname{mod}\;n}\right) \) . The goal of the problem is to study the converse.

1 / (Nombres pseudo-premiers). Soit un entier \( a \geq 2 \) . Un entier \( n \) est dit pseudo-premier en base \( a \) (ce que l’on note brièvement pp- \( a \) ) si \( n \) n’est pas premier et si \( {a}^{n - 1} \equiv 1\left( {\;\operatorname{mod}\;n}\right) \) . Si \( p > 2 \) est un nombre premier ne divisant pas \( a\left( {{a}^{2} - 1}\right) \) , montrer que \( n = \left( {{a}^{2p} - 1}\right) /\left( {{a}^{2} - 1}\right) \) est un nombre pp-a. En déduire qu'il existe une infinité de nombres pp-a.

> 1 / (Pseudoprime numbers). Let \( a \geq 2 \) be an integer. An integer \( n \) is said to be pseudoprime to the base \( a \) (briefly denoted pp- \( a \) ) if \( n \) is not prime and if \( {a}^{n - 1} \equiv 1\left( {\;\operatorname{mod}\;n}\right) \) . If \( p > 2 \) is a prime number not dividing \( a\left( {{a}^{2} - 1}\right) \) , show that \( n = \left( {{a}^{2p} - 1}\right) /\left( {{a}^{2} - 1}\right) \) is a pp-a number. Deduce that there exist infinitely many pp-a numbers.

2/ (Nombres de Carmichael). Un entier \( n \geq 2 \) est appelé nombre de Carmichael si \( n \) n’est pas un nombre premier et si pour tout entier \( a,{a}^{n} \equiv a\left( {\;\operatorname{mod}\;n}\right) \) (en particulier, pour tout entier \( a \) premier avec \( n, n \) est pp- \( a \) ).

> 2/ (Carmichael numbers). An integer \( n \geq 2 \) is called a Carmichael number if \( n \) is not a prime number and if for every integer \( a,{a}^{n} \equiv a\left( {\;\operatorname{mod}\;n}\right) \) (in particular, for every integer \( a \) coprime to \( n, n \) is pp- \( a \) ).

a) Si \( n = {p}_{1}\cdots {p}_{k} \) (où les \( {p}_{i} \) sont des nombres premiers distincts) et si \( {p}_{i} - 1 \mid n - 1 \) pour tout \( i \) , montrer que \( n \) est un nombre de Carmichael.

> a) If \( n = {p}_{1}\cdots {p}_{k} \) (where the \( {p}_{i} \) are distinct prime numbers) and if \( {p}_{i} - 1 \mid n - 1 \) for every \( i \) , show that \( n \) is a Carmichael number.

b) Réciproquement, montrer que tout nombre de Carmichael peut se mettre sous la forme \( n = {p}_{1}\cdots {p}_{k} \) où les \( {p}_{i} \) sont des nombres premiers distincts et où \( {p}_{i} - 1 \mid n - 1 \) pour tout \( i \) . (Indication : On pourra utiliser le fait que si \( p \) est premier, le groupe multiplicatif \( {\left( \mathbb{Z}/p\mathbb{Z}\right) }^{ * } \) est cyclique - voir la remarque de l'exercice 10 page 28).

> b) Conversely, show that every Carmichael number can be written in the form \( n = {p}_{1}\cdots {p}_{k} \) where the \( {p}_{i} \) are distinct prime numbers and where \( {p}_{i} - 1 \mid n - 1 \) for all \( i \) . (Hint: One may use the fact that if \( p \) is prime, the multiplicative group \( {\left( \mathbb{Z}/p\mathbb{Z}\right) }^{ * } \) is cyclic - see the remark in exercise 10 on page 28).

c) Montrer qu'un nombre de Carmichael a au moins 3 facteurs premiers.

> c) Show that a Carmichael number has at least 3 prime factors.

d) Soit \( n = {pqr} \) un nombre de Carmichael à trois facteurs premiers \( p < q < r \) . Si \( p \) est fixé, montrer que \( q \) et \( r \) sont bornés.

> d) Let \( n = {pqr} \) be a Carmichael number with three prime factors \( p < q < r \) . If \( p \) is fixed, show that \( q \) and \( r \) are bounded.

---

Solution. 1/ Remarquons tout d’abord que \( n = \left( \frac{{a}^{p} - 1}{a - 1}\right) \left( \frac{{a}^{p} + 1}{a + 1}\right) = \left( {{a}^{p - 1} + \cdots + a + 1}\right) \cdot \left( {{a}^{p - 1} - }\right. \; \left. {{a}^{p - 2} + \cdots - a + 1}\right) \) est un entier composé. Ceci étant, on a \( {a}^{2p} = 1 + n\left( {{a}^{2} - 1}\right) \) , de sorte que \( {a}^{2p} \equiv 1\left( {\;\operatorname{mod}\;n}\right) \;\left( *\right) \) . Le résultat sera donc acquis si on montre que \( {2p} \mid n - 1 \) . On a

> Solution. 1/ First, let us note that \( n = \left( \frac{{a}^{p} - 1}{a - 1}\right) \left( \frac{{a}^{p} + 1}{a + 1}\right) = \left( {{a}^{p - 1} + \cdots + a + 1}\right) \cdot \left( {{a}^{p - 1} - }\right. \; \left. {{a}^{p - 2} + \cdots - a + 1}\right) \) is a composite integer. Given this, we have \( {a}^{2p} = 1 + n\left( {{a}^{2} - 1}\right) \) , so that \( {a}^{2p} \equiv 1\left( {\;\operatorname{mod}\;n}\right) \;\left( *\right) \) . The result will thus be established if we show that \( {2p} \mid n - 1 \) . We have

\[
\left( {{a}^{2} - 1}\right) \left( {n - 1}\right)  = {a}^{2p} - {a}^{2} = a\left( {{a}^{p - 1} - 1}\right) \left( {{a}^{p} + a}\right) .
\]

D’après le théorème de Fermat, \( p \mid \left( {{a}^{p - 1} - 1}\right) \) puisque par hypothèse \( p \) ne divise pas \( a \) . On a donc \( p \mid \left( {{a}^{2} - 1}\right) \left( {n - 1}\right) \) . Or \( p \) ne divise pas \( {a}^{2} - 1 \) , donc \( p \) est premier avec \( {a}^{2} - 1 \) (car \( p \) est premier) et d’après le théorème de Gauss, \( p \mid n - 1 \) . Or \( n - 1 = {a}^{{2p} - 2} + \cdots + {a}^{4} + {a}^{2} \) est une somme paire de termes de même parité, donc \( 2 \mid n - 1 \) . Comme2et \( p \) sont premiers entre eux, on en déduit \( {2p} \mid n - 1 \) , donc \( n \) est pp- \( a \) d’après \( \left( *\right) \) .

> According to Fermat's theorem, \( p \mid \left( {{a}^{p - 1} - 1}\right) \) since by hypothesis \( p \) does not divide \( a \) . We thus have \( p \mid \left( {{a}^{2} - 1}\right) \left( {n - 1}\right) \) . However, \( p \) does not divide \( {a}^{2} - 1 \) , so \( p \) is coprime to \( {a}^{2} - 1 \) (because \( p \) is prime) and according to Gauss's lemma, \( p \mid n - 1 \) . Now \( n - 1 = {a}^{{2p} - 2} + \cdots + {a}^{4} + {a}^{2} \) is an even sum of terms of the same parity, so \( 2 \mid n - 1 \) . Since 2 and \( p \) are coprime, we deduce \( {2p} \mid n - 1 \) , therefore \( n \) is pp- \( a \) according to \( \left( *\right) \) .

---

Il n’y a qu’un nombre fini de nombres premiers \( p \) divisant \( a\left( {{a}^{2} - 1}\right) \) . Comme il y a une infinité de nombres premiers, on en déduit qu'il y a une infinité de nombres premiers \( p > 2 \) ne divisant pas \( a\left( {{a}^{2} - 1}\right) \) , donc une infinité de nombres pp- \( a \) .

> There is only a finite number of prime numbers \( p \) dividing \( a\left( {{a}^{2} - 1}\right) \) . Since there is an infinite number of prime numbers, we deduce that there is an infinite number of prime numbers \( p > 2 \) not dividing \( a\left( {{a}^{2} - 1}\right) \) , and thus an infinite number of pp- \( a \) .

2 / a) Soit \( a \) un entier et soit \( i,1 \leq i \leq k \) . Si \( {p}_{i} \nmid a \) , le théorème de Fermat entraîne \( {a}^{{p}_{i} - 1} \equiv 1 \; \left( {\;\operatorname{mod}\;{p}_{i}}\right) \) , et comme \( {p}_{i} - 1 \) divise \( n - 1 \) , on en déduit \( {a}^{n - 1} \equiv 1\left( {\;\operatorname{mod}\;{p}_{i}}\right) \) , donc \( {a}^{n} \equiv a\left( {\;\operatorname{mod}\;{p}_{i}}\right) \) . Cette dernière égalité reste évidemment vraie si \( {p}_{i} \mid a \) . Ainsi, pour tout entier \( a \) on a montré \( {a}^{n} \equiv a\left( {\;\operatorname{mod}\;{p}_{i}}\right) \) . Ceci s’écrit aussi \( {p}_{i} \mid \left( {{a}^{n} - a}\right) \) . Ceci étant vrai pour tout \( i \) , on en déduit \( n = {p}_{1}\cdots {p}_{k} \mid \left( {{a}^{n} - a}\right) \) puisque les \( {p}_{i} \) sont premiers entre eux deux à deux. On a donc bien \( {a}^{n} \equiv a\left( {{\;\operatorname{mod}\;n} }\right) . \)

> 2 / a) Let \( a \) be an integer and let \( i,1 \leq i \leq k \) . If \( {p}_{i} \nmid a \) , Fermat's theorem implies \( {a}^{{p}_{i} - 1} \equiv 1 \; \left( {\;\operatorname{mod}\;{p}_{i}}\right) \) , and since \( {p}_{i} - 1 \) divides \( n - 1 \) , we deduce \( {a}^{n - 1} \equiv 1\left( {\;\operatorname{mod}\;{p}_{i}}\right) \) , therefore \( {a}^{n} \equiv a\left( {\;\operatorname{mod}\;{p}_{i}}\right) \) . This last equality obviously remains true if \( {p}_{i} \mid a \) . Thus, for every integer \( a \) we have shown \( {a}^{n} \equiv a\left( {\;\operatorname{mod}\;{p}_{i}}\right) \) . This can also be written as \( {p}_{i} \mid \left( {{a}^{n} - a}\right) \) . Since this is true for every \( i \) , we deduce \( n = {p}_{1}\cdots {p}_{k} \mid \left( {{a}^{n} - a}\right) \) since the \( {p}_{i} \) are pairwise coprime. We therefore indeed have \( {a}^{n} \equiv a\left( {{\;\operatorname{mod}\;n} }\right) . \)

b) Soit \( n \) un nombre de Carmichael et \( p \) un nombre premier divisant \( n \) . Comme \( n \) est un nombre de Carmichael, \( n \) divise \( {p}^{n} - p \) , et comme \( {p}^{2} \nmid {p}^{n} - p \) (car \( n \geq 2 \) ), on en déduit \( {p}^{2} \nmid n \) .

> b) Let \( n \) be a Carmichael number and \( p \) a prime number dividing \( n \) . Since \( n \) is a Carmichael number, \( n \) divides \( {p}^{n} - p \) , and since \( {p}^{2} \nmid {p}^{n} - p \) (because \( n \geq 2 \) ), we deduce \( {p}^{2} \nmid n \) .

- On peut donc écrire \( n = {p}_{1}\cdots {p}_{k} \) , où les \( {p}_{i} \) sont des nombres premiers distincts. Soit \( i,1 \leq  i \leq  k \) . Il est bien connu que \( {\left( \mathbb{Z}/{p}_{i}\mathbb{Z}\right) }^{ * } \) est un groupe cyclique, donc il existe un entier \( a \) tel que \( \dot{a} \) soit d’ordre \( {p}_{i} - 1 \) dans \( {\left( \mathbb{Z}/{p}_{i}\mathbb{Z}\right) }^{ * } \) . Comme \( n \) est un nombre de Carmichael, on a \( n \mid  {a}^{n} - a \) donc \( {p}_{i} \mid  {a}^{n} - a \) , ou encore \( {a}^{n} \equiv  a\left( {\;\operatorname{mod}\;{p}_{i}}\right) \) . Comme \( \dot{a} \in  {\left( \mathbb{Z}/{p}_{i}\mathbb{Z}\right) }^{ * } \) , on en déduit \( {a}^{n - 1} \equiv  1\left( {\;\operatorname{mod}\;{p}_{i}}\right) \) . Or l’ordre \( \dot{a} \) dans \( {\left( \mathbb{Z}/{p}_{i}\mathbb{Z}\right) }^{ * } \) est \( {p}_{i} - 1 \) , donc \( {p}_{i} - 1 \mid  n - 1 \) . Ceci est vrai pour tout \( i \) , d’où le résultat.

> - We can therefore write \( n = {p}_{1}\cdots {p}_{k} \) , where the \( {p}_{i} \) are distinct prime numbers. Let \( i,1 \leq  i \leq  k \) . It is well known that \( {\left( \mathbb{Z}/{p}_{i}\mathbb{Z}\right) }^{ * } \) is a cyclic group, so there exists an integer \( a \) such that \( \dot{a} \) is of order \( {p}_{i} - 1 \) in \( {\left( \mathbb{Z}/{p}_{i}\mathbb{Z}\right) }^{ * } \) . Since \( n \) is a Carmichael number, we have \( n \mid  {a}^{n} - a \) so \( {p}_{i} \mid  {a}^{n} - a \) , or also \( {a}^{n} \equiv  a\left( {\;\operatorname{mod}\;{p}_{i}}\right) \) . Since \( \dot{a} \in  {\left( \mathbb{Z}/{p}_{i}\mathbb{Z}\right) }^{ * } \) , we deduce \( {a}^{n - 1} \equiv  1\left( {\;\operatorname{mod}\;{p}_{i}}\right) \) . However, the order of \( \dot{a} \) in \( {\left( \mathbb{Z}/{p}_{i}\mathbb{Z}\right) }^{ * } \) is \( {p}_{i} - 1 \) , so \( {p}_{i} - 1 \mid  n - 1 \) . This is true for all \( i \) , hence the result.

c) Supposons que \( n = \left( {a + 1}\right) \left( {b + 1}\right) \) soit un nombre de Carmichael avec \( a + 1 \) et \( b + 1 \) premiers et \( a \neq b \) . On a \( n = {ab} + a + b + 1 \) . Or \( a \mid n - 1 \) donc \( a \mid b = \left( {n - 1 - {ab} - a}\right) \) ; de même \( b \mid a \) . Donc \( a = b \) , ce qui impossible d’après la question précédente.

> c) Suppose that \( n = \left( {a + 1}\right) \left( {b + 1}\right) \) is a Carmichael number with \( a + 1 \) and \( b + 1 \) prime and \( a \neq b \) . We have \( n = {ab} + a + b + 1 \) . However \( a \mid n - 1 \) so \( a \mid b = \left( {n - 1 - {ab} - a}\right) \) ; likewise \( b \mid a \) . Thus \( a = b \) , which is impossible according to the previous question.

d) Comme \( n \) est un nombre de Carmichael, on a \( q - 1 \mid n - 1 \) , et donc \( q - 1 \mid \left( {n - 1}\right) - \left( {q - 1}\right) = \; q\left( {{pr} - 1}\right) \) . Or \( q \land \left( {q - 1}\right) = 1 \) donc d’après le théorème de Gauss, \( q - 1 \mid {pr} - 1 \) . De même \( r - 1 \mid {pq} - 1 \) , donc finalement \( \left( {q - 1}\right) \left( {r - 1}\right) \mid \left( {{pr} - 1}\right) \left( {{pq} - 1}\right) \) . Ceci entraîne

> d) Since \( n \) is a Carmichael number, we have \( q - 1 \mid n - 1 \) , and therefore \( q - 1 \mid \left( {n - 1}\right) - \left( {q - 1}\right) = \; q\left( {{pr} - 1}\right) \) . However \( q \land \left( {q - 1}\right) = 1 \) so according to Gauss's theorem, \( q - 1 \mid {pr} - 1 \) . Likewise \( r - 1 \mid {pq} - 1 \) , so finally \( \left( {q - 1}\right) \left( {r - 1}\right) \mid \left( {{pr} - 1}\right) \left( {{pq} - 1}\right) \) . This leads to

\[
\left( {q - 1}\right) \left( {r - 1}\right)  \mid  \left( {{pr} - 1}\right) \left( {{pq} - 1}\right)  - {p}^{2}\left( {q - 1}\right) \left( {r - 1}\right)  = {p}^{2}\left( {r + q}\right)  - p\left( {r + q}\right)  + 1 - {p}^{2},
\]

d’où on tire \( \left( {q - 1}\right) \left( {r - 1}\right) < {p}^{2}\left( {r + q}\right) \) . Comme \( q < r \) , on a donc \( {\left( q - 1\right) }^{2} < 2{p}^{2}r\;\left( *\right) \) . Nous avons vu plus haut que \( r - 1 \mid {pq} - 1 \) , ce qui entraîne \( r \leq {pq} \) donc \( {r}^{2} \leq {p}^{2}{q}^{2} \) , et d’après \( \left( *\right) {r}^{2} < {p}^{2}4{p}^{2}r \) , donc \( r < 4{p}^{4} \) . En remplaçant cette dernière inégalité dans \( \left( *\right) \) on tombe sur \( q < \sqrt{8}{p}^{3} + 1 \) .

> from which we derive \( \left( {q - 1}\right) \left( {r - 1}\right) < {p}^{2}\left( {r + q}\right) \) . Since \( q < r \) , we therefore have \( {\left( q - 1\right) }^{2} < 2{p}^{2}r\;\left( *\right) \) . We saw above that \( r - 1 \mid {pq} - 1 \) , which implies \( r \leq {pq} \) so \( {r}^{2} \leq {p}^{2}{q}^{2} \) , and according to \( \left( *\right) {r}^{2} < {p}^{2}4{p}^{2}r \) , therefore \( r < 4{p}^{4} \) . Substituting this last inequality into \( \left( *\right) \) , we arrive at \( q < \sqrt{8}{p}^{3} + 1 \) .

En résumé, on a prouvé que \( q < \sqrt{8}{p}^{3} + 1 \) et \( r < 4{p}^{4} \) . Donc si \( p \) est fixé, \( q \) et \( r \) sont bornés.

> In summary, we have proven that \( q < \sqrt{8}{p}^{3} + 1 \) and \( r < 4{p}^{4} \) . Thus, if \( p \) is fixed, \( q \) and \( r \) are bounded.

Remarque. Le plus petit nombre de Carmichael est \( {561} = 3 \cdot {11} \cdot {17} \) . Les suivants sont 1105, 1729, 2465, 2821.

> Remark. The smallest Carmichael number is \( {561} = 3 \cdot {11} \cdot {17} \) . The following ones are 1105, 1729, 2465, 2821.

- On sait depuis 1992 qu’il existe une infinité de nombres de Carmichael, et que si \( x \) est assez grand, il y a au moins \( {x}^{2/7} \) nombres de Carmichael inférieurs à \( x \) .

> - It has been known since 1992 that there are infinitely many Carmichael numbers, and that if \( x \) is large enough, there are at least \( {x}^{2/7} \) Carmichael numbers less than \( x \) .

Problems 3 (Quelques TESTS DE PRIMALITÉ). a) Soit un entier \( n \geq 2 \) vérifiant

> Problems 3 (Some PRIMALITY TESTS). a) Let \( n \geq 2 \) be an integer satisfying

\[
\exists a \in  \mathbb{Z},\left( {{a}^{n - 1} \equiv  1\;\left( {\;\operatorname{mod}\;n}\right) \;\text{ et }\;\forall q \mid  \left( {n - 1}\right) , q\text{ premier, }{a}^{\left( {n - 1}\right) /q} \text{ ≢ } 1\;\left( {\;\operatorname{mod}\;n}\right) }\right) .
\]

Montrer que \( n \) est un nombre premier.

> Show that \( n \) is a prime number.

b) Soit \( n \geq 2 \) un entier, \( n - 1 = {p}_{1}^{{\alpha }_{1}}\cdots {p}_{k}^{{\alpha }_{k}} \) la décomposition en facteurs premiers de \( n - 1 \) . On suppose que pour tout \( i,1 \leq i \leq k \) , il existe un entier \( {a}_{i} \) tel que

> b) Let \( n \geq 2 \) be an integer, \( n - 1 = {p}_{1}^{{\alpha }_{1}}\cdots {p}_{k}^{{\alpha }_{k}} \) the prime factorization of \( n - 1 \) . Suppose that for all \( i,1 \leq i \leq k \) , there exists an integer \( {a}_{i} \) such that

\[
{a}_{i}^{n - 1} \equiv  1\;\left( {\;\operatorname{mod}\;n}\right) \;\text{ et }\;{a}_{i}^{\left( {n - 1}\right) /{p}_{i}} \text{ ≢ } 1\;\left( {\;\operatorname{mod}\;n}\right) .
\]

Montrer que \( n \) est un nombre premier.

> Show that \( n \) is a prime number.

c) Soit \( p > 2 \) premier, et soit \( h \in \mathbb{N} \) tel que \( 1 \leq h \leq p - 1 \) . On pose \( n = 1 + h{p}^{2} \) . Si

> c) Let \( p > 2 \) be prime, and let \( h \in \mathbb{N} \) be such that \( 1 \leq h \leq p - 1 \) . Let \( n = 1 + h{p}^{2} \) . If

\[
{2}^{n - 1} \equiv  1\;\left( {\;\operatorname{mod}\;n}\right) \;\text{ et }\;{2}^{h} \text{ ≢ } 1\;\left( {\;\operatorname{mod}\;n}\right)
\]

montrer que \( n \) est premier. (Indication : utiliser l’ordre de \( \dot{2} \) pour montrer qu’il existe un nombre premier \( q \) divisant \( n \) avec \( p \mid q - 1 \) .)

> show that \( n \) is prime. (Hint: use the order of \( \dot{2} \) to show that there exists a prime number \( q \) dividing \( n \) with \( p \mid q - 1 \) .)

Solution. a) Soit \( m \) l’ordre de \( \dot{a} \) dans le groupe des inversibles de \( \mathbb{Z}/n\mathbb{Z} \) . Nous allons montrer que \( m = n - 1 \) . Supposons \( m < n - 1 \) . Comme \( {a}^{n - 1} \equiv 1\left( {\;\operatorname{mod}\;n}\right) , m \mid n - 1 \) et donc il existe un nombre premier \( q \) divisant \( n - 1 \) tel que \( m \mid \left( {n - 1}\right) /q \) . Ceci entraîne que \( {a}^{\left( {n - 1}\right) /q} \equiv 1\left( {\;\operatorname{mod}\;n}\right) \) , ce qui est contraire aux hypothèses.

> Solution. a) Let \( m \) be the order of \( \dot{a} \) in the group of units of \( \mathbb{Z}/n\mathbb{Z} \) . We will show that \( m = n - 1 \) . Suppose \( m < n - 1 \) . Since \( {a}^{n - 1} \equiv 1\left( {\;\operatorname{mod}\;n}\right) , m \mid n - 1 \) and therefore there exists a prime number \( q \) dividing \( n - 1 \) such that \( m \mid \left( {n - 1}\right) /q \) . This implies that \( {a}^{\left( {n - 1}\right) /q} \equiv 1\left( {\;\operatorname{mod}\;n}\right) \) , which contradicts the hypotheses.

Donc \( m = n - 1 \) , ce qui prouve que le groupe des inversibles de \( \mathbb{Z}/n\mathbb{Z} \) admet au moins \( n - 1 \) éléments, ce qui n’est possible que si \( n \) est premier. D’où le résultat.

> Thus \( m = n - 1 \) , which proves that the group of units of \( \mathbb{Z}/n\mathbb{Z} \) admits at least \( n - 1 \) elements, which is only possible if \( n \) is prime. Hence the result.

b) Pour tout \( i \) , notons \( {m}_{i} \) l’ordre de \( {a}_{i} \) dans le groupe des inversibles de \( \mathbb{Z}/n\mathbb{Z} \) . Comme \( {a}_{i}^{n - 1} \equiv \; 1\left( {\;\operatorname{mod}\;n}\right) \) , on a \( {m}_{i}\left| {\;n - 1 = \mathop{\prod }\limits_{j}{p}_{j}^{{\alpha }_{j}}}\right. \) . Comme de plus \( {a}_{i}^{\left( {n - 1}\right) /{p}_{i}} \text{ ≢ } 1\left( {\;\operatorname{mod}\;n}\right) \) , on a aussi \( {m}_{i} \nmid {p}_{i}^{{\alpha }_{i} - 1}\mathop{\prod }\limits_{{j \neq i}}{p}_{j}^{{\alpha }_{j}} \) . Ces relations concernant \( {m}_{i} \) permettent d’affirmer que \( {p}_{i}^{{\alpha }_{i}} \mid {m}_{i} \) , et donc \( {p}_{i}^{{\alpha }_{i}} \mid \varphi \left( n\right) \) (où \( \varphi \) désigne l’indicateur d’Euler) puisque l’ordre de \( {a}_{i} \) divise l’ordre du groupe des inversibles de \( \mathbb{Z}/n\mathbb{Z} \) qui est \( \varphi \left( n\right) \) . Ceci étant vrai pour tout \( i \) , on en déduit, les \( {p}_{i} \) étant premiers distincts, que \( n - 1 = \mathop{\prod }\limits_{i}{p}_{i}^{{\alpha }_{i}}\left| {\varphi \left( n\right) \text{ , donc que }\varphi \left( n\right) \geq n - 1\text{ . Donc le groupe des inversibles de }}\right| \; \mathbb{Z}/n\mathbb{Z} \) comporte au moins \( n - 1 \) éléments, ce qui n’est possible que si \( n \) est premier.

> b) For all \( i \) , let \( {m}_{i} \) be the order of \( {a}_{i} \) in the group of units of \( \mathbb{Z}/n\mathbb{Z} \) . Since \( {a}_{i}^{n - 1} \equiv \; 1\left( {\;\operatorname{mod}\;n}\right) \) , we have \( {m}_{i}\left| {\;n - 1 = \mathop{\prod }\limits_{j}{p}_{j}^{{\alpha }_{j}}}\right. \) . Furthermore, since \( {a}_{i}^{\left( {n - 1}\right) /{p}_{i}} \text{ ≢ } 1\left( {\;\operatorname{mod}\;n}\right) \) , we also have \( {m}_{i} \nmid {p}_{i}^{{\alpha }_{i} - 1}\mathop{\prod }\limits_{{j \neq i}}{p}_{j}^{{\alpha }_{j}} \) . These relations concerning \( {m}_{i} \) allow us to assert that \( {p}_{i}^{{\alpha }_{i}} \mid {m}_{i} \) , and thus \( {p}_{i}^{{\alpha }_{i}} \mid \varphi \left( n\right) \) (where \( \varphi \) denotes Euler's totient function) since the order of \( {a}_{i} \) divides the order of the group of units of \( \mathbb{Z}/n\mathbb{Z} \) which is \( \varphi \left( n\right) \) . As this is true for all \( i \) , we deduce, the \( {p}_{i} \) being distinct primes, that \( n - 1 = \mathop{\prod }\limits_{i}{p}_{i}^{{\alpha }_{i}}\left| {\varphi \left( n\right) \text{ , donc que }\varphi \left( n\right) \geq n - 1\text{ . Donc le groupe des inversibles de }}\right| \; \mathbb{Z}/n\mathbb{Z} \) contains at least \( n - 1 \) elements, which is only possible if \( n \) is prime.

c) Soit \( m \) l’ordre de \( \dot{2} \) dans le groupe des inversibles de \( \mathbb{Z}/n\mathbb{Z} \) . On a \( {2}^{n - 1} \equiv 1\left( {\;\operatorname{mod}\;n}\right) \) donc \( m \mid n - 1 = h{p}^{2} \) . Or \( {2}^{h} \text{ ≢ } 1\left( {\;\operatorname{mod}\;n}\right) \) donc \( m \nmid h \) . Finalement, \( p \mid m \) (si \( p \nmid m \) , alors \( p \) étant premier \( m \land {p}^{2} = 1 \) et donc \( m \mid h \) d’après le théorème de Gauss). Comme \( m \) divise l’ordre du groupe des inversibles de \( \mathbb{Z}/n\mathbb{Z} \) qui est \( \varphi \left( n\right) \) , on en déduit \( p \mid \varphi \left( n\right) \;\left( *\right) \) .

> c) Let \( m \) be the order of \( \dot{2} \) in the group of units of \( \mathbb{Z}/n\mathbb{Z} \) . We have \( {2}^{n - 1} \equiv 1\left( {\;\operatorname{mod}\;n}\right) \) so \( m \mid n - 1 = h{p}^{2} \) . However \( {2}^{h} \text{ ≢ } 1\left( {\;\operatorname{mod}\;n}\right) \) so \( m \nmid h \) . Finally, \( p \mid m \) (if \( p \nmid m \) , then \( p \) being prime \( m \land {p}^{2} = 1 \) and thus \( m \mid h \) by Gauss's theorem). As \( m \) divides the order of the group of units of \( \mathbb{Z}/n\mathbb{Z} \) which is \( \varphi \left( n\right) \) , we deduce \( p \mid \varphi \left( n\right) \;\left( *\right) \) .

Si \( n = {p}_{1}^{{\alpha }_{1}}\cdots {p}_{k}^{{\alpha }_{k}} \) désigne la décomposition de \( n \) en facteurs premiers, on sait que \( \varphi \left( n\right) = \; {p}_{1}^{{\alpha }_{1} - 1}\cdots {p}_{k}^{{\alpha }_{k} - 1}\left( {{p}_{1} - 1}\right) \cdots \left( {{p}_{k} - 1}\right) \) . Comme \( p \nmid n = 1 + h{p}^{2} \) , on a \( p \neq {p}_{i} \) pour tout \( i \) donc il existe d’après \( \left( *\right) \) un indice \( i \) tel que \( p \mid {p}_{i} - 1 \) . Autrement dit, il existe un facteur premier \( q \) de \( n \) tel que \( q \equiv 1\left( {\;\operatorname{mod}\;p}\right) \) . Soit \( r \) l’entier vérifiant \( {qr} = n \) . On a \( {qr} \equiv n \equiv 1 + h{p}^{2} \equiv 1\left( {\;\operatorname{mod}\;p}\right) \) , donc \( r \equiv 1\left( {\;\operatorname{mod}\;p}\right) \) . En résumé, on a montré qu’il existe \( q \) premier, \( q \mid n \) et \( r \) entier tels que \( {qr} = n \) avec \( q = 1 + {up}, r = 1 + {vp}, u, v \in \mathbb{N} \) . Le nombre \( q \) étant premier on a d’ailleurs \( u \geq 2 \) (si \( u = 0 \) , \( q = 1 \) et si \( u = 1, q \) est pair).

> If \( n = {p}_{1}^{{\alpha }_{1}}\cdots {p}_{k}^{{\alpha }_{k}} \) denotes the prime factorization of \( n \), we know that \( \varphi \left( n\right) = \; {p}_{1}^{{\alpha }_{1} - 1}\cdots {p}_{k}^{{\alpha }_{k} - 1}\left( {{p}_{1} - 1}\right) \cdots \left( {{p}_{k} - 1}\right) \) . Since \( p \nmid n = 1 + h{p}^{2} \) , we have \( p \neq {p}_{i} \) for all \( i \) so there exists according to \( \left( *\right) \) an index \( i \) such that \( p \mid {p}_{i} - 1 \) . In other words, there exists a prime factor \( q \) of \( n \) such that \( q \equiv 1\left( {\;\operatorname{mod}\;p}\right) \) . Let \( r \) be the integer satisfying \( {qr} = n \) . We have \( {qr} \equiv n \equiv 1 + h{p}^{2} \equiv 1\left( {\;\operatorname{mod}\;p}\right) \) , so \( r \equiv 1\left( {\;\operatorname{mod}\;p}\right) \) . In summary, we have shown that there exist a prime \( q \) , \( q \mid n \) and an integer \( r \) such that \( {qr} = n \) with \( q = 1 + {up}, r = 1 + {vp}, u, v \in \mathbb{N} \) . Since \( q \) is prime, we also have \( u \geq 2 \) (if \( u = 0 \) , \( q = 1 \) and if \( u = 1, q \) is even).

Supposons \( r > 1 \) . Alors \( v \geq 1 \) . Or on a \( 1 + h{p}^{2} = n = {qr} = \left( {1 + {up}}\right) \left( {1 + {vp}}\right) \) donc \( {hp} = \; \left( {uv}\right) p + \left( {u + v}\right) \) , ce qui entraîne

> Suppose \( r > 1 \) . Then \( v \geq 1 \) . However, we have \( 1 + h{p}^{2} = n = {qr} = \left( {1 + {up}}\right) \left( {1 + {vp}}\right) \) so \( {hp} = \; \left( {uv}\right) p + \left( {u + v}\right) \) , which implies

\[
\text{ (i) }{uv} < h \leq  p - 1\;\text{ et }\;\text{ (ii) }\;\left( {u + v}\right)  \geq  p\text{ car }p \mid  \left( {u + v}\right)  \neq  0\text{ . }
\]

Comme \( u \geq 2 \) ,(i) entraîne \( v < \left( {p - 1}\right) /2 \) , et d’après (ii) \( u \geq 1 + p/2 \) , donc toujours d’après (i), \( v < \left( {p - 1}\right) /\left( {1 + \frac{p}{2}}\right) < 2 \) . Finalement \( v = 1 \) , ce qui est absurde car (i) entraînerait \( u < p - 1 \) et (ii) entraînerait \( u \geq p - 1 \) .

> Since \( u \geq 2 \) , (i) implies \( v < \left( {p - 1}\right) /2 \) , and according to (ii) \( u \geq 1 + p/2 \) , so still according to (i), \( v < \left( {p - 1}\right) /\left( {1 + \frac{p}{2}}\right) < 2 \) . Finally \( v = 1 \) , which is absurd because (i) would imply \( u < p - 1 \) and (ii) would imply \( u \geq p - 1 \) .

On a donc forcément \( r = 1 \) , ce qui entraîne que \( n = q \) est premier.

> We therefore necessarily have \( r = 1 \) , which implies that \( n = q \) is prime.

Remarque. Le test c) fut utilisé avec le nombre premier \( p = {2}^{127} - 1 \) pour montrer que \( n = 1 + {190}{p}^{2} \) est premier (Miller et Wheeler,1951). Les tests de primalité de ce type permettent de prouver de manière efficace la primalité de nombres entiers ayant une forme particulière. Par exemple, le record du plus grand nombre premier connu en 2020 est un nombre de Mersenne (de la forme \( {2}^{p} - 1 \) avec \( p \) premier), d’un peu moins de 25 millions de chiffres, établi en 2018 en utilisant le test de Lucas (décrit dans la remarque de l'exercice 4 page 13). Tester la primalité d'un nombre entier donné, sans forme particulière, est un problème algorithmique beaucoup plus difficile (jusqu'en 2020, les records de tests de primalité de nombres sans forme particuliere, établissent la primalité d'entiers de quelques dizaines de milliers de décimales).

> Remark. Test c) was used with the prime number \( p = {2}^{127} - 1 \) to show that \( n = 1 + {190}{p}^{2} \) is prime (Miller and Wheeler, 1951). Primality tests of this type allow for the efficient proof of primality for integers of a particular form. For example, the record for the largest known prime number in 2020 is a Mersenne number (of the form \( {2}^{p} - 1 \) with \( p \) prime), with just under 25 million digits, established in 2018 using the Lucas test (described in the remark of exercise 4 on page 13). Testing the primality of a given integer without a particular form is a much more difficult algorithmic problem (as of 2020, records for primality tests of numbers without a particular form establish the primality of integers with a few tens of thousands of decimal places).

Problem 4. Soit \( m \in {\mathbb{N}}^{ * }, m \geq 2 \) . Donner une condition nécéssaire et suffisante sur \( a \in {\mathbb{N}}^{ * } \) pour qu’il existe une application \( f : \mathbb{N} \rightarrow \mathbb{N} \) vérifiant \( {f}^{m}\left( n\right) = n + a \) pour tout \( n \in \mathbb{N} \) (ici \( {f}^{m} \) désigne la composition \( m \) fois de \( f \) avec elle même \( {f}^{m} = f \circ {f}^{m - 1} \) ). Supposons maintenant qu’il existe \( f : \mathbb{N} \rightarrow \mathbb{N} \) vérifiant \( {f}^{m}\left( n\right) = n + a \) pour tout \( n \in \mathbb{N} \) . On a

> Problem 4. Let \( m \in {\mathbb{N}}^{ * }, m \geq 2 \). Give a necessary and sufficient condition on \( a \in {\mathbb{N}}^{ * } \) such that there exists a map \( f : \mathbb{N} \rightarrow \mathbb{N} \) satisfying \( {f}^{m}\left( n\right) = n + a \) for all \( n \in \mathbb{N} \) (here \( {f}^{m} \) denotes the composition \( m \) times of \( f \) with itself \( {f}^{m} = f \circ {f}^{m - 1} \)). Now suppose that there exists \( f : \mathbb{N} \rightarrow \mathbb{N} \) satisfying \( {f}^{m}\left( n\right) = n + a \) for all \( n \in \mathbb{N} \). We have

\[
\forall n \in  \mathbb{N},\;f\left( {n + a}\right)  = f\left( {{f}^{m}\left( n\right) }\right)  = {f}^{m + 1}\left( n\right)  = {f}^{m}\left( {f\left( n\right) }\right)  = f\left( n\right)  + a.
\]

---

Solution. On va prouver que la condition nécéssaire et suffisante recherchée est que \( m \) divise a. La condition est bien suffisante, si \( m \mid a \) , il suffit de choisir pour \( f \) la fonction \( f\left( n\right) = n + \left( {a/m}\right) \) .

> Solution. We will prove that the necessary and sufficient condition sought is that \( m \) divides a. The condition is indeed sufficient; if \( m \mid a \), it suffices to choose the function \( f\left( n\right) = n + \left( {a/m}\right) \) for \( f \).

---

Un récurrence immédiate sur \( k \) entraine ensuite \( f\left( {n + {ka}}\right) = f\left( n\right) + {ka} \) pour tout \( \left( {n, k}\right) \in {\mathbb{N}}^{2} \) . Ainsi la valeur de \( f\left( {n + {ka}}\right) \) modulo \( a \) ne dépend pas de \( k \) , on peut donc définir la fonction \( \widetilde{f} \) de \( \mathbb{Z}/a\mathbb{Z} \) sur lui-même par \( \widetilde{f}\left( \bar{n}\right) = \overline{f\left( n\right) } \) . Cette fonction vérifie \( {\widetilde{f}}^{m} = \mathrm{{Id}} \) . On en déduit que \( \widetilde{f} \) est une permutation de \( \mathbb{Z}/a\mathbb{Z} \) , et que dans sa décomposition \( {c}_{1}\cdots {c}_{p} \) en produit de cycles de supports disjoints, chaque cycle \( {c}_{i} \) vérifie \( {c}_{i}^{m} = \) Id. En particulier la longueur \( {\ell }_{i} \) de \( {c}_{i} \) divise \( m \) . Nous allons montrer que \( {\ell }_{i} = m \) . Pour cela raisonnons par l’absurde et supposons que \( {\alpha }_{i} = m/{\ell }_{i} > 1 \) . Soit \( \overline{{x}_{i}} \) un des éléments du support de \( {c}_{i} \) , choisi de sorte que \( {x}_{i} < a \) . On a \( {c}_{i}^{{\ell }_{i}} = \) Id, donc il existe \( {k}_{i} \in \mathbb{N} \) tel que \( {f}^{{\ell }_{i}}\left( {x}_{i}\right) = {x}_{i} + a{k}_{i} \) . En posant \( g = {f}^{{\ell }_{i}} \) , on a donc \( g\left( {x}_{i}\right) = {x}_{i} + a{k}_{i} \) . L’identité \( f\left( {n + {ak}}\right) = f\left( n\right) + {ka} \) , pour tout \( n \) , entraîne, avec une récurrence facile sur \( j \) , que \( {f}^{j}\left( {n + {ak}}\right) = {f}^{j}\left( n\right) + {ak} \) pour tout \( j \in \mathbb{N} \) , en particulier \( g\left( {n + {ak}}\right) = g\left( n\right) + {ak} \) pour tout \( k \in \mathbb{N} \) . Comme \( g\left( {x}_{i}\right) = {x}_{i} + a{k}_{i} \) une récurrence sur \( j \) donne ensuite \( {g}^{j}\left( {x}_{i}\right) = {x}_{i} + {aj}{k}_{i} \) . On en déduit

> An immediate recurrence on \( k \) then leads to \( f\left( {n + {ka}}\right) = f\left( n\right) + {ka} \) for all \( \left( {n, k}\right) \in {\mathbb{N}}^{2} \) . Thus, the value of \( f\left( {n + {ka}}\right) \) modulo \( a \) does not depend on \( k \) , so we can define the function \( \widetilde{f} \) from \( \mathbb{Z}/a\mathbb{Z} \) to itself by \( \widetilde{f}\left( \bar{n}\right) = \overline{f\left( n\right) } \) . This function satisfies \( {\widetilde{f}}^{m} = \mathrm{{Id}} \) . We deduce that \( \widetilde{f} \) is a permutation of \( \mathbb{Z}/a\mathbb{Z} \) , and that in its decomposition \( {c}_{1}\cdots {c}_{p} \) into a product of disjoint cycles, each cycle \( {c}_{i} \) satisfies \( {c}_{i}^{m} = \) Id. In particular, the length \( {\ell }_{i} \) of \( {c}_{i} \) divides \( m \) . We will show that \( {\ell }_{i} = m \) . To do this, let us reason by contradiction and assume that \( {\alpha }_{i} = m/{\ell }_{i} > 1 \) . Let \( \overline{{x}_{i}} \) be one of the elements of the support of \( {c}_{i} \) , chosen such that \( {x}_{i} < a \) . We have \( {c}_{i}^{{\ell }_{i}} = \) Id, so there exists \( {k}_{i} \in \mathbb{N} \) such that \( {f}^{{\ell }_{i}}\left( {x}_{i}\right) = {x}_{i} + a{k}_{i} \) . By setting \( g = {f}^{{\ell }_{i}} \) , we therefore have \( g\left( {x}_{i}\right) = {x}_{i} + a{k}_{i} \) . The identity \( f\left( {n + {ak}}\right) = f\left( n\right) + {ka} \) , for all \( n \) , implies, with an easy recurrence on \( j \) , that \( {f}^{j}\left( {n + {ak}}\right) = {f}^{j}\left( n\right) + {ak} \) for all \( j \in \mathbb{N} \) , in particular \( g\left( {n + {ak}}\right) = g\left( n\right) + {ak} \) for all \( k \in \mathbb{N} \) . Since \( g\left( {x}_{i}\right) = {x}_{i} + a{k}_{i} \) a recurrence on \( j \) then gives \( {g}^{j}\left( {x}_{i}\right) = {x}_{i} + {aj}{k}_{i} \) . We deduce from this

\[
{x}_{i} + a = {f}^{m}\left( {x}_{i}\right)  = {g}^{{\alpha }_{i}}\left( {x}_{i}\right)  = {x}_{i} + a{\alpha }_{i}{k}_{i}.
\]

Ceci entraîne \( {\alpha }_{i}{k}_{i} = 1 \) , ce qui est absurde. Donc \( {\ell }_{i} = m \) pour tout \( i \) , donc \( a = \mathop{\sum }\limits_{{i = 1}}^{p}{\ell }_{i} = {pm} \) et le résultat est prouvé.

> This leads to \( {\alpha }_{i}{k}_{i} = 1 \) , which is absurd. Therefore \( {\ell }_{i} = m \) for all \( i \) , so \( a = \mathop{\sum }\limits_{{i = 1}}^{p}{\ell }_{i} = {pm} \) and the result is proven.

Problem 5 (Quelques cas particuliers du théorème de Dirichlet).

> Problem 5 (Some special cases of Dirichlet's theorem).

1/ a) Soit \( p > 2 \) un nombre premier. Montrer que \( - \overline{1} \) est un carré dans \( \mathbb{Z}/p\mathbb{Z} \) si et seulement si \( p \equiv 1\left( {\;\operatorname{mod}\;4}\right) \) .

> 1/ a) Let \( p > 2 \) be a prime number. Show that \( - \overline{1} \) is a square in \( \mathbb{Z}/p\mathbb{Z} \) if and only if \( p \equiv 1\left( {\;\operatorname{mod}\;4}\right) \) .

b) En déduire qu’il existe une infinité de nombres premiers de la forme \( 1 + {4n}, n \in \mathbb{N} \) .

> b) Deduce from this that there are infinitely many prime numbers of the form \( 1 + {4n}, n \in \mathbb{N} \) .

2/ (Un résultat plus général). Soient un nombre premier \( p > 2 \) et un entier \( m \geq 1 \) . Montrer que l’ensemble \( {\mathcal{P}}_{m} \) des nombres premiers de la forme \( 1 + {2}^{m}{pn}\left( {n \in \mathbb{N}}\right) \) , est infini. (Indication. Si \( {\mathcal{P}}_{m} \) est fini, considérer un nombre premier \( q \) divisant \( \left( {{M}^{p} + 1}\right) /\left( {M + 1}\right) \) où \( M = {K}^{{2}^{m - 1}}, K = p\left( {\mathop{\prod }\limits_{{n \in {\mathcal{P}}_{m}}}n}\right) \) , et montrer que \( q \in {\mathcal{P}}_{m} \) ).

> 2/ (A more general result). Let \( p > 2 \) be a prime number and \( m \geq 1 \) an integer. Show that the set \( {\mathcal{P}}_{m} \) of prime numbers of the form \( 1 + {2}^{m}{pn}\left( {n \in \mathbb{N}}\right) \) is infinite. (Hint: If \( {\mathcal{P}}_{m} \) is finite, consider a prime number \( q \) dividing \( \left( {{M}^{p} + 1}\right) /\left( {M + 1}\right) \) where \( M = {K}^{{2}^{m - 1}}, K = p\left( {\mathop{\prod }\limits_{{n \in {\mathcal{P}}_{m}}}n}\right) \) , and show that \( q \in {\mathcal{P}}_{m} \) ).

Solution. 1/ a) Condition nécessaire. Supposons qu’il existe \( x \in \mathbb{Z}/p\mathbb{Z},{x}^{2} = - \overline{1} \) . Le groupe multiplicatif \( {\left( \mathbb{Z}/p\mathbb{Z}\right) }^{ * } \) étant d’ordre \( p - 1 \) (car \( p \) est premier), on a \( {x}^{p - 1} = \overline{1} \) . Donc \( {\left( {x}^{2}\right) }^{\left( {p - 1}\right) /2} = \; {\left( -\overline{1}\right) }^{\left( {p - 1}\right) /2} = \overline{1} \) , ce qui n’est possible que si \( \left( {p - 1}\right) /2 \) est pair. D’où la condition nécessaire. Condition suffisante. C'est plus difficile. Donnons deux méthodes.

> Solution. 1/ a) Necessary condition. Suppose there exists \( x \in \mathbb{Z}/p\mathbb{Z},{x}^{2} = - \overline{1} \) . Since the multiplicative group \( {\left( \mathbb{Z}/p\mathbb{Z}\right) }^{ * } \) is of order \( p - 1 \) (because \( p \) is prime), we have \( {x}^{p - 1} = \overline{1} \) . Thus \( {\left( {x}^{2}\right) }^{\left( {p - 1}\right) /2} = \; {\left( -\overline{1}\right) }^{\left( {p - 1}\right) /2} = \overline{1} \) , which is only possible if \( \left( {p - 1}\right) /2 \) is even. Hence the necessary condition. Sufficient condition. This is more difficult. Let us provide two methods.

- Première méthode. Comme \( p \) est premier, \( \mathbb{Z}/p\mathbb{Z} \) est un corps. L’équation \( {x}^{\left( {p - 1}\right) /2} = \overline{1} \) a donc au plus \( \left( {p - 1}\right) /2 \) solutions dans \( \mathbb{Z}/p\mathbb{Z} \) . Comme \( {\left( \mathbb{Z}/p\mathbb{Z}\right) }^{ * } \) contient \( p - 1 > \left( {p - 1}\right) /2 \) éléments, il existe \( x \in  {\left( \mathbb{Z}/p\mathbb{Z}\right) }^{ * } \) tel que \( y = {x}^{\left( {p - 1}\right) /2} \neq  \overline{1} \) . On a \( {y}^{2} = {x}^{p - 1} = \overline{1} \) donc \( \left( {y - \overline{1}}\right) \left( {y + \overline{1}}\right)  = \overline{0} \) , donc \( y =  - \overline{1} \) (car \( y \neq  \overline{1} \) ). Or \( p \equiv  1\left( {\;\operatorname{mod}\;4}\right) \) , donc il existe un entier \( k \) tel que \( \left( {p - 1}\right) /2 = {2k} \) . Si \( z = {x}^{k} \) , on a donc \( {z}^{2} = {x}^{2k} = {x}^{\left( {p - 1}\right) /2} = y =  - \overline{1} \) , d’où le résultat.

> - First method. Since \( p \) is prime, \( \mathbb{Z}/p\mathbb{Z} \) is a field. The equation \( {x}^{\left( {p - 1}\right) /2} = \overline{1} \) therefore has at most \( \left( {p - 1}\right) /2 \) solutions in \( \mathbb{Z}/p\mathbb{Z} \) . Since \( {\left( \mathbb{Z}/p\mathbb{Z}\right) }^{ * } \) contains \( p - 1 > \left( {p - 1}\right) /2 \) elements, there exists \( x \in  {\left( \mathbb{Z}/p\mathbb{Z}\right) }^{ * } \) such that \( y = {x}^{\left( {p - 1}\right) /2} \neq  \overline{1} \) . We have \( {y}^{2} = {x}^{p - 1} = \overline{1} \) so \( \left( {y - \overline{1}}\right) \left( {y + \overline{1}}\right)  = \overline{0} \) , thus \( y =  - \overline{1} \) (because \( y \neq  \overline{1} \) ). However \( p \equiv  1\left( {\;\operatorname{mod}\;4}\right) \) , so there exists an integer \( k \) such that \( \left( {p - 1}\right) /2 = {2k} \) . If \( z = {x}^{k} \) , we therefore have \( {z}^{2} = {x}^{2k} = {x}^{\left( {p - 1}\right) /2} = y =  - \overline{1} \) , hence the result.

- Seconde méthode (cette méthode est moins générale que la précédente). Soit l’entier \( k \) tel que \( p = 1 + {4k} \) . Comme \( p \) est premier, on a d’après le théorème de Wilson

> - Second method (this method is less general than the previous one). Let \( k \) be the integer such that \( p = 1 + {4k} \) . Since \( p \) is prime, we have by Wilson's theorem

\[
1 \cdot  2\cdots \left( {2k}\right)  \cdot  \left( {{2k} + 1}\right) \cdots \left( {{4k} - 1}\right)  \cdot  \left( {4k}\right)  \equiv   - 1\;\left( {{\;\operatorname{mod}\;4}k + 1}\right) ,
\]

ce qui s'écrit aussi

> which can also be written as

\[
1 \cdot  2\cdots \left( {2k}\right)  \cdot  \left( {-{2k}}\right) \cdots \left( {-1}\right)  \equiv   - 1\;\left( {\;\operatorname{mod}\;p}\right)
\]

ou encore

> or also

\[
{\left( -1\right) }^{2k}{\left( 1 \cdot  2\cdots \left( 2k\right) \right) }^{2} \equiv   - 1\;\left( {\;\operatorname{mod}\;p}\right) .
\]

Si on pose \( x = 1 \cdot 2\cdots \left( {2k}\right) \) , ceci s’écrit \( {\bar{x}}^{2} = - \overline{1} \) dans \( \mathbb{Z}/p\mathbb{Z} \) , d’où le résultat.

> If we set \( x = 1 \cdot 2\cdots \left( {2k}\right) \) , this is written as \( {\bar{x}}^{2} = - \overline{1} \) in \( \mathbb{Z}/p\mathbb{Z} \) , hence the result.

b) Supposons qu’il y ait un nombre fini de nombres premiers de la forme \( {4k} + 1, k \in \mathbb{N} \) . Soit \( p \) le plus grand d’entre eux et soit \( N = 1 + {\left( p!\right) }^{2} \) . Soit un nombre premier \( q \) divisant \( N \) . Alors \( {\left( p!\right) }^{2} \equiv - 1\left( {\;\operatorname{mod}\;q}\right) \) , donc \( - \overline{1} \) est un carré dans \( \mathbb{Z}/q\mathbb{Z} \) et donc \( q \) est de la forme \( {4k} + 1, k \in \mathbb{N} \)

> b) Suppose there is a finite number of prime numbers of the form \( {4k} + 1, k \in \mathbb{N} \) . Let \( p \) be the largest of them and let \( N = 1 + {\left( p!\right) }^{2} \) . Let \( q \) be a prime number dividing \( N \) . Then \( {\left( p!\right) }^{2} \equiv - 1\left( {\;\operatorname{mod}\;q}\right) \) , so \( - \overline{1} \) is a square in \( \mathbb{Z}/q\mathbb{Z} \) and thus \( q \) is of the form \( {4k} + 1, k \in \mathbb{N} \)

d’après a). Donc \( q \leq p \) , donc \( q \mid p \) !, donc \( q \mid 1 = N - {\left( p!\right) }^{2} \) , ce qui est absurde. Il y a donc une infinité de nombres premiers de la forme \( {4k} + 1, k \in \mathbb{N} \) .

> according to a). Thus \( q \leq p \) , so \( q \mid p \) !, so \( q \mid 1 = N - {\left( p!\right) }^{2} \) , which is absurd. There is therefore an infinite number of prime numbers of the form \( {4k} + 1, k \in \mathbb{N} \) .

2/ Supposons \( {\mathcal{P}}_{m} \) fini. Suivons l’indication en considérant l’entier \( N = \left( {{M}^{p} + 1}\right) /\left( {M + 1}\right) = \; {M}^{p - 1} - {M}^{p - 2} + \cdots - M + 1 \) avec \( M = {K}^{{2}^{m - 1}} \) où \( K = p\left( {\mathop{\prod }\limits_{{n \in {\mathcal{P}}_{m}}}n}\right) \) . Comme \( N > 1 \) , il existe un nombre premier \( q \) divisant \( N \) . On a \( {M}^{p} + 1 \equiv 0\left( {\;\operatorname{mod}\;q}\right) \) donc

> 2/ Suppose \( {\mathcal{P}}_{m} \) is finite. Let us follow the hint by considering the integer \( N = \left( {{M}^{p} + 1}\right) /\left( {M + 1}\right) = \; {M}^{p - 1} - {M}^{p - 2} + \cdots - M + 1 \) with \( M = {K}^{{2}^{m - 1}} \) where \( K = p\left( {\mathop{\prod }\limits_{{n \in {\mathcal{P}}_{m}}}n}\right) \) . Since \( N > 1 \) , there exists a prime number \( q \) dividing \( N \) . We have \( {M}^{p} + 1 \equiv 0\left( {\;\operatorname{mod}\;q}\right) \) so

\[
{K}^{{2}^{m - 1}p} \equiv  {M}^{p} \equiv   - 1\;\left( {\;\operatorname{mod}\;q}\right) \;\text{ et }\;{K}^{{2}^{m}p} \equiv  1\;\left( {\;\operatorname{mod}\;q}\right) .
\]

L’égalité de droite montre que l’ordre \( r \) de \( \bar{K} \) dans le groupe multiplicatif \( {\left( \mathbb{Z}/q\mathbb{Z}\right) }^{ * } \) divise \( {2}^{m}p \) . L’égalité de gauche montre que \( r \nmid {2}^{m - 1}p \) . Comme \( p \) est premier, on a donc \( r = {2}^{m} \) ou \( r = {2}^{m}p \) . Si \( r = {2}^{m} \) , comme \( N \) divise

> The equality on the right shows that the order \( r \) of \( \bar{K} \) in the multiplicative group \( {\left( \mathbb{Z}/q\mathbb{Z}\right) }^{ * } \) divides \( {2}^{m}p \) . The equality on the left shows that \( r \nmid {2}^{m - 1}p \) . Since \( p \) is prime, we therefore have \( r = {2}^{m} \) or \( r = {2}^{m}p \) . If \( r = {2}^{m} \) , since \( N \) divides

\[
{\left( {M}^{2}\right) }^{p - 1} + \cdots  + {M}^{2} + 1 = \frac{{M}^{2p} - 1}{{M}^{2} - 1} = \frac{{M}^{p} - 1}{M - 1} \cdot  \frac{{M}^{p} + 1}{M + 1}
\]

et que \( {M}^{2} = {K}^{{2}^{m}} \equiv 1\left( {\;\operatorname{mod}\;q}\right) \) , on a

> and that \( {M}^{2} = {K}^{{2}^{m}} \equiv 1\left( {\;\operatorname{mod}\;q}\right) \) , we have

\[
0 \equiv  {\left( {M}^{2}\right) }^{p - 1} + \cdots  + {M}^{2} + 1 \equiv  p\;\left( {\;\operatorname{mod}\;q}\right)
\]

donc \( q \mid p \) , donc \( q \mid M \) , ce qui est absurde vu que \( q \mid {M}^{p} + 1 \) . Ainsi, \( r = {2}^{m}p \) et comme l’ordre de tout élément de \( {\left( \mathbb{Z}/q\mathbb{Z}\right) }^{ * } \) divise \( q - 1 \) , on a \( {2}^{m}p \mid q - 1 \) c’est-à-dire \( q \in {\mathcal{P}}_{m} \) . Ceci entraîne \( q \mid M \) ce qui est impossible. L’ensemble \( {\mathcal{P}}_{m} \) est donc infini.

> so \( q \mid p \) , so \( q \mid M \) , which is absurd given that \( q \mid {M}^{p} + 1 \) . Thus, \( r = {2}^{m}p \) and since the order of any element of \( {\left( \mathbb{Z}/q\mathbb{Z}\right) }^{ * } \) divides \( q - 1 \) , we have \( {2}^{m}p \mid q - 1 \) that is to say \( q \in {\mathcal{P}}_{m} \) . This implies \( q \mid M \) which is impossible. The set \( {\mathcal{P}}_{m} \) is therefore infinite.

Remarque. Ces résultats sont des cas particuliers du théorème de Dirichlet (voir la remarque qui suit l'exercice 7 page 14). D'autres formes particulières du théorème de Dirichlet font l'objet du sujet d'étude 2 page 49 ou du problème 11 page 99.

> Remark. These results are special cases of Dirichlet's theorem (see the remark following exercise 7 on page 14). Other special forms of Dirichlet's theorem are the subject of study 2 on page 49 or problem 11 on page 99.

PROBLEME 6 (ANNEAUX EUCLIDIENS). 1/ Soit \( A \) un anneau commutatif unitaire in-tègre. On dit que \( A \) est euclidien s’il existe une application \( f : {A}^{ * } = A \smallsetminus \{ 0\} \rightarrow \mathbb{N} \) telle que

> PROBLEM 6 (EUCLIDEAN RINGS). 1/ Let \( A \) be a commutative unitary integral domain. We say that \( A \) is Euclidean if there exists a map \( f : {A}^{ * } = A \smallsetminus \{ 0\} \rightarrow \mathbb{N} \) such that

(i) \( \forall x, y \in {A}^{ * },\;f\left( {xy}\right) \geq f\left( y\right) \) ,

> (ii) \( \forall a \in A,\forall b \in {A}^{ * },\exists \left( {q, r}\right) \in {A}^{2} \) , tel que \( a = {bq} + r \) , avec \( r = 0 \) ou \( f\left( r\right) < f\left( b\right) \) .

(ii) \( \forall a \in A,\forall b \in {A}^{ * },\exists \left( {q, r}\right) \in {A}^{2} \) , such that \( a = {bq} + r \) , with \( r = 0 \) or \( f\left( r\right) < f\left( b\right) \) .

> a) Si \( A \) est euclidien, montrer que \( A \) est principal.

a) If \( A \) is Euclidean, show that \( A \) is a principal ideal domain.

> b) Si l’application \( f \) vérifie l’hypothèse supplémentaire

b) If the map \( f \) satisfies the additional hypothesis

> (iii) \( \forall x, y \in {A}^{ * }, x \neq y,\;f\left( {x - y}\right) \leq \sup \{ f\left( x\right) , f\left( y\right) \} \) ,

(iii) \( \forall x, y \in {A}^{ * }, x \neq y,\;f\left( {x - y}\right) \leq \sup \{ f\left( x\right) , f\left( y\right) \} \) ,

> montrer que le couple \( \left( {q, r}\right) \) dans (ii) est unique.

show that the pair \( \left( {q, r}\right) \) in (ii) is unique.

> c) Caractériser les éléments inversibles d'un anneau unitaire euclidien.

c) Characterize the invertible elements of a unitary Euclidean ring.

> 2/ Soit l’anneau des entiers de Gauss \( \mathbb{Z}\left\lbrack i\right\rbrack = \left\{ {x + {iy} \mid \left( {x, y}\right) \in {\mathbb{Z}}^{2}}\right\} \) .

2/ Let \( \mathbb{Z}\left\lbrack i\right\rbrack = \left\{ {x + {iy} \mid \left( {x, y}\right) \in {\mathbb{Z}}^{2}}\right\} \) be the ring of Gaussian integers.

> a) Montrer que si \( z \in \mathbb{C} \) , il existe \( {z}_{0} \in \mathbb{Z}\left\lbrack i\right\rbrack \) tel que \( \left| {z - {z}_{0}}\right| < 1 \) .

a) Show that if \( z \in \mathbb{C} \) , there exists \( {z}_{0} \in \mathbb{Z}\left\lbrack i\right\rbrack \) such that \( \left| {z - {z}_{0}}\right| < 1 \) .

> b) En déduire que \( \mathbb{Z}\left\lbrack i\right\rbrack \) est un anneau principal.

b) Deduce that \( \mathbb{Z}\left\lbrack i\right\rbrack \) is a principal ideal domain.

> c) Quels sont les inversibles de \( \mathbb{Z}\left\lbrack i\right\rbrack \) ?

c) What are the invertible elements of \( \mathbb{Z}\left\lbrack i\right\rbrack \) ?

> Solution. 1/ a) Soit \( I \) un idéal de \( A \) . Si \( I = \{ 0\} , I \) est évidemment principal. Si \( I \neq \{ 0\} \) , on considère l’ensemble \( \Gamma = \left\{ {f\left( x\right) \mid x \in {I}^{ * }}\right\} \subset \mathbb{N} \) . Soit \( a \in {I}^{ * } \) tel que \( f\left( a\right) = \inf \Gamma \) . Prenons maintenant un élément \( x \in I \) . D’après (ii),

Solution. 1/ a) Let \( I \) be an ideal of \( A \) . If \( I = \{ 0\} , I \) it is obviously principal. If \( I \neq \{ 0\} \) , we consider the set \( \Gamma = \left\{ {f\left( x\right) \mid x \in {I}^{ * }}\right\} \subset \mathbb{N} \) . Let \( a \in {I}^{ * } \) be such that \( f\left( a\right) = \inf \Gamma \) . Now take an element \( x \in I \) . According to (ii),

\[
\exists \left( {q, r}\right)  \in  {A}^{2},\;\left( {x = {aq} + r\text{ avec }f\left( r\right)  < f\left( a\right) \text{ ou }r = 0}\right) .
\]

Remarquons que \( r = x - {aq} \in I \) . Si \( r \neq 0 \) , alors \( f\left( r\right) < f\left( a\right) \) ce qui est absurde puisque \( r \in {I}^{ * } \) et \( f\left( a\right) = \inf \Gamma \) . Donc \( r = 0 \) , donc \( x = {aq} \) . On vient de montrer que \( I \subset \left( a\right) \) . Réciproquement, comme \( a \in I \) , on a \( \left( a\right) \subset I \) . Donc \( I = \left( a\right) \) et \( A \) est principal.

> Note that \( r = x - {aq} \in I \) . If \( r \neq 0 \) , then \( f\left( r\right) < f\left( a\right) \) which is absurd since \( r \in {I}^{ * } \) and \( f\left( a\right) = \inf \Gamma \) . Thus \( r = 0 \) , so \( x = {aq} \) . We have just shown that \( I \subset \left( a\right) \) . Conversely, as \( a \in I \) , we have \( \left( a\right) \subset I \) . Therefore \( I = \left( a\right) \) and \( A \) is principal.

b) Soit \( \left( {a, b}\right) \in A \times {A}^{ * } \) . Soient deux couples \( \left( {q, r}\right) \) et \( \left( {{q}^{\prime },{r}^{\prime }}\right) \) vérifiant (ii) pour \( \left( {a, b}\right) \) . L’égalité \( {bq} + r = b{q}^{\prime } + {r}^{\prime } \) s’écrit aussi \( b\left( {q - {q}^{\prime }}\right) = {r}^{\prime } - r \) . Si \( q \neq {q}^{\prime } \) , on a \( {r}^{\prime } - r \neq 0 \) et \( f\left( b\right) \leq f\left\lbrack {b\left( {q - {q}^{\prime }}\right) }\right\rbrack = \; f\left( {{r}^{\prime } - r}\right) \;\left( *\right) \) . Si \( r = 0 \) (le cas \( {r}^{\prime } = 0 \) se traite en échangeant les rôles de \( \left( {q, r}\right) \) et \( \left. \left( {{q}^{\prime },{r}^{\prime }}\right) \right) \) ,

> b) Let \( \left( {a, b}\right) \in A \times {A}^{ * } \) . Let two pairs \( \left( {q, r}\right) \) and \( \left( {{q}^{\prime },{r}^{\prime }}\right) \) satisfy (ii) for \( \left( {a, b}\right) \) . The equality \( {bq} + r = b{q}^{\prime } + {r}^{\prime } \) is also written \( b\left( {q - {q}^{\prime }}\right) = {r}^{\prime } - r \) . If \( q \neq {q}^{\prime } \) , we have \( {r}^{\prime } - r \neq 0 \) and \( f\left( b\right) \leq f\left\lbrack {b\left( {q - {q}^{\prime }}\right) }\right\rbrack = \; f\left( {{r}^{\prime } - r}\right) \;\left( *\right) \) . If \( r = 0 \) (the case \( {r}^{\prime } = 0 \) is handled by swapping the roles of \( \left( {q, r}\right) \) and \( \left. \left( {{q}^{\prime },{r}^{\prime }}\right) \right) \) ,

(*) entraîne \( f\left( b\right) \leq f\left( {r}^{\prime }\right) < f\left( b\right) \) , ce qui est absurde. Si \( r \neq 0 \) et \( {r}^{\prime } \neq 0 \) , alors (*) entraîne \( f\left( b\right) \leq \sup \left\{ {f\left( r\right) , f\left( {r}^{\prime }\right) }\right\} < f\left( b\right) \) , ce qui est également absurde. On a donc forcément \( q = {q}^{\prime } \) et donc \( r = {r}^{\prime } \) .

> (*) implies \( f\left( b\right) \leq f\left( {r}^{\prime }\right) < f\left( b\right) \) , which is absurd. If \( r \neq 0 \) and \( {r}^{\prime } \neq 0 \) , then (*) implies \( f\left( b\right) \leq \sup \left\{ {f\left( r\right) , f\left( {r}^{\prime }\right) }\right\} < f\left( b\right) \) , which is also absurd. We therefore necessarily have \( q = {q}^{\prime } \) and thus \( r = {r}^{\prime } \) .

c) Soit \( \alpha = \inf \left\{ {f\left( x\right) \mid x \in {A}^{ * }}\right\} \) . Nous allons montrer que \( x \in {A}^{ * } \) est inversible si et seulement si \( f\left( x\right) = \alpha . \)

> c) Let \( \alpha = \inf \left\{ {f\left( x\right) \mid x \in {A}^{ * }}\right\} \) . We will show that \( x \in {A}^{ * } \) is invertible if and only if \( f\left( x\right) = \alpha . \)

Condition nécessaire. Si \( x \) est inversible, alors il existe \( y \in {A}^{ * },{xy} = 1 \) . Donc \( \forall z \in {A}^{ * }, f\left( z\right) = \; f\left\lbrack {x\left( {yz}\right) }\right\rbrack \geq f\left( x\right) \) d’après (i), donc \( f\left( x\right) = \alpha \) .

> Necessary condition. If \( x \) is invertible, then there exists \( y \in {A}^{ * },{xy} = 1 \) . Thus \( \forall z \in {A}^{ * }, f\left( z\right) = \; f\left\lbrack {x\left( {yz}\right) }\right\rbrack \geq f\left( x\right) \) according to (i), so \( f\left( x\right) = \alpha \) .

Condition suffisante. Appliquant (ii) à \( \left( {a, b}\right) = \left( {1, x}\right) \) , on voit qu’il existe \( \left( {q, r}\right) \in {A}^{2} \) tel que \( 1 = {qx} + r \) avec \( r = 0 \) ou \( f\left( r\right) < f\left( x\right) \) . Cette dernière assertion est impossible car \( f\left( x\right) = \alpha \) , donc \( r = 0 \) et donc \( {bx} = 1 \) . L’élément \( x \) est donc inversible (on a aussi \( {xb} = 1 \) car \( A \) est commutatif).

> Sufficient condition. Applying (ii) to \( \left( {a, b}\right) = \left( {1, x}\right) \), we see that there exists \( \left( {q, r}\right) \in {A}^{2} \) such that \( 1 = {qx} + r \) with \( r = 0 \) or \( f\left( r\right) < f\left( x\right) \). This last assertion is impossible because \( f\left( x\right) = \alpha \), therefore \( r = 0 \) and thus \( {bx} = 1 \). The element \( x \) is therefore invertible (we also have \( {xb} = 1 \) because \( A \) is commutative).

2/ a) Soit \( z = x + {iy} \in \mathbb{C},\left( {x, y}\right) \in {\mathbb{R}}^{2} \) . En désignant par \( {x}_{0},{y}_{0} \in \mathbb{Z} \) les entiers les plus proches de \( x \) et \( y \) , on a \( \left| {x - {x}_{0}}\right| \leq 1/2 \) et \( \left| {y - {y}_{0}}\right| \leq 1/2 \) . Ainsi l’entier de Gauss \( {z}_{0} = {x}_{0} + i{y}_{0} \in \mathbb{Z}\left\lbrack i\right\rbrack \) vérifie \( {\left| z - {z}_{0}\right| }^{2} = {\left( x - {x}_{0}\right) }^{2} + {\left( y - {y}_{0}\right) }^{2} \leq 1/2 \) , donc \( \left| {z - {z}_{0}}\right| < 1 \) .

> 2/ a) Let \( z = x + {iy} \in \mathbb{C},\left( {x, y}\right) \in {\mathbb{R}}^{2} \). By denoting by \( {x}_{0},{y}_{0} \in \mathbb{Z} \) the integers closest to \( x \) and \( y \), we have \( \left| {x - {x}_{0}}\right| \leq 1/2 \) and \( \left| {y - {y}_{0}}\right| \leq 1/2 \). Thus the Gaussian integer \( {z}_{0} = {x}_{0} + i{y}_{0} \in \mathbb{Z}\left\lbrack i\right\rbrack \) satisfies \( {\left| z - {z}_{0}\right| }^{2} = {\left( x - {x}_{0}\right) }^{2} + {\left( y - {y}_{0}\right) }^{2} \leq 1/2 \), therefore \( \left| {z - {z}_{0}}\right| < 1 \).

b) D’après le résultat de la question \( 1/\mathrm{a} \) ), il suffit de montrer que \( \mathbb{Z}\left\lbrack i\right\rbrack \) est euclidien. Soit \( \left( {a, b}\right) \in \; \mathbb{Z}\left\lbrack i\right\rbrack \times \mathbb{Z}{\left\lbrack i\right\rbrack }^{ * } \) . D’après la question précédente, il existe \( q \in \mathbb{Z}\left\lbrack i\right\rbrack \) tel que \( \left| {q - a/b}\right| < 1 \) . En posant \( r = a - {bq} \) , on a donc \( a = {bq} + r \) avec \( \left| r\right| = \left| b\right| \left| {a/b - q}\right| < \left| b\right| \) , ce qui montre qu’en prenant \( f\left( z\right) = {\left| z\right| }^{2} = {x}^{2} + {y}^{2} \) pour \( z = x + {iy} \in \mathbb{Z}{\left\lbrack i\right\rbrack }^{ * } \) ,(ii) est vérifié. Or pour tout \( x \in \mathbb{Z}{\left\lbrack i\right\rbrack }^{ * }, f\left( x\right) \geq 1 \) , donc \( \forall y \in \mathbb{Z}{\left\lbrack i\right\rbrack }^{ * }, f\left( {xy}\right) = f\left( x\right) f\left( y\right) \geq f\left( y\right) \) . La condition (i) est donc vérifiée. Finalement, \( \mathbb{Z}\left\lbrack i\right\rbrack \) est euclidien.

> b) According to the result of question \( 1/\mathrm{a} \)), it suffices to show that \( \mathbb{Z}\left\lbrack i\right\rbrack \) is Euclidean. Let \( \left( {a, b}\right) \in \; \mathbb{Z}\left\lbrack i\right\rbrack \times \mathbb{Z}{\left\lbrack i\right\rbrack }^{ * } \). According to the previous question, there exists \( q \in \mathbb{Z}\left\lbrack i\right\rbrack \) such that \( \left| {q - a/b}\right| < 1 \). By setting \( r = a - {bq} \), we therefore have \( a = {bq} + r \) with \( \left| r\right| = \left| b\right| \left| {a/b - q}\right| < \left| b\right| \), which shows that by taking \( f\left( z\right) = {\left| z\right| }^{2} = {x}^{2} + {y}^{2} \) for \( z = x + {iy} \in \mathbb{Z}{\left\lbrack i\right\rbrack }^{ * } \), (ii) is satisfied. Now for any \( x \in \mathbb{Z}{\left\lbrack i\right\rbrack }^{ * }, f\left( x\right) \geq 1 \), therefore \( \forall y \in \mathbb{Z}{\left\lbrack i\right\rbrack }^{ * }, f\left( {xy}\right) = f\left( x\right) f\left( y\right) \geq f\left( y\right) \). Condition (i) is therefore satisfied. Finally, \( \mathbb{Z}\left\lbrack i\right\rbrack \) is Euclidean.

c) D’après \( 1/\mathrm{c} \) ), les inversibles de \( \mathbb{Z}\left\lbrack i\right\rbrack \) sont les éléments \( z \) vérifiant \( f\left( z\right) = {\left| z\right| }^{2} = 1 \) . Ce sont donc \( 1, - 1, i \) et \( - i \) .

> c) According to \( 1/\mathrm{c} \) ), the invertible elements of \( \mathbb{Z}\left\lbrack i\right\rbrack \) are the elements \( z \) satisfying \( f\left( z\right) = {\left| z\right| }^{2} = 1 \) . These are therefore \( 1, - 1, i \) and \( - i \) .

Remarque. Les anneaux euclidiens généralisent les propriétés de la division euclidienne des anneaux \( \mathbb{Z} \) et \( \mathbb{K}\left\lbrack X\right\rbrack \) (on a \( f\left( x\right) = \left| x\right| \) pour \( \mathbb{Z} \) et \( f\left( P\right) = \deg \left( P\right) \) pour \( \mathbb{K}\left\lbrack X\right\rbrack \) ).

> Remark. Euclidean rings generalize the properties of Euclidean division of the rings \( \mathbb{Z} \) and \( \mathbb{K}\left\lbrack X\right\rbrack \) (we have \( f\left( x\right) = \left| x\right| \) for \( \mathbb{Z} \) and \( f\left( P\right) = \deg \left( P\right) \) for \( \mathbb{K}\left\lbrack X\right\rbrack \) ).

Problem 7. Soit \( G \) un groupe fini tel que pour tout entier \( d \geq 1 \) , l’équation \( {x}^{d} = e \) (où \( e \) désigne le neutre de \( G \) ) a au plus \( d \) solutions dans \( G \) . Montrer que \( G \) est un groupe cyclique.

> Problem 7. Let \( G \) be a finite group such that for every integer \( d \geq 1 \) , the equation \( {x}^{d} = e \) (where \( e \) denotes the identity of \( G \) ) has at most \( d \) solutions in \( G \) . Show that \( G \) is a cyclic group.

Solution. Notons \( n \) l’ordre du groupe \( G \) . Pour tout entier \( d \) divisant \( n \) , notons \( {\Psi }_{d} \) l’ensemble des éléments de \( G \) d’ordre \( d \) . L’ordre de tout élément de \( G \) divise \( n \) , donc la famille \( {\left( {\Psi }_{d}\right) }_{d \mid n} \) forme une partition de \( G \) . Si \( {\psi }_{d} = \operatorname{Card}\left( {\Psi }_{d}\right) \) , on a donc \( \mathop{\sum }\limits_{{d \mid n}}{\psi }_{d} = n\;\left( *\right) \) .

> Solution. Let \( n \) be the order of the group \( G \) . For every integer \( d \) dividing \( n \) , let \( {\Psi }_{d} \) be the set of elements of \( G \) of order \( d \) . The order of any element of \( G \) divides \( n \) , so the family \( {\left( {\Psi }_{d}\right) }_{d \mid n} \) forms a partition of \( G \) . If \( {\psi }_{d} = \operatorname{Card}\left( {\Psi }_{d}\right) \) , we therefore have \( \mathop{\sum }\limits_{{d \mid n}}{\psi }_{d} = n\;\left( *\right) \) .

Nous allons maintenant montrer que si \( d \mid n,{\psi }_{d} \leq \varphi \left( d\right) \;\left( {* * }\right) \) où \( \varphi \) désigne l’indicateur d’Euler. Si \( {\psi }_{d} = 0 \) , c’est terminé. Sinon \( {\psi }_{d} \geq 1 \) et donc il existe \( {x}_{0} \in {\Psi }_{d} \) . Tous les éléments \( x \) de \( \left\langle {x}_{0}\right\rangle \) vérifient alors \( {x}^{d} = 1 \) . Or \( \left\langle {x}_{0}\right\rangle \) a \( d \) éléments et l’équation \( {x}^{d} = e \) a au plus \( d \) solutions. Les éléments qui vérifient \( {x}^{d} = e \) sont donc les éléments de \( \left\langle {x}_{0}\right\rangle \) . Donc \( {\Psi }_{d} \subset \left\langle {x}_{0}\right\rangle \) et \( {\Psi }_{d} \) correspond donc à l'ensemble des générateurs de \( \left\langle {x}_{0}\right\rangle \) qui, d’après la proposition 5 page 22, est de cardinal \( \varphi \left( d\right) \) . Donc \( {\psi }_{d} = \varphi \left( d\right) \) , d’où \( \left( {* * }\right) \) .

> We will now show that if \( d \mid n,{\psi }_{d} \leq \varphi \left( d\right) \;\left( {* * }\right) \) where \( \varphi \) denotes Euler's totient function. If \( {\psi }_{d} = 0 \) , we are done. Otherwise \( {\psi }_{d} \geq 1 \) and thus there exists \( {x}_{0} \in {\Psi }_{d} \) . All elements \( x \) of \( \left\langle {x}_{0}\right\rangle \) then satisfy \( {x}^{d} = 1 \) . However, \( \left\langle {x}_{0}\right\rangle \) has \( d \) elements and the equation \( {x}^{d} = e \) has at most \( d \) solutions. The elements that satisfy \( {x}^{d} = e \) are therefore the elements of \( \left\langle {x}_{0}\right\rangle \) . Thus \( {\Psi }_{d} \subset \left\langle {x}_{0}\right\rangle \) and \( {\Psi }_{d} \) therefore corresponds to the set of generators of \( \left\langle {x}_{0}\right\rangle \) which, according to proposition 5 on page 22, has cardinality \( \varphi \left( d\right) \) . Thus \( {\psi }_{d} = \varphi \left( d\right) \) , hence \( \left( {* * }\right) \) .

Or \( \mathop{\sum }\limits_{{d \mid n}}\varphi \left( d\right) = n \) (voir proposition 6 page 34). De (*) et (*) on en déduit que pour tout diviseur \( d \) de \( n \) , on a \( {\psi }_{d} = \varphi \left( d\right) \) . En particulier \( {\psi }_{n} = \varphi \left( n\right) > 0 \) , donc il existe au moins un élément d'ordre \( n \) , d’où le résultat.

> Or \( \mathop{\sum }\limits_{{d \mid n}}\varphi \left( d\right) = n \) (see proposition 6 page 34). From (*) and (*) we deduce that for any divisor \( d \) of \( n \), we have \( {\psi }_{d} = \varphi \left( d\right) \). In particular \( {\psi }_{n} = \varphi \left( n\right) > 0 \), so there exists at least one element of order \( n \), hence the result.

Remarque. Il découle de ce problème le résultat annoncé dans la remarque de l'exercice 10 page 28.

> Remark. It follows from this problem the result announced in the remark of exercise 10 page 28.

Problem 8. 1 / Pour tout \( n \in {\mathbb{N}}^{ * }, n \geq 3 \) , on note \( {D}_{n} \) le \( n \) -ième groupe diédral, constitué des isométries du plan qui conservent l’ensemble des sommets du polygône régulier de \( n \) cotés défini par \( {P}_{n} = \left\{ {{S}_{k} \mid 0 \leq k \leq n - 1}\right\} \) où \( {S}_{k} = \left( {\cos {2k\pi }/n,\sin {2k\pi }/n}\right) \) .

> Problem 8. 1 / For any \( n \in {\mathbb{N}}^{ * }, n \geq 3 \), we denote by \( {D}_{n} \) the \( n \)-th dihedral group, consisting of the isometries of the plane that preserve the set of vertices of the regular polygon with \( n \) sides defined by \( {P}_{n} = \left\{ {{S}_{k} \mid 0 \leq k \leq n - 1}\right\} \) where \( {S}_{k} = \left( {\cos {2k\pi }/n,\sin {2k\pi }/n}\right) \).

a) Montrer que \( {D}_{n} \) est un groupe d’ordre \( {2n} \) , non abélien.

> a) Show that \( {D}_{n} \) is a group of order \( {2n} \), non-abelian.

b) Déterminer le centre de \( {D}_{n} \) .

> b) Determine the center of \( {D}_{n} \).

2/a) Soit \( G \) un groupe fini non-abélien. Montrer que \( G/\mathcal{Z}\left( G\right) \) est non-cyclique. Montrer que \( G/\mathcal{Z}\left( G\right) \) peut être abélien.

> 2/a) Let \( G \) be a non-abelian finite group. Show that \( G/\mathcal{Z}\left( G\right) \) is non-cyclic. Show that \( G/\mathcal{Z}\left( G\right) \) can be abelian.

b) Montrer que la probabilité \( p \) que deux éléments de \( G \) commutent est inférieur à \( 5/8 \) , et exhiber un cas où on a \( p = 5/8 \) .

> b) Show that the probability \( p \) that two elements of \( G \) commute is less than \( 5/8 \), and exhibit a case where we have \( p = 5/8 \).

Solution. 1/a) Le sous-groupe \( {D}_{n}^{ + } \) de \( {D}_{n} \) formé de ses isométries directes, est constitué des rotations qui conservent \( {P}_{n} \) , c’est donc l’ensemble des rotations \( {r}_{k} \) d’angle \( {2k\pi }/n \) pour \( 0 \leq k \leq \; n - 1 \) . Par ailleurs, \( {P}_{n} \) est conservé par la symétrie \( \sigma \) par rapport à l’axe \( y = 0 \) . On en déduit \( \left\{ {{\sigma }^{j}{r}_{1}^{k} \mid j \in \{ 0,1\} ,0 \leq k < n}\right\} \subset {D}_{n} \) . Réciproquement si \( \mu \in {D}_{n} \) , alors soit \( \mu \) est une isométrie directe donc \( \mu = {r}_{k} = {r}_{1}^{k} \) pour \( 0 \leq k < n \) , soit \( {\sigma \mu } \) est une isométrie directe, donc \( {\sigma \mu } = {r}_{1}^{k} \) pour \( 0 \leq k < n \) , donc \( \mu = \sigma {r}_{1}^{k} \) . On a donc \( {D}_{n} = \left\{ {{\sigma }^{j}{r}_{1}^{k} \mid j \in \{ 0,1\} ,0 \leq k < n}\right\} \) et comme les \( {\sigma }^{j}{r}_{1}^{k} \) pour \( j \in \{ 0,1\} ,0 \leq k < n \) sont tous distincts, on a bien \( \left| {D}_{n}\right| = {2n} \) .

> Solution. 1/a) The subgroup \( {D}_{n}^{ + } \) of \( {D}_{n} \) formed by its direct isometries consists of the rotations that preserve \( {P}_{n} \), it is therefore the set of rotations \( {r}_{k} \) of angle \( {2k\pi }/n \) for \( 0 \leq k \leq \; n - 1 \). Furthermore, \( {P}_{n} \) is preserved by the symmetry \( \sigma \) with respect to the axis \( y = 0 \). We deduce \( \left\{ {{\sigma }^{j}{r}_{1}^{k} \mid j \in \{ 0,1\} ,0 \leq k < n}\right\} \subset {D}_{n} \). Conversely, if \( \mu \in {D}_{n} \), then either \( \mu \) is a direct isometry so \( \mu = {r}_{k} = {r}_{1}^{k} \) for \( 0 \leq k < n \), or \( {\sigma \mu } \) is a direct isometry, so \( {\sigma \mu } = {r}_{1}^{k} \) for \( 0 \leq k < n \), so \( \mu = \sigma {r}_{1}^{k} \). We thus have \( {D}_{n} = \left\{ {{\sigma }^{j}{r}_{1}^{k} \mid j \in \{ 0,1\} ,0 \leq k < n}\right\} \) and since the \( {\sigma }^{j}{r}_{1}^{k} \) for \( j \in \{ 0,1\} ,0 \leq k < n \) are all distinct, we indeed have \( \left| {D}_{n}\right| = {2n} \).

\( {D}_{n} \) est non-abélien, car \( \sigma {r}_{1}\left( {S}_{0}\right) = \sigma \left( {S}_{1}\right) = {S}_{n - 1} \) et \( {r}_{1}\sigma \left( {S}_{0}\right) = {r}_{1}\left( {S}_{0}\right) = {S}_{1} \) , donc \( \sigma {r}_{1} \neq {r}_{1}\sigma \) . b) Soit \( \mu \in \mathcal{Z}\left( {D}_{n}\right) \) . On a \( {\sigma \mu } = {\mu \sigma } \) , en particulier \( {\sigma \mu }\left( {S}_{0}\right) = {\mu \sigma }\left( {S}_{0}\right) = \mu \left( {S}_{0}\right) \) , donc \( \mu \left( {S}_{0}\right) \) est invariant par \( \sigma \) , donc \( \mu \left( {S}_{0}\right) \) est sur l’axe \( y = 0 \) .

> \( {D}_{n} \) is non-abelian, because \( \sigma {r}_{1}\left( {S}_{0}\right) = \sigma \left( {S}_{1}\right) = {S}_{n - 1} \) and \( {r}_{1}\sigma \left( {S}_{0}\right) = {r}_{1}\left( {S}_{0}\right) = {S}_{1} \) , therefore \( \sigma {r}_{1} \neq {r}_{1}\sigma \) . b) Let \( \mu \in \mathcal{Z}\left( {D}_{n}\right) \) . We have \( {\sigma \mu } = {\mu \sigma } \) , in particular \( {\sigma \mu }\left( {S}_{0}\right) = {\mu \sigma }\left( {S}_{0}\right) = \mu \left( {S}_{0}\right) \) , therefore \( \mu \left( {S}_{0}\right) \) is invariant by \( \sigma \) , so \( \mu \left( {S}_{0}\right) \) is on the axis \( y = 0 \) .

- Si \( n \) est impair, ceci entraîne \( \mu \left( {S}_{0}\right)  = {S}_{0} \) (car \( \mu \left( {S}_{0}\right)  \in  {P}_{n} \) , et le seul point de \( {P}_{n} \) sur \( y = 0 \) est \( {S}_{0} \) ). Les seules isométries de \( {D}_{n} \) qui conservent \( {S}_{0} \) sont Id et \( \sigma \) ; comme \( \mu  \in  \mathcal{Z}\left( {D}_{n}\right) \) et \( \sigma {r}_{1} \neq  {r}_{1}\sigma \) (vu plus haut), on a donc forcément \( \mu  = \mathrm{{Id}} \) , donc \( \mathcal{Z}\left( {D}_{n}\right)  = \{ \mathrm{{Id}}\} \) .

> - If \( n \) is odd, this implies \( \mu \left( {S}_{0}\right)  = {S}_{0} \) (because \( \mu \left( {S}_{0}\right)  \in  {P}_{n} \) , and the only point of \( {P}_{n} \) on \( y = 0 \) is \( {S}_{0} \) ). The only isometries of \( {D}_{n} \) that preserve \( {S}_{0} \) are Id and \( \sigma \) ; as \( \mu  \in  \mathcal{Z}\left( {D}_{n}\right) \) and \( \sigma {r}_{1} \neq  {r}_{1}\sigma \) (seen above), we therefore necessarily have \( \mu  = \mathrm{{Id}} \) , so \( \mathcal{Z}\left( {D}_{n}\right)  = \{ \mathrm{{Id}}\} \) .

- Si \( n \) est pair, les points \( {S}_{k} \) de l’axe \( y = 0 \) sont \( {S}_{0} \) et \( {S}_{n/2} \) donc \( \mu \left( {S}_{0}\right)  \in  \left\{  {{S}_{0},{S}_{n/2}}\right\} \) . Si \( \mu \left( {S}_{0}\right)  = {S}_{0} \) on a vu plus haut que \( \mu  = \) Id. Si \( \mu \left( {S}_{0}\right)  = {S}_{n/2} \) , alors \( \mu  = {\sigma }^{j}{r}_{1}^{n/2} \) avec \( j \in  \{ 0,1\} \) . Comme \( {r}_{1}\mu  = \mu {r}_{1} \) ceci entraîne

> - If \( n \) is even, the points \( {S}_{k} \) of the axis \( y = 0 \) are \( {S}_{0} \) and \( {S}_{n/2} \) therefore \( \mu \left( {S}_{0}\right)  \in  \left\{  {{S}_{0},{S}_{n/2}}\right\} \) . If \( \mu \left( {S}_{0}\right)  = {S}_{0} \) we saw above that \( \mu  = \) Id. If \( \mu \left( {S}_{0}\right)  = {S}_{n/2} \) , then \( \mu  = {\sigma }^{j}{r}_{1}^{n/2} \) with \( j \in  \{ 0,1\} \) . As \( {r}_{1}\mu  = \mu {r}_{1} \) this implies

\[
{r}_{1}{\sigma }^{j}\left( {S}_{n/2 - 1}\right)  = {r}_{1}\mu \left( {S}_{n - 1}\right)  = \mu {r}_{1}\left( {S}_{n - 1}\right)  = \mu \left( {S}_{0}\right)  = {S}_{n/2}.
\]

Lorsque \( j = 1 \) , on a \( {r}_{1}{\sigma }^{j}\left( {S}_{n/2 - 1}\right) = {S}_{n/2 + 2} \neq {S}_{n/2} \) , on a donc forcément \( j = 0 \) et \( \mu = {r}_{1}^{n/2} \) . Réciproquement, si \( \mu = {r}_{1}^{n/2} \) , on a \( {\mu \sigma } = {\sigma \mu } \) (pour tout \( k \) , on a \( {\mu \sigma }\left( {S}_{k}\right) = \mu {S}_{n - k} = {S}_{n/2 - k} \) et \( {\sigma \mu }\left( {S}_{k}\right) = \sigma {S}_{n/2 + k} = {S}_{n/2 - k} \) ), donc pour tout \( j, k,\mu \left( {{\sigma }^{j}{r}_{1}^{k}}\right) = {\sigma }^{j}\mu {r}_{1}^{k} = {\sigma }^{j}{r}_{1}^{k + n/2} = \; \left( {{\sigma }^{j}{r}_{1}^{k}}\right) \mu \) . Finalement, on a montré \( \mathcal{Z}\left( {D}_{n}\right) = \left\{ {\operatorname{Id},{r}_{1}^{n/2}}\right\} \) .

> When \( j = 1 \) , we have \( {r}_{1}{\sigma }^{j}\left( {S}_{n/2 - 1}\right) = {S}_{n/2 + 2} \neq {S}_{n/2} \) , so we necessarily have \( j = 0 \) and \( \mu = {r}_{1}^{n/2} \) . Conversely, if \( \mu = {r}_{1}^{n/2} \) , we have \( {\mu \sigma } = {\sigma \mu } \) (for all \( k \) , we have \( {\mu \sigma }\left( {S}_{k}\right) = \mu {S}_{n - k} = {S}_{n/2 - k} \) and \( {\sigma \mu }\left( {S}_{k}\right) = \sigma {S}_{n/2 + k} = {S}_{n/2 - k} \) ), so for all \( j, k,\mu \left( {{\sigma }^{j}{r}_{1}^{k}}\right) = {\sigma }^{j}\mu {r}_{1}^{k} = {\sigma }^{j}{r}_{1}^{k + n/2} = \; \left( {{\sigma }^{j}{r}_{1}^{k}}\right) \mu \) . Finally, we have shown \( \mathcal{Z}\left( {D}_{n}\right) = \left\{ {\operatorname{Id},{r}_{1}^{n/2}}\right\} \) .

2/a) Raisonnons par l’absurde et supposons \( G/\mathcal{Z}\left( G\right) \) cyclique. Soit \( h \in G \) tel que \( \bar{h} \) engendre \( G/\mathcal{Z}\left( G\right) \) (où \( \bar{g} \) désigne la classe d’équivalence de \( g \in G \) ). Soient \( a, b \in G \) . On peut écrire \( \bar{a} = {\bar{h}}^{i} \) et \( \bar{b} = {\bar{h}}^{j} \) , autrement dit il existe \( g,{g}^{\prime } \in \mathcal{Z}\left( G\right) \) tels que \( a = {h}^{i}g \) et \( b = {h}^{j}{g}^{\prime } \) . Donc \( {ab} = \left( {{h}^{i}g}\right) \left( {{h}^{j}{g}^{\prime }}\right) = \; g{h}^{i}{h}^{j}{g}^{\prime } = g{h}^{i + j}{g}^{\prime } = {g}^{\prime }{h}^{i + j}g = {g}^{\prime }{h}^{j}{h}^{i}g = {ba} \) . Ainsi \( a \) et \( b \) commutent pour tous les couples \( \left( {a, b}\right) \in {G}^{2} \) , donc \( G \) est abélien ce qui est absurde.

> 2/a) Let us reason by contradiction and assume \( G/\mathcal{Z}\left( G\right) \) is cyclic. Let \( h \in G \) be such that \( \bar{h} \) generates \( G/\mathcal{Z}\left( G\right) \) (where \( \bar{g} \) denotes the equivalence class of \( g \in G \) ). Let \( a, b \in G \) . We can write \( \bar{a} = {\bar{h}}^{i} \) and \( \bar{b} = {\bar{h}}^{j} \) , in other words there exist \( g,{g}^{\prime } \in \mathcal{Z}\left( G\right) \) such that \( a = {h}^{i}g \) and \( b = {h}^{j}{g}^{\prime } \) . Thus \( {ab} = \left( {{h}^{i}g}\right) \left( {{h}^{j}{g}^{\prime }}\right) = \; g{h}^{i}{h}^{j}{g}^{\prime } = g{h}^{i + j}{g}^{\prime } = {g}^{\prime }{h}^{i + j}g = {g}^{\prime }{h}^{j}{h}^{i}g = {ba} \) . Therefore \( a \) and \( b \) commute for all pairs \( \left( {a, b}\right) \in {G}^{2} \) , so \( G \) is abelian, which is absurd.

Le groupe quotient \( G/\mathcal{Z}\left( G\right) \) peut etre abélien, comme c’est le cas pour \( G = {D}_{4} \) ; dans ce cas, \( {D}_{4}/\mathcal{Z}\left( {D}_{4}\right) = {D}_{4}/\left\{ {\operatorname{Id},{r}_{1}^{2}}\right\} = \left\{ {\overline{\operatorname{Id}},\overline{\sigma },\overline{{r}_{1}},\overline{\sigma }\overline{{r}_{1}}}\right\} \) est isomorphe à \( {\left( \mathbb{Z}/2\mathbb{Z}\right) }^{2} \) qui est abélien (notons par ailleurs que le plus petit groupe non abélien est d’ordre 6, et est isomorphe à \( {D}_{3} \) ).

> The quotient group \( G/\mathcal{Z}\left( G\right) \) can be abelian, as is the case for \( G = {D}_{4} \) ; in this case, \( {D}_{4}/\mathcal{Z}\left( {D}_{4}\right) = {D}_{4}/\left\{ {\operatorname{Id},{r}_{1}^{2}}\right\} = \left\{ {\overline{\operatorname{Id}},\overline{\sigma },\overline{{r}_{1}},\overline{\sigma }\overline{{r}_{1}}}\right\} \) is isomorphic to \( {\left( \mathbb{Z}/2\mathbb{Z}\right) }^{2} \) which is abelian (note furthermore that the smallest non-abelian group is of order 6, and is isomorphic to \( {D}_{3} \) ).

b) Notons \( n = \left| G\right| \) . La probabilité \( p \) que deux éléments de \( G \) commutent est donnée par

> b) Let \( n = \left| G\right| \) . The probability \( p \) that two elements of \( G \) commute is given by

\[
p = \frac{\left| \left\{  \left( a, b\right)  \in  {G}^{2} \mid  ab = ba\right\}  \right| }{{\left| G\right| }^{2}} = \frac{1}{{n}^{2}}\mathop{\sum }\limits_{{a \in  G}}\left| {G}_{a}\right| ,\;\text{ où }\;{G}_{a} = \{ b \in  G \mid  {ab} = {ba}\} .
\]

Pour tout \( a \in G,{G}_{a} \) est un sous-groupe de \( G \) . Si \( a \in \mathcal{Z}\left( G\right) \) on a \( {G}_{a} = G \) , et si \( a \notin \mathcal{Z}\left( G\right) ,\left| {G}_{a}\right| \) divise \( \left| G\right| \) et \( \left| {G}_{a}\right| < \left| G\right| \) donc \( \left| {G}_{a}\right| \leq n/2 \) . On en déduit

> For any \( a \in G,{G}_{a} \) is a subgroup of \( G \) . If \( a \in \mathcal{Z}\left( G\right) \) we have \( {G}_{a} = G \) , and if \( a \notin \mathcal{Z}\left( G\right) ,\left| {G}_{a}\right| \) divides \( \left| G\right| \) and \( \left| {G}_{a}\right| < \left| G\right| \) then \( \left| {G}_{a}\right| \leq n/2 \) . We deduce

\[
{n}^{2}p = \mathop{\sum }\limits_{{a \in  \mathcal{Z}\left( G\right) }}\left| {G}_{a}\right|  + \mathop{\sum }\limits_{{a \notin  \mathcal{Z}\left( G\right) }}\left| {G}_{a}\right|  \leq  n\left| {\mathcal{Z}\left( G\right) }\right|  + \left( {n - \left| {\mathcal{Z}\left( G\right) }\right| }\right) \frac{n}{2} = \frac{n}{2}\left| {\mathcal{Z}\left( G\right) }\right|  + \frac{{n}^{2}}{2}.
\]

(*)

> Comme \( G \) est non-abélien, d’après 2/a) le groupe quotient \( G/\mathcal{Z}\left( G\right) \) n’est pas cyclique, donc son ordre n’est pas un nombre premier, donc \( \left| {G/\mathcal{Z}\left( G\right) }\right| \geq 4 \) . On en déduit \( \left| {\mathcal{Z}\left( G\right) }\right| \leq n/4 \) . En remplaçant dans (*) on en déduit \( p \leq 5/8 \) .

Since \( G \) is non-abelian, according to 2/a) the quotient group \( G/\mathcal{Z}\left( G\right) \) is not cyclic, so its order is not a prime number, so \( \left| {G/\mathcal{Z}\left( G\right) }\right| \geq 4 \) . We deduce \( \left| {\mathcal{Z}\left( G\right) }\right| \leq n/4 \) . Substituting into (*) we deduce \( p \leq 5/8 \) .

> L’égalité se produit lorsque \( \left| {\mathcal{Z}\left( G\right) }\right| = n/4 \) et \( \left| {G}_{a}\right| = n/2 \) pour tout \( a \notin \mathcal{Z}\left( G\right) \) , ce qui est le cas pour le groupe diédral \( G = {D}_{4} \) .

Equality occurs when \( \left| {\mathcal{Z}\left( G\right) }\right| = n/4 \) and \( \left| {G}_{a}\right| = n/2 \) for all \( a \notin \mathcal{Z}\left( G\right) \) , which is the case for the dihedral group \( G = {D}_{4} \) .

> Problem 9 (THÉORÉME DE SYLOW). a) Soit \( G \) un groupe abélien fini. Soit \( p \) un nombre premier divisant l’ordre de \( G \) . Montrer qu’il existe un sous-groupe de \( G \) d’ordre \( p \) (sans utiliser le résultat de l’exercice 10 page 28 ou de l’exercice 12 page 30).

Problem 9 (SYLOW'S THEOREM). a) Let \( G \) be a finite abelian group. Let \( p \) be a prime number dividing the order of \( G \) . Show that there exists a subgroup of \( G \) of order \( p \) (without using the result of exercise 10 on page 28 or exercise 12 on page 30).

> b) Soit \( G \) un groupe fini d’ordre \( h \) , non supposé abélien. Démontrer le théorème de Sylow : Si \( {p}^{\alpha } \mid h \) où \( p \) est un nombre premier et \( \alpha \in \mathbb{N} \) , alors il existe un sous-groupe de \( G \) d’ordre \( {p}^{\alpha } \) . (Indication : on pourra procéder par récurrence sur Card \( \left( G\right) \) en utilisant l’équation aux classes - voir le théorème 8 page 24.)

b) Let \( G \) be a finite group of order \( h \) , not assumed to be abelian. Prove Sylow's theorem: If \( {p}^{\alpha } \mid h \) where \( p \) is a prime number and \( \alpha \in \mathbb{N} \) , then there exists a subgroup of \( G \) of order \( {p}^{\alpha } \) . (Hint: one may proceed by induction on Card \( \left( G\right) \) using the class equation - see theorem 8 on page 24.)

> Solution. a) On procède de manière analogue à la question c) de l'exercice 10 page 28. \( G \) étant fini, il existe un système de générateurs \( \left( {{x}_{1},\ldots ,{x}_{n}}\right) \) de \( G \) . Notons \( {r}_{1},\ldots ,{r}_{n} \) les ordres de \( {x}_{1},\ldots ,{x}_{n} \) . Considérons l’application

Solution. a) We proceed analogously to question c) of exercise 10 on page 28. Since \( G \) is finite, there exists a generating set \( \left( {{x}_{1},\ldots ,{x}_{n}}\right) \) of \( G \) . Let \( {r}_{1},\ldots ,{r}_{n} \) be the orders of \( {x}_{1},\ldots ,{x}_{n} \) . Consider the map

\[
\varphi  : \left\langle  {x}_{1}\right\rangle   \times  \cdots  \times  \left\langle  {x}_{n}\right\rangle   \rightarrow  G\;\left( {{y}_{1},\ldots ,{y}_{n}}\right)  \mapsto  {y}_{1}\cdots {y}_{n}.
\]

Le groupe \( G \) étant abélien, \( \varphi \) est un morphisme de groupes. De plus, \( \varphi \) étant surjectif (puisque \( \left( {{x}_{1},\ldots ,{x}_{n}}\right) \) est un système de générateurs de \( G), G \) est isomorphe à \( \left( {\left\langle {x}_{1}\right\rangle \times \cdots \times \left\langle {x}_{n}\right\rangle }\right) /\operatorname{Ker}\varphi \) , donc \( \operatorname{Card}\left( G\right) \times \operatorname{Card}\left( {\operatorname{Ker}\varphi }\right) = \operatorname{Card}\left( {\left\langle {x}_{1}\right\rangle \times \cdots \times \left\langle {x}_{n}\right\rangle }\right) = {r}_{1}\cdots {r}_{n} \) , donc \( \operatorname{Card}\left( G\right) \mid {r}_{1}\cdots {r}_{n} \) . Donc \( p \mid {r}_{1}\cdots {r}_{n} \) , donc il existe \( {r}_{i} \) tel que \( p \mid {r}_{i} \) . Si \( {r}_{i} = {pq}, q \in {\mathbb{N}}^{ * } \) , alors \( x = {x}_{i}^{q} \) est d’ordre \( p \) et \( H = \langle x\rangle \) est un sous-groupe de \( G \) d’ordre \( p \) .

> Since the group \( G \) is abelian, \( \varphi \) is a group homomorphism. Furthermore, since \( \varphi \) is surjective (because \( \left( {{x}_{1},\ldots ,{x}_{n}}\right) \) is a generating set of \( G), G \) is isomorphic to \( \left( {\left\langle {x}_{1}\right\rangle \times \cdots \times \left\langle {x}_{n}\right\rangle }\right) /\operatorname{Ker}\varphi \) , thus \( \operatorname{Card}\left( G\right) \times \operatorname{Card}\left( {\operatorname{Ker}\varphi }\right) = \operatorname{Card}\left( {\left\langle {x}_{1}\right\rangle \times \cdots \times \left\langle {x}_{n}\right\rangle }\right) = {r}_{1}\cdots {r}_{n} \) , therefore \( \operatorname{Card}\left( G\right) \mid {r}_{1}\cdots {r}_{n} \) . Thus \( p \mid {r}_{1}\cdots {r}_{n} \) , so there exists \( {r}_{i} \) such that \( p \mid {r}_{i} \) . If \( {r}_{i} = {pq}, q \in {\mathbb{N}}^{ * } \) , then \( x = {x}_{i}^{q} \) is of order \( p \) and \( H = \langle x\rangle \) is a subgroup of \( G \) of order \( p \) .

b) Procédons par récurrence sur \( h = \operatorname{Card}\left( G\right) \) .

> b) Let us proceed by induction on \( h = \operatorname{Card}\left( G\right) \) .

- Si Card \( \left( G\right)  = 1 \) , c’est évident.

> - If Card \( \left( G\right)  = 1 \) , it is obvious.

- Sinon, supposons le résultat vrai pour les groupes d’ordres \( < h = \operatorname{Card}\left( G\right) \) . Si \( \alpha  = 0 \) , c’est évident, sinon \( \alpha  \geq  1 \) . D’après le théorème 8 page 24 il existe une famille finie \( {\left( {H}_{i}\right) }_{i \in  I} \) de sous-groupes stricts de \( G \) telle que

> - Otherwise, assume the result is true for groups of orders \( < h = \operatorname{Card}\left( G\right) \) . If \( \alpha  = 0 \) , it is obvious, otherwise \( \alpha  \geq  1 \) . According to Theorem 8 on page 24, there exists a finite family \( {\left( {H}_{i}\right) }_{i \in  I} \) of proper subgroups of \( G \) such that

\[
h = \operatorname{Card}\left( G\right)  = \operatorname{Card}\left( {\mathcal{Z}\left( G\right) }\right)  + \mathop{\sum }\limits_{{i \in  I}}\frac{h}{\operatorname{Card}\left( {H}_{i}\right) }.
\]

(*)

> Deux cas se présentent :

Two cases arise:

> - Il existe \( i \in  I \) tel que \( {p}^{\alpha } \mid  \operatorname{Card}\left( {H}_{i}\right) \) . Comme \( \operatorname{Card}\left( {H}_{i}\right)  < \operatorname{Card}\left( G\right) \) , d’après l’hypothèse de récurrence il existe un sous-groupe \( H \) de \( {H}_{i} \) d’ordre \( {p}^{\alpha } \) . Ainsi \( H \) est un sous-groupe de \( G \) d’ordre \( {p}^{\alpha } \) .

- There exists \( i \in  I \) such that \( {p}^{\alpha } \mid  \operatorname{Card}\left( {H}_{i}\right) \) . Since \( \operatorname{Card}\left( {H}_{i}\right)  < \operatorname{Card}\left( G\right) \) , by the induction hypothesis there exists a subgroup \( H \) of \( {H}_{i} \) of order \( {p}^{\alpha } \) . Thus \( H \) is a subgroup of \( G \) of order \( {p}^{\alpha } \) .

> - Pour tout \( i \in  I,{p}^{\alpha } \nmid  \operatorname{Card}\left( {H}_{i}\right) \) . Comme \( {p}^{\alpha } \mid  h, p \) divise \( h/\operatorname{Card}\left( {H}_{i}\right) \) pour tout \( i \in  I \) . D’après l’équation aux classes \( \left( *\right) \) , on a donc \( p \mid  \operatorname{Card}\left( {\mathcal{Z}\left( G\right) }\right) \) , et \( \mathcal{Z}\left( G\right) \) étant un groupe commutatif, il existe un sous-groupe \( C \) de \( \mathcal{Z}\left( G\right) \) d’ordre \( p \) d’après a). Comme \( C \subset  \mathcal{Z}\left( G\right) \) , \( C \) est distingué dans \( G \) . Soit \( \pi \) la surjection canonique de \( G \) dans \( G/C \) . L’ordre du groupe quotient \( G/C \) est \( \operatorname{Card}\left( G\right) /\operatorname{Card}\left( C\right)  = h/p < h = \operatorname{Card}\left( G\right) \) et comme \( {p}^{\alpha  - 1} \mid  \operatorname{Card}\left( {G/C}\right) \) , on sait d’après l’hypothèse de récurrence qu’il existe un sous-groupe \( {H}^{\prime } \) de \( G/C \) d’ordre \( {p}^{\alpha  - 1} \) . Le sous-groupe \( H = {\pi }^{-1}\left( {H}^{\prime }\right) \) est donc d’ordre \( \operatorname{Card}\left( C\right) \operatorname{Card}\left( {H}^{\prime }\right)  = {p}^{\alpha } \) . D’où le résultat.

- For all \( i \in  I,{p}^{\alpha } \nmid  \operatorname{Card}\left( {H}_{i}\right) \) . Since \( {p}^{\alpha } \mid  h, p \) divides \( h/\operatorname{Card}\left( {H}_{i}\right) \) for all \( i \in  I \) . According to the class equation \( \left( *\right) \) , we therefore have \( p \mid  \operatorname{Card}\left( {\mathcal{Z}\left( G\right) }\right) \) , and since \( \mathcal{Z}\left( G\right) \) is a commutative group, there exists a subgroup \( C \) of \( \mathcal{Z}\left( G\right) \) of order \( p \) according to a). Since \( C \subset  \mathcal{Z}\left( G\right) \) , \( C \) is normal in \( G \) . Let \( \pi \) be the canonical surjection from \( G \) to \( G/C \) . The order of the quotient group \( G/C \) is \( \operatorname{Card}\left( G\right) /\operatorname{Card}\left( C\right)  = h/p < h = \operatorname{Card}\left( G\right) \) and since \( {p}^{\alpha  - 1} \mid  \operatorname{Card}\left( {G/C}\right) \) , we know from the induction hypothesis that there exists a subgroup \( {H}^{\prime } \) of \( G/C \) of order \( {p}^{\alpha  - 1} \) . The subgroup \( H = {\pi }^{-1}\left( {H}^{\prime }\right) \) is therefore of order \( \operatorname{Card}\left( C\right) \operatorname{Card}\left( {H}^{\prime }\right)  = {p}^{\alpha } \) . Hence the result.

> Problem 10. Soit \( G \) un groupe fini et \( H \) un sous-groupe de \( G \) . On suppose que \( \operatorname{Card}\left( G\right) = p\operatorname{Card}\left( H\right) \) où \( p \) est le plus petit facteur premier de \( \operatorname{Card}\left( G\right) \) . Montrer que \( H \) est distingué dans \( G \) .

Problem 10. Let \( G \) be a finite group and \( H \) a subgroup of \( G \) . Suppose that \( \operatorname{Card}\left( G\right) = p\operatorname{Card}\left( H\right) \) where \( p \) is the smallest prime factor of \( \operatorname{Card}\left( G\right) \) . Show that \( H \) is normal in \( G \) .

> Solution. Considérons la relation d'équivalence sur \( G \) définie par

Solution. Consider the equivalence relation on \( G \) defined by

\[
x\mathcal{R}y \Leftrightarrow  {x}^{-1}y \in  H
\]

La classe d’équivalence d’un élément \( x \in G \) est de la forme \( \bar{x} = {xH} \) (classe à gauche suivant \( H) \) . Notons \( X \) l’ensemble quotient \( G/\mathcal{R} \) . Pour les mêmes raisons que dans la démonstration du théorème de Lagrange, \( \operatorname{Card}\left( X\right) = \operatorname{Card}\left( G\right) /\operatorname{Card}\left( H\right) = p \) . Fixons \( g \in G \) . Pour tout \( x \in G \) la classe \( \overline{gx} \) ne dépend pas du représentant \( x \) de \( \bar{x} \) car

> The equivalence class of an element \( x \in G \) is of the form \( \bar{x} = {xH} \) (left coset modulo \( H) \)). Let \( X \) denote the quotient set \( G/\mathcal{R} \). For the same reasons as in the proof of Lagrange's theorem, \( \operatorname{Card}\left( X\right) = \operatorname{Card}\left( G\right) /\operatorname{Card}\left( H\right) = p \). Let us fix \( g \in G \). For any \( x \in G \), the class \( \overline{gx} \) does not depend on the representative \( x \) of \( \bar{x} \) because

\[
x\mathcal{R}y \Rightarrow  {x}^{-1}y \in  H \Rightarrow  {\left( gx\right) }^{-1}\left( {gy}\right)  = {x}^{-1}y \in  H \Rightarrow  {gx}\mathcal{R}{gy}.
\]

Ainsi, l'application

> Thus, the map

\[
{\sigma }_{g} : X \rightarrow  X\;\bar{x} \mapsto  \overline{gx}
\]

est bien définie, et il est facile de vérifier que c’est une permutation de \( X \) . Comme \( {\sigma }_{g{g}^{\prime }} = {\sigma }_{g} \circ {\sigma }_{g}^{\prime } \) , l'application

> is well-defined, and it is easy to verify that it is a permutation of \( X \). Since \( {\sigma }_{g{g}^{\prime }} = {\sigma }_{g} \circ {\sigma }_{g}^{\prime } \), the map

\[
\varphi  : G \rightarrow  \mathcal{S}\;g \mapsto  {\sigma }_{g}
\]

(où \( \mathcal{S} \) désigne le groupe des permutations de \( X \) ) est un morphisme de groupes. On en déduit que \( \operatorname{Im}\varphi \) est isomorphe à \( G/\operatorname{Ker}\varphi \) , donc que \( \operatorname{Card}\left( {\operatorname{Im}\varphi }\right) = \operatorname{Card}\left( G\right) /\operatorname{Card}\left( {\operatorname{Ker}\varphi }\right) \) . De plus \( \operatorname{Im}\varphi \) est un sous-groupe de \( \mathcal{S} \) , donc Card(Im \( \varphi ) \mid \operatorname{Card}\left( \mathcal{S}\right) = p \) !. Finalement,

> (where \( \mathcal{S} \) denotes the group of permutations of \( X \)) is a group homomorphism. We deduce that \( \operatorname{Im}\varphi \) is isomorphic to \( G/\operatorname{Ker}\varphi \), and therefore that \( \operatorname{Card}\left( {\operatorname{Im}\varphi }\right) = \operatorname{Card}\left( G\right) /\operatorname{Card}\left( {\operatorname{Ker}\varphi }\right) \). Furthermore, \( \operatorname{Im}\varphi \) is a subgroup of \( \mathcal{S} \), so Card(Im \( \varphi ) \mid \operatorname{Card}\left( \mathcal{S}\right) = p \) !. Finally,

\[
\frac{\operatorname{Card}\left( G\right) }{\operatorname{Card}\left( {\operatorname{Ker}\varphi }\right) } \mid  p!
\]

Comme \( p \) est premier et que c’est le plus petit facteur premier de \( \operatorname{Card}\left( G\right) \) , on en déduit facile-ment que \( \operatorname{Card}\left( G\right) /\operatorname{Card}\left( {\operatorname{Ker}\varphi }\right) \) divise \( p \) . Ainsi, \( \operatorname{Card}\left( {\operatorname{Ker}\varphi }\right) \geq \operatorname{Card}\left( G\right) /p = \operatorname{Card}\left( H\right) \) . Un peu d'attention montre que

> Since \( p \) is prime and is the smallest prime factor of \( \operatorname{Card}\left( G\right) \), we easily deduce that \( \operatorname{Card}\left( G\right) /\operatorname{Card}\left( {\operatorname{Ker}\varphi }\right) \) divides \( p \). Thus, \( \operatorname{Card}\left( {\operatorname{Ker}\varphi }\right) \geq \operatorname{Card}\left( G\right) /p = \operatorname{Card}\left( H\right) \). A little attention shows that

\[
\operatorname{Ker}\varphi  = \left\{  {g \in  G\mid \forall x \in  G,{x}^{-1}{gx} \in  H}\right\}  ,
\]

(*)

> en particulier Ker \( \varphi \subset H \) . Comme Card(Ker \( \varphi ) \geq \operatorname{Card}\left( H\right) \) , ceci entraîne Ker \( \varphi = H \) . D’après \( \left( *\right) \) , ceci s’écrit \( \forall g \in H,\forall x \in G,{x}^{-1}{gx} \in H \) , c’est-à-dire que \( H \) est distingué dans \( G \) .

in particular Ker \( \varphi \subset H \). Since Card(Ker \( \varphi ) \geq \operatorname{Card}\left( H\right) \), this implies Ker \( \varphi = H \). According to \( \left( *\right) \), this is written as \( \forall g \in H,\forall x \in G,{x}^{-1}{gx} \in H \), which means that \( H \) is normal in \( G \).

> Problem 11. 1 / Soit \( G \) un groupe. Si \( A \subset G \) , on note \( {A}^{\prime } = \{ x \in G \mid \forall a \in A,{ax} = {xa}\} \) . a) Si \( A \subset G \) , montrer que \( {A}^{\prime } \) est un sous-groupe de \( G \) .

Problem 11. 1 / Let \( G \) be a group. If \( A \subset G \), we denote \( {A}^{\prime } = \{ x \in G \mid \forall a \in A,{ax} = {xa}\} \). a) If \( A \subset G \), show that \( {A}^{\prime } \) is a subgroup of \( G \).

> b) Soit \( D \) un sous-groupe de \( G \) distingué dans \( G \) . On note \( \mathcal{A}\left( D\right) \) le groupe des automor-phismes de \( D \) .

b) Let \( D \) be a subgroup of \( G \) normal in \( G \). We denote by \( \mathcal{A}\left( D\right) \) the group of automorphisms of \( D \).

> \( \alpha ) \) Montrer que \( {D}^{\prime } \) est distingué dans \( G \) et que \( G/{D}^{\prime } \) est isomorphe à un sous-groupe de \( \mathcal{A}\left( D\right) \) .

\( \alpha ) \) Show that \( {D}^{\prime } \) is normal in \( G \) and that \( G/{D}^{\prime } \) is isomorphic to a subgroup of \( \mathcal{A}\left( D\right) \).

> \( \beta ) \) Si \( D \) est d’ordre \( m \) premier, montrer que \( \mathcal{A}\left( D\right) \) est isomorphe au groupe multiplicatif \( {\left( \mathbb{Z}/m\mathbb{Z}\right) }^{ * } \) .

\( \beta ) \) If \( D \) is of prime order \( m \), show that \( \mathcal{A}\left( D\right) \) is isomorphic to the multiplicative group \( {\left( \mathbb{Z}/m\mathbb{Z}\right) }^{ * } \) .

> 2/ Soit \( G \) un groupe fini non abélien d’ordre \( {pq} \) , où \( p \) et \( q \) sont des nombres premiers, avec \( p < q \) . On note \( e \) le neutre de \( G \) .

2/ Let \( G \) be a non-abelian finite group of order \( {pq} \), where \( p \) and \( q \) are prime numbers, with \( p < q \) . Let \( e \) denote the identity of \( G \) .

> a) Montrer que le centre \( \mathcal{Z}\left( G\right) \) de \( G \) est réduit à \( \{ e\} \) .

a) Show that the center \( \mathcal{Z}\left( G\right) \) of \( G \) is reduced to \( \{ e\} \) .

> b) Montrer qu’il existe dans \( G \) au moins un sous-groupe d’ordre \( q \) (on pourra utiliser l'équation aux classes, voir le théorème 8 page 24).

b) Show that there exists in \( G \) at least one subgroup of order \( q \) (one may use the class equation, see theorem 8 on page 24).

> c) Montrer qu’il n’existe qu’un seul sous-groupe \( K \) de \( G \) d’ordre \( q \) , et que \( K \) est distingué dans \( G \) .

c) Show that there exists only one subgroup \( K \) of \( G \) of order \( q \), and that \( K \) is normal in \( G \) .

> d) Montrer que \( K = {K}^{\prime } \) puis que \( p \mid \left( {q - 1}\right) \) .

d) Show that \( K = {K}^{\prime } \) and then that \( p \mid \left( {q - 1}\right) \) .

> 3/ Soit \( G \) un groupe d’ordre \( {pq} \) avec \( p \) et \( q \) premiers, \( p < q \) et \( p \nmid \left( {q - 1}\right) \) . Montrer que \( G \) est cyclique (on pourra utiliser le résultat a) du problème 9 page 44).

3/ Let \( G \) be a group of order \( {pq} \) with \( p \) and \( q \) prime, \( p < q \) and \( p \nmid \left( {q - 1}\right) \) . Show that \( G \) is cyclic (one may use the result a) of problem 9 on page 44).

> Solution. 1/a) On a \( e \in {A}^{\prime } \) . Par ailleurs, si \( x \in {A}^{\prime } \) , alors pour tout \( a \in A,{ax} = {xa} \) donc en multipliant à gauche et à droite par \( {x}^{-1},{x}^{-1}a = a{x}^{-1} \) . Ainsi, \( {x}^{-1} \in {A}^{\prime } \) . Il ne reste plus qu’à montrer que si \( x, y \in {A}^{\prime } \) , alors \( {xy} \in {A}^{\prime } \) , ce qui est le cas car si \( a \in A, a\left( {xy}\right) = \left( {ax}\right) y = \left( {xa}\right) y = \; x\left( {ay}\right) = x\left( {ya}\right) = \left( {xy}\right) a. \)

Solution. 1/a) We have \( e \in {A}^{\prime } \) . Furthermore, if \( x \in {A}^{\prime } \) , then for all \( a \in A,{ax} = {xa} \) thus by multiplying on the left and on the right by \( {x}^{-1},{x}^{-1}a = a{x}^{-1} \) . Thus, \( {x}^{-1} \in {A}^{\prime } \) . It only remains to show that if \( x, y \in {A}^{\prime } \) , then \( {xy} \in {A}^{\prime } \) , which is the case because if \( a \in A, a\left( {xy}\right) = \left( {ax}\right) y = \left( {xa}\right) y = \; x\left( {ay}\right) = x\left( {ya}\right) = \left( {xy}\right) a. \)

> b) \( \alpha \) ) Soient \( x \in G \) et \( y \in {D}^{\prime } \) . Le sous-groupe \( D \) étant distingué dans \( G \) , on a \( {x}^{-1}{ax} \in D \) pour tout \( a \in D \) , donc \( \left( {{x}^{-1}{ax}}\right) y = y\left( {{x}^{-1}{ax}}\right) \) , ce qui entraîne \( a\left( {{xy}{x}^{-1}}\right) = \left( {{xy}{x}^{-1}}\right) a \) et ceci pour tout \( a \in D \) , donc \( {xy}{x}^{-1} \in {D}^{\prime } \) , ce qui prouve que \( {D}^{\prime } \) est distingué dans \( G \) .

b) \( \alpha \) ) Let \( x \in G \) and \( y \in {D}^{\prime } \) . Since the subgroup \( D \) is normal in \( G \) , we have \( {x}^{-1}{ax} \in D \) for all \( a \in D \) , thus \( \left( {{x}^{-1}{ax}}\right) y = y\left( {{x}^{-1}{ax}}\right) \) , which implies \( a\left( {{xy}{x}^{-1}}\right) = \left( {{xy}{x}^{-1}}\right) a \) and this for all \( a \in D \) , thus \( {xy}{x}^{-1} \in {D}^{\prime } \) , which proves that \( {D}^{\prime } \) is normal in \( G \) .

> - Pour tout \( a \in  G \) , on note \( {\varphi }_{a} : D \rightarrow  G\;x \mapsto  {\varphi }_{a}\left( x\right)  = {ax}{a}^{-1} \) . C’est un morphisme injectif, et \( D \) étant distingué dans \( G,{\varphi }_{a} \) est une bijection de \( D \) sur \( D \) . Autrement dit, \( {\varphi }_{a} \) est un automorphisme de \( D \) . Notons \( {\mathcal{A}}^{\prime } = \left\{  {{\varphi }_{a} \mid  a \in  G}\right\} \) . C’est un sous-groupe de \( \mathcal{A}\left( D\right) \) pour la loi de composition.

- For any \( a \in  G \), we denote \( {\varphi }_{a} : D \rightarrow  G\;x \mapsto  {\varphi }_{a}\left( x\right)  = {ax}{a}^{-1} \). This is an injective morphism, and since \( D \) is normal in \( G,{\varphi }_{a} \), it is a bijection from \( D \) to \( D \). In other words, \( {\varphi }_{a} \) is an automorphism of \( D \). Let us denote \( {\mathcal{A}}^{\prime } = \left\{  {{\varphi }_{a} \mid  a \in  G}\right\} \). This is a subgroup of \( \mathcal{A}\left( D\right) \) under the composition law.

> Soit \( f : G \rightarrow {\mathcal{A}}^{\prime }a \mapsto {\varphi }_{a} \) . L’application \( f \) est un morphisme de groupe surjectif. Par ailleurs, \( \operatorname{Ker}f = \left\{ {a \in G\mid \forall x \in D,{\varphi }_{a}\left( x\right) = x}\right\} = {D}^{\prime } \) , donc \( G/\operatorname{Ker}f = G/{D}^{\prime } \) est isomorphe à \( {\mathcal{A}}^{\prime } \) , qui est un sous-groupe de \( \mathcal{A}\left( D\right) \) . \( \beta ) \) L’ordre de \( D \) étant un nombre premier, \( D \) est cyclique donc il existe \( {x}_{0} \in D \) tel que \( D = \left\langle {x}_{0}\right\rangle \) .

Let \( f : G \rightarrow {\mathcal{A}}^{\prime }a \mapsto {\varphi }_{a} \). The map \( f \) is a surjective group morphism. Furthermore, \( \operatorname{Ker}f = \left\{ {a \in G\mid \forall x \in D,{\varphi }_{a}\left( x\right) = x}\right\} = {D}^{\prime } \), so \( G/\operatorname{Ker}f = G/{D}^{\prime } \) is isomorphic to \( {\mathcal{A}}^{\prime } \), which is a subgroup of \( \mathcal{A}\left( D\right) \). \( \beta ) \) Since the order of \( D \) is a prime number, \( D \) is cyclic, so there exists \( {x}_{0} \in D \) such that \( D = \left\langle {x}_{0}\right\rangle \).

> Pour tout entier \( p, m \nmid p \) , on note \( {\varphi }_{p} : D \rightarrow D\;x \mapsto {x}^{p} \) . Comme \( D \) est abélien (car cyclique), \( {\varphi }_{p} \) est un morphisme de groupe. Or si \( {x}^{p} = e \) alors \( x = e \) (sinon \( x \) est d’ordre \( m \) donc \( m \mid p \) , contradictoire). En d’autres termes, \( \operatorname{Ker}{\varphi }_{p} = \{ e\} \) . Le morphisme \( {\varphi }_{p} \) est donc injectif, donc bijectif \( \left( {{\varphi }_{p}\text{ va } \in D}\right. \) dans \( D \) et \( D \) est fini). En résumé, on a montré que \( {\varphi }_{p} \in \mathcal{A}\left( D\right) \) .

For any integer \( p, m \nmid p \), we denote \( {\varphi }_{p} : D \rightarrow D\;x \mapsto {x}^{p} \). Since \( D \) is abelian (because it is cyclic), \( {\varphi }_{p} \) is a group morphism. Now, if \( {x}^{p} = e \), then \( x = e \) (otherwise \( x \) is of order \( m \), so \( m \mid p \), which is a contradiction). In other words, \( \operatorname{Ker}{\varphi }_{p} = \{ e\} \). The morphism \( {\varphi }_{p} \) is therefore injective, and thus bijective (\( \left( {{\varphi }_{p}\text{ va } \in D}\right. \) in \( D \) and \( D \) is finite). In summary, we have shown that \( {\varphi }_{p} \in \mathcal{A}\left( D\right) \).

> - Soit \( f : {\left( \mathbb{Z}/m\mathbb{Z}\right) }^{ * } \rightarrow  \mathcal{A}\left( D\right) \;\dot{p} \mapsto  {\varphi }_{p} \) .

- Let \( f : {\left( \mathbb{Z}/m\mathbb{Z}\right) }^{ * } \rightarrow  \mathcal{A}\left( D\right) \;\dot{p} \mapsto  {\varphi }_{p} \).

> \( f \) est bien définie (si \( \dot{p} = \dot{q} \) , alors \( m \mid \left( {p - q}\right) \) donc \( {\varphi }_{p} = {\varphi }_{q} \) ).

\( f \) is well-defined (if \( \dot{p} = \dot{q} \), then \( m \mid \left( {p - q}\right) \), so \( {\varphi }_{p} = {\varphi }_{q} \)).

> \( f \) est un morphisme de groupe : \( {\varphi }_{pq} = {\varphi }_{p} \circ {\varphi }_{q} \) .

\( f \) is a group morphism: \( {\varphi }_{pq} = {\varphi }_{p} \circ {\varphi }_{q} \).

> \( f \) est injective. En effet, si \( \dot{p} \in \operatorname{Ker}f \) , alors \( {\varphi }_{p} = {\operatorname{Id}}_{D} \) donc \( {x}_{0}^{p} = {x}_{0} \) donc \( p \equiv 1\left( {\;\operatorname{mod}\;m}\right) \) . Ainsi, \( \operatorname{Ker}f = \{ \dot{1}\} \) .

\( f \) is injective. Indeed, if \( \dot{p} \in \operatorname{Ker}f \), then \( {\varphi }_{p} = {\operatorname{Id}}_{D} \), so \( {x}_{0}^{p} = {x}_{0} \), so \( p \equiv 1\left( {\;\operatorname{mod}\;m}\right) \). Thus, \( \operatorname{Ker}f = \{ \dot{1}\} \).

> \( f \) est surjective. En effet. Soit \( \varphi \in \mathcal{A}\left( D\right) \) . Il existe \( p,1 \leq p \leq m - 1 \) , tel que \( \varphi \left( {x}_{0}\right) = {x}_{0}^{p} \) (car si \( \varphi \left( {x}_{0}\right) = e \) alors \( \forall k,\varphi \left( {x}_{0}^{k}\right) = e \) et \( \varphi \) n’est pas bijective). Soit \( y \in D \) . Il existe \( q \in \mathbb{Z} \) tel que \( y = {x}_{0}^{q} \) , donc \( \varphi \left( y\right) = \varphi \left( {x}_{0}^{q}\right) = \varphi {\left( {x}_{0}\right) }^{q} = {x}_{0}^{pq} = {y}^{p} \) . Donc \( \varphi = {\varphi }_{p} = f\left( \dot{p}\right) \) .

\( f \) is surjective. Indeed. Let \( \varphi \in \mathcal{A}\left( D\right) \) . There exists \( p,1 \leq p \leq m - 1 \) , such that \( \varphi \left( {x}_{0}\right) = {x}_{0}^{p} \) (because if \( \varphi \left( {x}_{0}\right) = e \) then \( \forall k,\varphi \left( {x}_{0}^{k}\right) = e \) and \( \varphi \) is not bijective). Let \( y \in D \) . There exists \( q \in \mathbb{Z} \) such that \( y = {x}_{0}^{q} \) , therefore \( \varphi \left( y\right) = \varphi \left( {x}_{0}^{q}\right) = \varphi {\left( {x}_{0}\right) }^{q} = {x}_{0}^{pq} = {y}^{p} \) . Thus \( \varphi = {\varphi }_{p} = f\left( \dot{p}\right) \) .

> \( f \) est donc un isomorphisme, d’où le résultat.

\( f \) is therefore an isomorphism, hence the result.

> 2/a) Soit \( {p}_{1} \) l’ordre de \( \mathcal{Z}\left( G\right) \) . Supposons \( {p}_{1} > 1 \) . L’ensemble \( \mathcal{Z}\left( G\right) \) est un sous-groupe de \( G \) donc \( {p}_{1} \mid {pq} = \operatorname{Card}\left( G\right) \) donc \( {p}_{1} \in \{ p, q\} \) car \( G \) n’est pas abélien. Le centre de \( G \) est distingué dans \( G \) , et le groupe quotient \( G/\mathcal{Z}\left( G\right) \) est d’ordre \( {pq}/{p}_{1} \) , donc premier, donc cyclique. Soit \( a \in G \) tel que \( \dot{a} \) (la classe de \( a \) dans \( G/\mathcal{Z}\left( G\right) \) ) engendre \( G/\mathcal{Z}\left( G\right) \) . Si \( x \in G \) , il existe un entier \( n \) tel que \( \dot{x} = {\dot{a}}^{n} \) , autrement dit il existe \( y \in \mathcal{Z}\left( G\right) \) tel que \( x = y{a}^{n} \) . On voit donc que \( x \) commute avec \( a \) , et ceci pour tout \( x \in G \) . Donc \( a \in \mathcal{Z}\left( G\right) \) , donc \( \dot{a} = \dot{e} \) , ce qui est absurde puisque \( \dot{a} \) engendre \( G/\mathcal{Z}\left( G\right) \neq \{ \dot{e}\} \) . Donc \( {p}_{1} = 1 \) .

2/a) Let \( {p}_{1} \) be the order of \( \mathcal{Z}\left( G\right) \) . Suppose \( {p}_{1} > 1 \) . The set \( \mathcal{Z}\left( G\right) \) is a subgroup of \( G \) so \( {p}_{1} \mid {pq} = \operatorname{Card}\left( G\right) \) therefore \( {p}_{1} \in \{ p, q\} \) because \( G \) is not abelian. The center of \( G \) is normal in \( G \) , and the quotient group \( G/\mathcal{Z}\left( G\right) \) is of order \( {pq}/{p}_{1} \) , therefore prime, therefore cyclic. Let \( a \in G \) such that \( \dot{a} \) (the class of \( a \) in \( G/\mathcal{Z}\left( G\right) \) ) generates \( G/\mathcal{Z}\left( G\right) \) . If \( x \in G \) , there exists an integer \( n \) such that \( \dot{x} = {\dot{a}}^{n} \) , in other words there exists \( y \in \mathcal{Z}\left( G\right) \) such that \( x = y{a}^{n} \) . We thus see that \( x \) commutes with \( a \) , and this for all \( x \in G \) . Therefore \( a \in \mathcal{Z}\left( G\right) \) , so \( \dot{a} = \dot{e} \) , which is absurd since \( \dot{a} \) generates \( G/\mathcal{Z}\left( G\right) \neq \{ \dot{e}\} \) . Therefore \( {p}_{1} = 1 \) .

> b) D’après le théorème 8 page 24, il existe une famille finie de sous-groupes stricts \( {\left( {H}_{i}\right) }_{i \in I} \) de \( G \) telle que

b) According to theorem 8 page 24, there exists a finite family of proper subgroups \( {\left( {H}_{i}\right) }_{i \in I} \) of \( G \) such that

\[
{pq} = \operatorname{Card}\left( G\right)  = \operatorname{Card}\left( {\mathcal{Z}\left( G\right) }\right)  + \mathop{\sum }\limits_{{i \in  I}}\frac{pq}{\operatorname{Card}\left( {H}_{i}\right) }.
\]

S’il n’existe aucun sous-groupe de \( G \) d’ordre \( q \) , alors pour tout \( i \) on a forcément \( \operatorname{Card}\left( {H}_{i}\right) = p \) (car \( \operatorname{Card}\left( {H}_{i}\right) \mid {pq}, \neq 1, \neq {pq} \) et \( \neq q \) ). L’équation aux classes s’écrit donc \( {pq} = 1 + q\operatorname{Card}\left( I\right) \) , donc \( 1 = q\left( {p - \operatorname{Card}\left( I\right) }\right) \) , absurde. Il existe donc au moins un sous-groupe de \( G \) d’ordre \( q \) .

> If there is no subgroup of \( G \) of order \( q \), then for all \( i \) we necessarily have \( \operatorname{Card}\left( {H}_{i}\right) = p \) (since \( \operatorname{Card}\left( {H}_{i}\right) \mid {pq}, \neq 1, \neq {pq} \) and \( \neq q \)). The class equation is therefore written as \( {pq} = 1 + q\operatorname{Card}\left( I\right) \), so \( 1 = q\left( {p - \operatorname{Card}\left( I\right) }\right) \), which is absurd. There exists therefore at least one subgroup of \( G \) of order \( q \).

c) Supposons qu’il existe deux sous-groupes distincts \( {K}_{1} \) et \( {K}_{2} \) d’ordre \( q \) . Alors \( {K}_{1} \cap {K}_{2} = \{ e\} \) (car \( {K}_{1} \cap {K}_{2} \) est un sous-groupe de \( {K}_{1} \) , son cardinal divise donc \( q \) , donc vaut 1 ou \( q - \) car \( q \) est premier . Si son ordre est \( q \) , c’est que \( {K}_{1} = {K}_{2} \) ). L’application \( f : {K}_{1} \times {K}_{2} \rightarrow G\;\left( {{x}_{1},{x}_{2}}\right) \mapsto {x}_{1}{x}_{2} \) est donc injective (si \( {x}_{1}{x}_{2} = {y}_{1}{y}_{2} \) , alors \( {x}_{1}^{-1}{y}_{1} = {x}_{2}{y}_{2}^{-1} \in {K}_{1} \cap {K}_{2} \) donc \( {x}_{1}^{-1}{y}_{1} = {x}_{2}{y}_{2}^{-1} = e \) ). Donc Card \( \left( G\right) \geq \operatorname{Card}\left( {{K}_{1} \times {K}_{2}}\right) = {q}^{2} \) , absurde car \( p < q \) . Il n’y a donc qu’un seul sous-groupe \( K \) d’ordre \( q \) .

> c) Suppose there exist two distinct subgroups \( {K}_{1} \) and \( {K}_{2} \) of order \( q \). Then \( {K}_{1} \cap {K}_{2} = \{ e\} \) (since \( {K}_{1} \cap {K}_{2} \) is a subgroup of \( {K}_{1} \), its cardinality therefore divides \( q \), so it equals 1 or \( q - \) because \( q \) is prime. If its order is \( q \), then \( {K}_{1} = {K}_{2} \)). The map \( f : {K}_{1} \times {K}_{2} \rightarrow G\;\left( {{x}_{1},{x}_{2}}\right) \mapsto {x}_{1}{x}_{2} \) is therefore injective (if \( {x}_{1}{x}_{2} = {y}_{1}{y}_{2} \), then \( {x}_{1}^{-1}{y}_{1} = {x}_{2}{y}_{2}^{-1} \in {K}_{1} \cap {K}_{2} \) so \( {x}_{1}^{-1}{y}_{1} = {x}_{2}{y}_{2}^{-1} = e \)). Thus Card \( \left( G\right) \geq \operatorname{Card}\left( {{K}_{1} \times {K}_{2}}\right) = {q}^{2} \), which is absurd because \( p < q \). There is therefore only one subgroup \( K \) of order \( q \).

- Montrons que \( K \) est distingué dans \( G \) . Si \( x \in  K \) et si \( a \in  G \) , alors \( {\left( ax{a}^{-1}\right) }^{q} = a{x}^{q}{a}^{-1} = \; {ae}{a}^{-1} = e \) , donc \( {ax}{a}^{-1} \) est d’ordre \( q \) ou 1 ( \( q \) est premier), donc \( {ax}{a}^{-1} \in  K \) d’après l’unicité d’un sous-groupe d’ordre \( q \) . Le sous-groupe \( K \) est donc distingué dans \( G \) .

> - Let us show that \( K \) is normal in \( G \). If \( x \in  K \) and if \( a \in  G \), then \( {\left( ax{a}^{-1}\right) }^{q} = a{x}^{q}{a}^{-1} = \; {ae}{a}^{-1} = e \), so \( {ax}{a}^{-1} \) is of order \( q \) or 1 (\( q \) is prime), so \( {ax}{a}^{-1} \in  K \) according to the uniqueness of a subgroup of order \( q \). The subgroup \( K \) is therefore normal in \( G \).

d) Le sous-groupe \( K \) étant cyclique (car d’ordre \( q \) premier), il est commutatif. Donc \( K \subset {K}^{\prime } \) . Or \( {K}^{\prime } \) est un sous-groupe de \( G \) , donc \( \operatorname{Card}\left( {K}^{\prime }\right) \mid {pq} \) . Or \( \operatorname{Card}\left( {K}^{\prime }\right) \geq \operatorname{Card}\left( K\right) = q > p > 1 \) donc \( \operatorname{Card}\left( {K}^{\prime }\right) \in \{ q,{pq}\} \) . Si \( \operatorname{Card}\left( {K}^{\prime }\right) = {pq} \) , c’est que \( {K}^{\prime } = G \) et en retournant à la définition de \( {K}^{\prime } \) , ceci entraîne \( K \subset \mathcal{Z}\left( G\right) = \{ e\} \) , ce qui est absurde. Donc \( \operatorname{Card}\left( {K}^{\prime }\right) = q \) , donc \( K = {K}^{\prime } \) .

> d) The subgroup \( K \) being cyclic (as it is of prime order \( q \)), it is commutative. Thus \( K \subset {K}^{\prime } \) . However, \( {K}^{\prime } \) is a subgroup of \( G \) , so \( \operatorname{Card}\left( {K}^{\prime }\right) \mid {pq} \) . But \( \operatorname{Card}\left( {K}^{\prime }\right) \geq \operatorname{Card}\left( K\right) = q > p > 1 \) , therefore \( \operatorname{Card}\left( {K}^{\prime }\right) \in \{ q,{pq}\} \) . If \( \operatorname{Card}\left( {K}^{\prime }\right) = {pq} \) , then \( {K}^{\prime } = G \) and returning to the definition of \( {K}^{\prime } \) , this implies \( K \subset \mathcal{Z}\left( G\right) = \{ e\} \) , which is absurd. Therefore \( \operatorname{Card}\left( {K}^{\prime }\right) = q \) , so \( K = {K}^{\prime } \) .

- D’après \( 1/\mathrm{b}),{K}^{\prime } = K \) étant distingué dans \( G, G/{K}^{\prime } \) est isomorphe à un sous-groupe de \( \mathcal{A}\left( K\right) \) . Donc \( p = \operatorname{Card}\left( G\right) /K \) divise \( \operatorname{Card}\left( {\mathcal{A}\left( K\right) }\right) \) . Or d’après \( 1/\mathrm{b})\beta ),\mathcal{A}\left( K\right) \) est isomorphe à \( {\left( \mathbb{Z}/q\mathbb{Z}\right) }^{ * } \) . Donc \( \operatorname{Card}\left( {\mathcal{A}\left( K\right) }\right)  = q - 1 \) , donc \( p \mid  \left( {q - 1}\right) \) .

> - Since \( 1/\mathrm{b}),{K}^{\prime } = K \) is normal in \( G, G/{K}^{\prime } \) , it is isomorphic to a subgroup of \( \mathcal{A}\left( K\right) \) . Thus \( p = \operatorname{Card}\left( G\right) /K \) divides \( \operatorname{Card}\left( {\mathcal{A}\left( K\right) }\right) \) . However, according to \( 1/\mathrm{b})\beta ),\mathcal{A}\left( K\right) \) , it is isomorphic to \( {\left( \mathbb{Z}/q\mathbb{Z}\right) }^{ * } \) . Therefore \( \operatorname{Card}\left( {\mathcal{A}\left( K\right) }\right)  = q - 1 \) , so \( p \mid  \left( {q - 1}\right) \) .

3/ Comme \( p \nmid \left( {q - 1}\right) \) , \( G \) est abélien d’après 2/. D’après la question \( a \) ) du problème 9, on peut donc trouver deux sous-groupes \( {H}_{1} \) et \( {H}_{2} \) de \( G \) d’ordre \( p \) et \( q \) . Les nombres \( p \) et \( q \) étant premiers, \( {H}_{1} \) et \( {H}_{2} \) sont cycliques et donc il existe \( x \in {H}_{1} \) d’ordre \( p \) et \( y \in {H}_{2} \) d’ordre \( q \) . L’élément \( z = {xy} \) est alors d’ordre \( {pq} \) (si \( {z}^{m} = e \) alors \( {x}^{m} = {y}^{-m} \) donc \( {x}^{mq} = e \) donc \( p \mid {mq} \) donc \( p \mid m \) d’après le théorème de Gauss; de même \( q \mid m \) donc \( {pq} \mid m \) ), donc \( G = \langle z\rangle \) est cyclique.

> 3/ As \( p \nmid \left( {q - 1}\right) \) , \( G \) is abelian according to 2/. According to question \( a \) ) of problem 9, we can therefore find two subgroups \( {H}_{1} \) and \( {H}_{2} \) of \( G \) of order \( p \) and \( q \) . Since the numbers \( p \) and \( q \) are prime, \( {H}_{1} \) and \( {H}_{2} \) are cyclic and thus there exists \( x \in {H}_{1} \) of order \( p \) and \( y \in {H}_{2} \) of order \( q \) . The element \( z = {xy} \) is then of order \( {pq} \) (if \( {z}^{m} = e \) then \( {x}^{m} = {y}^{-m} \) so \( {x}^{mq} = e \) so \( p \mid {mq} \) so \( p \mid m \) according to Gauss's theorem; likewise \( q \mid m \) so \( {pq} \mid m \) ), therefore \( G = \langle z\rangle \) is cyclic.

Remarque. Le résultat de cet exercice est un cas particulier du résultat suivant : si \( G \) est un groupe fini d’ordre \( n \) et si \( n \) et \( \varphi \left( n\right) \) sont premiers entre eux (où \( \varphi \) désigne l’indicateur d’Euler), alors \( G \) est cyclique.

> Remark. The result of this exercise is a special case of the following result: if \( G \) is a finite group of order \( n \) and if \( n \) and \( \varphi \left( n\right) \) are coprime (where \( \varphi \) denotes Euler's totient function), then \( G \) is cyclic.

- Nous avons redémontré dans 2/a) le résultat de la question 2/a) du problème 8 page 42, qui affirme que pour \( G \) non abélien, \( G/\mathcal{Z}\left( G\right) \) ne peut pas être cyclique.

> - We re-proved in 2/a) the result of question 2/a) of problem 8 on page 42, which states that for non-abelian \( G \), \( G/\mathcal{Z}\left( G\right) \) cannot be cyclic.
