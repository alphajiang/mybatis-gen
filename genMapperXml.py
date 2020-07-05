




class GenRoMapperXml(object) :
    def __init__(self, entity, outDir):
        self.entity = entity
        self.outDir = outDir

    def gen(self) :
        out = self._genXml()
        
        self._writeFile(out)
    


    def _genXml(self):
        out = '<?xml version="1.0" encoding="UTF-8" ?>\r\n\
<!DOCTYPE mapper PUBLIC "-//mybatis.org//DTD Mapper 3.0//EN" "http://mybatis.org/dtd/mybatis-3-mapper.dtd">\r\n\
<mapper namespace="' + self.entity.fullRoMapper() + '">\r\n\r\n'

        out = out + self._genResultMap()
        out = out + self._genFunGeyByKey()
        out = out + '</mapper>\r\n'
        return out

    def _genResultMap(self):
        out = '\t<resultMap id="RESULT_' + self.entity.clazzName.upper() + '_PO" type="'\
            + self.entity.fullPo() + '">\r\n'
        if self.entity.keyCol :
            out = out + '\t\t<id column="' + self.entity.keyCol + '" jdbcType="'\
            + self.entity.getColJdbcType(self.entity.keyCol) + '" property="' + self.entity.keyCol + '" />\r\n'
        for col in self.entity.colList :
            if col.name == self.entity.keyCol :
                continue
            out = out + '\t\t<result column="' + col.name + '" jdbcType="'\
                + col.jdbcType + '" property="' + col.name + '" />\r\n'
        out = out + '\t</resultMap>\r\n\r\n'                
        return out


    def _genFunGeyByKey(self) :
        if self.entity.keyCol :
            
        
            out = '\t<select id="getById"\r\n'\
                + '\t\t\tresultMap="RESULT_' + self.entity.clazzName.upper() + '_PO">\t\n'\
                + '\t\tselect * from ' + self.entity.tableName + ' where '\
                + self.entity.keyCol + ' = #{' + self.entity.keyCol + '}\r\n'\
                + '\t</select>\r\n\r\n'
            return out
        else :
            return ''


    def _writeFile(self, content) :
        fileName = self.outDir + "/ro/" + self.entity.clazzName + "RoMapper.xml"
        with open(fileName, 'w') as f :
            f.write(content)







class GenRwMapperXml(object) :
    def __init__(self, entity, outDir):
        self.entity = entity
        self.outDir = outDir

    def gen(self) :
        out = self._genXml()
        
        self._writeFile(out)
    


    def _genXml(self):
        out = '<?xml version="1.0" encoding="UTF-8" ?>\r\n\
<!DOCTYPE mapper PUBLIC "-//mybatis.org//DTD Mapper 3.0//EN" "http://mybatis.org/dtd/mybatis-3-mapper.dtd">\r\n\
<mapper namespace="' + self.entity.fullRwMapper() + '">\r\n\r\n'



        out = out + self._genResultMap()
        out = out + self._genFunGeyByKey()

        out = out + '</mapper>\r\n'

        return out

    def _genResultMap(self):
        out = '\t<resultMap id="RESULT_' + self.entity.clazzName.upper() + '_PO" type="'\
            + self.entity.fullPo() + '">\r\n'
        if self.entity.keyCol :
            out = out + '\t\t<id column="' + self.entity.keyCol + '" jdbcType="'\
            + self.entity.getColJdbcType(self.entity.keyCol) + '" property="' + self.entity.keyCol + '" />\r\n'
        for col in self.entity.colList :
            if col.name == self.entity.keyCol :
                continue
            out = out + '\t\t<result column="' + col.name + '" jdbcType="'\
                + col.jdbcType + '" property="' + col.name + '" />\r\n'
        out = out + '\t</resultMap>\r\n\r\n'                
        return out

    def _genFunGeyByKey(self) :
        if self.entity.keyCol :
            
        
            out = '\t<select id="getById"\r\n'\
                + '\t\t\tresultMap="RESULT_' + self.entity.clazzName.upper() + '_PO">\t\n'\
                + '\t\tselect * from ' + self.entity.tableName + ' where '\
                + self.entity.keyCol + ' = #{' + self.entity.keyCol + '}\r\n'\
                + '\t\t<if test="lock == true">\r\n'\
                + '\t\t\tfor update\r\n'\
                + '\t\t</if>\r\n'\
                + '\t</select>\r\n\r\n'
            return out
        else :
            return ''

    def _writeFile(self, content) :
        fileName = self.outDir + "/rw/" + self.entity.clazzName + "RwMapper.xml"
        with open(fileName, 'w') as f :
            f.write(content)

