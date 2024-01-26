from django.shortcuts import render
from joblib import load

model = load('./models/model.joblib')

def predictor(request):
    return render(request, 'index.html')

def formInfo(request):
    surgery = request.GET['surgery']
    Age = request.GET['Age']
    Rectal_Temperature = request.GET['Rectal Temperature']
    Pulse = request.GET['Pulse']
    Respiratory_Rate = request.GET['Respiratory Rate']
    Temperature_Of_Extremities = request.GET['Temperature Of Extremities']
    Peripheral_Pulse = request.GET['Peripheral Pulse']
    Mucous_Membrane = request.GET['Mucous Membrane']
    Capillary_Refill_Time = request.GET['Capillary Refill Time']
    Pain = request.GET['Pain']
    Peristalsis= request.GET['Peristalsis']
    Abdominal_Distention= request.GET['Abdominal Distention']
    Nasogastric_Tube= request.GET['Nasogastric Tube']
    Nasogastric_Reflux= request.GET['Nasogastric Reflux']
    Nasogastric_Reflux_Ph = request.GET['Nasogastric Reflux Ph']
    Rectal_Exam_Feces = request.GET['Rectal Exam Feces']
    Abdomen = request.GET['Abdomen']
    Packed_Cell_Volume = request.GET['Packed Cell Volume']
    Total_Protein = request.GET['Total Protein']
    Abdomen_Appearance = request.GET['Abdomen Appearance']
    Abdomen_Protein = request.GET['Abdomen Protein']
    Surgical_Lesion = request.GET['Surgical Lesion']
    Lesion_1 = request.GET['Lesion 1']
    Lesion_2 = request.GET['Lesion 2']
    Lesion_3 = request.GET['Lesion 3']
    CP_Data = request.GET['CP Data']

    y_pred = model.predict([[surgery,
                             Age,
                                Rectal_Temperature,
                                Pulse,
                                Respiratory_Rate,
                                Temperature_Of_Extremities,
                                Peripheral_Pulse,
                                Mucous_Membrane,
                                Capillary_Refill_Time,
                                Pain,
                                Peristalsis,
                                Abdominal_Distention,
                                Nasogastric_Tube,
                                Nasogastric_Reflux,
                                Nasogastric_Reflux_Ph,
                                Rectal_Exam_Feces,
                                Abdomen,
                                Packed_Cell_Volume,
                                Total_Protein,
                                Abdomen_Appearance,
                                Abdomen_Protein,
                                Surgical_Lesion,
                                Lesion_1,
                                Lesion_2,
                                Lesion_3,
                                CP_Data
                                ]])
    print(y_pred)
    if y_pred == 1:
        return render(request, 'result.html', {'prediction': 'The horse is likely to survive'})
    else:
        return render(request, 'result.html', {'prediction': 'The horse is likely to die'})
    return render(request, 'result.html')