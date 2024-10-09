import streamlit as st
import pandas as pd
import joblib


Age = 0
Gender = 0
Smoking = 0
Hx_Smoking = 0
Hx_Radiotherapy = 0
Thyroid_Function_Clinical_Hyperthyroidism = 0
Thyroid_Function_Clinical_Hypothyroidism = 0
Thyroid_Function_Euthyroid = 0
Thyroid_Function_Subclinical_Hyperthyroidism = 0
Thyroid_Function_Subclinical_Hypothyroidism = 0
Physical_Examination_Diffuse_goiter = 0
Physical_Examination_Multinodular_goiter = 0
Physical_Examination_Normal = 0
Physical_Examination_Single_nodular_goiter_left = 0
Physical_Examination_Single_nodular_goiter_right = 0
Adenopathy_Bilateral = 0
Adenopathy_Extensive = 0
Adenopathy_Left = 0
Adenopathy_No = 0
Adenopathy_Posterior = 0
Adenopathy_Right = 0
Pathology_Follicular = 0
Pathology_Hurthel_cell = 0
Pathology_Micropapillary = 0
Pathology_Papillary = 0
Focality_Multi_Focal = 0
Focality_Uni_Focal = 0
Risk_High = 0
Risk_Intermediate = 0
Risk_Low = 0
T_T1a = 0
T_T1b = 0
T_T2 = 0
T_T3a = 0
T_T3b = 0
T_T4a = 0
T_T4b = 0
N_N0 = 0
N_N1a = 0
N_N1b = 0
M_M0 = 0
M_M1 = 0
Stage_I = 0
Stage_II = 0
Stage_III = 0
Stage_IVA = 0
Stage_IVB = 0
Response_Biochemical_Incomplete = 0
Response_Excellent = 0
Response_Indeterminate = 0
Response_Structural_Incomplete = 0

st.markdown("<h1 style='text-align: center; font-size: 30px;'>การทำนายความเสี่ยงการกลับมาเป็นซ้ำ </h1>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center; font-size: 30px;'>ของมะเร็งต่อมไทรอยด์</h1>", unsafe_allow_html=True)


model_Option = ['Please select','MLP']
Hx_Radiotherapy_Option = ['Please select','Yes','No']
Hx_Smoking_Option = ['Please select','Yes','No']
Smoking_Option = ['Please select','Yes','No']
Gender_Option = ['Please select','Male','Female']

Thyroid_Function = ['Please select','Clinical_Hyperthyroidism', 'Clinical_Hypothyroidism', 'Euthyroid','Subclinical_Hyperthyroidism','Subclinical_Hypothyroidism']
Physical_Examination = ['Please select','Diffuse_goiter', 'Multinodular_goiter', 'Normal','Single_nodular_goiter_left','Single_nodular_goiter_right']
Adenopathy = ['Please select','Bilateral', 'Extensive', 'Left','No','Posterior','Right']
Pathology = ['Please select','Follicular', 'Hurthel_cell', 'Micropapillary','Papillary']
Focality = ['Please select','Multi_Focal', 'Uni_Focal']

Risk = ['Please select','High', 'Intermediate', 'Low']
T = ['Please select','T1a', 'T1b', 'T2','T3a','T3b','T4a','T4b']
N = ['Please select','N0', 'N1a', 'N1b']
M = ['Please select','M0', 'M1']
Stage = ['Please select','I', 'II','III','IVA','IVB']
Response = ['Please select','Biochemical_Incomplete', 'Excellent', 'Indeterminate','Structural_Incomplete']



#Age
Age = st.number_input("Age:", min_value=0, max_value=80, value=0)

#Gender
selected_gender = st.selectbox("Gender:", Gender_Option)

if selected_gender == 'Male':
    Gender = 1
elif selected_gender == 'Female':
    Gender = 0
else:
    Gender = 0  

#Smoking
selected_smoking = st.selectbox("smoke" ,Smoking_Option)

if selected_smoking == 'Yes':
    Smoking = 1
elif selected_smoking == 'No':
    Smoking = 0
else:
    Smoking = 0

#Hx_Smoking
selected_Hx_Smoking = st.selectbox("History of smoking" ,Hx_Smoking_Option)

if selected_Hx_Smoking == 'Yes':
    Hx_Smoking = 1
elif selected_Hx_Smoking == 'No':
    Hx_Smoking = 0
else:
    
    Hx_Smoking = 0

#Hx_Radiotherapy
selected_Hx_Radiotherapy = st.selectbox("Have you had radiotherapy?:" ,Hx_Radiotherapy_Option)
if selected_Hx_Radiotherapy == 'Yes':
    Hx_Radiotherapy = 1
elif selected_Hx_Radiotherapy == 'No':
    Hx_Radiotherapy = 0
else:
    
    Hx_Radiotherapy = 0

