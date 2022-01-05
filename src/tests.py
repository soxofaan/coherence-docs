import pytest

from util import list_days
from preprocessing import list_products_by_time

def test_list_days():
    days_list = ["21", "30"]
    month_path = "/data/MTDA/CGS_S1/CGS_S1_SLC_L1/IW/DV/2021/08"
    expected_result = ["/data/MTDA/CGS_S1/CGS_S1_SLC_L1/IW/DV/2021/08/21/S1A_IW_SLC__1SDV_20210821T174107_20210821T174134_039331_04A51D_E85D/S1A_IW_SLC__1SDV_20210821T174107_20210821T174134_039331_04A51D_E85D.zip", "/data/MTDA/CGS_S1/CGS_S1_SLC_L1/IW/DV/2021/08/21/S1A_IW_SLC__1SDV_20210821T174132_20210821T174159_039331_04A51D_7184/S1A_IW_SLC__1SDV_20210821T174132_20210821T174159_039331_04A51D_7184.zip", "/data/MTDA/CGS_S1/CGS_S1_SLC_L1/IW/DV/2021/08/21/S1B_IW_SLC__1SDV_20210821T054128_20210821T054155_028340_0361A3_AB8D/S1B_IW_SLC__1SDV_20210821T054128_20210821T054155_028340_0361A3_AB8D.zip", "/data/MTDA/CGS_S1/CGS_S1_SLC_L1/IW/DV/2021/08/21/S1B_IW_SLC__1SDV_20210821T054152_20210821T054220_028340_0361A3_6100/S1B_IW_SLC__1SDV_20210821T054152_20210821T054220_028340_0361A3_6100.zip", "/data/MTDA/CGS_S1/CGS_S1_SLC_L1/IW/DV/2021/08/21/S1B_IW_SLC__1SDV_20210821T054217_20210821T054244_028340_0361A3_44E5/S1B_IW_SLC__1SDV_20210821T054217_20210821T054244_028340_0361A3_44E5.zip", "/data/MTDA/CGS_S1/CGS_S1_SLC_L1/IW/DV/2021/08/30/S1A_IW_SLC__1SDV_20210830T060647_20210830T060714_039455_04A951_7C4E/S1A_IW_SLC__1SDV_20210830T060647_20210830T060714_039455_04A951_7C4E.zip", "/data/MTDA/CGS_S1/CGS_S1_SLC_L1/IW/DV/2021/08/30/S1A_IW_SLC__1SDV_20210830T060712_20210830T060739_039455_04A951_1AC8/S1A_IW_SLC__1SDV_20210830T060712_20210830T060739_039455_04A951_1AC8.zip"]
    fun_result = list_days(days_list, month_path) 
    assert len(fun_result) == len(expected_result)
    assert set(fun_result) == set(expected_result)
    

def test_list_products_by_time_one_month():
    start = "2021/04/04"
    end = "2021/04/07"
    path = "/data/MTDA/CGS_S1/CGS_S1_SLC_L1/IW/DV/"
    expected = 18
    products = list_products_by_time(start, end, path)
    assert len(products) == expected
    
    
def test_list_products_by_time_two_months():
    start = "2017/06/28"
    end = "2017/07/03"
    path = "/data/MTDA/CGS_S1/CGS_S1_SLC_L1/IW/DV/"
    expected = 16 # usually 18
    products = list_products_by_time(start, end, path)
    assert len(products) == expected