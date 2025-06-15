from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import catboost
import json

class Data(BaseModel):
    Destination_Port: int
    Flow_Duration: int
    Total_Fwd_Packets: int
    Total_Backward_Packets: int
    Total_Length_of_Fwd_Packets: int
    Total_Length_of_Bwd_Packets: int
    Fwd_Packet_Length_Max: int
    Fwd_Packet_Length_Min: int
    Fwd_Packet_Length_Mean: float
    Fwd_Packet_Length_Std: float
    Bwd_Packet_Length_Max: int
    Bwd_Packet_Length_Min: int
    Bwd_Packet_Length_Mean: float
    Bwd_Packet_Length_Std: float
    Flow_Bytes_per_s: float
    Flow_Packets_per_s: float
    Flow_IAT_Mean: float
    Flow_IAT_Std: float
    Flow_IAT_Max: int
    Flow_IAT_Min: int
    Fwd_IAT_Total: int
    Fwd_IAT_Mean: float
    Fwd_IAT_Std: float
    Fwd_IAT_Max: int
    Fwd_IAT_Min: int
    Bwd_IAT_Total: int
    Bwd_IAT_Mean: float
    Bwd_IAT_Std: float
    Bwd_IAT_Max: int
    Bwd_IAT_Min: int
    Fwd_PSH_Flags: int
    Bwd_PSH_Flags: int
    Fwd_URG_Flags: float
    Bwd_URG_Flags: float
    Fwd_Header_Length: float
    Bwd_Header_Length: float
    Fwd_Packets_per_s: float
    Bwd_Packets_per_s: float
    Min_Packet_Length: float
    Max_Packet_Length: float
    Packet_Length_Mean: float
    Packet_Length_Std: float
    Packet_Length_Variance: float
    FIN_Flag_Count: float
    SYN_Flag_Count: float
    RST_Flag_Count: float
    PSH_Flag_Count: float
    ACK_Flag_Count: float
    URG_Flag_Count: float
    CWE_Flag_Count: float
    ECE_Flag_Count: float
    Down_Up_Ratio: float
    Average_Packet_Size: float
    Avg_Fwd_Segment_Size: float
    Avg_Bwd_Segment_Size: float
    Fwd_Header_Length_1: float
    Fwd_Avg_Bytes_Bulk: float
    Fwd_Avg_Packets_Bulk: float
    Fwd_Avg_Bulk_Rate: float
    Bwd_Avg_Bytes_Bulk: float
    Bwd_Avg_Packets_Bulk: float
    Bwd_Avg_Bulk_Rate: float
    Subflow_Fwd_Packets: float
    Subflow_Fwd_Bytes: float
    Subflow_Bwd_Packets: float
    Subflow_Bwd_Bytes: float
    Init_Win_bytes_forward: float
    Init_Win_bytes_backward: float
    act_data_pkt_fwd: float
    min_seg_size_forward: float
    Active_Mean: float
    Active_Std: float
    Active_Max: float
    Active_Min: float
    Idle_Mean: float
    Idle_Std: float
    Idle_Max: float
    Idle_Min: float



app = FastAPI()

@app.post("/predict")
async def getPrediction(data:Data):
    try:
        model = catboost.CatBoostClassifier().load_model("my_ddos_model")
        DataJson = json.loads(data.model_dump_json())
        df = pd.DataFrame([DataJson])
        df.columns = ['Destination Port', 'Flow Duration', 'Total Fwd Packets',
       'Total Backward Packets', 'Total Length of Fwd Packets',
       'Total Length of Bwd Packets', 'Fwd Packet Length Max',
       'Fwd Packet Length Min', 'Fwd Packet Length Mean',
       'Fwd Packet Length Std', 'Bwd Packet Length Max',
       'Bwd Packet Length Min', 'Bwd Packet Length Mean',
       'Bwd Packet Length Std', 'Flow Bytes/s', 'Flow Packets/s',
       'Flow IAT Mean', 'Flow IAT Std', 'Flow IAT Max', 'Flow IAT Min',
       'Fwd IAT Total', 'Fwd IAT Mean', 'Fwd IAT Std', 'Fwd IAT Max',
       'Fwd IAT Min', 'Bwd IAT Total', 'Bwd IAT Mean', 'Bwd IAT Std',
       'Bwd IAT Max', 'Bwd IAT Min', 'Fwd PSH Flags', 'Bwd PSH Flags',
       'Fwd URG Flags', 'Bwd URG Flags', 'Fwd Header Length',
       'Bwd Header Length', 'Fwd Packets/s', 'Bwd Packets/s',
       'Min Packet Length', 'Max Packet Length', 'Packet Length Mean',
       'Packet Length Std', 'Packet Length Variance', 'FIN Flag Count',
       'SYN Flag Count', 'RST Flag Count', 'PSH Flag Count', 'ACK Flag Count',
       'URG Flag Count', 'CWE Flag Count', 'ECE Flag Count', 'Down/Up Ratio',
       'Average Packet Size', 'Avg Fwd Segment Size', 'Avg Bwd Segment Size',
       'Fwd Header Length.1', 'Fwd Avg Bytes/Bulk', 'Fwd Avg Packets/Bulk',
       'Fwd Avg Bulk Rate', 'Bwd Avg Bytes/Bulk', 'Bwd Avg Packets/Bulk',
       'Bwd Avg Bulk Rate', 'Subflow Fwd Packets', 'Subflow Fwd Bytes',
       'Subflow Bwd Packets', 'Subflow Bwd Bytes', 'Init_Win_bytes_forward',
       'Init_Win_bytes_backward', 'act_data_pkt_fwd', 'min_seg_size_forward',
       'Active Mean', 'Active Std', 'Active Max', 'Active Min', 'Idle Mean',
       'Idle Std', 'Idle Max', 'Idle Min']
        prediction = model.predict(df)
        return {"response":str(prediction[0])}

    except Exception as e:
        return {"error":str(e)}  

