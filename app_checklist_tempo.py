
import streamlit as st
import datetime

st.set_page_config(page_title="Checklist - Gestão do Tempo", layout="centered")

st.title("✅ Checklist - Gestão do Tempo")

st.markdown("Preencha seus dados e marque os problemas que você enfrenta no seu dia a dia relacionados à administração do tempo.")

with st.form("form_tempo"):
    nome = st.text_input("Nome completo")
    telefone = st.text_input("Telefone / WhatsApp")
    data = st.date_input("Data", value=datetime.date.today())

    st.markdown("### Marque suas dificuldades e escreva uma justificativa (opcional):")
    problemas = {
        "Procrastinação": "",
        "Falta de foco": "",
        "Dificuldade para planejar o dia": "",
        "Excesso de tarefas e sobrecarga": "",
        "Distrações frequentes (redes sociais, celular...)": "",
        "Não saber por onde começar": "",
        "Não saber dizer 'não' para tarefas desnecessárias": "",
        "Dificuldade em estabelecer prioridades": "",
        "Dificuldade em manter uma rotina": "",
        "Sensação de que o dia 'voa' e nada é concluído": "",
    }

    respostas = {}
    for problema in problemas:
        marcado = st.checkbox(problema)
        justificativa = ""
        if marcado:
            justificativa = st.text_area(f"Justifique (opcional) - {problema}", key=problema)
        respostas[problema] = {"marcado": marcado, "justificativa": justificativa}

    enviar = st.form_submit_button("Enviar")

if enviar:
    st.success("✅ Respostas enviadas com sucesso! Obrigado pela sua participação.")
