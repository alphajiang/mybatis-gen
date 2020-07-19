



class DbColumn(object) : 
    def __init__(self, name, javaType, jdbcType, comment, nullable, maxLen) :
        self.name = name
        self.javaType = javaType
        self.jdbcType = jdbcType
        self.comment = comment
        self.nullable = nullable
        self.maxLen = maxLen


    def __str__(self) :
        return "name = " + self.name + ", javaType = " + self.javaType + ", comment = " + self.comment \
            + ', nullable = ' + str(self.nullable) + ", maxLen = " + str(self.maxLen)

class DbEntity(object) :
    def __init__(self, tableName, clazzName, clazzComment, keyCol, colList):
        self.tableName = tableName
        self.clazzName = clazzName
        self.clazzComment = clazzComment
        self.keyCol = keyCol
        self.colList = colList
        self._packageName = ''
        self._moduleName = ''
        self._modelPackage = ''
        self._dsPackage = ''

        
    def packageName(self, packageName) :
        self._packageName = packageName

    def packageName(self):
        return self._packageName
    
    def moduleName(self, moduleName) :
        self._moduleName = moduleName

    def moduleName(self) :
        return self._moduleName

    def modelPackage(self, modelPackage) :
        self._modelPackage = modelPackage

    def modelPackage(self) :
        return self._modelPackage

    def dsPackage(self, dsPackage) :
        self._dsPackage = dsPackage

    def dsPackage(self) :
        return self._dsPackage
        

    def poClazz(self) :
        return self.clazzName + 'Po'

    def poProp(self) :
        return self.clazzName[0].lower() + self.clazzName[1:] + 'Po'

    def fullPo(self) :
        return self.modelPackage + '.' + self.moduleName + '.po.' + self.clazzName + 'Po'

    
    def roMapperClazz(self) :
        return self.clazzName + 'RoMapper'

    def roMapperProp(self) :
        return self.clazzName[0].lower() + self.clazzName[1:] + 'RoMapper'

    def fullRoMapper(self) :
        return self.dsPackage + '.ro.' + self.moduleName + '.mapper.' + self.clazzName + 'RoMapper'

    def rwMapperClazz(self) :
        return self.clazzName + 'RwMapper'

    def rwMapperProp(self) :
        return self.clazzName[0].lower() + self.clazzName[1:] + 'RwMapper'        

    def fullRwMapper(self):
        return self.dsPackage + '.rw.' + self.moduleName + '.mapper.' + self.clazzName + 'RwMapper'

    def fullRoDs(self) :
        return self.packageName + '.ro.' + self.moduleName + '.ds.' + self.clazzName + 'RoDs'


    def fullRwDs(self) :
        return self.packageName + '.rw.' + self.moduleName + '.ds.' + self.clazzName + 'RwDs'


    def getColJavaType(self, colName) :
        for col in self.colList :
            if col.name == colName :
                return col.javaType
                        
        return 'TypeNotFound'


    def getColJdbcType(self, colName) :
        for col in self.colList :
            if col.name == colName :
                return col.jdbcType
                        
        return 'TypeNotFound'

    def __str__(self) :
        cols = ""
        for col in self.colList :
            cols += col.__str__()
            cols += "\r\n"
        #return "tableName = " + self.tableName
        return "clazzName = " + self.clazzName + ", clazzComment = " + self.clazzComment + " keyCol = " + str(self.keyCol) + ", cols = \r\n" + cols


