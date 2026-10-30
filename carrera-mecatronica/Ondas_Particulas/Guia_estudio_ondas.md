# Guía de estudio: Ondas, cuerdas y armónicos

> Fuente: `C:\Users\Monoga\Downloads\Problemas_examen_1.pdf`, págs. 9–18. Los diez ejercicios de esta sección son: 15.12, 15.44, 15.50, 15.41, 15.47, 15.60, 15.65, 15.74, 15.15 y 15.3.

## Hoja de fórmulas

| Idea | Fórmula |
|---|---|
| Onda viajera hacia (+x) / (-x) | \(y=A\cos(kx-\omega t)\) / \(y=A\cos(kx+\omega t)\) |
| Número de onda y frecuencia angular | \(k=2\pi/\lambda\), \(\omega=2\pi f\) |
| Rapidez de onda | \(v=\lambda f=\omega/k\) |
| Cuerda tensa | \(v=\sqrt{T/\mu}\), \(\mu=m/L\) |
| Cuerda fija en ambos extremos | \(\lambda_n=2L/n\), \(f_n=nv/(2L)\) |
| Onda estacionaria | \(A(x)=A_{\max}|\sin(kx)|\) |
| Movimiento transversal local | \(v_{y,\max}=\omega A(x)\), \(a_{y,\max}=\omega^2A(x)\) |
| Potencia media | \(P_{\mathrm{med}}=\tfrac12\mu\omega^2A^2v\) |
| Cambio de tensión | \(v,f\propto\sqrt T\) si \(L,\mu,n\) no cambian |

## Mapa de decisión

1. **¿Dan una ecuación \(y(x,t)\)?** Identificá \(A,k,\omega\); después obtené \(\lambda,f,T,v\). El signo delante de \(\omega t\) indica la dirección.
2. **¿Hay extremos fijos y “armónico” \(n\)?** Dibujá \(n\) vientres y usá \(\lambda_n=2L/n\).
3. **¿Hay masa colgante, fuerza o tensión?** Primero hacé DCL: en equilibrio \(T=mg\); luego \(v=\sqrt{T/\mu}\).
4. **¿Piden potencia?** Hallá \(\mu,\omega,v\) y aplicá \(P_{\mathrm{med}}\).
5. **¿La onda pasa de cuerda a aire?** La **frecuencia no cambia**; cambian \(v\) y \(\lambda\) según el medio.

---

## 15.12 — Rapidez de propagación y rapidez de las partículas

**Datos:** \(y=A\cos[(2\pi/\lambda)(x-vt)]=A\cos(kx-\omega t)\).

**Dibujo:** onda senoide que avanza hacia \(+x\); sobre una partícula de la cuerda, flecha vertical \(v_y\). La onda se desplaza horizontalmente, cada punto de cuerda oscila verticalmente.

**Patrón reutilizable:** para hallar la velocidad de una partícula, derivá respecto al tiempo; no confundas \(v_y\) con la rapidez de propagación \(v\).

**Derivación esencial:**

\[
v_y=\frac{\partial y}{\partial t}=A\omega\sin(kx-\omega t)
\]

\[
v_{y,\max}=A\omega=A\frac{2\pi v}{\lambda}=\frac{2\pi A}{\lambda}v
\]

**Resultado:**

\[
\boxed{v_{y,\max}=v\iff A=\frac{\lambda}{2\pi}}
\]

Es menor que \(v\) si \(A<\lambda/(2\pi)\), y mayor si \(A>\lambda/(2\pi)\).

---

## 15.44 — Instrumento musical, segundo sobretono

**Datos:** \(L=0.750\ \mathrm{m}\), \(m=8.75\ \mathrm{g}\), \(v_{aire}=344\ \mathrm{m/s}\), \(\lambda_{aire}=3.35\ \mathrm{cm}\). Segundo sobretono \(\Rightarrow n=3\).

**Dibujo:** cuerda fija con tres vientres y cuatro nodos:

```text
N   vientre   N   vientre   N   vientre   N
|     ∩       |     ∪       |     ∩       |
```

**Patrón reutilizable:** cuerda y sonido producido comparten \(f\). Para el armónico \(n\), \(\lambda_n=2L/n\).

