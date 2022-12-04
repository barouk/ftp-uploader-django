from django.shortcuts import render
from ftplib import FTP
from FtpUploader.settings import DOWNLOAD_HOST_IP, DOWNLOAD_HOST_USER,DOWNLOAD_HOST_PASSWORD
from rest_framework import viewsets
from rest_framework.response import Response




class UploaderView(viewsets.ViewSet):
    def create(self, request, *args, **kwargs):
        file_to_save = request.data['file']
        ftp_host = DOWNLOAD_HOST_IP
        ftp_user = DOWNLOAD_HOST_USER
        ftp_password = DOWNLOAD_HOST_PASSWORD
        ftp = FTP(ftp_host)
        ftp.login(user=ftp_user, passwd=ftp_password)
        ftp.cwd('files/')
        f = ftp.storbinary("STOR "+ file_to_save.name, file_to_save, 1024)
        return Response({"detail": "saved"})



