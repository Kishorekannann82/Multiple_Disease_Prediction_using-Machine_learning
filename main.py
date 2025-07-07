import streamlit as st
import pickle
import os
from streamlit_option_menu import option_menu


st.set_page_config(page_title="Multiple Disease Prediction",layout="wide",page_icon="👀")

working_dir=os.path.dirname(os.path.abspath(__file__))

diabetes_model = pickle.load(open(f'{working_dir}/diabetes.pkl','rb'))
heart_disease_model=pickle.load(open(f'{working_dir}/heart.pkl','rb'))
kidney_disease_model=pickle.load(open(f'{working_dir}/kidney.pkl','rb'))
parkinsons_disease_model=pickle.load(open(f'{working_dir}/Parkinsons.pkl','rb'))
breast_cancer_model=pickle.load(open(f'{working_dir}/breast_cancer.pkl','rb'))
liver_disease_model=pickle.load(open(f'{working_dir}/liver.pkl','rb'))

NewBMI_Overweight=0
NewBMI_Underweight=0
NewBMI_Obesity_1=0
NewBMI_Obesity_2=0 
NewBMI_Obesity_3=0
NewInsulinScore_Normal=0 
NewGlucose_Low=0
NewGlucose_Normal=0 
NewGlucose_Overweight=0
NewGlucose_Secret=0

with st.sidebar:
    selected= option_menu("Multiple Disease Prediction",
                ['Diabetes Prediction',
                 'Heart Disease Prediction',
                 'Kidney Disease Prediction',
                 'Parkinsons Disease Detection',
                 'Breast Cancer Disease Prediction',
                 'Liver Disease Prediction'
                 ],
                 menu_icon='hospital-fill',
                 icons=['activity','heart','droplet','cpu','gender-female','capsule'],
                 default_index=0)

if selected == "Diabetes Prediction":
    st.title("Diabetes Prediction Using Machine Learning")
    col1,col2,col3=st.columns(3)

    with col1:
        Pregnancies=st.text_input("Number of Pregnancies")
    with col2:
        Glucose=st.text_input("Glucose level")
    with col3:
        BloodPressure=st.text_input("BloodPressure Value")
    with col1:
        SkinThickness=st.text_input("SkinThickness Value")
    with col2:
        Insulin=st.text_input("Insulin Value")
    with col3:
        BMI=st.text_input("BMI Value")
    with col1:
        DiabetesPedigreeFunction=st.text_input("DiabetesPedigreeFunction Value")
    with col2:
        Age=st.text_input("Age")
    diabetes_result=""
    if st.button("Diabetes Test Result"):
        if float(BMI)<=18.5:
            NewBMI_Underweight = 1
        elif 18.5 < float(BMI) <=24.9:
            pass
        elif 24.9<float(BMI)<=29.9:
            NewBMI_Overweight =1
        elif 29.9<float(BMI)<=34.9:
            NewBMI_Obesity_1 =1
        elif 34.9<float(BMI)<=39.9:
            NewBMI_Obesity_2=1
        elif float(BMI)>39.9:
            NewBMI_Obesity_3 = 1
        
        if 16<=float(Insulin)<=166:
            NewInsulinScore_Normal = 1

        if float(Glucose)<=70:
            NewGlucose_Low = 1
        elif 70<float(Glucose)<=99:
            NewGlucose_Normal = 1
        elif 99<float(Glucose)<=126:
            NewGlucose_Overweight = 1
        elif float(Glucose)>126:
            NewGlucose_Secret = 1
        user_input=[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,
                    BMI,DiabetesPedigreeFunction,Age, NewBMI_Underweight,
                    NewBMI_Overweight,NewBMI_Obesity_1,
                    NewBMI_Obesity_2,NewBMI_Obesity_3,NewInsulinScore_Normal, 
                    NewGlucose_Low,NewGlucose_Normal, NewGlucose_Overweight,
                    NewGlucose_Secret]
        user_input=[float(x) for x in user_input]
        prediction=diabetes_model.predict([user_input])
        if prediction[0]==1:
            diabetes_result="The person has diabetic"
        else:
            diabetes_result="The person has no diabetes"
    st.success(diabetes_result)

    
#Heart Disease:
if selected == "Heart Disease Prediction":
    st.title("Heart Diseases Prediction Using Machine Learning ")
    col1,col2,col3=st.columns(3)

    with col1:
        age=st.text_input("Age")
    with col2:
        sex=st.text_input("Sex")
    with col3:
        cp=st.text_input("Chest Pain Types")
    with col1:
        trestbps=st.text_input("Resting Blood Pressure")
    with col2:
        chol=st.text_input("Serum Cholestroal in mg/dl")
    with col3:
        fbs=st.text_input("Fasting Blood Sugar > 120 mg/dl")
    with col1:
        restecg=st.text_input("Resting Electrocardiographic results")
    with col2:
        thalach=st.text_input("Maximum Heart Rate achieved")
    with col3:
        exang=st.text_input("Exercise Induced Angina")
    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')

    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')

    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')

    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')
    heart_disease_result=""
    if st.button("Heart Disease Test Result"):
        user_input=[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]
        user_input = [float(x) for x in user_input]
        prediction=heart_disease_model.predict([user_input])
        if prediction[0]==1:
            heart_disease_result="This person having Heart Disease"
        else:
            heart_disease_result="This person does not have any heart Disease"
        st.success(heart_disease_result)


