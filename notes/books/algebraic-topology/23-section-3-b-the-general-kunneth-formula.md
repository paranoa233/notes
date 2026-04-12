# 3.B The General Kunneth Formula

Künneth formulas describe the homology or cohomology of a product space in terms of the homology or cohomology of the factors. In nice cases these formulas take the form \( {H}_{ * }\left( {X \times  Y;R}\right)  \approx  {H}_{ * }\left( {X;R}\right)  \otimes  {H}_{ * }\left( {Y;R}\right) \) or \( {H}^{ * }\left( {X \times  Y;R}\right)  \approx  {H}^{ * }\left( {X;R}\right)  \otimes  {H}^{ * }\left( {Y;R}\right) \) for a coefficient ring \( R \) . For the case of cohomology, such a formula was given in Theorem 3.15, with hypotheses of finite generation and freeness on the cohomology of one factor. To obtain a completely general formula without these hypotheses it turns out that homology is more natural than cohomology, and the main aim in this section is to derive the general Künneth formula for homology. The new feature of the general case is that an extra Tor term is needed to describe the full homology of a product.

## The Cross Product in Homology

A major component of the Künneth formula is a cross product map

\[
{H}_{i}\left( {X;R}\right)  \times  {H}_{j}\left( {Y;R}\right) \overset{ \times  }{ \rightarrow  }{H}_{i + j}\left( {X \times  Y;R}\right)
\]

There are two ways to define this. One is a direct definition for singular homology, involving explicit simplicial formulas. More enlightening, however, is the definition in terms of cellular homology. This necessitates assuming \( X \) and \( Y \) are CW complexes, but this hypothesis can later be removed by the technique of CW approximation in §4.1. We shall focus therefore on the cellular definition, leaving the simplicial definition to later in this section for those who are curious to see how it goes.

The key ingredient in the definition of the cellular cross product will be the fact that the cellular boundary map satisfies \( d\left( {{e}^{i} \times  {e}^{j}}\right)  = d{e}^{i} \times  {e}^{j} + {\left( -1\right) }^{i}{e}^{i} \times  d{e}^{j} \) . Implicit in the right side of this formula is the convention of treating the symbol \( \times \) as a bilinear operation on cellular chains. With this convention we can then say more generally that \( d\left( {a \times  b}\right)  = {da} \times  b + {\left( -1\right) }^{i}a \times  {db} \) whenever \( a \) is a cellular \( i \) -chain and \( b \) is a cellular \( j \) -chain. From this formula it is obvious that the cross product of two cycles is a cycle. Also, the product of a boundary and a cycle is a boundary since \( {da} \times  b = d\left( {a \times  b}\right) \) if \( {db} = 0 \) , and similarly \( a \times  {db} = {\left( -1\right) }^{i}d\left( {a \times  b}\right) \) if \( {da} = 0 \) . Hence there is an induced bilinear map \( {H}_{i}\left( {X;R}\right)  \times  {H}_{j}\left( {Y;R}\right)  \rightarrow  {H}_{i + j}\left( {X \times  Y;R}\right) \) , which is by definition the cross product in cellular homology. Since it is bilinear, it could also be viewed as a homomorphism \( {H}_{i}\left( {X;R}\right) { \otimes  }_{R}{H}_{j}\left( {Y;R}\right)  \rightarrow  {H}_{i + j}\left( {X \times  Y;R}\right) \) . In either form, this cross product turns out to be independent of the cell structures on \( X \) and \( Y \) .

Our task then is to express the boundary maps in the cellular chain complex \( {C}_{ * }\left( {X \times  Y}\right) \) for \( X \times  Y \) in terms of the boundary maps in the cellular chain complexes \( {C}_{ * }\left( X\right) \) and \( {C}_{ * }\left( Y\right) \) . For simplicity we consider homology with \( \mathbb{Z} \) coefficients here, but the same formula for arbitrary coefficients follows immediately from this special case. With \( \mathbb{Z} \) coefficients, the cellular chain group \( {C}_{i}\left( X\right) \) is free with basis the \( i \) -cells of \( X \) , but there is a sign ambiguity for the basis element corresponding to each cell \( {e}^{i} \) , namely the choice of a generator for the \( \mathbb{Z} \) summand of \( {H}_{i}\left( {{X}^{i},{X}^{i - 1}}\right) \) corresponding to \( {e}^{i} \) . Only when \( i = 0 \) is this choice canonical. We refer to these choices as ’choosing orientations for the cells’. A choice of such orientations allows cellular \( i \) -chains to be written unambiguously as linear combinations of \( i \) -cells.

The formula \( d\left( {{e}^{i} \times  {e}^{j}}\right)  = d{e}^{i} \times  {e}^{j} + {\left( -1\right) }^{i}{e}^{i} \times  d{e}^{j} \) is not completely canonical since it contains the sign \( {\left( -1\right) }^{i} \) but not \( {\left( -1\right) }^{j} \) . Evidently there is some distinction being made between the two factors of \( {e}^{i} \times  {e}^{j} \) . Since the signs arise from orientations, we need to make explicit how an orientation of cells \( {e}^{i} \) and \( {e}^{j} \) determines an orientation of \( {e}^{i} \times  {e}^{j} \) . Via characteristic maps, orientations can be obtained from orientations of the domain disks of the characteristic maps. It will be convenient to choose these domains to be cubes since the product of two cubes is again a cube. Thus for a cell \( {e}_{\alpha }^{i} \) we take a characteristic map \( {\Phi }_{\alpha } : {I}^{i} \rightarrow  X \) where \( {I}^{i} \) is the product of \( i \) intervals \( \left\lbrack  {0,1}\right\rbrack \) . An orientation of \( {I}^{i} \) is a generator of \( {H}_{i}\left( {{I}^{i},\partial {I}^{i}}\right) \) , and the image of this generator under \( {\Phi }_{\alpha  * } \) gives an orientation of \( {e}_{\alpha }^{i} \) . We can identify \( {H}_{i}\left( {{I}^{i},\partial {I}^{i}}\right) \) with \( {H}_{i}\left( {{I}^{i},{I}^{i}-\{ x\} }\right) \) for any point \( x \) in the interior of \( {I}^{i} \) , and then an orientation is determined by a linear embedding \( {\Delta }^{i} \rightarrow  {I}^{i} \) with \( x \) chosen in the interior of the imaged of this embedding. The embedding is determined by its sequence of vertices \( {v}_{0},\cdots ,{v}_{i} \) . The vectors \( {v}_{1} - {v}_{0},\cdots ,{v}_{i} - {v}_{0} \) are linearly independent in \( {I}^{i} \) , thought of as the unit cube in \( {\mathbb{R}}^{i} \) , so an orientation in our sense is equivalent to an orientation in the sense of linear algebra, that is, an equivalence class of ordered bases, two ordered bases being equivalent if they differ by a linear transformation of positive determinant. (An ordered basis can be continuously deformed to an orthonormal basis, by the Gram-Schmidt process, and two orthonormal bases are related either by a rotation or a rotation followed by a reflection, according to the sign of the determinant of the transformation taking one to the other.)

With this in mind, we adopt the convention that an orientation of \( {I}^{i} \times  {I}^{j} = {I}^{i + j} \) is obtained by choosing an ordered basis consisting of an ordered basis for \( {I}^{i} \) followed by an ordered basis for \( {I}^{j} \) . Notice that reversing the orientation for either \( {I}^{i} \) or \( {I}^{j} \) then reverses the orientation for \( {I}^{i + j} \) , so all that really matters is the order of the two factors of \( {I}^{i} \times  {I}^{j} \) .

Proposition 3B.1. The boundary map in the cellular chain complex \( {C}_{ * }\left( {X \times  Y}\right) \) is determined by the boundary maps in the cellular chain complexes \( {C}_{ * }\left( X\right) \) and \( {C}_{ * }\left( Y\right) \) via the formula \( d\left( {{e}^{i} \times  {e}^{j}}\right)  = d{e}^{i} \times  {e}^{j} + {\left( -1\right) }^{i}{e}^{i} \times  d{e}^{j} \) .

Proof: Let us first consider the special case of the cube \( {I}^{n} \) . We give \( I \) the CW structure with two vertices and one edge, so the \( {i}^{th} \) copy of \( I \) has a 1-cell \( {e}_{i} \) and 0-cells \( {0}_{i} \) and \( {1}_{i} \) , with \( d{e}_{i} = {1}_{i} - {0}_{i} \) . The \( n \) -cell in the product \( {I}^{n} \) is \( {e}_{1} \times  \cdots  \times  {e}_{n} \) , and we claim that the boundary of this cell is given by the formula

(*)

\[
d\left( {{e}_{1} \times  \cdots  \times  {e}_{n}}\right)  = \mathop{\sum }\limits_{i}{\left( -1\right) }^{i + 1}{e}_{1} \times  \cdots  \times  d{e}_{i} \times  \cdots  \times  {e}_{n}
\]

