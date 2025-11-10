class DictHash():
    def __init__(self):
        #Vi använder en inbyggds dictionary som lagringsstruktur
        self._data = {}
    def store(self,nyckel, data):
        """Lagrar datan i en dictionary med nyckel som key"""
        self._data[nyckel] = data
    def search(self,nyckel):
        """Retunerar datat som hör till nyckeln, eller None om den inte finns"""
        return self._data.get(nyckel,None)
    def __getitem__(self,nyckel):
        """Gör så att man kan  """
        return self.search(nyckel)
    def __contains__(self,nyckel):
        """Gör så att man kan skriva 'if nyckel in d' """
        return nyckel in self._data


