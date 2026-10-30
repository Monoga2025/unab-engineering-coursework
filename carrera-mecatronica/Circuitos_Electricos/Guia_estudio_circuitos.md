# Guía de estudio - Taller de Circuitos

Fuente: `C:\Users\Monoga\Downloads\TALLER (1).pdf`. Los diagramas de las cuatro páginas se revisaron visualmente antes de plantear las ecuaciones.

## Reglas rápidas antes de empezar

### Análisis nodal

1. Elige la línea inferior como referencia: \(0\,\mathrm V\).
2. Rotula cada nodo desconocido. Un nodo unido a tierra por una fuente de tensión con \(+\) arriba vale directamente el voltaje de la fuente.
3. En cada nodo, toma como positivas las corrientes que **salen**:

\[
\sum \frac{V_{\text{nodo}}-V_{\text{vecino}}}{R}=0.
\]

4. Una fuente de corriente que entra al nodo se escribe negativa con esa convención.

### Análisis de mallas

1. Dibuja una corriente horaria por cada ventana del circuito.
2. En un resistor compartido por las mallas \(I_a,I_b\), la caída es \(R(I_a-I_b)\), según el sentido de recorrido de \(I_a\).
3. Al recorrer una fuente de \(-\) a \(+\), hay un ascenso: se escribe como \(-V_s\) si se están sumando caídas.

### Superposición

Se deja activa **una fuente independiente por vez**. Las fuentes dependientes nunca se apagan.

| Fuente apagada | Sustitución |
|---|---|
| Fuente independiente de tensión | Cortocircuito |
| Fuente independiente de corriente | Circuito abierto |

Al final se suman las contribuciones con signo. Un resultado negativo significa que la contribución real va opuesta a la flecha o polaridad definida.

### Transformación de fuentes

\[
V_s\text{ en serie con }R
\quad\Longleftrightarrow\quad
I_N=\frac{V_s}{R}\text{ en paralelo con }R.
\]

La orientación importa: una fuente Norton que inyecta hacia un nodo produce una tensión Thevenin positiva en ese nodo. Para una fuente de corriente de \(A\) hacia \(B\) en paralelo con \(R\), la equivalente Thevenin tiene \(B\) positivo respecto de \(A\), con magnitud \(IR\).

---

## I. Análisis nodal y de mallas

### 1. Hallar \(V_1\) por nodos

**Dibujo para el cuaderno.** Tierra en el riel inferior. El nodo \(V_1\) se une a \(10\,\mathrm V\) por resistores de \(10\Omega\) y \(5\Omega\), a \(20\,\mathrm V\) por \(4\Omega\), y a tierra por \(10\Omega\).

Aplicando KCL en \(V_1\):

\[
\frac{V_1-10}{10}+\frac{V_1-10}{5}+\frac{V_1-20}{4}+\frac{V_1}{10}=0.
\]

\[
\boxed{V_1=\frac{160}{13}=12.31\,\mathrm V}
\]

**Chequeo.** Las corrientes salientes suman
\[
\frac3{13}+\frac6{13}-\frac{25}{13}+\frac{16}{13}=0.
\]
El término negativo por \(4\Omega\) indica que ese ramal realmente inyecta corriente desde la fuente de \(20\,\mathrm V\).

### 2. Hallar \(i_o\) por nodos

**Dibujo para el cuaderno.** Marca el nodo superior \(V_T\), el nodo central \(V_B\), y el nodo izquierdo conocido \(60\,\mathrm V\). La fuente dependiente inyecta \(3i_o\) desde tierra hacia \(V_B\). La flecha \(i_o\) corresponde a la corriente del resistor de \(4\Omega\):

\[
i_o=\frac{60-V_T}{4}.
\]

\[
\frac{V_T-60}{4}+\frac{V_T-V_B}{2}+\frac{V_T}{8}=0
\]

\[
\frac{V_B-V_T}{2}+\frac{V_B-60}{10}-3i_o=0.
\]

\[
V_T=\frac{690}{13}=53.08\,\mathrm V,
\qquad V_B=62.88\,\mathrm V
\]

\[
\boxed{i_o=\frac{45}{26}=1.731\,\mathrm A}
\]

**Chequeo.** \(60>V_T\), así que la corriente real va desde la fuente de \(60\,\mathrm V\) hacia el nodo superior, igual que la flecha.

### 3. Hallar \(i_a,i_b,i_c\) por mallas

**Dibujo para el cuaderno.** Traza dos mallas horarias: \(I_1\) a la izquierda e \(I_2\) a la derecha. La rama central es compartida y tiene \(10\Omega\) en serie con la fuente de \(45\,\mathrm V\).

