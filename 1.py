import java.io.IOException;
import java.io.InputStream;
import java.util.zip.ZipEntry;
import java.util.zip.ZipFile;

public class JarFileOpener {

    public static void main(String[] args) throws IOException {
        String jarFilePath = "B787X.github.io-";
        String entryName = "spigot-1.19.2.jar"; // 替换为要打开的文件名
        
        ZipFile zipFile = new ZipFile(jarFilePath);
        try {
            ZipEntry entry = zipFile.getEntry(entryName);
            if (entry == null) {
                throw new IllegalArgumentException("Entry not found: " + entryName);
            }
            try (InputStream inputStream = zipFile.getInputStream(entry)) {
                // 在此处读取输入流并进行操作
            }
        } finally {
            zipFile.close();
        }
    }
}
