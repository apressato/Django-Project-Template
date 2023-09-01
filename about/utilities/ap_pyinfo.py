#   This file is part of APUtils.
#   APUtils is a porting with addictions of my Embarcadero Delphi APUtils package
#   made by APressato <apressato@gmail.com> in 2018 - 2023.
#
#   APUtils is free software: you can redistribute it and/or modify
#   it under the terms of the
#   Creative Commons Attribution ShareAlike 4.0 International
#   as published by Creative Commons.
#
#   APUtils is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   Creative Commons Attribution ShareAlike 4.0 International for more details.
#
#   You should have received a copy of the
#   Creative Commons Attribution ShareAlike 4.0 International
#   along with APUtils. If not,
#   see <https://creativecommons.org/licenses/by-sa/4.0/legalcode>.


import os
import sys
import platform
import html
import json
from pip._internal.operations.freeze import freeze


class pyInfo():
    def __init__(self, **kwargs):
        self.pyInfoDict = {}

        optional_modules_list = [
            'Cookie',
            'zlib', 'gzip', 'bz2', 'zipfile', 'tarfile',
            'ldap',
            'socket',
            'audioop', 'curses', 'imageop', 'aifc', 'sunau', 'wave', 'chunk', 'colorsys', 'rgbimg', 'imghdr', 'sndhdr',
            'ossaudiodev', 'sunaudiodev',
            'adodbapi', 'cx_Oracle', 'ibm_db', 'mxODBC', 'MySQLdb', 'pgdb', 'PyDO', 'sapdbapi', 'sqlite3', 'pymongo'
        ]

        for i in optional_modules_list:
            try:
                module = __import__(i)
                sys.modules[i] = module
                globals()[i] = module
            except:
                pass

    @staticmethod
    def _is_imported(module):
        if module in sys.modules:
            return 'enabled'
        return 'disabled'

    def _collect_info(self):
        self.pyInfoDict = {}
        self._system_section()
        self._py_internals_session()
        self._os_internals_session()
        self._environ_session()
        self._database_session()
        self._compression_session()

        if 'ldap' in sys.modules:
            self._ldap_session()

        if 'socket' in sys.modules:
            self._socket_session()

        self._multimedia_session()
        self._copyright_session()

    def _system_section(self):
        system = {
            'OS Version': f'{platform.platform()} ({platform.system()} {platform.release()})'
        }
        if hasattr(os, 'path'):
            system['OS Path'] = os.environ['PATH'].split(';')
        if hasattr(sys, 'version'):
            system['Python Version'] = ''.join(sys.version)
        if hasattr(sys, 'subversion'):
            system['Python Subversion'] = ', '.join(sys.subversion)
        if hasattr(sys, 'path'):
            system['Python Path'] = sys.path
        if hasattr(sys, 'path_importer_cache'):
            system['Import Path'] = [x for x in sys.path_importer_cache]
        if hasattr(sys, 'executable'):
            system['Python Interpreter'] = sys.executable
        system['Build Date'] = platform.python_build()[1]
        system['Compiler'] = platform.python_compiler()
        if hasattr(sys, 'api_version'):
            system['Python API'] = sys.api_version
        system['Unbuffered'] = os.environ.get('PYTHONUNBUFFERED') == "1"

        self.pyInfoDict['System'] = system

    def _py_internals_session(self):
        Internals = {}
        if hasattr(sys, 'builtin_module_names'):
            Internals['Built-in Modules'] = ', '.join(sys.builtin_module_names)
            Internals['Byte Order'] = sys.byteorder + ' endian'
        if hasattr(sys, 'getswitchinterval'):
            Internals['Check Interval'] = sys.getswitchinterval()
        if hasattr(sys, 'getfilesystemencoding'):
            Internals['File System Encoding'] = sys.getfilesystemencoding()
            Internals['Maximum Integer Size'] = str(sys.maxsize) + ' (%s)' % str(hex(sys.maxsize)).upper().replace("X",
                                                                                                                   "x")
        if hasattr(sys, 'getrecursionlimit'):
            Internals['Maximum Recursion Depth'] = sys.getrecursionlimit()
        if hasattr(sys, 'tracebacklimit'):
            Internals['Maximum Traceback Limit'] = str(sys.tracebacklimit)
        else:
            Internals['Maximum Traceback Limit'] = '1000'
            Internals['Maximum Unicode Code Point'] = sys.maxunicode

        self.pyInfoDict['Python Internals'] = Internals

    def _os_internals_session(self):
        data = {}
        if hasattr(os, 'getcwd'):
            data['Current Working Directory'] = os.getcwd()
        if hasattr(os, 'getegid'):
            data['Effective Group ID'] = os.getegid()
        if hasattr(os, 'geteuid'):
            data['Effective User ID'] = os.geteuid()
        if hasattr(os, 'getgid'):
            data['Group ID'] = os.getgid()
        if hasattr(os, 'getgroups'):
            data['Group Membership'] = ', '.join(map(str, os.getgroups()))
        if hasattr(os, 'linesep'):
            data['Line Seperator'] = repr(os.linesep)[1:-1]
        if hasattr(os, 'getloadavg'):
            data['Load Average'] = ', '.join(map(str, map(lambda x: round(x, 2), os.getloadavg())))
        if hasattr(os, 'pathsep'):
            data['Path Seperator'] = os.pathsep
        try:
            if hasattr(os, 'getpid') and hasattr(os, 'getppid'):
                data['Process ID'] = ('%s (parent: %s)' % (os.getpid(), os.getppid()))
        except:
            pass
        if hasattr(os, 'getuid'):
            data['User ID'] = os.getuid()

        self.pyInfoDict['OS Internals'] = data

    def _environ_session(self):
        data = {}
        envvars = os.environ.keys()
        envvars = sorted(envvars)
        for env_var in envvars:
            data[env_var] = html.escape(str(os.environ[env_var]))

        self.pyInfoDict['Environment Variables'] = data

    def _database_session(self):
        data = {
            'DB2/Informix (ibm_db)': self._is_imported('ibm_db'),
            'MSSQL (adodbapi)': self._is_imported('adodbapi'),
            'MySQL (MySQL-Python)': self._is_imported('MySQLdb'),
            'ODBC (mxODBC)': self._is_imported('mxODBC'),
            'Oracle (cx_Oracle)': self._is_imported('cx_Oracle'),
            'PostgreSQL (PyGreSQL)': self._is_imported('pgdb'),
            'Python Data Objects (PyDO)': self._is_imported('PyDO'),
            'SAP DB (sapdbapi)': self._is_imported('sapdbapi'),
            'SQLite3': self._is_imported('sqlite3'),
            'MongoDB': self._is_imported('pymongo')
        }
        self.pyInfoDict['Database support'] = data

    def _compression_session(self):
        data = {
            'Bzip2 Support': self._is_imported('bz2'),
            'Gzip Support': self._is_imported('gzip'),
            'Tar Support': self._is_imported('tarfile'),
            'Zip Support': self._is_imported('zipfile'),
            'Zlib Support': self._is_imported('zlib')
        }
        self.pyInfoDict['Compression and Archiving'] = data

    def _ldap_session(self):
        data = {
            'Python-LDAP Version' % urls['Python-LDAP']: ldap.__version__,
            'API Version': ldap.API_VERSION,
            'Default Protocol Version': ldap.VERSION,
            'Minimum Protocol Version': ldap.VERSION_MIN,
            'Maximum Protocol Version': ldap.VERSION_MAX,
            'SASL Support (Cyrus-SASL)': ldap.SASL_AVAIL,
            'TLS Support (OpenSSL)': ldap.TLS_AVAIL,
            'Vendor Version': ldap.VENDOR_VERSION
        }
        self.pyInfoDict['LDAP support'] = data

    def _multimedia_session(self):
        data = {
            'AIFF Support': self._is_imported('aifc'),
            'Color System Conversion Support': self._is_imported('colorsys'),
            'curses Support': self._is_imported('curses'),
            'IFF Chunk Support': self._is_imported('chunk'),
            'Image Header Support': self._is_imported('imghdr'),
            'OSS Audio Device Support': self._is_imported('ossaudiodev'),
            'Raw Audio Support': self._is_imported('audioop'),
            'Raw Image Support': self._is_imported('imageop'),
            'SGI RGB Support': self._is_imported('rgbimg'),
            'Sound Header Support': self._is_imported('sndhdr'),
            'Sun Audio Device Support': self._is_imported('sunaudiodev'),
            'Sun AU Support': self._is_imported('sunau'),
            'Wave Support': self._is_imported('wave')
        }
        self.pyInfoDict['Multimedia support'] = data

    def _socket_session(self):
        data = {
            'Hostname': socket.gethostname(),
            'Hostname (fully qualified)': socket.gethostbyaddr(socket.gethostname())[0]
        }
        try:
            data['IP Address'] = socket.gethostbyname(socket.gethostname())
        except:
            pass
        data['IPv6 Support'] = getattr(socket, 'has_ipv6', False)
        data['SSL Support'] = hasattr(socket, 'ssl')

        self.pyInfoDict['Socket'] = data

    def _copyright_session(self):
        data = {}
        copylist = sys.copyright.split('\n\n')
        copyrights = [x.replace('\n', ' ') for x in copylist]
        data['Python Copyright'] = copyrights
        self.pyInfoDict['Copyright & License'] = data

    def _installed_packages(self):
        self.pyInfoDict["packages"] = []
        for package in freeze():
            package_name, package_version = package.split("==")
            self.pyInfoDict["packages"].append({"name": package_name, "version": package_version})

    def _get_info(self):
        self._collect_info()
        return self.pyInfoDict

    info_data = property(fget=_get_info)


if __name__ == '__main__':
    myInfo = pyInfo()
    print(json.dumps(myInfo.info_data, indent=4, default=str))
    quit()
    for elementKey, elementValue in myInfo.info_data.items():
        print(elementKey)
        if elementValue:
            for subelemkey, subelemvalue in elementValue.items():
                print(subelemkey)
                print('<br/>\n'.join(subelemvalue) if isinstance(subelemvalue, list) else subelemvalue)
