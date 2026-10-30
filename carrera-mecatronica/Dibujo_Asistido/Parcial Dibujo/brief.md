# 📘 ESPECIFICACIÓN TÉCNICA Y PEDAGÓGICA: MÓDULO DE ESTUDIO INTELIGENTE (UNAB OS & JARVIS)

> **Autor / Usuario:** Monoga  
> **Ecosistema:** Monoga OS / UNAB Ingeniería Mecatrónica / Integración Jarvis  
> **Versión del Documento:** 2.0 (Consolidado Final con Feedback de UX & Machine Learning)  
> **Objetivo:** Definir la arquitectura, el diseño interactivo, el motor adaptativo de Machine Learning y la metodología pedagógica para el nuevo **Módulo de Estudio Inteligente** de la plataforma UNAB.

---

## 1. 🎯 Filosofía Pedagógica Central (El Método Práctico)

> *"No se trata de perder horas memorizando teoría abstracta densa, sino de aprender a resolver el parcial mediante un método algorítmico, visual y metódico paso a paso para reemplazar datos y sacar 5.0."*

### Pilares del Aprendizaje Rápido:
1. **Reconocimiento Inmediato de Patrones:** El estudiante mira el enunciado del examen, detecta las palabras clave ("pista de oro") y sabe inmediatamente qué fórmula mandar.
2. **Cero Texto de Relleno:** Reemplazar párrafos largos por esquemas visuales, simuladores interactivos 2D con sliders en tiempo real y tarjetas gamificadas.
3. **Aprendizaje Basado en el Solucionario Paso a Paso:** El estudiante aprende viendo exactamente qué se hace, por qué se usa cada fórmula y cómo se llega al resultado con unidades SI explícitas.

---

## 2. 🏛️ Arquitectura de los 3 Módulos Desarrollados

```text
┌─────────────────────────────────────────────────────────────────────────────────┐
│                      MÓDULO DE ESTUDIO INTELIGENTE (UNAB OS)                    │
├─────────────────────────┬───────────────────────────────┬───────────────────────┤
│   1. CUADERNO MAESTRO   │   2. LABORATORIO 2D EN VIVO   │ 3. ENTRENADOR IA      │
│     (index.html)        │ (laboratorio_interactivo.html)│(entrenador_duolingo)  │
├─────────────────────────┼───────────────────────────────┼───────────────────────┤
│ • 30 Ejercicios 1 a 1   │ • 60 FPS Canvas Interactivo   │ • Selección 1-Tap     │
│ • Recortes escaneados   │ • Fasor Giratorio ω en vivo   │ • Spaced Repetition   │
│ • Justificación fórmulas│ • Partícula Transversal verde │ • Diagnóstico de Error│
│ • Tips de Parcial       │ • Resistencia térmica (P=I²R) │ • Cero puntos gratis  │
└─────────────────────────┴───────────────────────────────┴───────────────────────┘
```

---

## 3. 🎮 Especificación del Entrenador IA (Diseño Gamificado Tipo Duolingo)

Basado en la retroalimentación directa y las pruebas de usabilidad, el entrenador debe implementar las siguientes reglas estrictas:

### 3.1. Evaluación Instantánea con 1 Solo Toque (One-Tap Feedback)
* **Regla:** Queda prohibido el flujo tradicional de dos pasos (*"Seleccionar -> Botón Comprobar"*).
* **Comportamiento:** Al hacer clic o tocar una de las 3 opciones de fórmula:
  1. Suena el sintetizador acústico en tiempo real (Web Audio API: tono armónico alegre si acierta, tono grave si falla).
  2. La tarjeta seleccionada cambia instantáneamente a verde brillante o rojo translúcido.
  3. Se desliza hacia arriba el cajón inferior de retroalimentación inteligente (*Feedback Drawer*).