# Kidney Disease Prediction
if selected == "Kidney Disease Prediction":
    st.title("Kidney Disease Prediction using ML")

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        age = st.text_input('Age')

    with col2:
        blood_pressure = st.text_input('Blood Pressure')

    with col3:
        specific_gravity = st.text_input('Specific Gravity')

    with col4:
        albumin = st.text_input('Albumin')

    with col5:
        sugar = st.text_input('Sugar')

    with col1:
        red_blood_cells = st.text_input('Red Blood Cell')

    with col2:
        pus_cell = st.text_input('Pus Cell')

    with col3:
        pus_cell_clumps = st.text_input('Pus Cell Clumps')

    with col4:
        bacteria = st.text_input('Bacteria')

    with col5:
        blood_glucose_random = st.text_input('Blood Glucose Random')

    with col1:
        blood_urea = st.text_input('Blood Urea')

    with col2:
        serum_creatinine = st.text_input('Serum Creatinine')

    with col3:
        sodium = st.text_input('Sodium')

    with col4:
        potassium = st.text_input('Potassium')

    with col5:
        haemoglobin = st.text_input('Haemoglobin')

    with col1:
        packed_cell_volume = st.text_input('Packed Cell Volume')

    with col2:
        white_blood_cell_count = st.text_input('White Blood Cell Count')

    with col3:
        red_blood_cell_count = st.text_input('Red Blood Cell Count')

    with col4:
        hypertension = st.text_input('Hypertension')

    with col5:
        diabetes_mellitus = st.text_input('Diabetes Mellitus')

    with col1:
        coronary_artery_disease = st.text_input('Coronary Artery Disease')

    with col2:
        appetite = st.text_input('Appetite')

    with col3:
        peda_edema = st.text_input('Peda Edema')

    with col4:
        anemia = st.text_input('Anemia')

    # code for Prediction
    kidney_diagnosis = ''

    # creating a button for Prediction    
    if st.button("Kidney's Test Result"):

        user_input = [age, blood_pressure, specific_gravity, albumin, sugar,
                      red_blood_cells, pus_cell, pus_cell_clumps, bacteria,
                      blood_glucose_random, blood_urea, serum_creatinine, sodium,
                      potassium, haemoglobin, packed_cell_volume,
                      white_blood_cell_count, red_blood_cell_count, hypertension,
                      diabetes_mellitus, coronary_artery_disease, appetite,
                      peda_edema, anemia]

        user_input = [float(x) for x in user_input]

        prediction = kidney_disease_model.predict([user_input])

        if prediction[0] == 1:
            kidney_diagnosis = "The person has Kidney's disease"
        else:
            kidney_diagnosis = "The person does not have Kidney's disease"

    st.success(kidney_diagnosis)
if selected=="Parkinsons Disease Detection":
    st.title("Parkinsons Disease Prediction Using Machine Learning")

    col1,col2,col3,col4,col5=st.columns(5)

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        MDVP_Fo_Hz = st.text_input("Fo (Hz)")
    with col2:
        MDVP_Fhi_Hz = st.text_input("Fhi (Hz)")
    with col3:
        MDVP_Flo_Hz = st.text_input("Flo (Hz)")
    with col4:
        MDVP_Jitter_percent = st.text_input("Jitter (%)")
    with col5:
        MDVP_Jitter_Abs = st.text_input("Jitter (Abs)")

    with col1:
        MDVP_RAP = st.text_input("RAP")
    with col2:
        MDVP_PPQ = st.text_input("PPQ")
    with col3:
        Jitter_DDP = st.text_input("DDP")
    with col4:
        MDVP_Shimmer = st.text_input("Shimmer")
    with col5:
        MDVP_Shimmer_dB = st.text_input("Shimmer (dB)")

    with col1:
        Shimmer_APQ3 = st.text_input("APQ3")
    with col2:
        Shimmer_APQ5 = st.text_input("APQ5")
    with col3:
        MDVP_APQ = st.text_input("APQ")
    with col4:
        Shimmer_DDA = st.text_input("DDA")
    with col5:
        NHR = st.text_input("NHR")

    with col1:
        HNR = st.text_input("HNR")
    with col2:
        RPDE = st.text_input("RPDE")
    with col3:
        DFA = st.text_input("DFA")
    with col4:
        spread1 = st.text_input("Spread1")
    with col5:
        spread2 = st.text_input("Spread2")

    with col1:
        D2 = st.text_input("D2")
    with col2:
        PPE = st.text_input("PPE")
    

    # code for Prediction
    parkinsons_result=""

    if st.button("Parkinsons Result"):
        user_input = [
            MDVP_Fo_Hz, MDVP_Fhi_Hz, MDVP_Flo_Hz, MDVP_Jitter_percent, MDVP_Jitter_Abs,
            MDVP_RAP, MDVP_PPQ, Jitter_DDP, MDVP_Shimmer, MDVP_Shimmer_dB,
            Shimmer_APQ3, Shimmer_APQ5, MDVP_APQ, Shimmer_DDA, NHR,
            HNR, RPDE, DFA, spread1, spread2, D2, PPE
        ]
        user_input=[float(x) for x in user_input]
        prediction=parkinsons_disease_model.predict([user_input])

        if prediction[0]==1:
            parkinsons_result="The person has Parkinson's disease"
        else:
            parkinsons_result="The Person does not have Parkinson's Disease"
    st.success(parkinsons_result)   

