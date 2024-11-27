import smbus2
import bme280
from datetime import datetime
from pymongo import MongoClient

port = 1
address = 0x76
bus = smbus2.SMBus(port)
calibration_params = bme280.load_calibration_params(bus, address)
data = bme280.sample(bus, address, calibration_params)
print("温度", data.temperature)
print("湿度", data.humidity)
print("压力", data.pressure)

# 连接到 MongoDB
client = MongoClient("mongodb+srv://new_hongwei:xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")

# 数据库名 集合名
db = client.hongweizhucom
collection = db.huanjing

# 执行插入操作
result = collection.insert_one({
    "temperature": round(data.temperature, 2),
    "humidity": round(data.humidity, 2),
    "pressure": round(data.pressure, 2),
    "created_at": datetime.now()  # 插入当前时间
})

# 打印 插入的文档 ID
print("document id:", result.inserted_id)
