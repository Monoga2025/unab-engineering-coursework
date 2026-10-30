# Guía de estudio: movimiento armónico, resortes y oscilaciones

> Alcance: problemas **13.68, 13.69, 13.73, 37, 42 y 63** de `Problemas_examen_1.pdf`.  
> Convención: al resolver un sistema vertical con resorte, el desplazamiento se mide desde el **equilibrio estático**. Así, el peso no aparece en la ecuación de oscilación.

## Hoja de fórmulas

| Situación | Ecuación clave | Recordatorio |
|---|---|---|
| Masa-resorte sin rozamiento | \(\omega_0=\sqrt{k/m}\), \(T=2\pi\sqrt{m/k}\), \(f=1/T\) | \(m\) es la masa que oscila realmente. |
| MAS | \(a=-\omega^2x\), \(a_{\max}=\omega^2A\), \(v_{\max}=\omega A\) | Aceleración máxima en \(x=\pm A\); velocidad máxima en \(x=0\). |
| Fricción estática | \(f_s\leq \mu_sN\) | No siempre vale \(f_s=\mu_sN\); aquí se iguala solo en el límite de no deslizar. |
| Choque perfectamente inelástico | \(m_1v_{1i}+m_2v_{2i}=(m_1+m_2)v_0\) | Durante el choque se conserva el momento, no la energía mecánica. |
| Amortiguado | \(\gamma=b/(2m)\), \(\omega_d=\sqrt{\omega_0^2-\gamma^2}\) | \(A(t)=A_0e^{-\gamma t}\), \(E(t)=E_0e^{-2\gamma t}\). |
| Forzado sin amortiguamiento | \(A=F_0/\lvert k-m\omega^2\rvert\) | Puede haber dos frecuencias con la misma amplitud, una a cada lado de resonancia. |
| Pequeñas oscilaciones | \(\sin\theta\approx\theta\approx y/L\) | Solo es válido si \(y\ll L\). |

## Mapa de decisión

```text
¿Hay una masa unida a un resorte?
├─ Sí, sin pérdida ni rozamiento → usa ω0 = √(k/m) y T = 2π√(m/k).
│  ├─ ¿Hay otro bloque encima? → revisa si fs requerida ≤ μsN.
│  ├─ ¿Hubo choque? → primero determina v0 con momento lineal.
│  └─ ¿La masa cambia lentamente? → reemplaza m por m(t) y deriva T(m).
├─ Sí, aparece b o fuerza −bv → oscilador amortiguado.
├─ Sí, aparece F0 cos(ωt) → oscilador forzado.
└─ No hay resorte, pero hay tensiones y pequeño desplazamiento →
   encuentra Fy; si Fy ≈ −C y, entonces ω = √(C/m).
```

---

## 1. Problema 13.68 — Bloque superior sin deslizar

### Datos

- Bloque inferior: \(M\).
- Bloque superior: \(m\).
- Resorte horizontal: \(k\).
- Coeficiente de fricción estática entre bloques: \(\mu_s\).
- Superficie inferior sin fricción.

### DCL/esquema que debés dibujar

```text
pared ──/\/\/\/── [ M ]
                    [ m ]
```

Para el bloque superior \(m\), dibujá \(mg\) hacia abajo, \(N\) hacia arriba y la fricción estática \(f_s\) horizontal. La dirección de \(f_s\) es la misma que la aceleración instantánea requerida para que \(m\) acompañe a \(M\).

### Principio

Si no hay deslizamiento, ambos bloques se mueven juntos y su masa efectiva es:

\[
m_{\mathrm{ef}}=M+m
\]

Por tanto:

\[
\omega=\sqrt{\frac{k}{M+m}}
\]

La máxima aceleración del MAS ocurre en los extremos \(x=\pm A\):

\[
a_{\max}=\omega^2 A
\]

### Derivación

La única fuerza horizontal sobre el bloque superior es la fricción. Debe suministrar:

\[
f_{\mathrm{requerida}}=m a_{\max}=m\omega^2A
\]

Para no deslizar:

\[
f_{\mathrm{requerida}}\leq f_{s,\max}=\mu_sN=\mu_smg
\]

\[
m\left(\frac{k}{M+m}\right)A\leq\mu_smg
\]

Cancelando \(m\):

\[
A\leq\frac{\mu_sg(M+m)}{k}
\]

### Resultado

\[
\boxed{A_{\max}=\frac{\mu_sg(M+m)}{k}}
\]

### Chequeo conceptual

