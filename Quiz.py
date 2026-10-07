import streamlit as st

st.header("How much do you know about glaciers?")
# These questions are taken from the 2025 USC Dynamic Glaciers Science Olympiad invitational,
# they are public domain and I have included them because I personally took this test my junior year of highschool

q1 = st.selectbox("What is the primary factor influencing the formation of glaciers?",("Select an answer", "Ocean temperature", "Annual snowfall exceeding melting","Volcanic activity", "Wind patterns"))
st.write("You selected: ", q1)

q2 = st.selectbox("What property gives glacial ice it's ability to flow?",("Select an answer", "Density", "Hardness", "Crystal structure", "Equilibrium point"))
st.write("You selected: ", q2)

q3 = st.multiselect("Ogives are not associated with which glacier features?",("Moraines", "Icefalls", "Subglacial drainage", "Striations"))
st.write("You selected: ", q3)

q4 = st.selectbox("What is a depositional feature formed by glaciers?",("Select an answer", "Horn", "Moraine", "Arete", "Cirque"))
st.write("You selected: ", q4)

q5 = st.number_input(
    "Which ice age is associated with the Laurentide Ice Sheet?",
    min_value=0,
    max_value=5,
    value=0,
    step=1
)
st.write("You selected: ", q5)
st.write("Hint: it's one of the five major ice ages, and it's not the oldest")

q6 = st.selectbox("What is an arete?",("Select an answer", "A type of moraine","A sharp ridge formed between glacial valleys","A depositional feature made of till","A lake formed by glacial melting"))
st.write("You selected: ", q6)


# Count how many questions have been answered
answered = 0

if q1 != "Select an answer":
    answered += 1
if q2 != "Select an answer":
    answered += 1
if len(q3) > 0:
    answered += 1
if q4 != "Select an answer":
    answered += 1
if q5 != 0:
    answered += 1
if q6 != "Select an answer":
    answered += 1


# Count how many questions are correct
correct = 0

if q1 == "Annual snowfall exceeding melting":
    correct += 1
if q2 == "Crystal structure":
    correct += 1
if "Moraines" in q3 and "Subglacial drainage" in q3 and "Striations" in q3 and len(q3) == 3:
    correct += 1
if q4 == "Moraine":
    correct += 1
if q5 == 5:
    correct += 1
if q6 == "A sharp ridge formed between glacial valleys":
    correct += 1


# Progress bar
progress = answered / 6
st.progress(progress)

st.write(f"Progress: {answered}/6")


# Final score
if answered == 6:
    st.write(f"You got {correct}/6 questions correct!")
    if correct > 3:
        st.write("You know your glaciers!")
    else:
        st.write("You don't know your glaciers :(")
