import streamlit as st
import pandas as pd
import pickle

with open('decision_tree_model.pkl', 'rb') as dt:
    dec_tr = pickle.load(dt)

def classify(num):
    if num == 0:
        return 'Healthy'
    elif num == 1:
        return 'Iron deficiency anemia'
    elif num == 2:
        return 'Leukemia'
    elif num == 3:
        return 'Leukemia with thrombocytopenia'
    elif num == 4:
        return 'Macrocytic anemia'
    elif num == 5:
        return 'Normocytic hypochromic anemia'
    elif num == 6:
        return 'Normocytic normochromic anemia'
    elif num == 7:
        return 'Other microcytic anemia'
    elif num == 8:
        return 'Thrombocytopenia'

def main():
    st.title('Diagnóstico de Anemia by @JeffersonEspinalA')
    st.sidebar.header('Parámetros de entrada del usuario')

    def user_input_parameters():
        WBC = st.sidebar.number_input('WBC - Recuento de glóbulos blancos.', 0.8, 45.7, 7.86)
        RBC = st.sidebar.number_input('RBC - Recuento de glóbulos rojos.', 1.36, 90.8, 4.71)
        HGB = st.sidebar.number_input('HGB - Cantidad de hemoglobina en la sangre.', -10.0, 87.1, 12.18)
        HCT = st.sidebar.number_input('HCT', 2.0, 3715.0, 46.15)
        MCV = st.sidebar.number_input('MCV - Volumen promedio de un solo glóbulo rojo.', -79.3, 990.0, 85.79)
        MCH = st.sidebar.number_input('MCH - Cantidad promedio de hemoglobina por glóbulo rojo.', 10.9, 3117.0, 32.08)
        MCHC = st.sidebar.number_input('MCHC - Concentración media de hemoglobina en los glóbulos rojos.', 11.5, 92.8, 31.74)
        PLT = st.sidebar.number_input('PLT - Cantidad de plaquetas en la sangre.', 10.0, 660.0, 229.98)
        data = {'WBC': WBC,
                'RBC': RBC,
                'HGB': HGB,
                'HCT': HCT,
                'MCV': MCV,
                'MCH': MCH,
                'MCHC': MCHC,
                'PLT': PLT,
                }
        features = pd.DataFrame(data, index=[0])
        return features

    df = user_input_parameters()

    st.subheader('Parámetros ingresados por el usuario')

    columns = list(df.columns)
    data = [columns[i:i+2] for i in range(0, len(columns), 2)]

    formatted_rows = [
        f"<tr><td>{pair[0]}: {df[pair[0]][0]:.2f}</td><td>{pair[1]}: {df[pair[1]][0]:.2f}</td></tr>"
        if len(pair) > 1 else
        f"<tr><td>{pair[0]}: {df[pair[0]][0]:.2f}</td><td></td></tr>"
        for pair in data
    ]

    html_table = f"""
    <table style="width:100%; border-collapse:collapse; text-align:left;">
        <tbody>
            {''.join(formatted_rows)}
        </tbody>
    </table>
    """

    st.markdown(html_table, unsafe_allow_html=True)

    if st.button('RUN'):

        st.success(classify(dec_tr.predict(df)))

if __name__ == '__main__':
    main()