- Más fricción permite mayor amplitud.
- Un resorte más rígido aumenta la aceleración para la misma amplitud, así que reduce \(A_{\max}\).
- No escribas automáticamente \(f_s=\mu_sN\): eso solo corresponde al caso límite de estar a punto de deslizar.

---

## 2. Problema 13.69 — Choque y oscilación con resorte

### Ambigüedad que hay que declarar

El enunciado visible dice que una masa choca contra otra unida al resorte, pero **no especifica el tipo de choque**. Sin saber qué ocurre después, no hay una respuesta única. La resolución numérica siguiente se obtiene bajo la condición estándar de este problema: **las masas se adhieren** (choque perfectamente inelástico). Si rebotaran o el choque fuera elástico, cambiaría la velocidad inicial de la oscilación.

### Datos

\[
m_1=m_2=10.0\,\mathrm{kg},\qquad v_{1i}=2.00\,\mathrm{m/s},
\qquad v_{2i}=0,\qquad k=80.0\,\mathrm{N/m}
\]

### DCL/esquema que debés dibujar

```text
Antes:  m1 = 10 kg  → 2.00 m/s       [ m2 = 10 kg ]──/\/\/\/──pared

Después:             [ m1 + m2 = 20 kg ]──/\/\/\/──pared
```

Tomá \(x=0\) como la posición del bloque inmediatamente después del choque; el resorte está en su posición de equilibrio horizontal.

### Principio

1. Durante el choque breve se conserva el momento lineal.
2. Tras adherirse, el conjunto de masa \(m_1+m_2\) realiza MAS.

### Derivación

**Choque:**

\[
m_1v_{1i}+m_2v_{2i}=(m_1+m_2)v_0
\]

\[
v_0=\frac{10.0(2.00)}{20.0}=1.00\,\mathrm{m/s}
\]

**MAS posterior:**

\[
\omega=\sqrt{\frac{k}{m_1+m_2}}
=\sqrt{\frac{80.0}{20.0}}
=2.00\,\mathrm{rad/s}
\]

\[
f=\frac{\omega}{2\pi}=0.318\,\mathrm{Hz},
\qquad
T=\frac{2\pi}{\omega}=3.14\,\mathrm{s}
\]

Como \(x(0)=0\) y \(v(0)=v_0\):

\[
x(t)=A\sin(\omega t)
\]

\[
v_{\max}=\omega A=v_0
\]

\[
A=\frac{v_0}{\omega}=\frac{1.00}{2.00}=0.500\,\mathrm{m}
\]

El primer regreso a \(x=0\), después de partir de \(x=0\) avanzando a la derecha, ocurre cuando:

\[
\omega t=\pi
\]

\[
t=\frac{\pi}{\omega}=1.57\,\mathrm{s}
\]

### Resultado

\[
\boxed{f=0.318\,\mathrm{Hz}},\qquad
\boxed{A=0.500\,\mathrm{m}},\qquad
\boxed{T=3.14\,\mathrm{s}}
\]

\[
\boxed{t_{\text{primer regreso a }x=0}=1.57\,\mathrm{s}}
\]

### Chequeo conceptual

El sistema inicia en equilibrio, donde la rapidez es máxima. Tarda medio período \(T/2\), no un cuarto de período, en regresar a esa misma posición.

---

## 3. Problema 13.73 — Cubeta que pierde agua

### Datos

\[
m_{\mathrm{cubeta}}=2.00\,\mathrm{kg},\qquad
m_{\mathrm{agua, inicial}}=10.0\,\mathrm{kg}
\]

\[
k=125\,\mathrm{N/m},\qquad
\frac{dm}{dt}=-2.00\,\mathrm{g/s}=-0.00200\,\mathrm{kg/s}
\]

La amplitud dada, \(3.00\,\mathrm{cm}\), no modifica el período de un resorte ideal lineal.

### DCL/esquema que debés dibujar

```text
techo
  │
 /\/\/\/\   k
  │
[cubeta + agua]
  ↑ Fs
  ↓ mg
```

Medí la oscilación desde el equilibrio instantáneo. Allí el peso solo desplaza el equilibrio, no altera la fórmula del período.

### Principio

\[
T(m)=2\pi\sqrt{\frac{m}{k}}
\]

La masa total que oscila es:

\[
m=m_{\mathrm{cubeta}}+m_{\mathrm{agua}}
\]

### Derivación

**Cuando queda la mitad del agua:**

\[
m=2.00+5.00=7.00\,\mathrm{kg}
\]

\[
T=2\pi\sqrt{\frac{7.00}{125}}
=1.49\,\mathrm{s}
\]

