# import modules.build_substring_yandex
import numpy as np
import pandas as pd
import urllib
import spacy
nlp = spacy.load("en_core_web_lg")

class BuildSubstring:
    def __init__(self, data: dict):
        self.data = data

        self.q = self.build_full_string()

    # def build_date_substring_(self, data: dict)->str:

    #     if self.data['start_date'] != '':

    def build_root_substring(self)->str:
        '''
        Docstring
        '''
    
        if self.data['root_terms'] == '':
            return ''
            
        return " & ".join([f'"{f}"' for f in self.data['root_terms']])


    def build_filetype_substring(self)->str:
        '''
        Docstring
        '''
    
        if self.data['filetypes'] != None:
            ft_append = " | ".join([f'filetype:{f}' for f in self.data['filetypes']])
            return f"({ft_append})"
        else:
            return ''


    def build_date_substring(self)->str:
        '''
        Docstring
        '''
        
        if self.data["start_date"]: start_dt = self.data["start_date"]
        else: start_dt = ""

        if self.data["end_date"]: end_dt = self.data["end_date"]
        else: end_dt = ""

        
        if start_dt != "" and end_dt != "":
            return f'after:{start_dt} & before:{end_dt}'
        elif start_dt == "" and end_dt != "":
            return f'before:{start_dt}'
        elif start_dt != "" and end_dt == "":
            return f'after:{start_dt}'
        elif start_dt == "" and end_dt == "":
            return ""
        else: 
            print("What is this even?")



    def build_full_string(self)->str:
        '''
        Docstring
        '''

        self.fragments = [
            self.build_root_substring(),
            self.build_date_substring(),
            self.build_filetype_substring()
        ]

        full_str = ' & '.join(self.fragments)
        return full_str


    def build_search_link(self)-> str:
        return f"https://www.google.com/search?q={urllib.parse.quote(self.q, safe='')}"

        return full_str

    def build_search_engine_strings(self)-> dict:
        
        print(self.data)
        res = {}
        
        
        for engine in self.data["search_engines"]:
            if engine == "google":
                res["google"] = self.build_date_substring()
            elif engine == "yandex":
                bsy = modules.build_substring_yandex.BuildStringYandex(self.data)
                res["yandex"] = bsy.q
                
        return res

import modules.build_substring

class BuildStringYandex(BuildSubstring):
    
    def __init__(self, data):
        super().__init__(data)

        self.data = data
        self.q = self.build_full_string()
        
        
    def build_filetype_substring(self)->str:
        '''
        Docstring
        '''
        if len(self.data['filetypes']) > 0:
            ft_append = " | ".join([f'mime:{f}' for f in self.data['filetypes']])
            return f"({ft_append})"
        else:
            return ''
        
    def build_date_substring(self)->str:
        '''
        Docstring
        '''
        start_dt = self.data["start_date"].replace('-', '') # consider doing this with concatenation
        end_dt = self.data["end_date"].replace('-', '')
        
        if start_dt != "" and end_dt != "":
            return f'date:{start_dt}..{end_dt}'
        elif start_dt == "" and end_dt != "":
            return f'(date:<{start_dt})'
        elif start_dt != "" and end_dt == "":
            return f'(date:>{start_dt})'
        elif start_dt == "" and end_dt == "":
            return ""
        else: 
            print("If this is printed, something went wrong")
class NERDString:
    
    def __init__(self, text:str, nlp = nlp):
        
        # self.nlp = spacy.load("en_core_web_lg")
    
        # text = text.upper()
        
        self.data = dict()

        self.nlp = nlp
        
        self.text = text

        self.doc = self.nlp(text)
        
        self.extract_ner()

        self.ner_extracts = dict()
#         for ent in self.entities.entity.unique():
#             # print(ent)
#             self.ner_extracts[ent] = self.summarize_entity_type(ent)

        self.extract_persons()
        self.extract_orgs()
        self.extract_date()
        self.extract_urls()
            
    def extract_ner(self):
        ner_tuplist = []
        for ent in self.doc.ents:
            ner_tuplist.append((ent.text, ent.label_))
            
        self.entities = pd.DataFrame(ner_tuplist, columns = ['name', 'entity'])
        
    def summarize_entity_type(self, entity_type:str):
        df_counts = pd.DataFrame(self.entities.loc[self.entities.entity == entity_type].groupby(['name', 'entity'])['name'].count())
        # t.reset_index()
        df_counts.columns = ['counts']
        df_counts.reset_index()
        df_counts = df_counts.sort_values('counts', ascending=False)
        df_counts.reset_index(inplace=True)
        df_counts.reset_index(drop=True, inplace=True)
        return df_counts[['name', 'counts']]
    
    def extract_persons(self):
        self.data['persons'] = self.entities.loc[self.entities.entity == 'PERSON'].name.tolist()
        
    def extract_orgs(self):
        self.data['orgs'] = self.entities.loc[self.entities.entity == 'ORG'].name.tolist()
    
    def extract_date(self):
        import re

        dates_df = self.entities.loc[self.entities.entity == 'DATE']

        date_series = dates_df.name.apply(lambda x: pd.to_datetime(re.sub('[A-Z]', '', x.upper())))
        min_date_dt = date_series.min()
        max_date_dt = date_series.max()

        min_date = str(min_date_dt).split()[0]
        max_date = str(max_date_dt).split()[0]

        if min_date != 'nan':
            self.data['min_date'] = min_date
        else:
            self.data['min_date'] = ""

        if max_date != 'nan':
            self.data['max_date'] = max_date
        else: 
            self.data['max_date'] = ""

#         return (f'Min date: {min_date}\nMax date: {max_date}')

    def extract_urls(self):
        import re
        self.data['urls'] = [i for i in self.text.split() if ('.' in i) and ('@' not in i) and (not re.search('\.$', i))]