**Derivación esencial:**

\[
\mu=\frac{0.00875}{0.750}=0.01167\ \mathrm{kg/m}
\]

\[
f_3=\frac{344}{0.0335}=1.027\times10^4\ \mathrm{Hz},\qquad
\lambda_3=\frac{2(0.750)}3=0.500\ \mathrm{m}
\]

\[
v_{cuerda}=f_3\lambda_3=5.13\times10^3\ \mathrm{m/s}
\]

\[
T=\mu v_{cuerda}^2=3.08\times10^5\ \mathrm{N}
\]

**Resultados:**

\[
\boxed{T=3.08\times10^5\ \mathrm{N}},\qquad
\boxed{f_1=f_3/3=3.42\times10^3\ \mathrm{Hz}}
\]

---

## 15.50 — Leer una ecuación de onda viajera

**Datos:**

\[
y=(0.750\ \mathrm{cm})\cos\{\pi[(0.400\ \mathrm{cm^{-1}})x+(250\ \mathrm{s^{-1}})t]\}
\]

**Dibujo:** senoide de amplitud \(0.750\ \mathrm{cm}\) con flecha hacia \(-x\). Para los tres tiempos, repetí la misma senoide desplazada a la izquierda.

**Patrón reutilizable:** en \(\cos(kx+\omega t)\), la onda se mueve hacia \(-x\). Extraé \(k\) y \(\omega\) respetando las unidades.

**Derivación esencial:**

\[
A=0.00750\ \mathrm{m},\quad k=125.66\ \mathrm{rad/m},\quad \omega=785.4\ \mathrm{rad/s}
\]

\[
\lambda=\frac{2\pi}{k}=0.0500\ \mathrm{m},\quad
f=\frac{\omega}{2\pi}=125\ \mathrm{Hz}
\]

\[
T_{per}=\frac1f=8.00\times10^{-3}\ \mathrm{s},\quad
v=\frac\omega k=6.25\ \mathrm{m/s}
\]

Para las formas solicitadas:

\[
\begin{aligned}
t=0 &: y=A\cos(kx)\\
t=0.0005\ \mathrm{s} &: y=A\cos(kx+\pi/8),\quad \Delta x=0.3125\ \mathrm{cm}\\
t=0.0010\ \mathrm{s} &: y=A\cos(kx+\pi/4),\quad \Delta x=0.625\ \mathrm{cm}
\end{aligned}
\]

Con \(\mu=0.0500\ \mathrm{kg/m}\):

\[
T_{cuerda}=\mu v^2=\boxed{1.95\ \mathrm{N}}
\]

\[
P_{med}=\tfrac12\mu\omega^2A^2v=\boxed{5.42\ \mathrm{W}}
\]

---

## 15.41 — Tercer armónico de una cuerda fija

**Datos:**

\[
y=(5.60\ \mathrm{cm})\sin[(0.0340\ \mathrm{rad/cm})x]\sin[(50.0\ \mathrm{rad/s})t]
\]

**Dibujo:** tercer armónico: tres vientres, cuatro nodos. Marcá \(N-A-N-A-N-A-N\).

**Patrón reutilizable:** en una estacionaria \(y=A_{est}\sin(kx)\sin(\omega t)\), las ondas viajeras componentes tienen amplitud \(A_{est}/2\).

**Derivación esencial:**

\[
k=3.40\ \mathrm{rad/m},\quad \omega=50.0\ \mathrm{rad/s}
\]

\[
L=\frac{3\pi}{k}=2.77\ \mathrm{m},\quad
\lambda=\frac{2\pi}{k}=1.85\ \mathrm{m}
\]

\[
f=\frac{\omega}{2\pi}=7.96\ \mathrm{Hz},\quad
T_{per}=\frac{2\pi}{\omega}=0.126\ \mathrm{s},\quad
v=\frac\omega k=14.7\ \mathrm{m/s}
\]

\[
A_{viajera}=\frac{5.60}{2}=\boxed{2.80\ \mathrm{cm}}
\]

