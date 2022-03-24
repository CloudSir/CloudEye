'''
Author: CloudSir
@Github: https://github.com/cloudsir
Date: 2022-03-24 14:41:54
LastEditTime: 2022-03-24 15:18:24
LastEditors: CloudSir
Description: 
'''

import os


class classification(object):
    def __init__(self):
        pass

    def init(self, print_info=True):
        """
        初始化分类器
        Args:
            print_info(bool): 是否打印初始化信息
        Returns:
            None
        """
        if print_info:
            print("分类器正在初始化...")
        import paddlex as pdx
        # 获取当前文件所在目录
        cur_dir = os.path.dirname(os.path.abspath(__file__))
        # 获取模型文件路径
        model_path = os.path.join(cur_dir, 'model')
        
        self.pdx = pdx
        self.model = pdx.load_model(model_path)

        if print_info:
            print("分类器初始化完成！")

 
    def classify(self, *, img, score_threshold=0.5):
        """
        返回手势的类别
        Args:
            img(str/img): 要识别的图片
            score_threshold(float): 最低自信度，超过该自信度的才会认为是已知的手势
        Returns:
            一个整数，表示手势类别，「0-9」分别对应10种手势，「-1」表示未知的手势
        """
        """
        
        """
        result = self.model.predict(img)[0]

        if result['score'] > score_threshold:
            return int(result['category'])
        else:
            return -1

        