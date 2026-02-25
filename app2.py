import streamlit as st

# 1. EL ARCHIVADOR DE CAPITALES (9 preguntas)
preguntas = [
    {"texto": "¿Cuál es la capital de Francia?", "opciones": ["Selecciona...", "Marsella", "París", "Lyon"], "correcta": "París"},
    {"texto": "¿Cuál es la capital de Japón?", "opciones": ["Selecciona...", "Kioto", "Osaka", "Tokio"], "correcta": "Tokio"},
    {"texto": "¿Cuál es la capital de Australia?", "opciones": ["Selecciona...", "Sídney", "Canberra", "Melbourne"], "correcta": "Canberra"},
    {"texto": "¿Cuál es la capital de Brasil?", "opciones": ["Selecciona...", "Río de Janeiro", "Brasilia", "San Pablo"], "correcta": "Brasilia"},
    {"texto": "¿Cuál es la capital de Egipto?", "opciones": ["Selecciona...", "El Cairo", "Alejandría", "Giza"], "correcta": "El Cairo"},
    {"texto": "¿Cuál es la capital de Canadá?", "opciones": ["Selecciona...", "Toronto", "Vancouver", "Ottawa"], "correcta": "Ottawa"},
    {"texto": "¿Cuál es la capital de Italia?", "opciones": ["Selecciona...", "Milán", "Roma", "Nápoles"], "correcta": "Roma"},
    {"texto": "¿Cuál es la capital de Corea del Sur?", "opciones": ["Selecciona...", "Seúl", "Busan", "Incheon"], "correcta": "Seúl"},
    {"texto": "¿Cuál es la capital de Portugal?", "opciones": ["Selecciona...", "Oporto", "Lisboa", "Coímbra"], "correcta": "Lisboa"}
]

st.title("🌍 El Gran Test de las Capitales")
st.markdown("""
**Instrucciones:**
* Cada acierto suma puntos.
* Cada fallo **resta 0.5 puntos**.
* Si no sabes la respuesta, déjala en **'Selecciona...'** para no restar.
""")

with st.form("examen_capitales"):
    respuestas_usuario = []
    
    for i, p in enumerate(preguntas):
        st.write(f"### Pregunta {i+1}")
        eleccion = st.selectbox(p["texto"], p["opciones"], key=f"cap_{i}")
        respuestas_usuario.append(eleccion)
        st.write("---")
    
    boton_enviar = st.form_submit_button("Finalizar y Calificar")

# 3. LÓGICA DE CORRECCIÓN Y REDONDEO
if boton_enviar:
    puntos = 0
    total = len(preguntas)
    
    for i in range(total):
        user_ans = respuestas_usuario[i]
        correct_ans = preguntas[i]["correcta"]
        
        if user_ans == correct_ans:
            puntos += 1
        elif user_ans != "Selecciona...":
            puntos -= 0.5 # Penalización por error
            
    # Calculamos la nota sobre 10 (asegurando que no sea menor a 0)
    nota_sin_redondear = (max(0, puntos) / total) * 10
    
    # INVESTIGACIÓN: La función round() toma (número, decimales)
    nota_final = round(nota_sin_redondear, 2)

    st.divider()
    st.header(f"Tu nota: {nota_final} / 10")

    # 4. FEEDBACK PERSONALIZADO CON ANIMACIONES
    if nota_final < 3:
        st.error(f"Nota: {nota_final} - Muy insuficiente. ¡Necesitas un mapa urgente! 🗺️")
    elif 3 <= nota_final < 5:
        st.warning(f"Nota: {nota_final} - Insuficiente. ¡Casi lo logras! ✈️")
    elif 5 <= nota_final < 6:
        st.success(f"Nota: {nota_final} - Suficiente. ¡Aprobado raspado! 🎓")
        st.snow()
    elif 6 <= nota_final < 7:
        st.success(f"Nota: {nota_final} - Bien. ¡Conoces bastante mundo! 🌎")
        st.snow()
    elif 7 <= nota_final < 9:
        st.success(f"Nota: {nota_final} - Notable. ¡Eres un gran viajero! 🧗")
        st.balloons()
    elif 9 <= nota_final < 10:
        st.success(f"Nota: {nota_final} - Sobresaliente. ¡Impresionante! 🚀")
        st.balloons()
    elif nota_final == 10:
        st.success(f"Nota: {nota_final} - ¡EXCELENTE! Eres un experto en geografía. 🏆")
        st.balloons()
