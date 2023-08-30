import streamlit as st
import pickle
from streamlit_option_menu import option_menu



    
    # sidebar for navigation
with st.sidebar:
        
    selected = option_menu('Multiple Disease Prediction',['Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Hepatitis Prediction','Breast Cancer Prediction'],
                            icons=['activity','heart','person'],
                            default_index=0)
    # Load the saved models
diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))
heart_disease_model = pickle.load(open('heart_disease_model.sav', 'rb'))
hepatitis_model = pickle.load(open("hepatitis_model.sav",'rb'))
 
        
    # Diabetes Prediction Page
if (selected == 'Diabetes Prediction'):
        
    # page title
    st.title('Diabetes Prediction')
    
    
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
        
    with col2:
        Glucose = st.text_input('Glucose Level')
    
    with col3:
        BloodPressure = st.text_input('Blood Pressure value')
    
    with col1:
        SkinThickness = st.text_input('Skin Thickness value')
    
    with col2:
        Insulin = st.text_input('Insulin Level')
    
    with col3:
        BMI = st.text_input('BMI value')
    
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    
    with col2:
        Age = st.text_input('Age of the Person')
    
    
    # code for Prediction and medication info
    diab_diagnosis = ''
    medication_info = ''
    
    # creating a button for Prediction
    
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        

        if (diab_prediction[0] > 0.5 and diab_prediction[0] < 0.6):
            diab_diagnosis = 'Diabetes - Insulin Resistance'
                        
            # add medication information to diagnosis
            medication_info = 'No medications that treat insulin resistance specifically But may take BP medications'
        
        elif (diab_prediction[0] > 0.6 and diab_prediction[0] < 0.7):
            diab_diagnosis = 'Pre - Diabetes' 
                        
            # add medication information to diagnosis
            medication_info = 'metformin, Glumetza. Medications to control cholestrol and high blood pressure might also be prescribed'

        elif (diab_prediction[0] > 0.7 and diab_prediction[0] < 0.85):
            diab_diagnosis = 'Type 2 Diabetes '
                        
            # add medication information to diagnosis
            medication_info = 'Sulfonylureas , Glinides , Thiazolidinediones and DPP - 4 inhibitors'
        
        elif (diab_prediction[0] > 0.85):
                 diab_diagnosis = 'Type 2 Diabetes with Vascular Complications'
                 medication_info = 'There is no Cure, but losing weight,eating well and exercising can help you manage the disease'
        else:
            diab_diagnosis = 'The person doesnt have Diabetes'
        
    st.success(diab_diagnosis)
    
    if (medication_info != ''):
        st.info(medication_info)




# Heart Disease Prediction Page
if (selected == 'Heart Disease Prediction'):
    
    # page title
    st.title('Heart Disease Prediction')

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Age')
        
    with col2:
        sex = st.text_input('Sex')
        
    with col3:
        cp = st.text_input('Chest Pain types')
        
    with col1:
        trestbps = st.text_input('Resting Blood Pressure')
        
    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')
        
    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')
        
    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')
        
    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')
        
    with col3   :
        oldpeak = st.text_input('ST depression induced by exercise')
        
    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')
        
    
    # code for Prediction and Medications
    # code for Prediction and Medications
    heart_diagnosis = ''
    heart_prediction = -1 


        # creating a button for Prediction

    if st.button('Heart Disease Test Result'):
        age = float(age)
        sex = int(sex)
        cp = int(cp)
        trestbps = float(trestbps)
        chol = float(chol)
        fbs = int(fbs)
        restecg = int(restecg)
        thalach = float(thalach)
        oldpeak = float(oldpeak)
        thal = int(thal)
        heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg,thalach,oldpeak,thal]])  
        medication_info = ''                        
        if (heart_prediction[0] > 0.5 and heart_prediction[0] < 0.6):
            heart_diagnosis = 'Stage A - People with this stage have no problems with structure of the heart or how thier heart works'
                        
            # add medication information to diagnosis
            medication_info = 'Keep stress under control , Exercise regularly , Avoid smoking , Manage BP and Cholestrol level'
        
        elif (heart_prediction[0] > 0.6 and heart_prediction[0] < 0.7):
            heart_diagnosis = 'Stage B - Most people do not show symptoms'
                        
            # add medication information to diagnosis
            medication_info = 'ACE inhibitor / ARB or ARNI and beta blockers'

        elif (heart_prediction[0] > 0.7 and heart_prediction[0] < 0.85):
            heart_diagnosis = 'Stage C - Fatigue and Difficulty in breathing '
                        
            # add medication information to diagnosis
            medication_info = 'Diuretics , mineralocorticoid receptor blockers or SGLT2 inhibitors'
        
        elif (heart_prediction[0] > 0.85):
                 heart_diagnosis = 'Stage D - Rapid heart beat , persistent Cough'
                 medication_info = 'This stage is severe and may require advanced specialized treatment such as mechanical circulatory support'
        else:
            heart_diagnosis = 'The person doesnt have Heart Disease'
            
        st.success(heart_diagnosis)
        
        if (medication_info != ''):
            st.info(medication_info)



def yesto(val):
    if val=="Yes":
        return 1
    else:
        return 0


if (selected == 'Hepatitis Prediction'):
    
    # page title
    st.title('Hepatitis Prediction')

    col1, col2, col3 = st.columns(3)
            
    with col1:
        apetite = st.radio("Loss of apetite",("Yes","No"))
        
    with col2:
        vomit = st.radio("Vomitting ?",("Yes","No"))

    with col3:
        diar = st.radio("Facing Diarrhoea",("Yes","No"))

    with col1:
        fever = st.radio("You having Mild Fever",("Yes","No"))
        
    with col2:
        nausea = st.radio("Facing Nausea ?",("Yes","No"))

    with col3:
        skin = st.radio("Having Yellowish Skin ?",("Yes","No"))

    with col1:
        urine = st.radio("Dark Urine ?",("Yes","No"))
        
    with col2:
        pain = st.radio("Any Abdominal pain ?",("Yes","No"))

    with col3:
        fatigue = st.radio("Do you feel Fatigue ?",("Yes","No"))

    if st.button('Hepatitis Prediction'):
        apetite = yesto(apetite)
        vomit = yesto(vomit)
        diar = yesto(diar)
        fever = yesto(fever)
        nausea = yesto(nausea)
        skin = yesto(skin)
        urine = yesto(urine)
        pain = yesto(pain)
        fatigue = yesto(fatigue)
        hep_prediction = hepatitis_model.predict([[apetite,vomit,diar,fever,nausea,skin,urine,pain,fatigue]])

        medication_info = ''                        
        if (hep_prediction[0]=='hepatitis A'):
            hep_diagnosis = 'Hepatitis A'
                        
            # add medication information to diagnosis
            medication_info = 'No specific treatment for Hepatitis A, your body will clean it on its own '
        
        elif (hep_prediction[0]=='Hepatitis B'):
            hep_diagnosis = 'Hepatitis B'
                        
            # add medication information to diagnosis
            medication_info = 'Interferon alfa-2b , Intron A , Liver transplant'

        elif (hep_prediction[0]=='Hepatitis C'):
            hep_diagnosis = 'Hepatitis C'
                        
            # add medication information to diagnosis
            medication_info = 'Anti-viral Medications , Best to discuss your treatment options with a specialist'

        st.success(hep_diagnosis)
        
        if (medication_info != ''):
            st.info(medication_info)