### 3.2. Repetición Espaciada Inteligente (True Spaced Repetition)
* **El Problema Detectado:** Si una pregunta fallada se reinserta de inmediato a los 2 turnos, el estudiante no aprende; simplemente recuerda por memoria visual cuál fue la que marcó mal.
* **La Solución Implementada:**
  * Toda pregunta fallada se reagenda **al final de la sesión o aleatoriamente en la segunda mitad de la cola** (con al menos 4 o más preguntas de distancia).
  * Cada vez que la pregunta reaparece, **sus 3 opciones se rebarajan aleatoriamente en un orden distinto**, obligando al estudiante a leer y deducir la fórmula por lógica física.

### 3.3. Puntuación Estricta y Cero Puntos Regalados
* **Acierto a la Primera:** $+15\text{ XP}$, incrementa el contador de Racha ($\text{Streak} + 1$), lanza lluvia de confeti y sube el peso de dominio en la red neuronal.
* **Respuesta Incorrecta:** $0\text{ XP}$, la racha se reinicia inmediatamente a $0$ y se descuenta $1$ vida ($\heartsuit$).
* **Pregunta Recuperada (Spaced Review):** Si el estudiante acierta una pregunta que había fallado previamente, solo recibe $+5\text{ XP}$ de recuperación (sin bonificación de racha), premiando la maestría real a la primera.

### 3.4. Lenguaje Humano y Cero Tecnicismos Densos
El cajón de diagnóstico siempre desglosa 3 secciones claras:
* 🔍 **Pista Clave del Enunciado:** Resalta las palabras del problema que dictan la fórmula (ej: *"segundo sobretono"*, *"masa colgando en reposo"*, *"nodo compartido"*).
* 💡 **Explicación Sencilla:** Analogía o lógica directa de por qué esa fórmula es la correcta.
* ❌ **Por qué la otra fórmula era una trampa:** Explica con precisión el error conceptual común del estudiante (ej: *"Confundiste la fórmula de resortes con la de cuerdas de guitarra"*).

---

## 4. 🌊 Especificación del Laboratorio Visual 2D (Simulador Dinámico)

Para evitar la confusión conceptual entre frecuencia ($f$), velocidad de onda ($v$), longitud ($\lambda$) y frecuencia angular ($\omega$), el simulador 2D incorpora:

1. **Fasor / Círculo Generador de $\omega$ a la Izquierda:**
   * Un disco giratorio morado rota a velocidad angular constante $\omega = 2\pi f\text{ rad/s}$.
   * Una línea horizontal proyecta el movimiento circular directamente hacia la cuerda, demostrando de forma 100% visual *por qué* la onda resultante es senoidal y *qué* significa $\omega t$.
2. **Tracker de Partícula Transversal (Punto Verde):**
   * Muestra visualmente que la materia **no viaja horizontalmente**; solo vibra de arriba a abajo con vector de velocidad $v_y = \omega A$.
   * Se contrasta con la flecha azul de propagación horizontal $v = \sqrt{T/\mu}$.
3. **Módulo de Ondas Estacionarias y Armónicos ($n=1, 2, 3...$):**
   * Destaca los **Nodos (N)** fijos y los vientres oscilantes con ajuste de $\lambda_n = 2L/n$.
4. **Módulo M.A.S. (Masa-Resorte):**
   * Bloque arrastrable con el mouse y barras dinámicas de energía que intercambian $E_k \leftrightarrow E_p$ en tiempo real manteniendo $E_{tot}$ constante.
5. **Módulo de Circuitos & Mallas:**
   * Visualización esquemática con flujo de electrones amarillos en vivo y **resplandor térmico** en los resistores proporcional a la potencia disipada $P = I^2 R$.

---

## 5. 📐 Protocolo Metódico para Cálculo & Ecuaciones Diferenciales (Ejemplo EDO Bernoulli)

Para temas de cálculo avanzado como las **Ecuaciones Diferenciales de Bernoulli**, la plataforma debe aplicar la siguiente receta algorítmica de 5 pasos:

```text
Forma Estándar de Bernoulli:   y' + p(x)·y = g(x)·yᵃ
```

