# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 20:24:28 2021

@author: 沈
"""
#
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from utils import AnimalUtil
from PIL import Image, ImageTk

#using tkinter to make a visible interface
class Application(tk.Frame):
    def __init__(self,root):
        super().__init__(root)
        self.master = root
        self.pack()
        self.AnimalName = tk.StringVar()
        self.AnimalType = tk.StringVar()
        self.select = tk.StringVar()
        root.minsize(500,145)
        root.minsize(500,145)
        root.title('查询')
        
        self.intWind()
#first button:using name to search for specific animals
    def buttonActive_AnimalFeature(self):
        u=self.AnimalName.get()
        p=self.AnimalType.get()
        tmp = AnimalUtil(u,p)
        data = tmp.GetAnimalFromAPI()
        if data == {}:
          messagebox.showinfo('查询结果','not found')
        else:
          data1 = data['newslist'][0]
          messagebox.showinfo('查询结果','名称:  '+ data1['name'] + 
                            '\n祖籍:  '+data1['nation']+'\n寿命:  '+data1['life']+'\n价格: '+data1['price']+
                            '\n易患病:  '+data1['easyOfDisease']+'\n性格特点: ' +data1['characters']+
                            '\n描述:'+data1['desc']+'\n\n体态特征: '+data1['feature']+'\n\n特点:'+data1['characterFeature']+
                            '\n\n照顾须知:'+data1['careKnowledge']+'\n\n喂养注意:'+data1['feedPoints'])

        return
#Second button: using type to search for animal names
    def buttonActive_AnimalType(self):
        u=self.AnimalName.get()
        p=self.selector.get()
        if p == "猫科" :
            p='0'
        elif p=="犬类" :
            p='1'
        elif p=="爬行类" :
            p='2'
        elif p=="小宠物类" :
            p='3'
        elif p=="水族类" :
            p='4'
        tmp = AnimalUtil(u,p)
        data = tmp.GetTypeFromAPI()
        if data == {}:
            messagebox.showinfo('查询结果','not found')
        else:
            output=[]
            for i in range(len(data['newslist'])):
                if data['newslist'][i]['name']:
                    output.append(data['newslist'][i]['name'])
            messagebox.showinfo('',output)
#other labels and entries
    def intWind(self):
      pass       
if __name__ == '__main__':
    root = tk.Tk()
    application = Application(root=root)
    application.mainloop()