**Cuando queda vacía:**

\[
m=2.00\,\mathrm{kg}
\]

\[
T=2\pi\sqrt{\frac{2.00}{125}}
=0.795\,\mathrm{s}
\]

Para la tasa de cambio, derivá la fórmula del período:

\[
\frac{dT}{dt}
=\frac{d}{dt}\left(2\pi\sqrt{\frac{m}{k}}\right)
=\frac{\pi}{\sqrt{km}}\frac{dm}{dt}
\]

A mitad de capacidad:

\[
\left.\frac{dT}{dt}\right|_{m=7.00}
=\frac{\pi}{\sqrt{125(7.00)}}(-0.00200)
=-2.12\times10^{-4}\,\mathrm{s/s}
\]

Vacía:

\[
\left.\frac{dT}{dt}\right|_{m=2.00}
=\frac{\pi}{\sqrt{125(2.00)}}(-0.00200)
=-3.97\times10^{-4}\,\mathrm{s/s}
\]

### Resultado

\[
\boxed{T_{\text{mitad}}=1.49\,\mathrm{s}}
\]

\[
\boxed{T_{\text{vacía}}=0.795\,\mathrm{s}}
\]

\[
\boxed{T_{\min}=0.795\,\mathrm{s}}
\]

### Chequeo conceptual

Como \(T\propto\sqrt{m}\), al perder agua el período disminuye: el sistema oscila más rápido. El signo negativo de \(dT/dt\) confirma esa conclusión.

---

## 4. Problema 37 — Oscilador amortiguado

### Datos

\[
m=10.6\,\mathrm{kg},\qquad
k=2.05\times10^4\,\mathrm{N/m},\qquad
b=3.00\,\mathrm{N\,s/m}
\]

### DCL/esquema que debés dibujar

```text
techo
  │
 /\/\/\/\  k
  │
  [m]
  ↑ Fs
  ↓ mg
  F_b = −bv  (siempre opuesta a v)
```

### Principio

\[
\gamma=\frac{b}{2m},\qquad
\omega_0=\sqrt{\frac{k}{m}},\qquad
\omega_d=\sqrt{\omega_0^2-\gamma^2}
\]

La amplitud y la energía decaen como:

\[
A(t)=A_0e^{-\gamma t},
\qquad
E(t)=E_0e^{-2\gamma t}=E_0e^{-(b/m)t}
\]

### Derivación

\[
\gamma=\frac{3.00}{2(10.6)}=0.1415\,\mathrm{s^{-1}}
\]

\[
\omega_0=\sqrt{\frac{2.05\times10^4}{10.6}}
=43.9768\,\mathrm{rad/s}
\]

\[
\omega_d=\sqrt{(43.9768)^2-(0.1415)^2}
=43.9766\,\mathrm{rad/s}
\]

\[
f_d=\frac{\omega_d}{2\pi}=6.999\,\mathrm{Hz}\approx7.00\,\mathrm{Hz}
\]

El período amortiguado es:

\[
T_d=\frac{2\pi}{\omega_d}=0.1429\,\mathrm{s}
\]

La razón de amplitudes de ciclos consecutivos es:

\[
\frac{A_{n+1}}{A_n}=e^{-\gamma T_d}=0.97998
\]

Porcentaje de disminución:

\[
(1-0.97998)(100\%)=2.00\%
\]

Para \(E/E_0=0.0500\):

\[
0.0500=e^{-(b/m)t}
\]

\[
t=-\frac{m}{b}\ln(0.0500)=10.6\,\mathrm{s}
\]

### Resultado

\[
\boxed{f_d=7.00\,\mathrm{Hz}}
\]

\[
\boxed{\text{La amplitud disminuye }2.00\%\text{ por ciclo}}
\]

\[
\boxed{t_{E=0.0500E_0}=10.6\,\mathrm{s}}
\]

### Chequeo conceptual

El amortiguamiento es débil: \(\gamma\ll\omega_0\). Por eso \(f_d\) es casi igual a la frecuencia natural, pero la amplitud y la energía sí disminuyen con el tiempo.

---

## 5. Problema 42 — Oscilador forzado sin amortiguamiento

### Datos

\[
m=0.150\,\mathrm{kg},\qquad
k=6.30\,\mathrm{N/m},\qquad
F_0=1.70\,\mathrm{N},\qquad
A=0.440\,\mathrm{m}
\]

### DCL/esquema que debés dibujar

```text
techo
  │
 /\/\/\/\  k
  │
  [m]
  ↑/↓ Fuerza externa: F(t)=F0 cos(ωt)
```