This formula is correct modulo the signs of the individual terms \( {e}_{1} \times  \cdots  \times  {0}_{i} \times  \cdots  \times  {e}_{n} \) and \( {e}_{1} \times  \cdots  \times  {1}_{i} \times  \cdots  \times  {e}_{n} \) since these are exactly the \( \left( {n - 1}\right) \) -cells in the boundary sphere \( \partial {I}^{n} \) of \( {I}^{n} \) . To obtain the signs in \( \left( *\right) \) , note that switching the two ends of an \( I \) factor of \( {I}^{n} \) produces a reflection of \( \partial {I}^{n} \) , as does a transposition of two adjacent \( I \) factors. Since reflections have degree -1, this implies that \( \left( *\right) \) is correct up to an overall sign. This final sign can be determined by looking at any term, say the term \( {0}_{1} \times  {e}_{2} \times  \cdots  \times  {e}_{n} \) , which has a minus sign in \( \left( *\right) \) . To check that this is right, consider the \( n \) -simplex \( \left\lbrack  {{v}_{0},\cdots ,{v}_{n}}\right\rbrack \) with \( {v}_{0} \) at the origin and \( {v}_{k} \) the unit vector along the \( {k}^{th} \) coordinate axis for \( k > 0 \) . This simplex defines the ’positive’ orientation of \( {I}^{n} \) as described earlier, and in the usual formula for its boundary the face \( \left\lbrack  {{v}_{0},{v}_{2},\cdots ,{v}_{n}}\right\rbrack \) , which defines the positive orientation for the face \( {0}_{1} \times  {e}_{2} \times  \cdots  \times  {e}_{n} \) of \( {I}^{n} \) , has a minus sign.

If we write \( {I}^{n} = {I}^{i} \times  {I}^{j} \) with \( i + j = n \) and we set \( {e}^{i} = {e}_{1} \times  \cdots  \times  {e}_{i} \) and \( {e}^{j} = \; {e}_{i + 1} \times  \cdots  \times  {e}_{n} \) , then the formula \( \left( *\right) \) becomes \( d\left( {{e}^{i} \times  {e}^{j}}\right)  = d{e}^{i} \times  {e}^{j} + {\left( -1\right) }^{i}{e}^{i} \times  d{e}^{j} \) . We will use naturality to reduce the general case of the boundary formula to this special case. When dealing with cellular homology, the maps \( f : X \rightarrow  Y \) that induce chain maps \( {f}_{ * } : {C}_{ * }\left( X\right)  \rightarrow  {C}_{ * }\left( Y\right) \) of the cellular chain complexes are the cellular maps, taking \( {X}^{n} \) to \( {Y}^{n} \) for all \( n \) , hence \( \left( {{X}^{n},{X}^{n - 1}}\right) \) to \( \left( {{Y}^{n},{Y}^{n - 1}}\right) \) . The naturality statement we want is then:

Lemma 3B.2. For cellular maps \( f : X \rightarrow  Z \) and \( g : Y \rightarrow  W \) , the cellular chain maps \( {f}_{ * } : {C}_{ * }\left( X\right)  \rightarrow  {C}_{ * }\left( Z\right) ,{g}_{ * } : {C}_{ * }\left( Y\right)  \rightarrow  {C}_{ * }\left( W\right) \) , and \( {\left( f \times  g\right) }_{ * } : {C}_{ * }\left( {X \times  Y}\right)  \rightarrow  {C}_{ * }\left( {Z \times  W}\right) \) are related by the formula \( {\left( f \times  g\right) }_{ * } = {f}_{ * } \times  {g}_{ * } \) .

Proof: The relation \( {\left( f \times  g\right) }_{ * } = {f}_{ * } \times  {g}_{ * } \) means that if \( {f}_{ * }\left( {e}_{\alpha }^{i}\right)  = \mathop{\sum }\limits_{\gamma }{m}_{\alpha \gamma }{e}_{\gamma }^{i} \) and if \( {g}_{ * }\left( {e}_{\beta }^{j}\right)  = \mathop{\sum }\limits_{\delta }{n}_{\beta \delta }{e}_{\delta }^{j} \) , then \( {\left( f \times  g\right) }_{ * }\left( {{e}_{\alpha }^{i} \times  {e}_{\beta }^{j}}\right)  = \mathop{\sum }\limits_{{\gamma \delta }}{m}_{\alpha \gamma }{n}_{\beta \delta }\left( {{e}_{\gamma }^{i} \times  {e}_{\delta }^{j}}\right) \) . The coefficient \( {m}_{\alpha \gamma } \) is the degree of the composition \( {f}_{\alpha \gamma } : {S}^{i} \rightarrow  {X}^{i}/{X}^{i - 1} \rightarrow  {Z}^{i}/{Z}^{i - 1} \rightarrow  {S}^{i} \) where the first and third maps are induced by characteristic maps for the cells \( {e}_{\alpha }^{i} \) and \( {e}_{\gamma }^{i} \) , and the middle map is induced by the cellular map \( f \) . With the natural choices of basepoints in these quotient spaces, \( {f}_{\alpha \gamma } \) is basepoint-preserving. The \( {n}_{\beta \delta } \) ’s are obtained similarly from maps \( {g}_{\beta \delta } : {S}^{j} \rightarrow  {S}^{j} \) . For \( f \times  g \) , the map \( {\left( f \times  g\right) }_{{\alpha \beta },{\gamma \delta }} : {S}^{i + j} \rightarrow  {S}^{i + j} \) whose degree is the coefficient of \( {e}_{y}^{i} \times  {e}_{\delta }^{j} \) in \( {\left( f \times  g\right) }_{ * }\left( {{e}_{\alpha }^{i} \times  {e}_{\beta }^{j}}\right) \) is obtained from the product map \( {f}_{\alpha \gamma } \times  {g}_{\beta \delta } : {S}^{i} \times  {S}^{j} \rightarrow  {S}^{i} \times  {S}^{j} \) by collapsing the \( \left( {i + j - 1}\right) \) -skeleton of \( {S}^{i} \times  {S}^{j} \) to a point. In other words, \( {\left( f \times  g\right) }_{{\alpha \beta },{\gamma \delta }} \) is the smash product map \( {f}_{\alpha \gamma } \land  {g}_{\beta \delta } \) . What we need to show is the formula \( \deg \left( {f \land  g}\right)  = \deg \left( f\right) \deg \left( g\right) \) for basepoint-preserving maps \( f : {S}^{i} \rightarrow  {S}^{i} \) and \( g : {S}^{j} \rightarrow  {S}^{j}. \)

Since \( f \land  g \) is the composition of \( f \land  \mathbb{1} \) and \( \mathbb{1} \land  g \) , it suffices to show that \( \deg \left( {f \land  \mathbb{1}}\right)  = \deg \left( f\right) \) and \( \deg \left( {\mathbb{1} \land  g}\right)  = \deg \left( g\right) \) . We do this by relating smash products to suspension. The smash product \( X \land  {S}^{1} \) can be viewed as \( X \times  I/\left( {X \times  \partial I \cup  \left\{  {x}_{0}\right\}   \times  I}\right) \) , so it is the reduced suspension \( {\sum X} \) , the quotient of the ordinary suspension \( {SX} \) obtained by collapsing the segment \( \left\{  {x}_{0}\right\}   \times  I \) to a point. If \( X \) is a CW complex with \( {x}_{0} \) a 0-cell, the quotient map \( {SX} \rightarrow  X \land  {S}^{1} \) induces an isomorphism on homology since it collapses a contractible subcomplex to a point. Taking \( X = {S}^{i} \) , we have the commutative diagram at the right, and from the induced commutative diagram of homology groups \( {H}_{i + 1} \) we deduce that \( {Sf} \) and \( f \land  \mathbb{1} \) have the same degree. Since suspension preserves degree by Proposition 2.33, we conclude that \( \deg \left( {f \land  \mathbb{1}}\right)  = \; \deg \left( f\right) \) . The1in this formula is the identity map on \( {S}^{1} \) , and by iteration we obtain the same result for1the identity map on \( {S}^{j} \) since \( {S}^{j} \) is the smash product of \( j \) copies of \( {S}^{1} \) . This implies also that \( \deg \left( {\mathbb{1} \land  g}\right)  = \deg \left( g\right) \) since a permutation of coordinates in \( {S}^{i + j} \) does not affect the degree of maps \( {S}^{i + j} \rightarrow  {S}^{i + j} \) .

![bo_d7dtv0s91nqc73eq8nv0_279_1229_208_361_187_0.jpg](images/bo_d7dtv0s91nqc73eq8nv0_279_1229_208_361_187_0.jpg)

