import numpy as np
import joblib
import streamlit as st
import warnings
warnings.filterwarnings('ignore')

load_model = joblib.load(open('model.joblib','rb'))
def health_predict(input_data):
    id_asnumpy = np.asarray(input_data)
    input_reshaped = id_asnumpy.reshape(1,-1)
    predict = load_model.predict(input_reshaped)
    print(predict)
    if predict == 0:
        st.success("Your horse is died")
    elif predict == 1:
        st.success("Your horse is lived")
    else:
        st.success("Your horse is euthanized")

def main():
    st.title('Horse Heatlh Prediction')
    surgery = st.text_input('surgery')
    age = st.text_input('Age')
    rectal_temp = st.text_input('Rectal temperature')
    pulse = st.text_input('Pulse')
    respiratory_rate = st.text_input('respiratory rate')
    temp_of_extremities = st.text_input('temperature of extremities')
    peripheral_pulse = st.text_input('peripheral pulse')
    mucous_membrane = st.text_input('mucous membrane')    
    capillary_refill_time = st.text_input('capillary_refill_time')
    pain = st.text_input('Pain')
    peristalsis = st.text_input('Peristalsis')
    abdominal_distention = st.text_input('abdominal distention')
    nasogastric_tube = st.text_input('nasogastric tube')
    nasogastric_reflux = st.text_input('nasogastric reflux')
    nasogastric_reflux_ph = st.text_input('nasogastric reflux ph')
    rectal_exam_feces = st.text_input('rectal exam feces')
    abdomen = st.text_input('Abdomen')
    packed_cell_volume = st.text_input('packed_cell_volume')
    total_protein = st.text_input('Total protein')
    abdomo_appearance = st.text_input('abdomo appearance')
    abdomo_protein = st.text_input('abdomen protein')
    surgical_lesion = st.text_input('Surgical Lesion')
    lesion_1 = st.text_input('Lesion 1')
    lesion_2 = st.text_input('Lesion 2')
    lesion_3 = st.text_input('Lesion 3')
    cp_data = st.text_input('cp data')

    predicted = ''

    if st.button('Prediction Result'):
        predicted = health_predict([surgery,age,rectal_temp,pulse,respiratory_rate,temp_of_extremities,peripheral_pulse,mucous_membrane,capillary_refill_time,pain,peristalsis,abdominal_distention,nasogastric_tube,nasogastric_reflux,nasogastric_reflux_ph,rectal_exam_feces,abdomen,packed_cell_volume,total_protein,abdomo_appearance,abdomo_protein,surgical_lesion,lesion_1,lesion_2,lesion_3,cp_data])


if __name__ == '__main__':
    main()