\[
30-20I_1-10(I_1-I_2)-45=0
\]

\[
45-10(I_2-I_1)-5I_2-15I_2=0
\]

\[
30I_1-10I_2=-15,
\qquad -10I_1+30I_2=45
\]

\[
I_1=0,qquad I_2=1.5\,\mathrm A.
\]

Las flechas originales se relacionan así:

\[
\boxed{i_a=0\,\mathrm A},\qquad
\boxed{i_b=I_1-I_2=-1.5\,\mathrm A},\qquad
\boxed{i_c=I_2=1.5\,\mathrm A}.
\]

**Chequeo.** \(i_b<0\): la corriente real de la rama central sube \(1.5\,\mathrm A\), no baja como la flecha de referencia.

### 4. Hallar \(v_{ab}\) e \(i_o\) por mallas

**Dibujo para el cuaderno.** Hay tres mallas horarias: \(I_1\) arriba a la izquierda, \(I_2\) abajo a la izquierda y \(I_3\) en el triángulo derecho. El resistor horizontal central de \(20\Omega\) es compartido por \(I_1\) e \(I_2\). El resistor vertical derecho es de \(30\Omega\); por él baja \(i_o=I_3\).

\[
20I_1+30(I_1-I_3)+20(I_1-I_2)-80=0
\]

\[
20(I_2-I_1)+30(I_2-I_3)+20I_2-80=0
\]

\[
30(I_3-I_1)+30I_3+30(I_3-I_2)=0.
\]

\[
70I_1-20I_2-30I_3=80
\]

\[
-20I_1+70I_2-30I_3=80
\]

\[
-30I_1-30I_2+90I_3=0.
\]

\[
I_1=I_2=\frac83\,\mathrm A,
\qquad I_3=\frac{16}{9}\,\mathrm A.
\]

\[
\boxed{i_o=\frac{16}{9}=1.778\,\mathrm A}
\]

\[
\boxed{v_{ab}=30I_3=\frac{160}{3}=53.33\,\mathrm V}
\]

**Chequeo.** \(v_{ab}>0\), coherente con la polaridad \(+\) arriba y \(-\) abajo del diagrama.

### 5. Hallar \(v_1,v_2,v_3\) por nodos

**Dibujo para el cuaderno.** Rotula los tres nodos superiores \(v_1,v_2,v_3\). La fuente de \(3\,\mathrm A\) va de \(v_1\) hacia \(v_3\); la de \(5\,\mathrm A\) inyecta de tierra a \(v_1\). El extremo inferior del resistor derecho de \(8\Omega\) está a \(+12\,\mathrm V\), no a tierra.

\[
\frac{v_1}{4}+\frac{v_1-v_2}{8}+\frac{v_1-v_3}{2}+3-5=0
\]

\[
\frac{v_2}{2}+\frac{v_2-v_1}{8}+\frac{v_2-v_3}{4}=0
\]

\[
\frac{v_3-12}{8}+\frac{v_3-v_2}{4}+\frac{v_3-v_1}{2}-3=0.
\]

\[
7v_1-v_2-4v_3=16,
\quad -v_1+7v_2-2v_3=0,
\quad -4v_1-2v_2+7v_3=36.
\]

\[
\boxed{v_1=20.80\,\mathrm V},
\qquad \boxed{v_2=8.533\,\mathrm V},
\qquad \boxed{v_3=19.47\,\mathrm V}.
\]

**Chequeo.** En \(v_1\), las corrientes por resistores más los \(3\,\mathrm A\) que salen equilibran los \(5\,\mathrm A\) que entran.

---

## II. Linealidad, superposición y transformación de fuentes

### 6. Linealidad: \(v_o\) e \(i_o\)

**Dibujo para el cuaderno.** Llame \(v_m\) al nodo central y \(v_o\) al nodo superior del resistor derecho. Inicialmente los cinco resistores valen \(1\Omega\), y \(i_o\) baja por el resistor de salida.

\[
(v_m-v_s)+(v_m-v_o)+v_m=0
\]

\[
(v_o-v_s)+(v_o-v_m)+v_o=0.
\]

\[
v_m=v_o=\frac{v_s}{2},
\qquad i_o=\frac{v_o}{1\Omega}=\frac{v_s}{2}\,\mathrm A.
\]

| Caso | \(v_o\) | \(i_o\) |
|---|---:|---:|
| \(v_s=1\,\mathrm V\) | \(0.5\,\mathrm V\) | \(0.5\,\mathrm A\) |
| \(v_s=10\,\mathrm V\) | \(5.0\,\mathrm V\) | \(5.0\,\mathrm A\) |
| Todas las resistencias cambian a \(10\Omega\), \(v_s=10\,\mathrm V\) | \(5.0\,\mathrm V\) | \(0.5\,\mathrm A\) |