Now to finish the proof of the proposition, let \( \Phi  : {I}^{i} \rightarrow  {X}^{i} \) and \( \Psi  : {I}^{j} \rightarrow  {Y}^{j} \) be characteristic maps of cells \( {e}_{\alpha }^{i} \subset  X \) and \( {e}_{\beta }^{j} \subset  Y \) . The restriction of \( \Phi \) to \( \partial {I}^{i} \) is the attaching map of \( {e}_{\alpha }^{i} \) . We may perform a preliminary homotopy of this attaching map \( \partial {I}^{i} \rightarrow  {X}^{i - 1} \) to make it cellular. There is no need to appeal to the cellular approximation theorem to do this since a direct argument is easy: First deform the attaching map so that it sends all but one face of \( {I}^{i} \) to a point, which is possible since the union of these faces is contractible, then do a further deformation so that the image point of this union of faces is a 0-cell. A homotopy of the attaching map \( \partial {I}^{i} \rightarrow  {X}^{i - 1} \) does not affect the cellular boundary \( d{e}_{\alpha }^{i} \) , since \( d{e}_{\alpha }^{i} \) is determined by the induced map \( {H}_{i - 1}\left( {\partial {I}^{i}}\right)  \rightarrow  {H}_{i - 1}\left( {X}^{i - 1}\right)  \rightarrow  {H}_{i - 1}\left( {{X}^{i - 1},{X}^{i - 2}}\right) \) . So we may assume \( \Phi \) is cellular, and likewise \( \Psi \) , hence also \( \Phi  \times  \Psi \) . The map of cellular chain complexes induced by a cellular map between CW complexes is a chain map, commuting with the cellular boundary maps.

If \( {e}^{i} \) is the \( i \) -cell of \( {I}^{i} \) and \( {e}^{j} \) the \( j \) -cell of \( {I}^{j} \) , then \( {\Phi }_{ * }\left( {e}^{i}\right)  = {e}_{\alpha }^{i},{\Psi }_{ * }\left( {e}^{j}\right)  = {e}_{\beta }^{j} \) , and \( {\left( \Phi  \times  \Psi \right) }_{ * }\left( {{e}^{i} \times  {e}^{j}}\right)  = {e}_{\alpha }^{i} \times  {e}_{\beta }^{j} \) , hence

\[
d\left( {{e}_{\alpha }^{i} \times  {e}_{\beta }^{j}}\right)  = d\left( {{\left( \Phi  \times  \Psi \right) }_{ * }\left( {{e}^{i} \times  {e}^{j}}\right) }\right)
\]

\[
= {\left( \Phi  \times  \Psi \right) }_{ * }d\left( {{e}^{i} \times  {e}^{j}}\right) \;\text{ since }{\left( \Phi  \times  \Psi \right) }_{ * }\text{ is a chain map }
\]

\[
= {\left( \Phi  \times  \Psi \right) }_{ * }\left( {d{e}^{i} \times  {e}^{j} + {\left( -1\right) }^{i}{e}^{i} \times  d{e}^{j}}\right) \;\text{ by the special case }
\]

\[
= {\Phi }_{ * }\left( {d{e}^{i}}\right)  \times  {\Psi }_{ * }\left( {e}^{j}\right)  + {\left( -1\right) }^{i}{\Phi }_{ * }\left( {e}^{i}\right)  \times  {\Psi }_{ * }\left( {d{e}^{j}}\right) \;\text{ by the lemma }
\]

\[
= d{\Phi }_{ * }\left( {e}^{i}\right)  \times  {\Psi }_{ * }\left( {e}^{j}\right)  + {\left( -1\right) }^{i}{\Phi }_{ * }\left( {e}^{i}\right)  \times  d{\Psi }_{ * }\left( {e}^{j}\right) \;\text{ since }{\Phi }_{ * }\text{ and }{\Psi }_{ * }\text{ are }
\]

\[
= d{e}_{\alpha }^{i} \times  {e}_{\beta }^{j} + {\left( -1\right) }^{i}{e}_{\alpha }^{i} \times  d{e}_{\beta }^{j}
\]

which completes the proof of the proposition.

Example 3B.3. Consider \( X \times  {S}^{k} \) where we give \( {S}^{k} \) its usual CW structure with two cells. The boundary formula in \( {C}_{ * }\left( {X \times  {S}^{k}}\right) \) takes the form \( d\left( {a \times  b}\right)  = {da} \times  b \) since \( d = 0 \) in \( {C}_{ * }\left( {S}^{k}\right) \) . So the chain complex \( {C}_{ * }\left( {X \times  {S}^{k}}\right) \) is just the direct sum of two copies of the chain complex \( {C}_{ * }\left( X\right) \) , one of the copies having its dimension shifted upward by \( k \) . Hence \( {H}_{n}\left( {X \times  {S}^{k};\mathbb{Z}}\right)  \approx  {H}_{n}\left( {X;\mathbb{Z}}\right)  \oplus  {H}_{n - k}\left( {X;\mathbb{Z}}\right) \) for all \( n \) . In particular, we see that all the homology classes in \( X \times  {S}^{k} \) are cross products of homology classes in \( X \) and \( {S}^{k} \) .

Example 3B.4. More subtle things can happen when \( X \) and \( Y \) both have torsion in their homology. To take the simplest case, let \( X \) be \( {S}^{1} \) with a cell \( {e}^{2} \) attached by a map \( {S}^{1} \rightarrow  {S}^{1} \) of degree \( m \) , so \( {H}_{1}\left( {X;\mathbb{Z}}\right)  \approx  {\mathbb{Z}}_{m} \) and \( {H}_{i}\left( {X;\mathbb{Z}}\right)  = 0 \) for \( i > 1 \) . Similarly, let \( Y \) be obtained from \( {S}^{1} \) by attaching a 2-cell by a map of degree \( n \) . Thus \( X \) and \( Y \) each have CW structures with three cells and so \( X \times  Y \) has nine cells. These are indicated by the dots in the diagram at the right, with \( X \) in the horizontal direction and \( Y \) in the vertical direction. The arrows denote the nonzero cellular boundary maps. For example the two arrows leaving the dot in the upper right corner indicate that \( \partial \left( {{e}^{2} \times  {e}^{2}}\right)  = m\left( {{e}^{1} \times  {e}^{2}}\right)  + n\left( {{e}^{2} \times  {e}^{1}}\right) \) . Obviously \( {H}_{1}\left( {X \times  Y;\mathbb{Z}}\right) \) is \( {\mathbb{Z}}_{m} \oplus  {\mathbb{Z}}_{n} \) . In dimension 2, Ker \( \partial \) is generated by \( {e}^{1} \times  {e}^{1} \) , and the image of the boundary map from dimension 3 consists of the multiples \( \left( {\ell m - {kn}}\right) \left( {{e}^{1} \times  {e}^{1}}\right) \) . These form a cyclic group generated by \( q\left( {{e}^{1} \times  {e}^{1}}\right) \) where \( q \) is the greatest common divisor of \( m \) and \( n \) , so \( {H}_{2}\left( {X \times  Y;\mathbb{Z}}\right)  \approx  {\mathbb{Z}}_{q} \) . In dimension 3 the cycles are the multiples of \( \left( {m/q}\right) \left( {{e}^{1} \times  {e}^{2}}\right)  + \left( {n/q}\right) \left( {{e}^{2} \times  {e}^{1}}\right) \) , and the smallest such multiple that is a boundary is \( q\left\lbrack  {\left( {m/q}\right) \left( {{e}^{1} \times  {e}^{2}}\right)  + \left( {n/q}\right) \left( {{e}^{2} \times  {e}^{1}}\right) }\right\rbrack   = m\left( {{e}^{1} \times  {e}^{2}}\right)  + n\left( {{e}^{2} \times  {e}^{1}}\right) \) , so \( {H}_{3}\left( {X \times  Y;\mathbb{Z}}\right)  \approx  {\mathbb{Z}}_{q} \) . Since \( X \) and \( Y \) have no homology above dimension 1, this 3-dimensional homology of \( X \times  Y \) cannot be realized by cross products. As the general theory will show, \( {H}_{2}\left( {X \times  Y;\mathbb{Z}}\right) \) is \( {H}_{1}\left( {X;\mathbb{Z}}\right)  \otimes  {H}_{1}\left( {Y;\mathbb{Z}}\right) \) and \( {H}_{3}\left( {X \times  Y;\mathbb{Z}}\right) \) is \( \operatorname{Tor}\left( {{H}_{1}\left( {X;\mathbb{Z}}\right) ,{H}_{1}\left( {Y;\mathbb{Z}}\right) }\right) \) .

![bo_d7dtv0s91nqc73eq8nv0_280_1144_537_445_352_0.jpg](images/bo_d7dtv0s91nqc73eq8nv0_280_1144_537_445_352_0.jpg)

This example generalizes easily to higher dimensions, with \( X = {S}^{i} \cup  {e}^{i + 1} \) and \( Y = {S}^{j} \cup  {e}^{j + 1} \) , the attaching maps having degrees \( m \) and \( n \) , respectively. Essentially the same calculation shows that \( X \times  Y \) has both \( {H}_{i + j} \) and \( {H}_{i + j + 1} \) isomorphic to \( {\mathbb{Z}}_{q} \) .