#Thyroid_Function
selected_Thyroid_Function = st.selectbox("thyroid function" ,Thyroid_Function)

if selected_Thyroid_Function == 'Clinical_Hyperthyroidism':
    Thyroid_Function_Clinical_Hyperthyroidism = 1
    
elif selected_Thyroid_Function == 'Clinical_Hypothyroidism':
    Thyroid_Function_Clinical_Hypothyroidism = 1
    
elif selected_Thyroid_Function == 'Euthyroid':
    Thyroid_Function_Euthyroid = 1
    
elif selected_Thyroid_Function == 'Subclinical_Hyperthyroidism':
    Thyroid_Function_Subclinical_Hyperthyroidism = 1
    
elif selected_Thyroid_Function == 'Subclinical_Hypothyroidism':
    Thyroid_Function_Subclinical_Hypothyroidism = 1
    
else:
    st.write("Error Thyroid_Function")

#Physical_Examination
selected_physical_Examination = st.selectbox("Physical_Examination" ,Physical_Examination)

if selected_physical_Examination == 'Diffuse_goiter':
    Physical_Examination_Diffuse_goiter = 1
    
elif selected_physical_Examination == 'Multinodular_goiter':
    Physical_Examination_Multinodular_goiter = 1
    
elif selected_physical_Examination == 'Normal':
    Physical_Examination_Normal = 1
    
elif selected_physical_Examination == 'Single_nodular_goiter_left':
    Physical_Examination_Single_nodular_goiter_left = 1
    
elif selected_physical_Examination == 'Single_nodular_goiter_right':
    Physical_Examination_Single_nodular_goiter_right = 1
    
else:
    st.write("Error Physical_Examination")

#Adenopathy
selected_Adenopathy = st.selectbox("Adenopathy :" ,Adenopathy)

if selected_Adenopathy == 'Bilateral':
    Adenopathy_Bilateral = 1
    
elif selected_Adenopathy == 'Extensive':
    Adenopathy_Extensive = 1
    
elif selected_Adenopathy == 'Left':
    Adenopathy_Left = 1
    
elif selected_Adenopathy == 'No':
    Adenopathy_No = 1
    
elif selected_Adenopathy == 'Posterior':
    Adenopathy_Posterior = 1
    
elif selected_Adenopathy == 'Right':
    Adenopathy_Right = 1
    
else:
    st.write("Error Adenopathy")

#Pathology
selected_Pathology = st.selectbox("Pathology" ,Pathology)

if selected_Pathology == 'Follicular':
    Pathology_Follicular = 1
    
elif selected_Pathology == 'Hurthel_cell':
    Pathology_Hurthel_cell = 1
    
elif selected_Pathology == 'Micropapillary':
    Pathology_Micropapillary = 1
    
elif selected_Pathology == 'Papillary':
    Pathology_Papillary = 1
    
else:
    st.write("Error Pathology")

#Focality
selected_Focality = st.selectbox("Focality" ,Focality)
if selected_Focality == 'Multi_Focal':
    Focality_Multi_Focal = 1
    
elif selected_Focality == 'Uni_Focal':
    Focality_Uni_Focal = 1
    
else:
    st.write("Error Focality")

#Risk
selected_Risk = st.selectbox("Risk" ,Risk)
if selected_Risk == 'High':
    Risk_High = 1
    
elif selected_Risk == 'Intermediate':
    Risk_Intermediate = 1
    
elif selected_Risk == 'Low':
    Risk_Low = 1
    
else:
    st.write("Error Risk")


#T
selected_T = st.selectbox("Enter T" ,T)
if selected_T == 'T1a':
    T_T1a = 1
    
elif selected_T == 'T1b':
    T_T1b = 1
    
elif selected_T == 'T2':
    T_T2 = 1
    
elif selected_T == 'T3a':
    T_T3a = 1
    
elif selected_T == 'T3b':
    T_T3b = 1
    
elif selected_T == 'T4a':
    T_T4a = 1
    
elif selected_T == 'T4b':
    T_T4b = 1
    
else:
    st.write("Error T")

#N
selected_N = st.selectbox("Enter N" ,N)

if selected_N == 'N0':
    N_N0 = 1
    
elif selected_N == 'N1a':
    N_N1a = 1
    
elif selected_N == 'N1b':
    N_N1b = 1
    
else:
    st.write("Error N")

#M
selected_M = st.selectbox("Enter M" ,M)

if selected_M == 'M0':
    M_M0 = 1
    
elif selected_M == 'M1':
    M_M1 = 1
    
else:
    st.write("Error M")

#Stage
selected_Stage = st.selectbox("Stage" ,Stage)
if selected_Stage == 'I':
    Stage_I = 1
    
elif selected_Stage == 'II':
    Stage_II = 1
    
elif selected_Stage == 'III':
    Stage_III = 1
    
