from pydantic import BaseModel
# 2. Class which describes Bank Notes measurements
class Schema(BaseModel): 
    radius_mean: float 
    perimeter_mean: float 
    area_mean: float
    compactness_mean: float 
    concavity_mean: float
    concave_points_mean: float
    radius_se: float
    perimeter_se: float 
    area_se: float
    radius_worst: float
    perimeter_worst: float 
    area_worst: float 
    compactness_worst: float 
    concavity_worst: float
    concave_points_worst: float
