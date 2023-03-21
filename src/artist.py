class Artist:
    def __init__(self, name):
        self.name = name
        self.records = []
    
    def get_name(self):
        return self.name
    
    def get_records(self):
        return self.records 
    
    def get_first_record(self):
        min_record = self.records[0]
        for i in self.records:
            if i.year < min_record.year:
                min_record = i 
            return min_record

    

    

     