### Receta Algorítmica Paso a Paso:
```text
PASO 1: Extraer los 4 Ingredientes
        p(x) = ...  |  g(x) = ...  |  a = ...  |  (1 - a) = ...

PASO 2: Armar la Ecuación Auxiliar en u (Lineal Estándar)
        u' + (1 - a)·p(x)·u = (1 - a)·g(x)
        (Queda en la forma estándar: u' + P(x)·u = Q(x))

PASO 3: Calcular el Factor Integrante F(x)
        F(x) = e^[ ∫ P(x) dx ]

PASO 4: Resolver u(x) con la Fórmula Maestra
        u(x) = (1 / F(x)) · [ ∫ F(x)·Q(x) dx + C ]

PASO 5: Devolver el Cambio de Variable
        y(x) = [ u(x) ]^( 1 / (1 - a) )
```

### Caso Real del Tablero de Clase:
$$y' + y = -\frac{x}{y} \implies y' + (1)y = (-x)y^{-1}$$
* **Ingredientes:** $p(x)=1$, $g(x)=-x$, $a=-1 \implies (1-a) = 2$.
* **Ecuación en $u$:** $u' + 2u = -2x$.
* **Factor Integrante:** $F(x) = e^{\int 2dx} = e^{2x}$.
* **Solución $u(x)$:** $u(x) = \frac{1}{e^{2x}}\left[\int -2x e^{2x}dx + C\right] = -x + \frac{1}{2} + C e^{-2x}$.
* **Resultado Final en $y$:** $\mathbf{y(x) = \pm\sqrt{-x + \frac{1}{2} + C e^{-2x}}}$.

---

## 6. 🤖 Integración con Jarvis (Bot de Telegram & Monoga OS)

```text
┌─────────────────────────────────────────────────────────────────────────────────┐
│                           ARQUITECTURA DE INTEGRACIÓN JARVIS                    │
├─────────────────────────────────────────────────────────────────────────────────┤
│ 1. Canal Telegram (Móvil):                                                      │
│    Estudiante envía foto del tablero o pide "¿Cómo resuelvo Bernoulli?".        │
│                                                                                 │
│ 2. Backend de Jarvis (Monoga OS / UNAB Platform):                               │
│    • Parsea el tema con el reconocedor de patrones.                             │
│    • Aplica la "Receta de Cocina" de 5 pasos.                                   │
│    • Despacha un mini-test interactivo estilo Duolingo con 3 fórmulas.          │
│                                                                                 │
│ 3. Sincronización Local:                                                        │
│    • Guarda el perfil de aciertos/errores en el almacén de aprendizaje local.   │
│    • Utiliza las suscripciones locales (Antigravity / Codex) sin costos de API. │
└─────────────────────────────────────────────────────────────────────────────────┘
```

---

## 7. 🚀 Entregables y Archivos Listos en el Espacio Local

| Archivo | Descripción y Función |
|---|---|
| [`index.html`](file:///C:/Users/Monoga/Desktop/Monoga%20OS/04_UNAB_INGENIERIA/Carrera_Mecatronica/index.html) | Cuaderno de apuntes maestro interactivo con los 30 ejercicios desarrollados al 100%. |
| [`laboratorio_interactivo.html`](file:///C:/Users/Monoga/Desktop/Monoga%20OS/04_UNAB_INGENIERIA/Carrera_Mecatronica/laboratorio_interactivo.html) | Simulador 2D en tiempo real con fasor $\omega$, sliders y explicador dinámico. |
| [`entrenador_ia_duolingo.html`](file:///C:/Users/Monoga/Desktop/Monoga%20OS/04_UNAB_INGENIERIA/Carrera_Mecatronica/entrenador_ia_duolingo.html) | Entrenador gamificado adaptativo con evaluación a 1 toque y Spaced Repetition al final. |
| [`brief.md`](file:///C:/Users/Monoga/Desktop/Monoga%20OS/04_UNAB_INGENIERIA/Carrera_Mecatronica/brief.md) | Este documento de especificación técnica y pedagógica para integración. |

---
*Fin del Brief de Especificación.*
