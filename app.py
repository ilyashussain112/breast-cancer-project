from flask import Flask, render_template, request
import pandas as pd
from predict import prediction


# user data
df = pd.read_csv("artifacts\\data.csv")
data= df.drop(['diagnosis', 'id', 'Unnamed: 0'], axis=1)
col = data.head(1).columns



app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():

    if request.method == "POST":
        radius_mean =float (request.form.get(col[0]))
        texture_mean = float (request.form.get(col[1]))
        perimeter_mean =float (request.form.get(col[2]))
        area_mean =float (request.form.get(col[3]))
        smoothness_mean =float (request.form.get(col[4]))
        compactness_mean =float (request.form.get(col[5]))
        concavity_mean =float( request.form.get(col[6]))
        concave_points_mean =float (request.form.get(col[7]))
        symmetry_mean = float(request.form.get(col[8]))
        fractal_dimension_mean =float( request.form.get(col[9]))
        radius_se =float( request.form.get(col[10]))
        texture_se = float(request.form.get(col[11]))
        perimeter_se =float( request.form.get(col[12]))
        area_se = float(request.form.get(col[13]))
        smoothness_se = float(request.form.get(col[14]))
        compactness_se =float (request.form.get(col[15]))
        concavity_se =float (request.form.get(col[16]))
        concave_points_se =float( request.form.get(col[17]))
        symmetry_se =float (request.form.get(col[18]))
        fractal_dimension_se = float(request.form.get(col[19]))
        radius_worst = float(request.form.get(col[20]))
        texture_worst = float(request.form.get(col[21]))
        perimeter_worst =float( request.form.get(col[22]))
        area_worst =float( request.form.get(col[23]))
        smoothness_worst =float( request.form.get(col[24]))
        compactness_worst =float (request.form.get(col[25]))
        concavity_worst = float(request.form.get(col[26]))
        concave_points_worst = float (request.form.get(col[27]))
        symmetry_worst = float(request.form.get(col[28]))
        fractal_dimension_worst = float(request.form.get(col[29]))

        array = [[radius_mean,texture_mean,perimeter_mean,area_mean,smoothness_mean,compactness_mean,concavity_mean,
                 concave_points_mean,symmetry_mean,fractal_dimension_mean,radius_se,texture_se,
                 perimeter_se,area_se,smoothness_se,compactness_se,concavity_se,concave_points_se,symmetry_se,
                 fractal_dimension_se,radius_worst,texture_worst,perimeter_worst,area_worst,smoothness_worst,
                 compactness_worst,concavity_worst,concave_points_worst,symmetry_worst,fractal_dimension_worst]]
        # Passig this array to `prediction function`

        a = prediction(data=array)
        if a[0] == 1:
            a = "positive"
        else:
            a = "no"

        return render_template('index.html', name=a, columns=col)
    
    return render_template("index.html", columns=col)

if __name__ == "__main__":
    app.run(debug=True)