\[
v_{y,\max}=A_{est}\omega=(0.0560)(50.0)=\boxed{2.80\ \mathrm{m/s}}
\]

Para \(n=8\), si se conserva la amplitud dada:

\[
\boxed{y_8=(5.60\ \mathrm{cm})\sin[(0.0907\ \mathrm{rad/cm})x]\sin[(133\ \mathrm{rad/s})t]}
\]

---

## 15.47 — Cuerda de guitarra

**Datos:** \(L=0.635\ \mathrm{m}\), \(f_1=245\ \mathrm{Hz}\), \(v_{aire}=344\ \mathrm{m/s}\).

**Dibujo:** modo fundamental: dos nodos en extremos y un vientre central: `N — ∩ — N`.

**Patrón reutilizable:** fundamental de cuerda fija: \(\lambda_1=2L\). Si la tensión cambia, \(f\propto\sqrt T\). La frecuencia se conserva al producir sonido en el aire.

**Derivación esencial y resultados:**

\[
\lambda_1=2L=1.270\ \mathrm{m}
\]

\[
v_{cuerda}=\lambda_1f_1=(1.270)(245)=\boxed{311\ \mathrm{m/s}}
\]

\[
f_{nuevo}=245\sqrt{1.010}=\boxed{246.2\ \mathrm{Hz}}
\]

Para el sonido en aire de la cuerda inicialmente afinada:

\[
f_{aire}=\boxed{245\ \mathrm{Hz}},\qquad
\lambda_{aire}=\frac{344}{245}=\boxed{1.40\ \mathrm{m}}
\]

**Chequeo:** \(f\) y \(\omega\) son iguales en ambos medios; \(v\) y \(\lambda\) no.

---

## 15.60 — Alambre vertical con esfera

**Datos:** \(L=1.20\ \mathrm{m}\), tercer armónico \(n=3\), esfera de \(100.0\ \mathrm{N}\) y luego de \(500.0\ \mathrm{N}\).

**Dibujo/DCL:** tercer armónico con tres vientres y cuatro nodos. Para la esfera: flecha \(T\) hacia arriba y \(W\) hacia abajo; equilibrio \(T=W\).

**Patrón reutilizable:** para longitud fija y mismo número armónico, \(\lambda_n=2L/n\) no depende de la tensión. La tensión cambia \(v\) y \(f\), no la geometría modal.

**Derivación:**

\[
\lambda_3=\frac{2L}{3}=\frac{2(1.20)}3=\boxed{0.800\ \mathrm{m}}
\]

Al aumentar la carga, sigue siendo \(n=3\) y \(L\) no cambia:

\[
\boxed{\Delta\lambda_3=0}
\]

---

## 15.65 — Potencia media de una onda

**Datos:** \(L=8.00\ \mathrm{m}\), \(m=6.00\ \mathrm{g}\), \(v=30.0\ \mathrm{m/s}\), \(\lambda=0.200\ \mathrm{m}\), \(P_{med}=50.0\ \mathrm{W}\).

**Dibujo:** onda viajera con flecha de propagación; marcá amplitud \(A\), una longitud de onda \(\lambda\), y tensión \(T\) en cada extremo.

**Patrón reutilizable:** para la misma cuerda y amplitud, si \(\lambda\) se mantiene constante, \(P\propto\omega^2v\propto v^3\).

**Derivación esencial:**

\[
\mu=\frac{0.00600}{8.00}=7.50\times10^{-4}\ \mathrm{kg/m}
\]

\[
f=\frac v\lambda=150\ \mathrm{Hz},\quad \omega=2\pi f=942.5\ \mathrm{rad/s}
\]

\[
A=\sqrt{\frac{2P_{med}}{\mu\omega^2v}}
=\boxed{0.0707\ \mathrm{m}=7.07\ \mathrm{cm}}
\]

Si \(v\) se duplica con \(A,\lambda\) constantes:

\[
P_{nuevo}=2^2(2)P=8(50.0)=\boxed{400\ \mathrm{W}}
\]

---

## 15.74 — Amplitud, velocidad y aceleración según la posición

