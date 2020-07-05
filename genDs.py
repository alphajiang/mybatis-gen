




class GenRoDs(object) :
    def __init__(self, entity, outDir):
        self.entity = entity
        self.outDir = outDir

    def gen(self) :
        out = self._genImport()
        out = out + self._genClazz()
        self._writeFile(out)
    


    def _genImport(self):
        out = 'package ' + self.entity.dsPackage + '.ro.' + self.entity.moduleName + '.ds;\r\n\r\n\
import ' + self.entity.fullPo() + ';\r\n\
import ' + self.entity.fullRoMapper() + ';\r\n\
import lombok.extern.slf4j.Slf4j;\r\n\
import org.springframework.beans.factory.annotation.Autowired;\r\n\
import org.springframework.stereotype.Service;\r\n\
import java.math.BigDecimal;\r\n\
import java.util.Date;\r\n\r\n'

        return out


    def _genClazz(self) :
        out = '@Slf4j\r\n\
@Service\r\n\
public class ' + self.entity.clazzName + 'RoDs {\r\n\r\n\
\t@Autowired\r\n\
\tprivate ' + self.entity.roMapperClazz() + ' ' + self.entity.roMapperProp() + ';\r\n\r\n'
    


        if self.entity.keyCol :
            out = out + '\tpublic ' + self.entity.poClazz() + ' getBy' + self.entity.keyCol.capitalize() + '(\
' + self.entity.getColJavaType(self.entity.keyCol) + ' ' + self.entity.keyCol + ') {\r\n\
\t\treturn this.' + self.entity.roMapperProp() + '.getBy'  + self.entity.keyCol.capitalize() \
    + '(' + self.entity.keyCol + ');\r\n' \
        + '\t}'


        out = out + '\r\n}\r\n'
        return out

    def _writeFile(self, content) :
        fileName = self.outDir + "/ro/" + self.entity.clazzName + "RoDs.java"
        with open(fileName, 'w') as f :
            f.write(content)




class GenRwDs(object) :
    def __init__(self, entity, outDir):
        self.entity = entity
        self.outDir = outDir

    def gen(self) :
        out = self._genImport()
        out = out + self._genClazz()
        self._writeFile(out)
    


    def _genImport(self):
        out = 'package ' + self.entity.dsPackage + '.rw.' + self.entity.moduleName + '.ds;\r\n\r\n\
import ' + self.entity.fullPo() + ';\r\n\
import ' + self.entity.fullRwMapper() + ';\r\n\
import lombok.extern.slf4j.Slf4j;\r\n\
import org.springframework.beans.factory.annotation.Autowired;\r\n\
import org.springframework.stereotype.Service;\r\n\
import java.math.BigDecimal;\r\n\
import java.util.Date;\r\n\r\n'

        return out


    def _genClazz(self) :
        out = '@Slf4j\r\n\
@Service\r\n\
public class ' + self.entity.clazzName + 'RwDs {\r\n\r\n\
\t@Autowired\r\n\
\tprivate ' + self.entity.rwMapperClazz() + ' ' + self.entity.rwMapperProp() + ';\r\n\r\n\
'    

        if self.entity.keyCol :
            out = out + '\tpublic ' + self.entity.poClazz() + ' getBy' + self.entity.keyCol.capitalize() + '(\
' + self.entity.getColJavaType(self.entity.keyCol) + ' ' + self.entity.keyCol + ', boolean lock) {\r\n\
\t\treturn this.' + self.entity.rwMapperProp() + '.getBy'  + self.entity.keyCol.capitalize() \
    + '(' + self.entity.keyCol + ', lock);\r\n' \
        + '\t}\r\n\r\n'

        out = out + self._genFunInsert()
        out = out + self._genFunUpdate()
        out = out + '\r\n}\r\n'
        return out

    def _genFunInsert(self) :
        out = '\tboolean insert' + self.entity.clazzName + '('\
            + self.entity.poClazz() + ' ' + self.entity.poProp() + ') {\r\n'\
            + '\t\treturn this.' + self.entity.rwMapperProp() \
            + '.insert' + self.entity.clazzName + '(' + self.entity.poProp() \
            + ') > 0;\r\n'\
            + '\t}\r\n\r\n'
        return out

    def _genFunUpdate(self) :
        out = '\tboolean update' + self.entity.clazzName + '('\
            + self.entity.poClazz() + ' ' + self.entity.poProp() + ') {\r\n'\
            + '\t\treturn this.' + self.entity.rwMapperProp() \
            + '.update' + self.entity.clazzName + '(' + self.entity.poProp() \
            + ') > 0;\r\n'\
            + '\t}\r\n\r\n'
        return out


    def _writeFile(self, content) :
        fileName = self.outDir + "/rw/" + self.entity.clazzName + "RwDs.java"
        with open(fileName, 'w') as f :
            f.write(content)
