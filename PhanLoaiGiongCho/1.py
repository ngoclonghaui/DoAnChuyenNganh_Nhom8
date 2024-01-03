from flask import Flask, jsonify, render_template
from skimage.util import img_as_ubyte
from skimage.transform import resize
import base64
import os
import glob
from skimage.color import rgb2gray
from skimage.io import imread
import numpy as np
import joblib
from sklearn.metrics import accuracy_score, f1_score, recall_score, precision_score
from sklearn.preprocessing import MinMaxScaler
from flask_cors import CORS
from PIL import Image
from io import BytesIO
import pandas as pd
app = Flask(__name__)
CORS(app)
RESIZED_DIMENSIONS = (50, 50, 3)
DATASET_PATH = 'archive'
MODEL_PATH = 'model/Dog14_Kaggle.pkl'
N_CATEGORIES = 3

# Load danh sách các thư mục test
CATEGORIES_TEST = os.listdir(os.path.join(DATASET_PATH, 'test'))
if not isinstance(CATEGORIES_TEST, list):
    CATEGORIES_TEST = list(CATEGORIES_TEST)
# Đọc model đã train
model = joblib.load(MODEL_PATH)

# Hàm tiền xử lý dữ liệu test
def preprocess_test_data():
    flat_data_arr = []
    target_arr = []
    original_images = []
    for category in CATEGORIES_TEST:
        image_files = glob.glob(os.path.join(DATASET_PATH, 'test', category, '*.jpg'))

        if not image_files:
            print(f"No images found for category: {category}")
        for img_file in image_files:
            img_array = imread(img_file)
            img_gray = rgb2gray(img_array)

            img_resized = resize(img_gray, RESIZED_DIMENSIONS)
            flat_data_arr.append(img_resized.flatten())
            target_arr.append(CATEGORIES_TEST.index(category))
            original_images.append(img_array)
    flat_data = np.array(flat_data_arr)
    target = np.array(target_arr)
    return flat_data, target,original_images


@app.route('/api/getall', methods=['GET'])
def get_all():
    y_pred = model.predict(test_flat_data)
    predicted_labels = []
    for label in y_pred:
        predicted_labels.append(label)

  #  print(predicted_labels)

    y_test = df_test.iloc[:, -1]
    print("nhãn thực tế", y_test)
    true_label_acc = []
    for label in y_test:
        true_label_acc.append(label)
    print(true_label_acc)
    images = []
    for img, pred_label, true_label in zip(original_images, predicted_labels, true_label_acc):
        img_pil = Image.fromarray((img * 255).astype(np.uint8))

        buffered = BytesIO()
        img_pil.save(buffered, format="JPEG")
        img_base64 = base64.b64encode(buffered.getvalue()).decode("utf-8")

        images.append({
            'image': img_base64,
            'predicted_label': pred_label,
            'true_label': true_label
        })

    return jsonify(images)


def load_images(path, categories):
    flat_data_arr = []
    target_arr = []
    original_images = []

    for category in categories:
        print(f'Loading... Category: {category}')

        image_files = glob.glob(os.path.join(path, category, '*.jpg'))

        for img_file in image_files:
            img = Image.open(img_file)
            img_array = np.array(img)
            original_images.append(img_array)

            img_gray = rgb2gray(img_array)
            img_resized = resize(img_gray, RESIZED_DIMENSIONS)
            flat_data_arr.append(img_resized.flatten())
            target_arr.append(category)

        print(f'Loaded category: {category} successfully')

    flat_data = np.array(flat_data_arr)
    target = np.array(target_arr)

    return flat_data, original_images, target


@app.route('/results', methods=['GET'])
def get_results():

    result = [accuracy, f1, recall, precision,num_correct,num_fail]
    return jsonify(result)

_, _, original_images = preprocess_test_data()
test_flat_data, _, _ = preprocess_test_data()
_, test_target, _ = preprocess_test_data()
test_flat_data, original_images, test_target = load_images(os.path.join(DATASET_PATH, 'test'), CATEGORIES_TEST)

df_test = pd.DataFrame(test_flat_data)
df_test['Target'] = test_target

x_test = df_test.iloc[:, :-1]
y_test = df_test.iloc[:, -1]
y_pred = model.predict(x_test)

print("Predicted label : ")
print(y_pred)

# Tính toán các độ đo đánh giá
accuracy = accuracy_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred, average='weighted')
recall = recall_score(y_test, y_pred, average='weighted')
precision = precision_score(y_test, y_pred, average='weighted')

print("Accuracy:", accuracy)
print("F1 Score:", f1)
print("Recall:", recall)
print("Precision:", precision)
list = []
for index in list:
    list.append(accuracy)
    list.append(f1)
    list.append(recall)
    list.append(precision)
print(list)
num_correct = 0
num_fail = 0
for pred_label, true_label in zip(y_pred, y_test):
    if pred_label == true_label:
        num_correct += 1
    else:
        num_fail += 1
print("Số lượng dữ liệu dự đoán đúng:", num_correct)
print("Số lượng dữ liệu dự đoán sai:", num_fail)

if __name__ == '__main__':
    app.run(host='localhost', port=8080, debug=True)

