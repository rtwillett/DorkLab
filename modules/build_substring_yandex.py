import modules.build_substring

class BuildStringYandex(modules.build_substring.BuildSubstring):
    
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

        