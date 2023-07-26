import streamlit as st

st.title('B.M.I CALCULATOR')
st.write('')
st.write('B.M.I stands for Body Mass Index, which is a measurement of body fat based on height and weight. It is calculated by dividing a person\'s weight in kilograms by the square of their height in meters.'
    'B.M.I is commonly used as an indicator of overall health and is often used by doctors and other health professionals to assess a person\'s risk of certain health conditions such as heart disease, diabetes, and certain cancers.'
    'However, B.M.I has its limitations and may not be an accurate measure of body fat for everyone, particularly for athletes and individuals with a lot of muscle mass. Other factors such as waist circumference, body composition, and overall lifestyle should also be taken into account when evaluating an individual\'s overall health.')

st.write('')
st.header('B.M.I CATEGORIES')
st.write('')
st.write('SEVERELY UNDERWEIGHT - B.M.I less than 16.5kg/m^2')
st.write('UNDERWEIGHT - B.M.I under 18.5 kg/m^2')
st.write('HEALTHY - B.M.I greater than or equal to 18.5 to 24.9 kg/m^2')
st.write('OVERWEIGHT – B.M.I greater than or equal to 25 to 29.9 kg/m^2')
st.write('OBESITY – B.M.I greater than or equal to 30 kg/m^2')
st.write('')

st.header('ENTER THE DETAILS')
st.write('')

name = st.text_input("ENTER NAME:")
st.write('')
gen = st.radio("ENTER GENDER:", ('Male', 'Female'))
if gen == 'Male':
    st.write('')
else:
    st.write('')

age = st.number_input('ENTER AGE:')
st.write('')
add = st.text_input('ENTER ADDRESS:')
st.write('')

st.write('SELECT HOBBIES:')
st.write("For hobbies not in the list below select 'OTHERS' and mention accordingly.")
if st.checkbox('PIANO'):
    st.text('')
if st.checkbox('BASKETBALL'):
    st.text('')
if st.checkbox('COOKING'):
    st.text('')
if st.checkbox('KARATE'):
    st.text('')
if st.checkbox('READING'):
    st.text('')
if st.checkbox('OTHERS'):
    st.text_input('')
st.write('')

weight = st.number_input("ENTER YOUR WEIGHT (KG):", value=10)
st.write('')
height = st.number_input("ENTER YOUR HEIGHT (CMS):", value=10)
st.write('')

if (height <= 0) or (weight <= 0):
    st.error("INVALID INPUT")
else:
    if st.button('CALCULATE B.M.I'):
        bmi = float(weight / (height / 100) ** 2)
        st.text('YOUR B.M.I IS {:.2f}'.format(bmi))
        if bmi < 16.5:
            st.error("YOU ARE SEVERELY UNDERWEIGHT")
        elif bmi < 18.5:
            st.error("YOU ARE UNDERWEIGHT")
        elif (bmi >= 18.5) and (bmi < 24.9):
            st.success("YOU ARE HEALTHY")
        elif (bmi >= 25) and (bmi < 30):
            st.warning("YOU ARE OVERWEIGHT")
        elif bmi >= 30:
            st.error("YOU ARE OBESE")
        else:
            st.error("INVALID INPUT")