### Principio

Para el estado estacionario sin amortiguamiento:

\[
A=\frac{F_0}{\lvert k-m\omega^2\rvert}
\]

### Derivación

\[
\lvert k-m\omega^2\rvert=\frac{F_0}{A}
=\frac{1.70}{0.440}=3.864\,\mathrm{N/m}
\]

Por el valor absoluto hay dos casos.

**Frecuencia por debajo de resonancia:**

\[
6.30-0.150\omega^2=3.864
\]

\[
\omega_1=4.03\,\mathrm{rad/s}
\]

\[
f_1=\frac{\omega_1}{2\pi}=0.641\,\mathrm{Hz}
\]

**Frecuencia por encima de resonancia:**

\[
6.30-0.150\omega^2=-3.864
\]

\[
\omega_2=8.23\,\mathrm{rad/s}
\]

\[
f_2=\frac{\omega_2}{2\pi}=1.31\,\mathrm{Hz}
\]

### Resultado

\[
\boxed{\omega_1=4.03\,\mathrm{rad/s},\quad f_1=0.641\,\mathrm{Hz}}
\]

\[
\boxed{\omega_2=8.23\,\mathrm{rad/s},\quad f_2=1.31\,\mathrm{Hz}}
\]

### Chequeo conceptual

La frecuencia natural es:

\[
f_0=\frac{1}{2\pi}\sqrt{\frac{k}{m}}=1.03\,\mathrm{Hz}
\]

Las dos respuestas quedan a lados opuestos de \(f_0\). No descartes una: el valor absoluto produce dos frecuencias físicas para la misma amplitud solicitada.

---

## 6. Problema 63 — Bola entre dos bandas de hule

### Datos

- Masa de la bola: \(m\).
- Dos bandas, cada una de longitud horizontal inicial \(L\).
- Cada banda tiene tensión constante \(T\).
- Desplazamiento transversal pequeño \(y\).

### DCL/esquema que debés dibujar

```text
soporte                 soporte
  ●─────── L ───────●─────── L ───────●
                    bola

Después de subir y:
  ●  ↘ T          T ↙  ●
        \          /
         \   ●    /
           y
```

Sobre la bola dibujá las dos tensiones hacia los soportes. Sus componentes horizontales se anulan. Las dos componentes verticales apuntan hacia la posición de equilibrio.

### Principio

La fuerza transversal neta es la suma de las componentes verticales de ambas tensiones:

\[
F_y=-2T\sin\theta
\]

Para una desviación pequeña, \(y\ll L\), se puede linealizar la geometría.

### Derivación

Geométricamente:

\[
\sin\theta=\frac{y}{\sqrt{L^2+y^2}}
\]

Por tanto, la fuerza exacta es:

\[
F_y=-\frac{2Ty}{\sqrt{L^2+y^2}}
\]

Si \(y\ll L\):

\[
\sqrt{L^2+y^2}\approx L
\]

\[
F_y\approx-\frac{2T}{L}y
\]

Aplicando \(\sum F_y=m\ddot y\):

\[
m\ddot y=-\frac{2T}{L}y
\]

\[
\ddot y+\frac{2T}{mL}y=0
\]

Al comparar con \(\ddot y+\omega^2y=0\):

\[
\omega^2=\frac{2T}{mL}
\]

### Resultado

\[
\boxed{F_y\approx-\frac{2T}{L}y}
\]

\[
\boxed{\omega=\sqrt{\frac{2T}{mL}}}
\]

### Chequeo conceptual

El signo negativo confirma que la fuerza es restauradora. La segunda conclusión, MAS, depende de dos hipótesis: \(y\ll L\) y tensión aproximadamente constante. Sin la aproximación de pequeña desviación, la fuerza exacta no es estrictamente proporcional a \(y\), de modo que ya no sería MAS perfecto.

## Repaso final de patrones

1. **Resorte + masa:** antes de poner números, identificá cuál es la masa efectiva.
2. **Bloque sobre bloque:** preguntá qué fuerza acelera al bloque superior; la respuesta es la fricción estática.
3. **Choque + resorte:** resolvé primero el choque y recién después empezá el MAS.
4. **Amortiguamiento:** amplitud decae como \(e^{-\gamma t}\), energía como \(e^{-2\gamma t}\).
5. **Fuerza periódica externa:** conservá el valor absoluto; suelen existir dos frecuencias posibles.
6. **Tensión y pequeño desplazamiento:** proyectá componentes y buscá una fuerza de forma \(-Cy\).
