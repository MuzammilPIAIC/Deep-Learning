import numpy as np
from PIL import Image
from feature_extractor import FeatureExtractor
from datetime import datetime
from flask import Flask, request, render_template, jsonify
from pathlib import Path
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


# Read image features
fe = FeatureExtractor()
features = []
img_paths = []
for feature_path in Path("C:/Users/Crown/Desktop/search-by-image/made/sis/static/feature").glob("*.npy"):
    features.append(np.load(feature_path))
    img_paths.append(Path("C:/Users/Crown/Desktop/search-by-image/made/sis/static/img") / (feature_path.stem + ".jpg"))
features = np.array(features)

print(img_paths)
@app.route('/', methods=['POST'])
def index():
    #if request.method == 'POST':
    file = request.files['query_img']
    text = request.files["txt"]

        # Save query image
    img = Image.open(file.stream)  # PIL image
    uploaded_img_path = "C:/Users/Crown/Desktop/search-by-image/made/sis/static/uploaded/" + datetime.now().isoformat().replace(":", ".") + "_" + file.filename
    img.save(uploaded_img_path)

        # Run search
    query = fe.extract(img)
    dists = np.linalg.norm(features-query, axis=1)  # L2 distances to features
    ids = np.argsort(dists)[:3]  # Top 30 results
    print("this is IDS: ",ids)
    scores = [(dists[id], img_paths[id]) for id in ids]
    result = []
    for i in ids:
        print("this is img: ",img_paths[i])
        result.append(str(img_paths[i]))
    dicw = {
            "path": result,
            "text": text
            }

    return jsonify(result)
    #else:
        #return render_template('index.html')


if __name__=="__main__":
    app.run("0.0.0.0")
