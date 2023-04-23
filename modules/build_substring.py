# import modules.build_substring_yandex
import numpy as np
import pandas as pd
import urllib
import spacy
nlp = spacy.load("en_core_web_lg")

class BuildSubstringGoogle:
    def __init__(self, data: dict):
        self.data = data

        self.q = self.build_full_string()

    def and_logical_substring(self, col)->str:
        '''
        Docstring
        '''
    
        if self.data[col] == '':
            return ''
        else:    
            return " & ".join([f'"{f}"' for f in self.data[col]])

    def or_logical_substring(self, col)->str:
        '''
        Docstring
        '''
    
        if self.data[col] == '' or self.data[col] == []:
            return ''
        else:
            return " | ".join([f'"{f}"' for f in self.data[col]])

    # def build_root_substring(self)->str:
    #     '''
    #     Docstring
    #     '''
    
    #     if self.data['root_terms'] == '':
    #         return ''
    #     else:
    #         return " & ".join([f'"{f}"' for f in self.data['root_terms']])

    # def build_persons_substring(self)->str:

    #     if self.data['persons'] == []:
    #         return ''
    #     else:    
    #         return " & ".join([f'"{f}"' for f in self.data['persons']])

    # def build_persons_substring(self)->str:

    #     if self.data['gpe'] == []:
    #         return ''
    #     else: 
    #         return " & ".join([f'"{f}"' for f in self.data['gpe']])

class BuildSubstringGoogle(BuildSubstring):
    def __init__(self, data: dict):
        self.data = data

        self.q = self.build_full_string()

    def build_filetype_substring(self)->str:
        '''
        Docstring
        '''
    
        if self.data['filetypes'] != None:
            ft_append = " ".join([f'filetype:{f}' for f in self.data['filetypes']])
            return f"{ft_append}"
        else:
            return ''

    def build_site_substring(self)->str:
        '''
        Docstring
        '''
    
        # if self.data['urls'] != None:
        if 'urls' in self.data:
            ft_append = " ".join([f'site:{f}' for f in self.data['urls']])
            return f"{ft_append}"
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

    def build_morewords_substring(self): 
        if self.data["moreterms"]:
            return ' '.join({f'intext:{term}' for term in self.data['moreterms'] if term.strip() != ''})
        else: 
            return ''

    def build_filterwords_substring(self): 
        if self.data["filterwords"]:
            return ' '.join({f'-{term}' for term in self.data['filterwords'] if term.strip() != ''})
        else: 
            return ''

    def build_full_string(self)->str:
        '''
        Docstring
        '''

        import re

        self.fragments = [
            "(" + self.or_logical_substring('persons') + ")",
            "(" + self.or_logical_substring('orgs') + ")",
            "(" + self.or_logical_substring('gpe') + ")"
        ]

        # remove empty strings from the list before joining it
        self.fragments = [list_item for list_item in self.fragments if (list_item.strip() != "") or (list_item.strip() !="()")]

        full_str = ' & '.join(self.fragments) + ' ' +  self.build_morewords_substring() + ' ' + self.build_date_substring() + \
            ' ' + self.build_filetype_substring() + ' ' + self.build_morewords_substring() + ' ' + self.build_filterwords_substring()

        # Removes & with nothing between them, empty parentheses and leading/trailing whitespace
        # This should be revisited to make so that this cleaning is not necessary in the first place
        full_str = re.sub('&\s{0,}&', '', full_str).replace('()', '').strip()

        return full_str


    def build_search_link(self)-> str:
        from urllib.parse import quote
        
        return f"https://www.google.com/search?q={quote(self.q, safe='')}"

    # def build_search_engine_strings(self)-> dict:
        
    #     self.links_dict = {}
        
        
    #     for engine in self.data["search_engines"]:
    #         if engine == "google":
    #             self.links_dict["google"] = self.build_search_link()
    #         elif engine == "yandex":
    #             bsy = BuildStringYandex(self.data)
    #             self.links_dict["yandex"] = bsy.link
        
                
    #     return self.links_dict

class BuildStringYandex(BuildSubstring):
    '''
    https://yandex.com/support/search/query-language/search-context.html
    https://seosly.com/blog/yandex-search-operators/
    '''
    
    def __init__(self, data):
        super().__init__(data)

        self.data = data
        self.link = self.build_search_link()
        
    def and_logical_substring(self, col)->str:
        '''
        Using polymorphism to override the method of the same name in the abstract class
        Yandex uses && or << to match terms in the same document.
        '''
    
        if self.data[col] == '':
            return ''
            
        return " & ".join([f'"{f}"' for f in self.data[col]])
        
    def build_filetype_substring(self)->str:
        '''
        Docstring
        '''
        if len(self.data['filetypes']) > 0:
            ft_append = " | ".join([f'mime:{f}' for f in self.data['filetypes']])
            return f"({ft_append})"
        else:
            return ''
        
    def build_site_substring(self)->str:
        '''
        Docstring
        '''
    