elif selected_Stage == 'IVA':
    Stage_IVA = 1
    
elif selected_Stage == 'IVB':
    Stage_IVB = 1
    
else:
    st.write("Error Stage")

#Response
selected_Response = st.selectbox("Response" ,Response)

if selected_Response == 'Biochemical_Incomplete':
    Response_Biochemical_Incomplete = 1
    
elif selected_Response == 'Excellent':
    Response_Excellent = 1
    
elif selected_Response == 'Indeterminate':
    Response_Indeterminate = 1
    
elif selected_Response == 'Structural_Incomplete':
    Response_Structural_Incomplete = 1
    
else:
    st.write("Error Response")



#model
selected_model = st.selectbox("Model selected:", model_Option)

if selected_model == 'MLP':
    best_model = joblib.load('best_model_MLP.pkl')   
else:
    st.write("Error: Please select a valid model")
    st.stop()  # หยุดการประมวลผลตรงนี้

# สร้าง DataFrame จากค่าตัวแปร
data = {
    'Age': [Age],
    'Gender': [Gender],
    'Smoking': [Smoking],
    'Hx Smoking': [Hx_Smoking],
    'Hx Radiothreapy': [Hx_Radiotherapy],
    'Thyroid Function_Clinical Hyperthyroidism': [Thyroid_Function_Clinical_Hyperthyroidism],
    'Thyroid Function_Clinical Hypothyroidism': [Thyroid_Function_Clinical_Hypothyroidism],
    'Thyroid Function_Euthyroid': [Thyroid_Function_Euthyroid],
    'Thyroid Function_Subclinical Hyperthyroidism': [Thyroid_Function_Subclinical_Hyperthyroidism],
    'Thyroid Function_Subclinical Hypothyroidism': [Thyroid_Function_Subclinical_Hypothyroidism],
    'Physical Examination_Diffuse goiter': [Physical_Examination_Diffuse_goiter],
    'Physical Examination_Multinodular goiter': [Physical_Examination_Multinodular_goiter],
    'Physical Examination_Normal': [Physical_Examination_Normal],
    'Physical Examination_Single nodular goiter-left': [Physical_Examination_Single_nodular_goiter_left],
    'Physical Examination_Single nodular goiter-right': [Physical_Examination_Single_nodular_goiter_right],
    'Adenopathy_Bilateral': [Adenopathy_Bilateral],
    'Adenopathy_Extensive': [Adenopathy_Extensive],
    'Adenopathy_Left': [Adenopathy_Left],
    'Adenopathy_No': [Adenopathy_No],
    'Adenopathy_Posterior': [Adenopathy_Posterior],
    'Adenopathy_Right': [Adenopathy_Right],
    'Pathology_Follicular': [Pathology_Follicular],
    'Pathology_Hurthel cell': [Pathology_Hurthel_cell],
    'Pathology_Micropapillary': [Pathology_Micropapillary],
    'Pathology_Papillary': [Pathology_Papillary],
    'Focality_Multi-Focal': [Focality_Multi_Focal],
    'Focality_Uni-Focal': [Focality_Uni_Focal],
    'Risk_High': [Risk_High],
    'Risk_Intermediate': [Risk_Intermediate],
    'Risk_Low': [Risk_Low],
    'T_T1a': [T_T1a],
    'T_T1b': [T_T1b],
    'T_T2': [T_T2],
    'T_T3a': [T_T3a],
    'T_T3b': [T_T3b],
    'T_T4a': [T_T4a],
    'T_T4b': [T_T4b],
    'N_N0': [N_N0],
    'N_N1a': [N_N1a],
    'N_N1b': [N_N1b],
    'M_M0': [M_M0],
    'M_M1': [M_M1],
    'Stage_I': [Stage_I],
    'Stage_II': [Stage_II],
    'Stage_III': [Stage_III],
    'Stage_IVA': [Stage_IVA],
    'Stage_IVB': [Stage_IVB],
    'Response_Biochemical Incomplete': [Response_Biochemical_Incomplete],
    'Response_Excellent': [Response_Excellent],
    'Response_Indeterminate': [Response_Indeterminate],
    'Response_Structural Incomplete': [Response_Structural_Incomplete]
}

X_test = pd.DataFrame(data)

# ใช้โมเดลในการพยากรณ์
y_pred = best_model.predict(X_test)

st.write("prediction",y_pred)

for prediction in y_pred:
    if prediction == 0:
        st.write("ผลการทำนาย:")
        st.markdown("<h3 style='text-align: center; color: green;'>ไม่มีความเสี่ยงกลับมาเป็นซ้ำ</h3>", unsafe_allow_html=True)
    elif prediction == 1:
        st.write("ผลการทำนาย:")
        st.markdown("<h3 style='text-align: center; color: red;'>มีความเสี่ยงกลับมาเป็นซ้ำ</h3>", unsafe_allow_html=True)