if selected == "Breast Cancer Disease Prediction":
    st.title("Breast Cancer Prediction Using Machine Learning")
    col1,col2,col3,col4,col5=st.columns(5)

    with col1:
        radius_mean = st.text_input("Radius Mean")
    with col2:
        texture_mean = st.text_input("Texture Mean")
    with col3:
        perimeter_mean = st.text_input("Perimeter Mean")
    with col4:
        area_mean = st.text_input("Area Mean")
    with col5:
        smoothness_mean = st.text_input("Smoothness Mean")

    with col1:
        compactness_mean = st.text_input("Compactness Mean")
    with col2:
        concavity_mean = st.text_input("Concavity Mean")
    with col3:
        concave_points_mean = st.text_input("Concave Points Mean")
    with col4:
        symmetry_mean = st.text_input("Symmetry Mean")
    with col5:
        fractal_dimension_mean = st.text_input("Fractal Dimension Mean")

    with col1:
        radius_se = st.text_input("Radius SE")
    with col2:
        texture_se = st.text_input("Texture SE")
    with col3:
        perimeter_se = st.text_input("Perimeter SE")
    with col4:
        area_se = st.text_input("Area SE")
    with col5:
        smoothness_se = st.text_input("Smoothness SE")

    with col1:
        compactness_se = st.text_input("Compactness SE")
    with col2:
        concavity_se = st.text_input("Concavity SE")
    with col3:
        concave_points_se = st.text_input("Concave Points SE")
    with col4:
        symmetry_se = st.text_input("Symmetry SE")

    with col5:
        radius_worst = st.text_input("Radius Worst")
    with col1:
        texture_worst = st.text_input("Texture Worst")
    with col2:
        perimeter_worst = st.text_input("Perimeter Worst")
    # Breast Cancer Prediction 
    breast_cancer_result=""
    if st.button("Breast Cancer Result"):
        user_input = [
            radius_mean, texture_mean, perimeter_mean, area_mean, smoothness_mean,
            compactness_mean, concavity_mean, concave_points_mean, symmetry_mean, fractal_dimension_mean,
            radius_se, texture_se, perimeter_se, area_se, smoothness_se,
            compactness_se, concavity_se, concave_points_se, symmetry_se,
            radius_worst, texture_worst, perimeter_worst
        ]
        user_input=[float(x) for x in user_input]
        prediction=breast_cancer_model.predict


        if prediction[0]==1:
            breast_cancer_result="The Person has Breast Cancer"
        else:
            breast_cancer_result="The Person does not have Breast Cancer"
    st.success(breast_cancer_result)
if selected=="Liver Disease Prediction":
    
    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input("Age")
    with col2:
        gender = st.text_input("Gender (1=Male, 0=Female)")
    with col3:
        total_bilirubin = st.text_input("Total Bilirubin")

    with col1:
        direct_bilirubin = st.text_input("Direct Bilirubin")
    with col2:
        alkaline_phosphotase = st.text_input("Alkaline Phosphotase")
    with col3:
        alamine_aminotransferase = st.text_input("Alamine Aminotransferase")

    with col1:
        aspartate_aminotransferase = st.text_input("Aspartate Aminotransferase")
    with col2:
        total_proteins = st.text_input("Total Proteins")
    with col3:
        albumin = st.text_input("Albumin")

    with col1:
        albumin_and_globulin_ratio = st.text_input("Albumin/Globulin Ratio")

    

    #Liver Disease Prediction
    liver_disease_result="" 
    if st.button("Liver Disease Result"):
        user_input = [
            age, 
            gender, 
            total_bilirubin, 
            direct_bilirubin, 
            alkaline_phosphotase, 
            alamine_aminotransferase, 
            aspartate_aminotransferase, 
            total_proteins, 
            albumin, 
            albumin_and_globulin_ratio
        ]

        user_input=[float(x) for x in user_input]
        prediction=liver_disease_model.predict([user_input])

        if prediction==1:
            liver_disease_result="The person has Liver Disease"
        else:
            liver_disease_result="The person does have Liver Disease"
    st.success(liver_disease_result)