#         if self.data['urls']:
        if 'urls' in self.data:
            ft_append = " | ".join([f'site:{f}' for f in self.data['urls']])
            return f"{ft_append}"
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
            
    def build_full_string(self)->str:
        '''
        Docstring
        '''

        import re

        self.fragments = [
            "(" + self.or_logical_substring('persons') + ")",
            "(" + self.or_logical_substring('orgs') + ")",
            "(" + self.or_logical_substring('gpe') + ")"
        ]

        # remove empty strings from the list before joining it
        self.fragments = [list_item for list_item in self.fragments if (list_item != "") or (list_item !="()")]

        full_str = ' << '.join(self.fragments) + ' ' +  self.build_morewords_substring() + ' ' + self.build_date_substring() + \
            ' ' + self.build_filetype_substring() + ' ' + self.build_morewords_substring() + ' ' + self.build_filterwords_substring()

        # Removes & with nothing between them, empty parentheses and leading/trailing whitespace
        # This should be revisited to make so that this cleaning is not necessary in the first place
        full_str = re.sub('<<\s{0,}<<', '', full_str).replace('()', '').strip()

        return full_str
    
    def build_morewords_substring(self): 
        if self.data["moreterms"]:
            return ' '.join({f'!{term}' for term in self.data['moreterms'] if term.strip() != ''})
        else: 
            return ''

    def build_filterwords_substring(self): 
        if self.data["filterwords"]:
            return ' '.join({f'-{term}' for term in self.data['filterwords'] if term.strip() != ''})
        else: 
            return ''


    def build_search_link(self)-> str:
        from urllib.parse import quote

        return f"https://yandex.com/search/?text={quote(self.q, safe='')}"

class BuildSubstringBing(BuildSubstring):
    def __init__(self, data: dict):
        self.data = data

        self.q = self.build_full_string()

    def build_filetype_substring(self)->str:
        '''
        Docstring
        '''
    
        if self.data['filetypes'] != None:
            ft_append = " ".join([f'filetype:{f}' for f in self.data['filetypes']])
            return f"{ft_append}"
        else:
            return ''

    def build_site_substring(self)->str:
        '''
        Docstring
        '''
    
        # if self.data['urls'] != None:
        if 'urls' in self.data:
            ft_append = " ".join([f'site:{f}' for f in self.data['urls']])
            return f"{ft_append}"
        else:
            return ''


#     def build_date_substring(self)->str:
#         '''
#         Docstring
#         '''
        
#         if self.data["start_date"]: start_dt = self.data["start_date"]
#         else: start_dt = ""

#         if self.data["end_date"]: end_dt = self.data["end_date"]
#         else: end_dt = ""

        
#         if start_dt != "" and end_dt != "":
#             return f'after:{start_dt} & before:{end_dt}'
#         elif start_dt == "" and end_dt != "":
#             return f'before:{start_dt}'
#         elif start_dt != "" and end_dt == "":
#             return f'after:{start_dt}'
#         elif start_dt == "" and end_dt == "":
#             return ""
#         else: 
#             print("What is this even?")

    def build_morewords_substring(self): 
        if self.data["moreterms"]:
            return ' '.join({f'inbody:{term}' for term in self.data['moreterms'] if term.strip() != ''})
        else: 
            return ''

    def build_filterwords_substring(self): 
        if self.data["filterwords"]:
            return ' '.join({f'-{term}' for term in self.data['filterwords'] if term.strip() != ''})
        else: 
            return ''

    def build_full_string(self)->str:
        '''
        Docstring
        '''

        import re

        self.fragments = [
            "(" + self.or_logical_substring('persons') + ")",
            "(" + self.or_logical_substring('orgs') + ")",
            "(" + self.or_logical_substring('gpe') + ")"
        ]

        # remove empty strings from the list before joining it
        self.fragments = [list_item for list_item in self.fragments if (list_item.strip() != "") or (list_item.strip() !="()")]

        full_str = ' & '.join(self.fragments) + ' ' +  self.build_morewords_substring() + ' ' + \
            ' ' + self.build_filetype_substring() + ' ' + self.build_morewords_substring() + ' ' + self.build_filterwords_substring()

        # Removes & with nothing between them, empty parentheses and leading/trailing whitespace
        # This should be revisited to make so that this cleaning is not necessary in the first place
        full_str = re.sub('&\s{0,}&', '', full_str).replace('()', '').strip()

        return full_str


    def build_search_link(self)-> str:
        from urllib.parse import quote
        
        return f"https://www.bing.com/search?q={quote(self.q, safe='')}"

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
        self.extract_gpe()
        self.extract_date()
        self.extract_urls()
        self.extract_filetypes()
            
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

    def extract_gpe(self):
        self.data['gpe'] = self.entities.loc[self.entities.entity == 'GPE'].name.tolist()

    def extract_filetypes(self):
        import re
        self.data['filetypes'] = re.findall('pdf|txt| doc[x]{0,1}|json', self.text)
    
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

