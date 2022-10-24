# from asyncore import read
# from encodings import utf_8
from ast import Break
from calendar import FRIDAY, MONDAY, SATURDAY, THURSDAY, TUESDAY, WEDNESDAY
import requests as req
from bs4 import BeautifulSoup as BS
import pandas as pd
import numpy as np
from fake_useragent import UserAgent
import json


useragent = UserAgent()
headers = {'Uset-Agent':
            f'{useragent.random}'
        }


def get_link():
    url = 'https://www.oksei.ru/studentu/raspisanie_uchebnykh_zanyatij'

    response = req.get(url=url, headers=headers)

    soup = BS(response.text, 'lxml')

    link = soup.find_all('a')

    for i in link:
        if i.text == 'Расписание занятий на нижнюю неделю' or i.text == 'Расписание учебных занятий на верхнюю неделю':
            a = i.get('href')
            link_excel = 'https://www.oksei.ru' + a
            return link_excel
        else:
            continue


def array(link_excel):
    r = req.get(link_excel)
    with open('excel.xlsx', 'wb') as f:
        f.write(r.content)

def alfabet_def():
    alfabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    alfabet_2b = []


    for i in alfabet:
        for z in alfabet:
            alfabet_2b.append(i + z)
    
    alfabet_twice = alfabet + alfabet_2b
    return alfabet_twice

def open_excel():
    array(get_link())
    list_group = []
    for i in alfabet_def():
        # print(i)

        if i == 'BK':
            break
        if i != 'A' and i != 'B':
            data = pd.read_excel(r'C:\Users\koooo\Desktop\проект по допам\excel.xlsx', usecols=f'{i}')
            df = pd.DataFrame(data)
            list_subject = df.values.tolist()
            new_list_subject = []
            for i in list_subject:
                for z in i:
                    new_list_subject.append(z)

                

            MONDAY = {
                1 : new_list_subject[4],
                2 : new_list_subject[5],
                3 : new_list_subject[6],
                4 : new_list_subject[7],
                5 : new_list_subject[8],
                6 : new_list_subject[9]
            }
            TUESDAY= {
                1 : new_list_subject[10],
                2 : new_list_subject[11],
                3 : new_list_subject[12],
                4 : new_list_subject[13],
                5 : new_list_subject[14],
                6 : new_list_subject[15]
            }
            WEDNESDAY = {
                1 : new_list_subject[16],
                2 : new_list_subject[17],
                3 : new_list_subject[18],
                4 : new_list_subject[19],
                5 : new_list_subject[20],
                6 : new_list_subject[21]
            }
            THURSDAY = {
                1 : new_list_subject[22],
                2 : new_list_subject[23],
                3 : new_list_subject[24],
                4 : new_list_subject[25],
                5 : new_list_subject[26],
                6 : new_list_subject[27]
            }
            FRIDAY= {
                1 : new_list_subject[28],
                2 : new_list_subject[29],
                3 : new_list_subject[30],
                4 : new_list_subject[31],
                5 : new_list_subject[32],
                6 : new_list_subject[33]
            }
            SATURDAY = {
                1 : new_list_subject[34],
                2 : new_list_subject[35],
                3 : new_list_subject[36],
                4 : new_list_subject[37],
                5 : new_list_subject[38],
                6 : new_list_subject[39]
            }
                
            object_group = {
                'Группа' : new_list_subject[3],
                'Понедельник': MONDAY,
                'Вторник' : TUESDAY,
                'Среда' : WEDNESDAY,
                'Четверг' : THURSDAY,
                'Пятница' : FRIDAY,
                'Суббота' : SATURDAY
            }
            list_group.append(object_group)
   
        else:
            continue
        # print(list_group)
    answer = input('Введите название группы ')
    for group in list_group:
        if answer == group['Группа']:
            # print(group)
            jsonStr = json.dumps(group,
                                sort_keys=False,
                                indent=4,
                                ensure_ascii=False,
                                separators=(',', ': '))
            print(jsonStr)
        else:
            continue
            
           

open_excel()








    # for i in alfabet_def():
    #     if i != 'BK':
    #         new_list_subject = []
    #         data = pd.read_excel(r'C:\Users\koooo\Desktop\проект по допам\excel.xlsx', usecols=f'{i}')
    #         df = pd.DataFrame(data)
    #         for i in df:
    #             new_list_subject.append(i)
    #         print(new_list_subject)
    #     else:
    #         break