We should say a few words about why the cross product is independent of CW structures. For this we will need a fact proved in the next chapter in Theorem 4.8, that every map between CW complexes is homotopic to a cellular map. As we mentioned earlier, a cellular map induces a chain map between cellular chain complexes. It is easy to see from the equivalence between cellular and singular homology that the map on cellular homology induced by a cellular map is the same as the map induced on singular homology. Now suppose we have cellular maps \( f : X \rightarrow  Z \) and \( g : Y \rightarrow  W \) . Then Lemma 3B.2 implies that we have a commutative diagram

\[
{H}_{i}\left( {X;\mathbb{Z}}\right)  \times  {H}_{j}\left( {Y;\mathbb{Z}}\right) \xrightarrow[]{\;}{H}_{i + j}\left( {X \times  Y;\mathbb{Z}}\right)
\]

\[
\int {f}_{ * } \times  {g}_{ * }\; \downarrow  {\left( f \times  g\right) }_{ * }
\]

\[
{H}_{i}\left( {Z;\mathbb{Z}}\right)  \times  {H}_{j}\left( {W;\mathbb{Z}}\right) \xrightarrow[]{ \times  }{H}_{i + j}\left( {Z \times  W;\mathbb{Z}}\right)
\]

Now take \( Z \) and \( W \) to be the same spaces as \( X \) and \( Y \) but with different CW structures, and let \( f \) and \( g \) be cellular maps homotopic to the identity. The vertical maps in the diagram are then the identity, and commutativity of the diagram says that the cross products defined using the different CW structures coincide.

Cross product is obviously bilinear, or in other words, distributive. It is not hard to check that it is also associative. What about commutativity? If \( T : X \times  Y \rightarrow  Y \times  X \) is transposition of the factors, then we can ask whether \( {T}_{ * }\left( {a \times  b}\right) \) equals \( b \times  a \) . The only effect transposing the factors has on the definition of cross product is in the convention for orienting a product \( {I}^{i} \times  {I}^{j} \) by taking an ordered basis in the first factor followed by an ordered basis in the second factor. Switching the two factors can be achieved by moving each of the \( i \) coordinates of \( {I}^{i} \) past each of the coordinates of \( {I}^{j} \) . This is a total of \( {ij} \) transpositions of adjacent coordinates, each realizable by a reflection, so a sign of \( {\left( -1\right) }^{ij} \) is introduced. Thus the correct formula is \( {T}_{ * }\left( {a \times  b}\right)  = \; {\left( -1\right) }^{ij}b \times  a \) for \( a \in  {H}_{i}\left( X\right) \) and \( b \in  {H}_{j}\left( Y\right) \) .

## The Algebraic Künneth Formula

By adding together the various cross products we obtain a map

\[
{\bigoplus }_{i}\left( {{H}_{i}\left( {X;\mathbb{Z}}\right)  \otimes  {H}_{n - i}\left( {Y;\mathbb{Z}}\right) }\right)  \rightarrow  {H}_{n}\left( {X \times  Y;\mathbb{Z}}\right)
\]

and it is natural to ask whether this is an isomorphism. Example 3B.4 above shows that this is not always the case, though it is true in Example 3B.3. Our main goal in what follows is to show that the map is always injective, and that its cokernel is \( { \oplus  }_{i}\operatorname{Tor}\left( {{H}_{i}\left( {X;\mathbb{Z}}\right) ,{H}_{n - i - 1}\left( {Y;\mathbb{Z}}\right) }\right) \) . More generally, we consider other coefficients besides \( \mathbb{Z} \) and show in particular that with field coefficients the map is an isomorphism.

For CW complexes \( X \) and \( Y \) , the relationship between the cellular chain complexes \( {C}_{ * }\left( X\right) ,{C}_{ * }\left( Y\right) \) , and \( {C}_{ * }\left( {X \times  Y}\right) \) can be expressed nicely in terms of tensor products. Since the \( n \) -cells of \( X \times  Y \) are the products of \( i \) -cells of \( X \) with \( \left( {n - i}\right) \) -cells of \( Y \) , we have \( {C}_{n}\left( {X \times  Y}\right)  \approx  {\bigoplus }_{i}\left( {{C}_{i}\left( X\right)  \otimes  {C}_{n - i}\left( Y\right) }\right) \) , with \( {e}^{i} \times  {e}^{j} \) corresponding to \( {e}^{i} \otimes  {e}^{j} \) . Under this identification the boundary formula of Proposition 3B. 1 becomes \( d\left( {{e}^{i} \otimes  {e}^{j}}\right)  = \; d{e}^{i} \otimes  {e}^{j} + {\left( -1\right) }^{i}{e}^{i} \otimes  d{e}^{j} \) . Our task now is purely algebraic, to compute the homology of the chain complex \( {C}_{ * }\left( {X \times  Y}\right) \) from the homology of \( {C}_{ * }\left( X\right) \) and \( {C}_{ * }\left( Y\right) \) .

Suppose we are given chain complexes \( C \) and \( {C}^{\prime } \) of abelian groups \( {C}_{n} \) and \( {C}_{n}^{\prime } \) , or more generally \( R \) -modules over a commutative ring \( R \) . The tensor product chain complex \( C{ \otimes  }_{R}{C}^{\prime } \) is then defined by \( {\left( C{ \otimes  }_{R}{C}^{\prime }\right) }_{n} = {\bigoplus }_{i}\left( {{C}_{i}{ \otimes  }_{R}{C}_{n - i}^{\prime }}\right) \) , with boundary maps given by \( \partial \left( {c \otimes  {c}^{\prime }}\right)  = \partial c \otimes  {c}^{\prime } + {\left( -1\right) }^{i}c \otimes  \partial {c}^{\prime } \) for \( c \in  {C}_{i} \) and \( {c}^{\prime } \in  {C}_{n - i}^{\prime } \) . The sign \( {\left( -1\right) }^{i} \) guarantees that \( {\partial }^{2} = 0 \) in \( C{ \otimes  }_{R}{C}^{\prime } \) , since

\[
{\partial }^{2}\left( {c \otimes  {c}^{\prime }}\right)  = \partial \left( {\partial c \otimes  {c}^{\prime } + {\left( -1\right) }^{i}c \otimes  \partial {c}^{\prime }}\right)
\]

\[
= {\partial }^{2}c \otimes  {c}^{\prime } + {\left( -1\right) }^{i - 1}\partial c \otimes  \partial {c}^{\prime } + {\left( -1\right) }^{i}\partial c \otimes  \partial {c}^{\prime } + c \otimes  {\partial }^{2}{c}^{\prime } = 0
\]

From the boundary formula \( \partial \left( {c \otimes  {c}^{\prime }}\right)  = \partial c \otimes  {c}^{\prime } + {\left( -1\right) }^{i}c \otimes  \partial {c}^{\prime } \) it follows that the tensor product of cycles is a cycle, and the tensor product of a cycle and a boundary, in either order, is a boundary, just as for the cross product defined earlier. So there is induced a natural map on homology groups \( {H}_{i}\left( C\right) { \otimes  }_{R}{H}_{n - i}\left( {C}^{\prime }\right)  \rightarrow  {H}_{n}\left( {C{ \otimes  }_{R}{C}^{\prime }}\right) \) . Summing over \( i \) then gives a map \( {\bigoplus }_{i}\left( {{H}_{i}\left( C\right) { \otimes  }_{R}{H}_{n - i}\left( {C}^{\prime }\right) }\right)  \rightarrow  {H}_{n}\left( {C{ \otimes  }_{R}{C}^{\prime }}\right) \) . This figures in the following algebraic version of the Künneth formula:

Theorem 3B.5. If \( R \) is a principal ideal domain and the \( R \) -modules \( {C}_{i} \) are free, then for each \( n \) there is a natural short exact sequence

