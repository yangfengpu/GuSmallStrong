

class record:
    def __init__(self):
        self._PN = ""
        self._description = ""


    @property
    def PN(self):
        return self._PN
    
    @property
    def description(self):
        return self._description


    @property
    def supplier(self):
        return self._supplier

    @property
    def inventory(self):
        return self._inventory


    @property
    def inventory(self):
        return self._inventory
        


    @property
    def inventory(self):
        return self._inventory
        


    @property
    def OEM(self):
        return self._OEM
        
 
    @property
    def tags(self):
        return self._tags

    def add_a_tag(tag):
    	self._tags.append(tag)
        


if __name__ == '__main__':
	r = record()
	r.PN = "a"
	r.OEM = "ss"
	r.description = "b"
	r.tags = "s"
	r.add_a_tag = "w"
	print r.PN, r.description, r.OEM, r.tags