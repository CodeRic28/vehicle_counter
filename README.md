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
Download here: https://drive.google.com/file/d/1EHtOi7_NZ7RcIeF79LSj9Q5IsM_9lt3x/view

## 5. Run the script
```python main.py```


## If you wish to train the model yourself:
```yolo detect train data=config.yaml model="yolov8n.yaml" epochs=100"```

### For better accuracy, use:
```yolo detect train data=config.yaml model="yolov8m.yaml" epochs=100```


