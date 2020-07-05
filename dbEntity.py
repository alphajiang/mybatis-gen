



class DbColumn(object) : 
    def __init__(self, name, type, comment) :
        self.name = name
        self.type = type
        self.comment = comment


    def __str__(self) :
        return "name = " + self.name + ", type = " + self.type + ", comment = " + self.comment

class DbEntity(object) :
    def __init__(self, clazzName, clazzComment, colList):
        self.clazzName = clazzName
        self.clazzComment = clazzComment
        self.colList = colList
        self._packageName = ''
        self._moduleName = ''

        
    def packageName(self, packageName) :
        self._packageName = packageName

    def packageName(self):
        return self._packageName
    
    def moduleName(self, moduleName) :
        self._moduleName = moduleName

    def moduleName(self) :
        return self._moduleName

    def fullPo(self) :
        return self.packageName + '.' + self.moduleName + '.po.' + self.clazzName + 'Po'

    def roMapper(self) :
        return self.clazzName[0].lower() + self.clazzName[1:] + 'RoMapper'

    def fullRoMapper(self) :
        return self.packageName + '.ro.' + self.moduleName + '.mapper.' + self.clazzName + 'RoMapper'


    def rwMapper(self) :
        return self.clazzName[0].lower() + self.clazzName[1:] + 'RwMapper'        

    def fullRwMapper(self):
        return self.packageName + '.rw.' + self.moduleName + '.mapper.' + self.clazzName + 'RwMapper'

    def fullRoDs(self) :
        return self.packageName + '.ro.' + self.moduleName + '.ds.' + self.clazzName + 'RoDs'


    def fullRwDs(self) :
        return self.packageName + '.rw.' + self.moduleName + '.ds.' + self.clazzName + 'RwDs'

    def __str__(self) :
        cols = ""
        for col in self.colList :
            cols += col.__str__()
            cols += "\r\n"
        return "clazzName = " + self.clazzName + ", clazzComment = " + self.clazzComment + ", cols = \r\n" + cols


