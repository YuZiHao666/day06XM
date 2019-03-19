"""
需求：
    写入 data = {'Search_Data': {
                'search_test_002': {'expect': {'value': '你好'}, 'value': '你好'},
                'search_test_001': {'expect': [4, 5, 6], 'value': 456}}}
    write.yaml
"""

# 导包
import yaml

# 写入的数据
data = {'Search_Data': {
                'search_test_002': {'expect': {'value': '你好'}, 'value': '你好'},
                'search_test_001': {'expect': [4, 5, 6], 'value': 456}}}

# 写入文件流
with open("../data/write.yaml", "w", encoding="utf-8") as f:
    # 调用 dump方法
    yaml.dump(data, f, encoding="utf-8", allow_unicode=True)