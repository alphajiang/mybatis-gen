




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
<mapper namespace="' + self.entity.fullRoMapper() + '">\r\n\
</mapper>\r\n'

        return out




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
<mapper namespace="' + self.entity.fullRwMapper() + '">\r\n\
</mapper>\r\n'

        return out




    def _writeFile(self, content) :
        fileName = self.outDir + "/rw/" + self.entity.clazzName + "RwMapper.xml"
        with open(fileName, 'w') as f :
            f.write(content)

