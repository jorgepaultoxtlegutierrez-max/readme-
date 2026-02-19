import streamlit as st

# ==================================
# 1️⃣ BASE DE DATOS - 9 PREGUNTAS
# ==================================

preguntas = [
    {"texto": "¿Cuál es la capital de Italia?",
     "opciones": ["Roma", "Milán", "Venecia", "Florencia"],
     "correcta": "Roma"},

    {"texto": "¿Quién descubrió América en 1492?",
     "opciones": ["Cristóbal Colón", "Magallanes", "Napoleón", "Julio César"],
     "correcta": "Cristóbal Colón"},

    {"texto": "¿Cuál es el océano más grande del mundo?",
     "opciones": ["Atlántico", "Índico", "Pacífico", "Ártico"],
     "correcta": "Pacífico"},

    {"texto": "¿Cuántos continentes hay?",
     "opciones": ["5", "6", "7", "8"],
     "correcta": "7"},

    {"texto": "¿Qué planeta es conocido como el planeta rojo?",
     "opciones": ["Marte", "Venus", "Saturno", "Mercurio"],
     "correcta": "Marte"},

    {"texto": "¿Quién escribió 'Romeo y Julieta'?",
     "opciones": ["Shakespeare", "Cervantes", "Lorca", "Dante"],
     "correcta": "Shakespeare"},

    {"texto": "¿Cuál es el río más largo del mundo?",
     "opciones": ["Amazonas", "Nilo", "Danubio", "Misisipi"],
     "correcta": "Nilo"},

    {"texto": "¿Qué gas es necesario para la respiración humana?",
     "opciones": ["Oxígeno", "Hidrógeno", "Helio", "Nitrógeno"],
     "correcta": "Oxígeno"},

    {"texto": "¿En qué año llegó el hombre a la Luna?",
     "opciones": ["1965", "1969", "1972", "1959"],
     "correcta": "1969"}
]

# ==================================
# 2️⃣ INTERFAZ
# ==================================

st.title("📚 Examen de Cultura General")
st.write("✔ Cada acierto suma 1 punto")
st.write("❌ Cada error resta 0.5 puntos")
st.write("➖ En blanco no suma ni resta")

with st.form("quiz_form"):

    respuestas_usuario = []

    for pregunta in preguntas:
        st.subheader(pregunta["texto"])
        eleccion = st.radio(
            "Elige una opción:",
            [""] + pregunta["opciones"],
            key=pregunta["texto"]
        )
        respuestas_usuario.append(eleccion)
        st.write("---")

    boton_enviar = st.form_submit_button("Entregar examen")

# ==================================
# 3️⃣ CORRECCIÓN
# ==================================

if boton_enviar:

    puntuacion = 0
    total_preguntas = len(preguntas)
    informe = ""

    for i in range(total_preguntas):

        if respuestas_usuario[i] == "":
            informe += f"❔ **Pregunta {i+1}**: No contestada\n\n"

        elif respuestas_usuario[i] == preguntas[i]["correcta"]:
            puntuacion += 1
            informe += f"✅ **Pregunta {i+1}**: Correcta\n\n"

        else:
            puntuacion -= 0.5
            informe += f"❌ **Pregunta {i+1}**: Incorrecta\n\n"

    # Nota sobre 10
    nota = (puntuacion / total_preguntas) * 10

    if nota < 0:
        nota = 0

    # 🔵 REDONDEAR SIN DECIMALES
    nota = round(nota)

    st.divider()
    st.header(f"📊 Nota final: {nota} / 10")

    # ==================================
    # 4️⃣ FEEDBACK
    # ==================================

    if nota < 2:
        st.error("Muy insuficiente 😟 Debes repasar todo el contenido.")

    elif 2 <= nota < 5:
        st.warning("Insuficiente 😕 Necesitas practicar más.")

    elif 5 <= nota < 6:
        st.info("Suficiente 🙂 Has aprobado por poco.")
        st.balloons()

    elif 6 <= nota < 7:
        st.success("Bien 👍 Buen trabajo.")
        st.balloons()

    elif 7 <= nota < 9:
        st.success("Notable 🌟 ¡Muy buen resultado!")
        st.balloons()

    elif 9 <= nota < 10:
        st.success("Sobresaliente 🎉 ¡Excelente trabajo!")
        st.balloons()

    elif nota == 10:
        st.success("🏆 EXCELENTE 🏆 ¡Perfecto!")
        st.balloons()

    # ==================================
    # 5️⃣ TAB INFORME
    # ==================================

    tab1, tab2 = st.tabs(["📊 Resultado", "📝 Informe detallado"])

    with tab2:
        st.markdown("## Informe del examen")
        st.markdown(informe)
