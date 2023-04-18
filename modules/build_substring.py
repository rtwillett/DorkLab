class BuildSubstring:
    def __init__(self):
        pass


    def build_filetype_substring(self, files: list):
    
        # files = data['filetypes']
        ft_append = " OR ".join([f'filetype:{f}' for f in files])
        return f"({ft_append})"


    def build_date_substring(self, date: str, isStartDate: bool):
        
        # start_dt = data["start_date"]
        # end_dt = data["end_date"]
        
        # if start_dt != "" and end_dt != "":
        #     return f'(after:{start_dt} before:{end_dt})'
        # elif start_dt == "" and end_dt != "":
        #     return f'(before:{start_dt})'
        # elif start_dt != "" and end_dt == "":
        #     return f'(after:{start_dt})'
        # elif start_dt == "" and end_dt == "":
        #     return "No date inputs"
        # else: 
        #     print("Default")

        if isStartDate:
            return f'(after:{date})'
        else:
            return f'(before:{date})'



    
    def build_full_string(self, data:dict):
        full_str = ""

        for key in data:

            if key == "root_terms":
                full_str += " ".join(data[key])
            elif key == "start_date":
                full_str += self.build_date_substring(data[key], True)
            elif key == "end_date":
                full_str += self.build_date_substring(data[key], False)
            elif key == "filetypes":
                full_str += self.build_filetype_substring(data[key])
            
            full_str += " "
            


        return full_str

def test():
    print("test")
