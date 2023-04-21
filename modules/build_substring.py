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
            return f'(before:{start_dt})'
        elif start_dt != "" and end_dt == "":
            return f'(after:{start_dt})'
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


    def build_search_engine_strings(self)-> dict:
        
        res = {}
        
        
        for engine in self.data["search_engines"]:
            if engine == "google":
                res["google"] = self.q
            elif engine == "yandex":
                res["yandex"] = BuildStringYandex(self.data).q
                
        return res