\[
0 \rightarrow  {\bigoplus }_{i}\left( {{H}_{i}\left( C\right) { \otimes  }_{R}{H}_{n - i}\left( {C}^{\prime }\right) }\right)  \rightarrow  {H}_{n}\left( {C{ \otimes  }_{R}{C}^{\prime }}\right)  \rightarrow  {\bigoplus }_{i}\left( {{\operatorname{Tor}}_{R}\left( {{H}_{i}\left( C\right) ,{H}_{n - i - 1}\left( {C}^{\prime }\right) }\right)  \rightarrow  0}\right.
\]

and this sequence splits.

This is a generalization of the universal coefficient theorem for homology, which is the case that \( R = \mathbb{Z} \) and \( {C}^{\prime } \) consists of just the coefficient group \( G \) in dimension zero. The proof will also be a natural generalization of the proof of the universal coefficient theorem.

Proof: First we do the special case that the boundary maps in \( C \) are all zero, so \( {H}_{i}\left( C\right)  = {C}_{i} \) . In this case \( \partial \left( {c \otimes  {c}^{\prime }}\right)  = {\left( -1\right) }^{i}c \otimes  \partial {c}^{\prime } \) and the chain complex \( C{ \otimes  }_{R}{C}^{\prime } \) is simply the direct sum of the complexes \( {C}_{i}{ \otimes  }_{R}{C}^{\prime } \) , each of which is a direct sum of copies of \( {C}^{\prime } \) since \( {C}_{i} \) is free. Hence \( {H}_{n}\left( {{C}_{i}{ \otimes  }_{R}{C}^{\prime }}\right)  \approx  {C}_{i}{ \otimes  }_{R}{H}_{n - i}\left( {C}^{\prime }\right)  = {H}_{i}\left( C\right) { \otimes  }_{R}{H}_{n - i}\left( {C}^{\prime }\right) \) . Summing over \( i \) yields an isomorphism \( {H}_{n}\left( {C{ \otimes  }_{R}{C}^{\prime }}\right)  \approx  {\bigoplus }_{i}\left( {{H}_{i}\left( C\right) { \otimes  }_{R}{H}_{n - i}\left( {C}^{\prime }\right) }\right) \) , which is the statement of the theorem since there are no Tor terms, \( {H}_{i}\left( C\right)  = {C}_{i} \) being free.

In the general case, let \( {Z}_{i} \subset  {C}_{i} \) and \( {B}_{i} \subset  {C}_{i} \) denote kernel and image of the boundary homomorphisms for \( C \) . These give subchain complexes \( Z \) and \( B \) of \( C \) with trivial boundary maps. We have a short exact sequence of chain complexes \( 0 \rightarrow  Z \rightarrow  C \rightarrow  B \rightarrow  0 \) made up of the short exact sequences \( 0 \rightarrow  {Z}_{i} \rightarrow  {C}_{i}\overset{\partial }{ \rightarrow  }{B}_{i - 1} \rightarrow  0 \) each of which splits since \( {B}_{i - 1} \) is free, being a submodule of \( {C}_{i - 1} \) which is free by assumption. Because of the splitting, when we tensor \( 0 \rightarrow  Z \rightarrow  C \rightarrow  B \rightarrow  0 \) with \( {C}^{\prime } \) we obtain another short exact sequence of chain complexes, and hence a long exact sequence in homology

\[
\cdots  \rightarrow  {H}_{n}\left( {Z{ \otimes  }_{R}{C}^{\prime }}\right)  \rightarrow  {H}_{n}\left( {C{ \otimes  }_{R}{C}^{\prime }}\right)  \rightarrow  {H}_{n - 1}\left( {B{ \otimes  }_{R}{C}^{\prime }}\right)  \rightarrow  {H}_{n - 1}\left( {Z{ \otimes  }_{R}{C}^{\prime }}\right)  \rightarrow  \cdots
\]

where we have \( {H}_{n - 1}\left( {B{ \otimes  }_{R}{C}^{\prime }}\right) \) instead of the expected \( {H}_{n}\left( {B{ \otimes  }_{R}{C}^{\prime }}\right) \) since \( \partial  : C \rightarrow  B \) decreases dimension by one. Checking definitions, one sees that the 'boundary' map \( {H}_{n - 1}\left( {B{ \otimes  }_{R}{C}^{\prime }}\right)  \rightarrow  {H}_{n - 1}\left( {Z{ \otimes  }_{R}{C}^{\prime }}\right) \) in the preceding long exact sequence is just the map induced by the natural map \( B{ \otimes  }_{R}{C}^{\prime } \rightarrow  Z{ \otimes  }_{R}{C}^{\prime } \) coming from the inclusion \( B \subset  Z \) .

Since \( Z \) and \( B \) are chain complexes with trivial boundary maps, the special case at the beginning of the proof converts the preceding exact sequence into

\[
\cdots \overset{{i}_{n}}{ \rightarrow  }{ \oplus  }_{i}\left( {{Z}_{i}{ \otimes  }_{R}{H}_{n - i}\left( {C}^{\prime }\right) }\right)  \rightarrow  {H}_{n}\left( {C{ \otimes  }_{R}{C}^{\prime }}\right)  \rightarrow  { \oplus  }_{i}\left( {{B}_{i}{ \otimes  }_{R}{H}_{n - i - 1}\left( {C}^{\prime }\right) }\right) \overset{{i}_{n - 1}}{ \rightarrow  }
\]

\[
{\bigoplus }_{i}\left( {{Z}_{i}{ \otimes  }_{R}{H}_{n - i - 1}\left( {C}^{\prime }\right) }\right)  \rightarrow  \cdots
\]

So we have short exact sequences

\[
0 \rightarrow  \text{ Coker }{i}_{n} \rightarrow  {H}_{n}\left( {C{ \otimes  }_{R}{C}^{\prime }}\right)  \rightarrow  \operatorname{Ker}{i}_{n - 1} \rightarrow  0
\]

where Coker \( {i}_{n} = {\bigoplus }_{i}\left( {{Z}_{i}{ \otimes  }_{R}{H}_{n - i}\left( {C}^{\prime }\right) }\right) /\operatorname{Im}{i}_{n} \) , and this equals \( {\bigoplus }_{i}\left( {{H}_{i}\left( C\right) { \otimes  }_{R}{H}_{n - i}\left( {C}^{\prime }\right) }\right) \) by Lemma 3A.1. It remains to identify \( \operatorname{Ker}{i}_{n - 1} \) with \( { \oplus  }_{i}{\operatorname{Tor}}_{R}\left( {{H}_{i}\left( C\right) ,{H}_{n - i}\left( {C}^{\prime }\right) }\right) \) .

By the definition of Tor, tensoring the free resolution \( 0 \rightarrow  {B}_{i} \rightarrow  {Z}_{i} \rightarrow  {H}_{i}\left( C\right)  \rightarrow  0 \) with \( {H}_{n - i}\left( {C}^{\prime }\right) \) yields an exact sequence

\[
0 \rightarrow  {\operatorname{Tor}}_{R}\left( {{H}_{i}\left( C\right) ,{H}_{n - i}\left( {C}^{\prime }\right) }\right)  \rightarrow  {B}_{i}{ \otimes  }_{R}{H}_{n - i}\left( {C}^{\prime }\right)  \rightarrow  {Z}_{i}{ \otimes  }_{R}{H}_{n - i}\left( {C}^{\prime }\right)  \rightarrow
\]

\[
{H}_{i}\left( C\right) { \otimes  }_{R}{H}_{n - i}\left( {C}^{\prime }\right)  \rightarrow  0
\]

Hence, summing over \( i \) , \( \operatorname{Ker}{i}_{n} = {\bigoplus }_{i}{\operatorname{Tor}}_{R}\left( {{H}_{i}\left( C\right) ,{H}_{n - i}\left( {C}^{\prime }\right) }\right) \) .

Naturality should be obvious, and we leave it for the reader to fill in the details.

We will show that the short exact sequence in the statement of the theorem splits assuming that both \( C \) and \( {C}^{\prime } \) are free. This suffices for our applications. For the extra argument needed to show splitting when \( {C}^{\prime } \) is not free, see the exposition in [Hilton & Stammbach 1970].

The splitting is via a homomorphism \( {H}_{n}\left( {C{ \otimes  }_{R}{C}^{\prime }}\right)  \rightarrow  {\bigoplus }_{i}\left( {{H}_{i}\left( C\right) { \otimes  }_{R}{H}_{n - i}\left( {C}^{\prime }\right) }\right) \) constructed in the following way. As already noted, the sequence \( 0 \rightarrow  {Z}_{i} \rightarrow  {C}_{i} \rightarrow  {B}_{i - 1} \rightarrow  0 \) splits, so the quotient maps \( {Z}_{i} \rightarrow  {H}_{i}\left( C\right) \) extend to homomorphisms \( {C}_{i} \rightarrow  {H}_{i}\left( C\right) \) . Similarly we obtain \( {C}_{j}^{\prime } \rightarrow  {H}_{j}\left( {C}^{\prime }\right) \) if \( {C}^{\prime } \) is free. Viewing the sequences of homology groups \( {H}_{i}\left( C\right) \) and \( {H}_{j}\left( {C}^{\prime }\right) \) as chain complexes \( H\left( C\right) \) and \( H\left( {C}^{\prime }\right) \) with trivial boundary maps, we thus have chain maps \( C \rightarrow  H\left( C\right) \) and \( {C}^{\prime } \rightarrow  H\left( {C}^{\prime }\right) \) , whose tensor product is a chain map \( C{ \otimes  }_{R}{C}^{\prime } \rightarrow  H\left( C\right) { \otimes  }_{R}H\left( {C}^{\prime }\right) \) . The induced map on homology for this last chain map is the desired splitting map since the chain complex \( H\left( C\right) { \otimes  }_{R}H\left( {C}^{\prime }\right) \) equals its own homology, the boundary maps being trivial.

## The Topological Künneth Formula

Now we can apply the preceding algebra to obtain the topological statement we are looking for:

Theorem 3B.6. If \( X \) and \( Y \) are \( {CW} \) complexes and \( R \) is a principal ideal domain, then there are natural short exact sequences

\[
0 \rightarrow  {\bigoplus }_{i}\left( {{H}_{i}\left( {X;R}\right) { \otimes  }_{R}{H}_{n - i}\left( {Y;R}\right) }\right)  \rightarrow  {H}_{n}\left( {X \times  Y;R}\right)  \rightarrow
\]

\[
{\bigoplus }_{i}{\operatorname{Tor}}_{R}\left( {{H}_{i}\left( {X;R}\right) ,{H}_{n - i - 1}\left( {Y;R}\right) }\right)  \rightarrow  0
\]

and these sequences split.

Naturality means that maps \( X \rightarrow  {X}^{\prime } \) and \( Y \rightarrow  {Y}^{\prime } \) induce a map from the short exact sequence for \( X \times  Y \) to the corresponding short exact sequence for \( {X}^{\prime } \times  {Y}^{\prime } \) , with commuting squares. The splitting is not natural, however, as an exercise at the end of this section demonstrates.

Proof: When dealing with products of CW complexes there is always the bothersome fact that the compactly generated CW topology may not be the same as the product topology. However, in the present context this is not a real problem. Since the two topologies have the same compact sets, they have the same singular simplices and hence the same singular homology groups.

Let \( C = {C}_{ * }\left( {X;R}\right) \) and \( {C}^{\prime } = {C}_{ * }\left( {Y;R}\right) \) , the cellular chain complexes with coefficients in \( R \) . Then \( C{ \otimes  }_{R}{C}^{\prime } = {C}_{ * }\left( {X \times  Y;R}\right) \) by Proposition 3B.1, so the algebraic Künneth formula gives the desired short exact sequences. Their naturality follows from naturality in the algebraic Künneth formula, since we can homotope arbitrary maps \( X \rightarrow  {X}^{\prime } \) and \( Y \rightarrow  {Y}^{\prime } \) to be cellular by Theorem 4.8, assuring that they induce chain maps of cellular chain complexes.

With field coefficients the Künneth formula simplifies because the Tor terms are always zero over a field:

Corollary 3B.7. If \( F \) is a field and \( X \) and \( Y \) are CW complexes, then the cross product map \( h : {\bigoplus }_{i}\left( {{H}_{i}\left( {X;F}\right) { \otimes  }_{F}{H}_{n - i}\left( {Y;F}\right) }\right)  \rightarrow  {H}_{n}\left( {X \times  Y;F}\right) \) is an isomorphism for all \( n \) .

There is also a relative version of the Künneth formula for CW pairs \( \left( {X, A}\right) \) and \( \left( {Y, B}\right) \) . This is a split short exact sequence

\[
0 \rightarrow  {\bigoplus }_{i}\left( {{H}_{i}\left( {X, A;R}\right) { \otimes  }_{R}{H}_{n - i}\left( {Y, B;R}\right) }\right)  \rightarrow  {H}_{n}\left( {X \times  Y, A \times  Y \cup  X \times  B;R}\right)  \rightarrow
\]

\[
{\bigoplus }_{i}{\operatorname{Tor}}_{R}\left( {{H}_{i}\left( {X, A;R}\right) ,{H}_{n - i - 1}\left( {Y, B;R}\right) }\right)  \rightarrow  0
\]

for \( R \) a principal ideal domain. This too follows from the algebraic Künneth formula since the isomorphism of cellular chain complexes \( {C}_{ * }\left( {X \times  Y}\right)  \approx  {C}_{ * }\left( X\right)  \otimes  {C}_{ * }\left( Y\right) \) passes down to a quotient isomorphism

\[
{C}_{ * }\left( {X \times  Y}\right) /{C}_{ * }\left( {A \times  Y \cup  X \times  B}\right)  \approx  {C}_{ * }\left( X\right) /{C}_{ * }\left( A\right)  \otimes  {C}_{ * }\left( Y\right) /{C}_{ * }\left( B\right)
\]

since bases for these three relative cellular chain complexes correspond bijectively with the cells of \( \left( {X - A}\right)  \times  \left( {Y - B}\right) , X - A \) , and \( Y - B \) , respectively.

As a special case, suppose \( A \) and \( B \) are basepoints \( {x}_{0} \in  X \) and \( {y}_{0} \in  Y \) . Then the subcomplex \( A \times  Y \cup  X \times  B \) can be identified with the wedge sum \( X \vee  Y \) and the quotient \( X \times  Y/X \vee  Y \) is the smash product \( X \land  Y \) . Thus we have a reduced Künneth formula

\[
0 \rightarrow  {\bigoplus }_{i}\left( {{\widetilde{H}}_{i}\left( {X;R}\right) { \otimes  }_{R}{\widetilde{H}}_{n - i}\left( {Y;R}\right) }\right)  \rightarrow  {\widetilde{H}}_{n}\left( {X \land  Y;R}\right)  \rightarrow
\]

\[
{\bigoplus }_{i}{\operatorname{Tor}}_{R}\left( {{\widetilde{H}}_{i}\left( {X;R}\right) ,{\widetilde{H}}_{n - i - 1}\left( {Y;R}\right) }\right)  \rightarrow  0
\]

If we take \( Y = {S}^{k} \) for example, then \( X \land  {S}^{k} \) is the \( k \) -fold reduced suspension of \( X \) , and we obtain isomorphisms \( {\widetilde{H}}_{n}\left( {X;R}\right)  \approx  {\widetilde{H}}_{n + k}\left( {X \land  {S}^{k};R}\right) \) .

The Künneth formula and the universal coefficient theorem can be combined to give a more concise formula \( {H}_{n}\left( {X \times  Y;R}\right)  \approx  { \oplus  }_{i}{H}_{i}\left( {X;{H}_{n - i}\left( {Y;R}\right) }\right) \) . The naturality of this isomorphism is somewhat problematic, however, since it uses the splittings in the Künneth formula and universal coefficient theorem. With a little more algebra the formula can be shown to hold more generally for an arbitrary coefficient group \( G \) in place of \( R \) ; see [Hilton & Wylie 1967], p. 227.

There is an analogous formula \( {\widetilde{H}}_{n}\left( {X \land  Y;R}\right)  \approx  {\bigoplus }_{i}{\widetilde{H}}_{i}\left( {X;{\widetilde{H}}_{n - i}\left( {Y;R}\right) }\right) \) . As a special case, when \( Y \) is a Moore space \( M\left( {G, k}\right) \) we obtain isomorphisms \( {\widetilde{H}}_{n}\left( {X;G}\right)  \approx \; {\widetilde{H}}_{n + k}\left( {X \land  M\left( {G, k}\right) ;\mathbb{Z}}\right) \) . Again naturality is an issue, but in this case there is a natural isomorphism obtainable by applying Theorem 4.59 in §4.3, after verifying that the functors \( {h}_{n}\left( X\right)  = {\widetilde{H}}_{n + k}\left( {X \land  M\left( {G, k}\right) ;\mathbb{Z}}\right) \) define a reduced homology theory, which is not hard. The isomorphism \( {\widetilde{H}}_{n}\left( {X;G}\right)  \approx  {\widetilde{H}}_{n + k}\left( {X \land  M\left( {G, k}\right) ;\mathbb{Z}}\right) \) says that homology with arbitrary coefficients can be obtained from homology with \( \mathbb{Z} \) coefficients by a topological construction as well as by the algebra of tensor products. For general homology theories this formula can be used as a definition of homology with coefficients.

One might wonder about a cohomology version of the Künneth formula. Taking coefficients in a field \( F \) and using the natural isomorphism \( \operatorname{Hom}\left( {A \otimes  B, C}\right)  \approx \; \operatorname{Hom}\left( {A,\operatorname{Hom}\left( {B, C}\right) }\right) \) , the Künneth formula for homology and the universal coefficient theorem give isomorphisms

\[
{H}^{n}\left( {X \times  Y;F}\right)  \approx  {\operatorname{Hom}}_{F}\left( {{H}_{n}\left( {X \times  Y;F}\right) , F}\right)  \approx  {\bigoplus }_{i}{\operatorname{Hom}}_{F}\left( {{H}_{i}\left( {X;F}\right)  \otimes  {H}_{n - i}\left( {Y;F}\right) , F}\right)
\]

\[
\approx  {\bigoplus }_{i}{\operatorname{Hom}}_{F}\left( {{H}_{i}\left( {X;F}\right) ,{\operatorname{Hom}}_{F}\left( {{H}_{n - i}\left( {Y;F}\right) , F}\right) }\right)
\]

\[
\approx  {\bigoplus }_{i}{\operatorname{Hom}}_{F}\left( {{H}_{i}\left( {X;F}\right) ,{H}^{n - i}\left( {Y;F}\right) }\right)
\]

\[
\approx  {\bigoplus }_{i}{H}^{i}\left( {X;{H}^{n - i}\left( {Y;F}\right) }\right)
\]

More generally, there are isomorphisms \( {H}^{n}\left( {X \times  Y;G}\right)  \approx  {\bigoplus }_{i}{H}^{i}\left( {X;{H}^{n - i}\left( {Y;G}\right) }\right) \) for any coefficient group \( G \) ; see [Hilton &Wylie 1967], p. 227. However, in practice it usually suffices to apply the Künneth formula for homology and the universal coefficient theorem for cohomology separately. Also, Theorem 3.15 shows that with stronger hypotheses one can draw stronger conclusions using cup products.

## The Simplicial Cross Product

Let us sketch how the cross product \( {H}_{m}\left( {X;R}\right)  \otimes  {H}_{n}\left( {Y;R}\right)  \rightarrow  {H}_{m + n}\left( {X \times  Y;R}\right) \) can be defined directly in terms of singular homology. What one wants is a cross product at the level of singular chains, \( {C}_{m}\left( {X;R}\right)  \otimes  {C}_{n}\left( {Y;R}\right)  \rightarrow  {C}_{m + n}\left( {X \times  Y;R}\right) \) . If we are given singular simplices \( f : {\Delta }^{m} \rightarrow  X \) and \( g : {\Delta }^{n} \rightarrow  Y \) , then we have the product map \( f \times  g : {\Delta }^{m} \times  {\Delta }^{n} \rightarrow  X \times  Y \) , and the idea is to subdivide \( {\Delta }^{m} \times  {\Delta }^{n} \) into simplices of dimension \( m + n \) and then take the sum of the restrictions of \( f \times  g \) to these simplices, with appropriate signs.

In the special cases that \( m \) or \( n \) is 1 we have already seen how to subdivide \( {\Delta }^{m} \times  {\Delta }^{n} \) into simplices when we constructed prism operators in \( \text{ § }{2.1} \) . The generalization to \( {\Delta }^{m} \times  {\Delta }^{n} \) is not completely obvious, however. Label the vertices of \( {\Delta }^{m} \) as \( {v}_{0},{v}_{1},\cdots ,{v}_{m} \) and the vertices of \( {\Delta }^{n} \) as \( {w}_{0},{w}_{1},\cdots ,{w}_{n} \) . Think of the pairs \( \left( {i, j}\right) \) with \( 0 \leq  i \leq  m \) and \( 0 \leq  j \leq  n \) as the vertices of an \( m \times  n \) rectangular grid in \( {\mathbb{R}}^{2} \) . Let \( \sigma \) be a path formed by a sequence of \( m + n \) horizontal and vertical edges in this grid starting at \( \left( {0,0}\right) \) and ending at \( \left( {m, n}\right) \) , always moving either to the right or upward. To such a path \( \sigma \) we associate a linear map \( {\ell }_{\sigma } : {\Delta }^{m + n} \rightarrow  {\Delta }^{m} \times  {\Delta }^{n} \) sending the \( {k}^{th} \) vertex of \( {\Delta }^{m + n} \) to \( \left( {{v}_{{i}_{k}},{w}_{{j}_{k}}}\right) \) where \( \left( {{i}_{k},{j}_{k}}\right) \) is the \( {k}^{th} \) vertex of the edgepath \( \sigma \) . Then we define a simplicial cross product

\[
{C}_{m}\left( {X;R}\right)  \otimes  {C}_{n}\left( {Y;R}\right) \overset{ \times  }{ \rightarrow  }{C}_{m + n}\left( {X \times  Y;R}\right)
\]

by the formula

\[
f \times  g = \mathop{\sum }\limits_{\sigma }{\left( -1\right) }^{\left| \sigma \right| }\left( {f \times  g}\right) {\ell }_{\sigma }
\]

where \( \left| \sigma \right| \) is the number of squares in the grid lying below the path \( \sigma \) . Note that the symbol ‘ \( \times \) ’ means different things on the two sides of the equation. From this definition it is a calculation to show that \( \partial \left( {f \times  g}\right)  = \partial f \times  g + {\left( -1\right) }^{m}f \times  \partial g \) . This implies that the cross product of two cycles is a cycle, and the cross product of a cycle and a boundary is a boundary, so there is an induced cross product in singular homology.

One can see that the images of the maps \( {\ell }_{\sigma } \) give a simplicial structure on \( {\Delta }^{m} \times  {\Delta }^{n} \) in the following way. We can view \( {\Delta }^{m} \) as the subspace of \( {\mathbb{R}}^{m} \) defined by the inequalities \( 0 \leq  {x}_{1} \leq  \cdots  \leq  {x}_{m} \leq  1 \) , with the vertex \( {v}_{i} \) as the point having coordinates \( m - i \) zeros followed by \( i \) ones. Similarly we have \( {\Delta }^{n} \subset  {\mathbb{R}}^{n} \) with coordinates \( 0 \leq  {y}_{1} \leq  \cdots  \leq  {y}_{n} \leq  1 \) . The product \( {\Delta }^{m} \times  {\Delta }^{n} \) then consists of \( \left( {m + n}\right) \) -tuples \( \left( {{x}_{1},\cdots ,{x}_{m},{y}_{1},\cdots ,{y}_{n}}\right) \) satisfying both sets of inequalities. The combined inequalities \( 0 \leq  {x}_{1} \leq  \cdots  \leq  {x}_{m} \leq  {y}_{1} \leq  \cdots  \leq  {y}_{n} \leq  1 \) define a simplex \( {\Delta }^{m + n} \) in \( {\Delta }^{m} \times  {\Delta }^{n} \) , and every other point of \( {\Delta }^{m} \times  {\Delta }^{n} \) satisfies a similar set of inequalities obtained from \( 0 \leq  {x}_{1} \leq  \cdots  \leq  {x}_{m} \leq  {y}_{1} \leq  \cdots  \leq  {y}_{n} \leq  1 \) by a permutation of the variables ’shuffling’ the \( {y}_{j} \) ’s into the \( {x}_{i} \) ’s. Each such shuffle corresponds to an edgepath \( \sigma \) consisting of a rightward edge for each \( {x}_{i} \) and an upward edge for each \( {y}_{j} \) in the shuffled sequence. Thus we have \( {\Delta }^{m} \times  {\Delta }^{n} \) expressed as the union of simplices \( {\Delta }_{\sigma }^{m + n} \) indexed by the edgepaths \( \sigma \) . One can check that these simplices fit together nicely to form a \( \Delta \) -complex structure on \( {\Delta }^{m} \times  {\Delta }^{n} \) , which is also a simplicial complex structure. See [Eilenberg & Steenrod 1952], p. 68. In fact this construction is sufficiently natural to make the product of any two \( \Delta \) -complexes into a \( \Delta \) -complex.

## The Cohomology Cross Product

In §3.2 we defined a cross product

\[
{H}^{k}\left( {X;R}\right)  \times  {H}^{\ell }\left( {Y;R}\right) \overset{ \times  }{ \rightarrow  }{H}^{k + \ell }\left( {X \times  Y;R}\right)
\]

in terms of the cup product. Let us now describe the alternative approach in which the cross product is defined directly via cellular cohomology, and then cup product is defined in terms of this cross product.

The cellular definition of cohomology cross product is very much like the definition in homology. Given CW complexes \( X \) and \( Y \) , define a cross product of cellular cochains \( \varphi  \in  {C}^{k}\left( {X;R}\right) \) and \( \psi  \in  {C}^{\ell }\left( {Y;R}\right) \) by setting

\[
\left( {\varphi  \times  \psi }\right) \left( {{e}_{\alpha }^{k} \times  {e}_{\beta }^{\ell }}\right)  = \varphi \left( {e}_{\alpha }^{k}\right) \psi \left( {e}_{\beta }^{\ell }\right)
\]

and letting \( \varphi  \times  \psi \) take the value 0 on \( \left( {k + \ell }\right) \) -cells of \( X \times  Y \) which are not the product of a \( k \) -cell of \( X \) with an \( \ell \) -cell of \( Y \) . Another way of saying this is to use the convention that a cellular cochain in \( {C}^{k}\left( {X;R}\right) \) takes the value 0 on cells of dimension different from \( k \) , and then we can let \( \left( {\varphi  \times  \psi }\right) \left( {{e}_{\alpha }^{m} \times  {e}_{\beta }^{n}}\right)  = \varphi \left( {e}_{\alpha }^{m}\right) \psi \left( {e}_{\beta }^{n}\right) \) for all \( m \) and \( n \) .

The cellular coboundary formula \( \delta \left( {\varphi  \times  \psi }\right)  = {\delta \varphi } \times  \psi  + {\left( -1\right) }^{k}\varphi  \times  {\delta \psi } \) for cellular cochains \( \varphi  \in  {C}^{k}\left( {X;R}\right) \) and \( \psi  \in  {C}^{\ell }\left( {Y;R}\right) \) follows easily from the corresponding boundary formula in Proposition 3B.1, namely

\[
\delta \left( {\varphi  \times  \psi }\right) \left( {{e}_{\alpha }^{m} \times  {e}_{\beta }^{n}}\right)  = \left( {\varphi  \times  \psi }\right) \left( {\partial \left( {{e}_{\alpha }^{m} \times  {e}_{\beta }^{n}}\right) }\right)
\]

\[
= \left( {\varphi  \times  \psi }\right) \left( {\partial {e}_{\alpha }^{m} \times  {e}_{\beta }^{n} + {\left( -1\right) }^{m}{e}_{\alpha }^{m} \times  \partial {e}_{\beta }^{n}}\right)
\]

\[
= {\delta \varphi }\left( {e}_{\alpha }^{m}\right) \psi \left( {e}_{\beta }^{n}\right)  + {\left( -1\right) }^{m}\varphi \left( {e}_{\alpha }^{m}\right) {\delta \psi }\left( {e}_{\beta }^{n}\right)
\]

\[
= \left( {{\delta \varphi } \times  \psi  + {\left( -1\right) }^{k}\varphi  \times  {\delta \psi }}\right) \left( {{e}_{\alpha }^{m} \times  {e}_{\beta }^{n}}\right)
\]

where the coefficient \( {\left( -1\right) }^{m} \) in the next-to-last line can be replaced by \( {\left( -1\right) }^{k} \) since \( \varphi \left( {e}_{\alpha }^{m}\right)  = 0 \) unless \( k = m \) . From the formula \( \delta \left( {\varphi  \times  \psi }\right)  = {\delta \varphi } \times  \psi  + {\left( -1\right) }^{k}\varphi  \times  {\delta \psi } \) it follows just as for homology and for cup product that there is an induced cross product in cellular cohomology.

To show this agrees with the earlier definition, we can first reduce to the case that \( X \) has trivial \( \left( {k - 1}\right) \) -skeleton and \( Y \) has trivial \( \left( {\ell  - 1}\right) \) -skeleton via the commutative diagram

\[
{H}^{k}\left( {X/{X}^{k - 1};R}\right)  \times  {H}^{\ell }\left( {Y/{Y}^{\ell  - 1};R}\right) \xrightarrow[]{ \times  }{H}^{k + \ell }\left( {X/{X}^{k - 1} \times  Y/{Y}^{\ell  - 1};R}\right)
\]

\( {H}^{k}\left( {X;R}\right)  \times  {H}^{\ell }\left( {Y;R}\right) \xrightarrow[]{ \times  }{H}^{k + \ell }\left( {X \times  Y;R}\right) \)

The left-hand vertical map is surjective, so by commutativity, if the two definitions of cross product agree in the upper row, they agree in the lower row. Next, assuming \( {X}^{k - 1} \) and \( {Y}^{\ell  - 1} \) are trivial, consider the commutative diagram

![bo_d7dtv0s91nqc73eq8nv0_287_475_1388_837_190_0.jpg](images/bo_d7dtv0s91nqc73eq8nv0_287_475_1388_837_190_0.jpg)

The vertical maps here are injective, \( {X}^{k} \times  {Y}^{\ell } \) being the \( \left( {k + \ell }\right) \) -skeleton of \( X \times  Y \) , so it suffices to see that the two definitions agree in the lower row. We have \( {X}^{k} = \mathop{\bigvee }\limits_{\alpha }{S}_{\alpha }^{k} \) and \( {Y}^{\ell } = \mathop{\bigvee }\limits_{\beta }{S}_{\beta }^{\ell } \) , so by restriction to these wedge summands the question is reduced finally to the case of a product \( {S}_{\alpha }^{k} \times  {S}_{\beta }^{\ell } \) . In this case, taking \( R = \mathbb{Z} \) , we showed in Theorem 3.15 that the cross product in question is the map \( \mathbb{Z} \times  \mathbb{Z} \rightarrow  \mathbb{Z} \) sending \( \left( {1,1}\right) \) to \( \pm  1 \) , with the original definition of cross product. The same is obviously true using the cellular cross product. So for \( R = \mathbb{Z} \) the two cross products agree up to sign, and it follows that this is also true for arbitrary \( R \) . We leave it to the reader to sort out the matter of signs.

To relate cross product to cup product we use the diagonal map \( \Delta  : X \rightarrow  X \times  X \) , \( x \mapsto  \left( {x, x}\right) \) . If we are given a definition of cross product, we can define cup product as the composition

\[
{H}^{k}\left( {X;R}\right)  \times  {H}^{\ell }\left( {X;R}\right) \overset{ \times  }{ \rightarrow  }{H}^{k + \ell }\left( {X \times  X;R}\right) \overset{{\Delta }^{ * }}{ \rightarrow  }{H}^{k + \ell }\left( {X;R}\right)
\]

This agrees with the original definition of cup product since we have \( {\Delta }^{ * }\left( {a \times  b}\right)  = \; {\Delta }^{ * }\left( {{p}_{1}^{ * }\left( a\right)  \smile  {p}_{2}^{ * }\left( b\right) }\right)  = {\Delta }^{ * }\left( {{p}_{1}^{ * }\left( a\right) }\right)  \smile  {\Delta }^{ * }\left( {{p}_{2}^{ * }\left( b\right) }\right)  = a \smile  b \) , as both compositions \( {p}_{1}\Delta \) and \( {p}_{2}\Delta \) are the identity map of \( X \) .

Unfortunately, the definition of cellular cross product cannot be combined with \( \Delta \) to give a definition of cup product at the level of cellular cochains. This is because \( \Delta \) is not a cellular map, so it does not induce a map of cellular cochains. It is possible to homotope \( \Delta \) to a cellular map by Theorem 4.8, but this involves arbitrary choices. For example, the diagonal of a square can be pushed across either adjacent triangle. In particular cases one might hope to understand the geometry well enough to compute an explicit cellular approximation to the diagonal map, but usually other techniques for computing cup products are preferable.

The cohomology cross product satisfies the same commutativity relation as for homology, namely \( {T}^{ * }\left( {a \times  b}\right)  = {\left( -1\right) }^{k\ell }b \times  a \) for \( T : X \times  Y \rightarrow  Y \times  X \) the transposition map, \( a \in  {H}^{k}\left( {Y;R}\right) \) , and \( b \in  {H}^{\ell }\left( {X;R}\right) \) . The proof is the same as for homology. Taking \( X = Y \) and noting that \( {T\Delta } = \Delta \) , we obtain a new proof of the commutativity property of cup product.

## Exercises

1. Compute the groups \( {H}_{i}\left( {{\mathbb{{RP}}}^{m} \times  {\mathbb{{RP}}}^{n};G}\right) \) and \( {H}^{i}\left( {{\mathbb{{RP}}}^{m} \times  {\mathbb{{RP}}}^{n};G}\right) \) for \( G = \mathbb{Z} \) and \( {\mathbb{Z}}_{2} \) via the cellular chain and cochain complexes. [See Example 3B.4.]

2. Let \( C \) and \( {C}^{\prime } \) be chain complexes, and let \( I \) be the chain complex consisting of \( \mathbb{Z} \) in dimension 1 and \( \mathbb{Z} \times  \mathbb{Z} \) in dimension 0, with the boundary map taking a generator \( e \) in dimension 1 to the difference \( {v}_{1} - {v}_{0} \) of generators \( {v}_{i} \) of the two \( \mathbb{Z} \) ’s in dimension 0 . Show that a chain map \( f : I \otimes  C \rightarrow  {C}^{\prime } \) is precisely the same as a chain homotopy between the two chain maps \( {f}_{i} : C \rightarrow  {C}^{\prime }, c \mapsto  f\left( {{v}_{i} \otimes  c}\right) , i = 0,1 \) . [The chain homotopy is \( h\left( c\right)  = f\left( {e \otimes  c}\right) \) .]

3. Show that the splitting in the topological Künneth formula cannot be natural by considering the map \( f \times  \mathbb{1} : M\left( {{\mathbb{Z}}_{m}, n}\right)  \times  M\left( {{\mathbb{Z}}_{m}, n}\right)  \rightarrow  {S}^{n + 1} \times  M\left( {{\mathbb{Z}}_{m}, n}\right) \) where \( f \) collapses the \( n \) -skeleton of \( M\left( {{\mathbb{Z}}_{m}, n}\right)  = {S}^{n} \cup  {e}^{n + 1} \) to a point.

4. Show that the cross product of fundamental classes for closed \( R \) -orientable manifolds \( M \) and \( N \) is a fundamental class for \( M \times  N \) .

## 5. Show that slant products

\[
{H}_{n}\left( {X \times  Y;R}\right)  \times  {H}^{j}\left( {Y;R}\right)  \rightarrow  {H}_{n - j}\left( {X;R}\right) ,\;\left( {{e}^{i} \times  {e}^{j},\varphi }\right)  \mapsto  \varphi \left( {e}^{j}\right) {e}^{i}
\]

\[
{H}^{n}\left( {X \times  Y;R}\right)  \times  {H}_{j}\left( {Y;R}\right)  \rightarrow  {H}^{n - j}\left( {X;R}\right) ,\;\left( {\varphi ,{e}^{j}}\right)  \mapsto  \left( {{e}^{i} \mapsto  \varphi \left( {{e}^{i} \times  {e}^{j}}\right) }\right)
\]

can be defined via the indicated cellular formulas. [These 'products' are in some ways more like division than multiplication, and this is reflected in the common notation \( a/b \) for them, or \( a \smallsetminus  b \) when the order of the factors is reversed. The first of the two slant products is related to cap product in the same way that the cohomology cross product is related to cup product.]