**Datos:** tercer armónico, \(v=192\ \mathrm{m/s}\), \(f=240\ \mathrm{Hz}\), \(A_{max}=0.400\ \mathrm{cm}=0.00400\ \mathrm{m}\).

**Dibujo obligatorio:**

```text
N(0) - A(0.20) - N(0.40) - A(0.60) - N(0.80) - A(1.00) - N(1.20)
```

**Patrón reutilizable:** primero localizá nodo/vientre con \(A(x)=A_{max}|\sin(kx)|\); luego el punto oscila como MAS con esa amplitud local.

**Derivación esencial:**

\[
\lambda=\frac{192}{240}=0.800\ \mathrm{m},\quad L=\frac{3\lambda}{2}=1.20\ \mathrm{m}
\]

\[
k=\frac{2\pi}{0.800}=2.5\pi\ \mathrm{rad/m},\quad \omega=2\pi(240)=1508\ \mathrm{rad/s}
\]

| Posición | \(A(x)\) | \(v_{y,max}=\omega A\) | \(a_{y,max}=\omega^2A\) |
|---|---:|---:|---:|
| \(0.400\ \mathrm{m}\) | \(0\) | \(0\) | \(0\) |
| \(0.200\ \mathrm{m}\) | \(0.00400\ \mathrm{m}\) | \(6.03\ \mathrm{m/s}\) | \(9.10\times10^3\ \mathrm{m/s^2}\) |
| \(0.100\ \mathrm{m}\) | \(0.00283\ \mathrm{m}\) | \(4.27\ \mathrm{m/s}\) | \(6.43\times10^3\ \mathrm{m/s^2}\) |

De desplazamiento máximo arriba a máximo abajo:

\[
\Delta t=\frac{T_{per}}2=\frac1{2f}=\boxed{2.08\times10^{-3}\ \mathrm{s}}
\]

No aplica al nodo porque nunca se desplaza.

---

## 15.15 — Cuerda tensada por masa colgante

**Datos:** \(f=120\ \mathrm{Hz}\), \(m=1.50\ \mathrm{kg}\), \(\mu=0.0550\ \mathrm{kg/m}\); después \(m=3.00\ \mathrm{kg}\).

**Dibujo/DCL:** tramo horizontal de cuerda a una polea y masa colgante. Sobre la masa: \(T\) arriba, \(mg\) abajo. En equilibrio, \(T=mg\).

**Patrón reutilizable:** obtené primero tensión mediante DCL, luego \(v=\sqrt{T/\mu}\) y finalmente \(\lambda=v/f\).

**Derivación esencial:**

\[
T=mg=(1.50)(9.80)=14.7\ \mathrm{N}
\]

\[
v=\sqrt{\frac{14.7}{0.0550}}=\boxed{16.3\ \mathrm{m/s}}
\]

\[
\lambda=\frac{16.3}{120}=\boxed{0.136\ \mathrm{m}}
\]

Al duplicar la masa, \(T\) se duplica:

\[
v_{nuevo}=\sqrt2v=\boxed{23.1\ \mathrm{m/s}},\qquad
\lambda_{nueva}=\frac{v_{nuevo}}{120}=\boxed{0.193\ \mathrm{m}}
\]

---

## 15.3 — Tsunami

**Datos:** distancia cresta-cresta \(=800\ \mathrm{km}\), período \(=1.0\ \mathrm{h}\).

**Dibujo:** superficie senoidal del mar, dos crestas consecutivas; flecha entre crestas etiquetada \(\lambda=800\ \mathrm{km}\).

**Patrón reutilizable:** distancia entre crestas es \(\lambda\); tiempo entre llegada de crestas es \(T\). Aplicá \(v=\lambda/T\) antes de convertir unidades.

**Derivación y resultado:**

\[
v=\frac{\lambda}{T}=\frac{800\ \mathrm{km}}{1.0\ \mathrm{h}}
=\boxed{800\ \mathrm{km/h}}
\]

\[
v=800\left(\frac{1000}{3600}\right)=\boxed{222\ \mathrm{m/s}}
\]

**Chequeo físico:** es comparable a la rapidez de un avión comercial; transporta energía sobre una escala oceánica enorme, por eso puede ser devastador al llegar a la costa.
