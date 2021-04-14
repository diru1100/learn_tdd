import unittest
from ..ner_client import NamedEntityClient
from .test_doubles import NerModelTestDouble


class TestNerClient(unittest.TestCase):

    # {ents:[{...}],
    #     html: "<span>..."}

    def test_get_ents_returns_dict_given_empty_string_causes_empty_spacy_docs_ents(self):
        # https://martinfowler.com/bliki/TestDouble.html
        model = NerModelTestDouble("eng")
        ner = NamedEntityClient(model, "")
        model.set_doc_ents([])
        ents = ner.get_ents("")
        self.assertIsInstance(ents, dict)

    def test_get_ents_returns_dict_given_nonempty_string_causes_empty_spacy_doc_ents(self):
        model = NerModelTestDouble("eng")
        ner = NamedEntityClient(model, "")
        model.set_doc_ents([])
        ents = ner.get_ents("Rohit likes to eat Biryani")
        self.assertIsInstance(ents, dict)

    def test_get_ents_given_spacy_PERSON_is_returned_serializes_to_Person(self):
        model = NerModelTestDouble("eng")
        doc_ents = [{"text": "Naruto", "label_": "PERSON"}]
        model.set_doc_ents(doc_ents)
        ner = NamedEntityClient(model, "")
        result = ner.get_ents("...")
        expected_result = {
            "ents": [{"text": "Naruto", "label": "Person"}], "html": ""}
        self.assertListEqual(result["ents"], expected_result["ents"])

    def test_get_ents_given_spacy_NORP_is_returned_serializes_to_Group(self):
        model = NerModelTestDouble("eng")
        doc_ents = [{"text": "Indian", "label_": "NORP"}]
        model.set_doc_ents(doc_ents)
        ner = NamedEntityClient(model, "")
        result = ner.get_ents("...")
        expected_result = {
            "ents": [{"text": "Indian", "label": "Group"}], "html": ""}
        self.assertListEqual(result["ents"], expected_result["ents"])

    def test_get_ents_given_spacy_LOC_is_returned_serializes_to_Location(self):
        model = NerModelTestDouble("eng")
        doc_ents = [{"text": "the river", "label_": "LOC"}]
        model.set_doc_ents(doc_ents)
        ner = NamedEntityClient(model, "")
        result = ner.get_ents("...")
        expected_result = {
            "ents": [{"text": "the river", "label": "Location"}], "html": ""}
        self.assertListEqual(result["ents"], expected_result["ents"])

    def test_get_ents_given_spacy_GPE_is_returned_serializes_to_Location(self):
        model = NerModelTestDouble("eng")
        doc_ents = [{"text": "India", "label_": "GPE"}]
        model.set_doc_ents(doc_ents)
        ner = NamedEntityClient(model, "")
        result = ner.get_ents("...")
        expected_result = {
            "ents": [{"text": "India", "label": "Location"}], "html": ""}
        self.assertListEqual(result["ents"], expected_result["ents"])

    def test_get_ents_multiple_ents_serializes_all(self):
        model = NerModelTestDouble("eng")
        doc_ents = [{"text": "India", "label_": "GPE"},
                    {"text": "Naruto", "label_": "PERSON"}]
        model.set_doc_ents(doc_ents)
        ner = NamedEntityClient(model, "")
        result = ner.get_ents("...")
        expected_result = {
            "ents": [{"text": "India", "label": "Location"}, {"text": "Naruto", "label": "Person"}], "html": ""}
        self.assertListEqual(result["ents"], expected_result["ents"])
