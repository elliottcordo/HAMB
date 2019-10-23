"""
drops watch file in ftp folder per [hamb] config section
"""
from time import sleep
import ftplib
from cocore.Logger import Logger

LOG = Logger()


class Handler(object):
    def __init__(self, CONF):
        self.environment = CONF["hamb"]["environment"]
        self.site = CONF["hamb_ftp"]["site"]
        self.user = CONF["hamb_ftp"]["user"]
        self.password = CONF["hamb_ftp"]["password"]
        self.ftp_path = CONF["hamb_ftp"]["path"]

        self.ftp = None

    def setup(self):
        self.ftp = ftplib.FTP(self.ftp_site)
        self.ftp.login(self.ftp_user, self.ftp_password)

        return self

    def run(self, result, conf):
        level = result["summary"]["status"]

        if level == "failure":
            LOG.l("exiting")
            return

        file_name = str(self.environment).lower() + "_" + conf

        path = self.ftp_path
        self.ftp.cwd(path)

        LOG.l("listing files:")
        for f in self.ftp.nlst():
            LOG.l(f)
            if f == file_name:
                self.ftp.delete(f)

        with open(file_name, "wb") as f:
            if self.environment != "dev":
                f.write("yippee")

        sleep(10)

        LOG.l("uploading to FTP")
        self.ftp.storbinary("STOR " + file_name, open(file_name, "rb"))
        LOG.l("FTP upload complete")

        self.ftp.quit()
