import base64
import secrets
import os
from django.conf import settings

def secure_upload_filename(instance, filename):
    FName, Ext = os.path.splitext(filename)
    fName = f"{FName}_{secrets.token_hex(8)}"
    HashedName = base64.b64encode(fName.encode('utf-8')).decode("utf-8").replace('=', '').upper()
    return f"{settings.PROFILE_PIC_FOLDER}{HashedName}{Ext}"
    
