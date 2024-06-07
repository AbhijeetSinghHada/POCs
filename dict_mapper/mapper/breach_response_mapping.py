from .field_mappings import breach_mapping
from dark_web_proxy_common.mapper.mapper import Mapper

def breach_mapper(breaches : list):
    transformer_breaches = []
    for breach in breaches:
        mapper = Mapper(breach, breach_mapping)
        breach = mapper.map_dict()
        transformer_breaches.append(breach)
    return transformer_breaches


breach_info_response_mapping  = {
    "EmailAlias" : "missing",
    "EmailDomain" : "missing",
    "PassowordCount" : "NotFound",
    "Passwords" : [""],
    "Breaches" : ["data.results", breach_mapper],
}
