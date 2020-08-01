import time
from multiprocessing import Process

import requests

import numpy as np
import pandas as pd
from bs4 import BeautifulSoup

import database as db1        # for pymysql coonection
import datetime


class UniversityMiner:

    def __init__(self):
        self.base_url = "https://www.ugc.ac.in"

    def central(self):
        url = self.base_url + "/centraluniversity.aspx"
        

        html_content = requests.get(url).text
        soup = BeautifulSoup(html_content, "lxml")
        soup.prettify

        table_data = soup.find('td')
        state_names = table_data.find_all('a')

        # States names in central university page
        state_links = {}   # dict for states and website links

        for i in state_names:
            state_links[i.text.strip()] = (self.base_url + '/' + i['href'])

        # Websites url for all states in central university data
        urls = []
        for i in state_links.values():
            urls.append(i)

        data_list = []

        for i in range(0, int(len(urls))):
            html2 = requests.get(urls[i]).text
            soup_1 = BeautifulSoup(html2, 'lxml')
            soup_1.prettify()

            soup_2 = soup_1.findAll('td')
            for j in soup_2:
                text = j.find('b').text
                text = " ".join(text.split())
                data_list.append(text)
                name1 = j.findAll('div', {'class': 'box200'})
                for name in name1:
                    name = name.text
                    name = " ".join(name.split())
                    data_list.append(name)
                data_list.append("Central University")

        data_list = np.reshape(data_list, (int(len(data_list)/4), 4))
        central_df = pd.DataFrame(
            data_list, columns=['UniversityName', 'Address', 'State', 'Type'])

        return central_df

    def state(self):
        html_content = requests.get(
            self.base_url + '/stateuniversity.aspx').text
        soup = BeautifulSoup(html_content, "lxml")
        soup.prettify

        states = []
        table = soup.findAll('td')

        for i in table:
            states.append(i.find('a'))

        data2 = []
        for i in states:
            if i != None:
                data2.append(i)

        # States names in states university page
        states_links = {}   # dict for states and website links

        for i in data2:
            states_links[i.text.strip()] = (self.base_url + '/' + i['href'])

        # Websites url for all states in state university data
        web_urls = []
        for i in states_links.values():
            web_urls.append(i)

        data_list1 = []

        for i in range(0, int(len(web_urls))):
            html2 = requests.get(web_urls[i]).text
            soup_1 = BeautifulSoup(html2, 'lxml')
            soup_1.prettify()

            soup_2 = soup_1.findAll('td')
            for j in soup_2:
                text = j.find('b').text
                text = " ".join(text.split())
                data_list1.append(text)
                name1 = j.findAll('div', {'class': 'box200'})
                for name in name1:
                    name = name.text
                    name = " ".join(name.split())
                    data_list1.append(name)
                data_list1.append("State university")

        data_list1 = np.reshape(data_list1, (int(len(data_list1)/4), 4))
        state_df = pd.DataFrame(data_list1, columns=[
                                'UniversityName', 'Address', 'State', 'Type'])

        return state_df

    def deemed(self):
        html_content_1 = requests.get(
            self.base_url + '/deemeduniversity.aspx').text
        deemed_soup = BeautifulSoup(html_content_1, "lxml")
        deemed_soup.prettify

        deemed_states = []
        deemed = deemed_soup.findAll('td')

        for i in deemed:
            deemed_states.append(i.find('a'))

        data4 = []
        for i in deemed_states:
            if i != None:
                data4.append(i)
        data4.pop(0)

        # States names in deemed university page
        states_links = {}   # dict for states and website links

        for i in data4:
            states_links[i.text.strip()] = (self.base_url + '/' + i['href'])

        # Websites url for all states in state university data
        web_urls = []
        for i in states_links.values():
            web_urls.append(i)

        deemed_list = []

        for i in range(0, int(len(web_urls))):
            html2 = requests.get(web_urls[i]).text
            soup_1 = BeautifulSoup(html2, 'lxml')
            soup_1.prettify()

            soup_2 = soup_1.findAll('td')
            for j in soup_2:
                text = j.find('b').text
                text = " ".join(text.split())
                deemed_list.append(text)
                name1 = j.findAll('div', {'class': 'box200'})
                for name in name1:
                    name = name.text
                    name = " ".join(name.split())
                    deemed_list.append(name)
                deemed_list.append("Deemed University")

        deemed_list = np.reshape(deemed_list, (int(len(deemed_list)/4), 4))
        deemed_df = pd.DataFrame(deemed_list, columns=['UniversityName', 'Address', 'State', 'Type'])

        return deemed_df

    def state_private(self):
        html_content_1 = requests.get(
            self.base_url + '/privatuniversity.aspx').text
        private_soup = BeautifulSoup(html_content_1, "lxml")
        private_soup.prettify

        private_states = []
        private = private_soup.findAll('td')
        private
        for i in private:
            private_states.append(i.find('a'))

        private_data = []
        for i in private_states:
            if i != None:
                private_data.append(i)

        states_links = {}   # dict for states and website links

        for i in private_data:
            states_links[i.text.strip()] = (self.base_url + '/' + i['href'])

        web_urls = []
        for i in states_links.values():
            web_urls.append(i)

        state_name = []
        for i in states_links:
            state_name.append(i)

        data = []
        for k in range(0, len(web_urls)):
            html2 = requests.get(web_urls[k]).text
            soup_1 = BeautifulSoup(html2, 'lxml')
            soup_1
            soup_2 = soup_1.findAll('td')

            links = []

            for i in soup_2:
                text = i.find_all('a', string='More Details...')
                for j in text:
                    links.append(self.base_url + '/'+j['href'])

            for i in range(0, len(links)):
                html = requests.get(links[i]).text
                data_soup = BeautifulSoup(html, 'lxml')
                data_soup.prettify

                data_soup1 = data_soup.findAll('font')

                j = 0
                for i in data_soup1:
                    if j == 2:
                        data.append(state_name[k])
                        break
                    data.append(i.text)
                    j = j+1
                data.append("State Private University")

        data = np.reshape(data, (int(len(data)/4), 4))

        state_private_df = pd.DataFrame(
            data,  columns=['UniversityName', 'Address', 'State', 'Type'])

        return state_private_df

    def getUniversitiesDF(self):
        dataframe = [miner.central(), miner.state(), miner.deemed(), miner.state_private()]
        # dataframe = [miner.central()]
        whole_data = pd.concat( dataframe, ignore_index = True )
        return whole_data


if __name__ == "__main__":
    miner = UniversityMiner()
    df = miner.getUniversitiesDF()
    df.to_csv('university.csv')
    data = pd.read_csv('university.csv')
    

# pymysql connection
    db1.delete_data()
    db1.append_data(df)
    