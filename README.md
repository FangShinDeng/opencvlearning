# 今天讓我們來學習opencv吧!
    學習參考: https://medium.com/@airwaves/opencv-%E5%9C%A8windows%E4%B8%AD%E5%AE%89%E8%A3%9D-opencv-python-295ae092ca57

## 虛擬環境參考教學影片
    影片連結: https://www.youtube.com/watch?v=Y9JMfWAr_04

## 虛擬環境搭建練習
    先進行安裝虛擬環境的套件
    pip install virtualenv

    安裝完畢後創建一個虛擬環境
    virtualenv venv

    啟動虛擬環境
    source venv/Scripts/activate
    
    查看虛擬環境的套件
    pip list

    退出虛擬環境
    deactivate

## 虛擬環境的導出跟安裝! 
    開發完一個項目時，整個開發的包使用了很多不同的套件，如果別人也要使用，也當然要安裝那些包，但要如何讓別人知道這個開發項目用了哪些套件呢?
    
    使用指令: pip freeze > requirement.txt
    然後我們去查看這個requirement.txt的檔案，就可以得知我們這個環境所安裝的所有套件及版本了！
    
    再來我們創建一個新的虛擬環境叫mydev，然後使用以下指令來把venv的套件給安裝到mydev上，要記得先進到mydev的目錄才可以執行安裝套件的指令哦
    pip install -r requirement.txt
    指令-r的教學參考: https://www.twle.cn/t/85

## 學會了虛擬環境，再來搭建opencv吧!
    官方安裝連結: 官方安裝連結: https://pypi.org/project/opencv-python/
    
    進到了mydev後，我們進行以下指令來安裝opencv
    pip install opencv-python

## 圖形辨識安裝
    官方安裝連結: https://pypi.org/project/Pillow/
    pip install Pillow
    
    官方安裝連結: https://pypi.org/project/matplotlib/
    pip install matplotlib


## 驗證碼破解
    參考教學影片: https://www.youtube.com/watch?v=KESG8I9C3oA&list=PLohb4k71XnPaQRTvKW4Uii1oq-JPGpwWF&index=24
    
    一般思路
    驗證碼識別的一般思路為：
    1、圖片降噪
    2、圖片切割
    3、圖像文本輸出
    3.1 圖片降噪
    原文網址：https://kknews.cc/tech/ag98qvj.html