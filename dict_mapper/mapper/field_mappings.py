from .helpers import get_data_classes, check_validity_by_score, check_sensitivity

breach_mapping = {
    "name" : "source.name",
    "title" : "source.name",
    "domain" : "missing",
    "breach_date" : "information.date",
    "disclosure_date" : "missing",
    "added_date" : "missing",
    "modified_date" : "missing",
    "record_count" : "missing",
    "description" : "source.description",
    "logo_path" : "missing",
    "data_classes" : ["information", get_data_classes],
    "is_verified" : ["validated", check_validity_by_score],
    "is_sensitive" : "missing",
    "is_retired" : "missing",
    "is_spam" : "missing",
    "is_collection" : "missing",
    "is_enabled" : "missing",
}