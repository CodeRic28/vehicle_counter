# Vehicle Counter
# How to run:

## 1. Clone the repository
ssh: ```git clone git@github.com:CodeRic28/vehicle_counter.git```
https: ```git clone https://github.com/CodeRic28/vehicle_counter.git```

## 2. Install requirements
```pip install -r requirements.txt```

## 3. Download and extract the "data" folder in the project file
Download here: https://drive.google.com/drive/folders/1q6W_ljlutuashEL5X0fhnbRPEaWa5ca9?usp=sharing

## 4. Download the video and place it in the "videos" directory
Create the directory names "videos" if its not created already.
Download here: https://drive.google.com/file/d/1EHtOi7_NZ7RcIeF79LSj9Q5IsM_9lt3x/view

## 5. Run the script
```python main.py```


## If you wish to train the model yourself:
```yolo detect train data=config.yaml model="yolov8n.yaml" epochs=100"```

### For better accuracy, use:
```yolo detect train data=config.yaml model="yolov8m.yaml" epochs=100```

Note: `After model training, change the "model_path" variable to the new weights in main.py

# Confusion Matrix
![confusion_matrix](https://github.com/CodeRic28/vehicle_counter/assets/51741804/14f2f024-6f20-4479-bc82-8ed9e1154281)
# Confusion Matrix Normalized
![confusion_matrix_normalized](https://github.com/CodeRic28/vehicle_counter/assets/51741804/2f18c45a-f51d-4ff3-9df3-cadcc2c0f534)
# Metrics
![labels](https://github.com/CodeRic28/vehicle_counter/assets/51741804/1c538519-96ea-4c88-a39b-117d01262727)
![labels_correlogram](https://github.com/CodeRic28/vehicle_counter/assets/51741804/66d649ad-2533-498f-a281-0f790e53c640)
# Batches
![train_batch0](https://github.com/CodeRic28/vehicle_counter/assets/51741804/37317189-e4d5-4691-9266-6894c7b6a357)
![train_batch1](https://github.com/CodeRic28/vehicle_counter/assets/51741804/6377ee28-0e9a-4e43-907e-618c4ed92fef)
![train_batch2](https://github.com/CodeRic28/vehicle_counter/assets/51741804/8371c808-3923-4dd3-bd00-c9a79039a512)
![train_batch4230](https://github.com/CodeRic28/vehicle_counter/assets/51741804/92adcb75-d5f5-4329-a017-9504cf423606)

