from django.shortcuts import render

# Create your views here.
def migranes(request):
    if (request.method=="POST"):
        data=request.POST
        age=float(data.get('textage'))
        duration=float(data.get('textduration'))
        frequency=float(data.get('textfrequency'))
        location=float(data.get('textlocation'))
        character=float(data.get('textcharacter'))
        intensity=float(data.get('textintensity'))
        nausea=float(data.get('textnausea'))
        vomit=float(data.get('textvomit'))
        phonophobia=float(data.get('textphonophobia'))
        photophobia=float(data.get('textphotophobia'))
        visual=float(data.get('textvisual'))
        sensory=float(data.get('textsensory'))
        dysphasia=float(data.get('textdysphasia'))
        dysarthria=float(data.get('textdysarthria'))
        vertigo=float(data.get('textvertigo'))
        tinnitus=float(data.get('texttinnitus'))
        hypoacusis=float(data.get('texthypoacusis'))
        diplopia=float(data.get('textdiplopia'))
        defect=float(data.get('textdefect'))
        ataxia=float(data.get('textataxia'))
        conscience=float(data.get('textconscience'))
        paresthesia=float(data.get('textparesthesia'))
        dpf=float(data.get('textdpf'))
        if ('buttonpredict' in request.POST):
            import pandas as pd 
            path="C:\\Users\\cheth\\OneDrive\\Desktop\\Batch_04\\Data\\data.csv" 
            data=pd.read_csv(path) 
            inputs=data.drop('Type',axis=1)
            output=data['Type']
            import sklearn
            from sklearn.model_selection import train_test_split
            x_train,x_test,y_train,y_test=train_test_split(inputs,output,train_size=0.8)
            import sklearn
            from sklearn.ensemble import RandomForestClassifier
            model=RandomForestClassifier(n_estimators=50)
            model.fit(x_train,y_train)
            y_pred=model.predict(x_test)
            result=model.predict([[age,duration,frequency,location,character,intensity,nausea,vomit,phonophobia,photophobia,visual,sensory,dysphasia,dysarthria,vertigo,tinnitus,hypoacusis,diplopia,defect,ataxia,conscience,paresthesia,dpf]])
        return render(request,'migranes.html',context={'result':result[0]})
    return render (request,'migranes.html')