**Chequeo.** Al multiplicar todas las resistencias por diez, las razones de voltaje no cambian; las corrientes sí disminuyen diez veces.

### 7. Superposición: \(v_o\)

**Dibujo para el cuaderno.** Dibuja tres versiones del circuito: solo la fuente de \(20\,\mathrm V\), solo la fuente de \(2\,\mathrm A\), y solo la fuente de \(1\,\mathrm A\). Apaga las otras fuentes independientes según la tabla inicial.

| Fuente activa | Contribución a \(v_o\) |
|---|---:|
| \(20\,\mathrm V\) | \(v_o^{(20V)}=10\,\mathrm V\) |
| \(2\,\mathrm A\), de derecha a izquierda | \(v_o^{(2A)}=-3\,\mathrm V\) |
| \(1\,\mathrm A\), de tierra al nodo central | \(v_o^{(1A)}=1\,\mathrm V\) |

\[
\boxed{v_o=10-3+1=8\,\mathrm V}.
\]

**Chequeo.** La fuente de \(2\,\mathrm A\) reduce la salida; por eso su contribución debe conservar el signo negativo.

### 8. Superposición: \(i_o\)

**Dibujo para el cuaderno.** La corriente \(i_o\) va hacia la derecha por el resistor de \(4\Omega\). Dibuja tres circuitos con una fuente activa: \(108\,\mathrm V\), \(36\,\mathrm A\) y \(18\,\mathrm A\).

\[
i_o=\frac{108-V_A}{4}
\]

| Fuente activa | \(V_A\) | Contribución a \(i_o\) |
|---|---:|---:|
| \(108\,\mathrm V\) | \(60\,\mathrm V\) | \(+12\,\mathrm A\) |
| \(36\,\mathrm A\) | \(24\,\mathrm V\) | \(-6\,\mathrm A\) |
| \(18\,\mathrm A\) | \(20\,\mathrm V\) | \(-5\,\mathrm A\) |

\[
\boxed{i_o=12-6-5=1.0\,\mathrm A}.
\]

**Chequeo.** El resultado positivo confirma que la corriente neta sigue la flecha de referencia.

### 9. Transformación de fuentes: \(i_o\)

**Dibujo para el cuaderno.** Marca nodo \(A\) a la izquierda, nodo \(B\) antes del resistor de \(4\Omega\), y el nodo conocido de \(20\,\mathrm V\) a la derecha. Redibuja estas equivalencias:

\[
6\,\mathrm A\parallel2\Omega
\Longleftrightarrow
12\,\mathrm V\text{ en serie con }2\Omega
\]

\[
3\,\mathrm A\parallel5\Omega
\Longleftrightarrow
15\,\mathrm V\text{ en serie con }5\Omega,
\quad (+)\text{ en }B.
\]

Como verificación nodal del circuito equivalente:

\[
\frac{V_A}{2}+\frac{V_A-V_B}{5}+3-6=0
\]

\[
\frac{V_B-V_A}{5}+\frac{V_B-20}{4}-3=0.
\]

\[
V_A=\frac{118}{11}\,\mathrm V,
\qquad V_B=\frac{248}{11}\,\mathrm V
\]

\[
\boxed{i_o=\frac{V_B-20}{4}=\frac7{11}=0.636\,\mathrm A}.
\]

**Chequeo.** \(V_B>20\,\mathrm V\), por eso la corriente real por \(4\Omega\) va hacia la derecha.

### 10. Transformación de fuentes dependiente: \(i_x\)

**Dibujo para el cuaderno.** El nodo a la salida de \(15\Omega\) es \(V_A\); el nodo derecho es \(V_B\). Dibuja la transformación de la fuente independiente:

\[
60\,\mathrm V\text{ serie }15\Omega
\Longleftrightarrow
4\,\mathrm A\parallel15\Omega.
\]

No se apaga ni se sustituye sin cuidado la fuente dependiente \(0.5i_x\). Conserva la definición de control:

\[
i_x=\frac{60-V_A}{15}.
\]

\[
\frac{V_A-60}{15}+\frac{V_A}{50}+\frac{V_A-V_B}{10}+0.5i_x=0
\]

\[
\frac{V_B}{40}+\frac{V_B-V_A}{10}-0.5i_x=0.
\]

\[
V_A=36\,\mathrm V,
\qquad V_B=35.2\,\mathrm V
\]

\[
\boxed{i_x=\frac{60-36}{15}=1.60\,\mathrm A}.
\]

**Chequeo en \(V_A\).**

\[
-1.60+0.72+0.08+0.80=0.
\]
