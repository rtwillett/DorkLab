class BuildSubstring:
    def __init__(self):
        pass


    def build_filetype_substring(self, data: dict):
    
        files = data['filetypes']
        ft_append = " OR ".join([f'filetype:{f}' for f in files])
        return f"({ft_append})"


    def build_date_substring(self, data: dict):
        
        start_dt = data["start_date"]
        end_dt = data_dict["end_date"]
        
        if start_dt != "" and end_dt != "":
            return f'(after:{start_dt} before:{end_dt})'
        elif start_dt == "" and end_dt != "":
            return f'(before:{start_dt})'
        elif start_dt != "" and end_dt == "":
            return f'(after:{start_dt})'
        elif start_dt == "" and end_dt == "":
            return "No date inputs"
        else: 
            print("Default")

    
    def build_full_string(self, data:dict):

        return f'{build_filetype_substring(data_dict)} {build_date_substring(data_dict)}'
