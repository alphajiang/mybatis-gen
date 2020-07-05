




class GenRoDs(object) :
    def __init__(self, entity, outDir):
        self.entity = entity
        self.outDir = outDir

    def gen(self) :
        out = self._genImport()
        out = out + self._genClazz()
        self._writeFile(out)
    


    def _genImport(self):
        out = 'package ' + self.entity.packageName + '.ro.' + self.entity.moduleName + '.ds;\r\n\r\n\
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
\tprivate ' + self.entity.clazzName + 'RoMapper ' + self.entity.roMapper() + ';\r\n\r\n\
'    
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
        out = 'package ' + self.entity.packageName + '.rw.' + self.entity.moduleName + '.ds;\r\n\r\n\
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
\tprivate ' + self.entity.clazzName + 'RwMapper ' + self.entity.rwMapper() + ';\r\n\r\n\
'    
        out = out + '\r\n}\r\n'
        return out

    def _writeFile(self, content) :
        fileName = self.outDir + "/rw/" + self.entity.clazzName + "RwDs.java"
        with open(fileName, 'w') as f :
            f.write(content)
