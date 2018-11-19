# print("Hello, World!")
import subprocess
# subprocess.Popen("cwm --rdf test.rdf --ntriples > test.nt")
subprocess.Popen("pwd")
# subprocess.run('foo=bar', shell=True)
subprocess.run('tesseract scan1.jpg out -l spa', shell=True)
# subprocess.Popen("tesseract scan1.jpg out")
subprocess.run('cat out.txt', shell=True)



