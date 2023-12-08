# config.py
class AppConfig:
    def __init__(self, company, access_id, access_key):
        self.company = company
        self.access_id = access_id
        self.access_key = access_key


app_config = AppConfig(
    company="your_company",
    access_id="your_access_id",
    access_key="your_access_key"
)
