from zipfile import ZipFile
import sys
import os
import argparse

class UnZipHelper:
    """
       Helper to unzip the Django Project Template (https://github.com/apressato/Django-Project-Template/tree/master) 
       cleaning end fixing some info to adjust the template to your project info.
    """
    def __init__(self, **kwargs):
        self.parser = argparse.ArgumentParser(prog=__name__)
        self.parser.add_argument("-f", "--file", help = "Zip File to extract")
        self.parser.add_argument("-o", "--outdir", default = "", help = "Destination Folder")
        self.parser.add_argument("-p", "--projectname", help = "Django Project Name")
        self.parser.add_argument("-m", "--mainproject", action = "store_false", help = "Django Project Template Archive")
        self.options = self.parser.parse_args()
    
    def Extract(self):
        if self.options.outdir != "":
            destfolder = self.options.outdir
        else:
            destfolder = os.getcwd()

        with ZipFile(self.options.file, "r") as zObject:
            zObject.infolist()
            for file in zObject.infolist():
               splitted = file.filename.split("/")
               pathlist = splitted[1:-1]
               
               if splitted[-1] != "":
                   dpath = destfolder
                   if "DjangoProjectTemplate" in splitted: 
                       if splitted[-1] not in ["wsgi.py", "asgi.py"]:
                           pathlist = [self.options.projectname]
                       
                   for path in pathlist:
                       dpath = os.path.join(dpath, path)
                       
                   if "DjangoProjectTemplate" not in dpath:
                       if not os.path.exists(dpath):
                           os.makedirs(dpath)
                           
                   dpath = os.path.join(dpath, splitted[-1])
                   
                   if splitted[-1] in ["wsgi.py", "asgi.py", "manage.py"]:
                       pass
                   elif (splitted[-1] == "README.md") and ("Django-Project-Template-master" in splitted):
                       with open(dpath, "w") as target:
                           target.write(f"# {self.options.projectname}")
                   else:
                       print(f"{file.filename}")
                       with open(dpath, "wb") as target:
                           target.write(zObject.open(file).read())
                       
                       if (self.options.projectname is not None) and (self.options.projectname in dpath): 
                           if ("urls.py" in dpath) or ("settings.py" in dpath):
                              with open(dpath, "r") as source:
                                  file_content = source.read().replace("DjangoProjectTemplate", self.options.projectname)
                              with open(dpath, "w") as target:
                                  target.write(file_content)
                              print(f"{dpath} Fixed")
           
           
if __name__ == '__main__':
    rc = 1
    try:
        unzip_helper = UnZipHelper()
        unzip_helper.Extract()
        rc = 0
    except Exception as ex:
        print(f"Error: {ex}", file=sys.stderr)
    sys.exit(rc)