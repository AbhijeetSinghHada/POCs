from pydantic import BaseModel, Field, AliasPath, computed_field

class Breach(BaseModel):
    name : str = Field(validation_alias=AliasPath("source", "name"), title="Name")
    title: str = Field(validation_alias=AliasPath("source", "name"), title="Title")
    description : str = Field(validation_alias=AliasPath("source", "description"), title="Description")
    priv_data_classes : dict = Field(validation_alias=AliasPath("information"), title="Data Classes", exclude=True)

    domain : str = Field(None, title="Domain")
    breach_date : str = Field(default="", title="Breach Date")
    disclosure_date : str = Field(default="", title="Disclosure Date")
    added_date : str = Field(default="", title="Added Date")
    modified_date : str = Field(default="", title="Modified Date")
    record_count : int = Field(default=None, title="Record Count")
    logo_path : str = Field(default="", title="Logo Path")
    is_verified : int = Field(default=0, title="Is Verified")
    is_sensitive : int = Field(default=0, title="Is Sensitive")
    is_retired : int = Field(default=0, title="Is Retired")
    is_spam : int = Field(default=0, title="Is Spam")
    is_collection : int = Field(default=0, title="Is Collection")
    is_enabled : int = Field(default=0, title="Is Enabled")


    @computed_field(return_type=list)
    def data_classes(self):
        keys = list(self.priv_data_classes.keys())
        return keys
    

class BreachInfo(BaseModel):
    EmailAlias : str = Field(None, title="Email Alias")
    EmailDomain : str = Field(None, title="Email Domain")
    PasswordCount : int = Field(None, title="Password Count")
    priv_passwords : list = Field(validation_alias=AliasPath("data", "results"), exclude=True)
    Breaches : list[Breach] = Field(validation_alias=AliasPath("data", "results"), title="Breaches")

    @computed_field(return_type=list)
    def Passwords(self):
        password_path = ["information","password_info", "password_last_chars"]
        passwords = []
        for breach in self.priv_passwords:
            try:
                for key in password_path:
                    breach = breach[key]
                passwords.append(breach)
            except KeyError:
                continue
        return passwords

                

