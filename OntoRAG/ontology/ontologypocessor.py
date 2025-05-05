class OntologyProcessor:
    def __init__(self, ontology):
        """
        Initialize with any OWL ontology loaded via OWLready2.
        :param ontology: OWLready2 ontology object
        """
        self.ontology = ontology

    def get_all_classes(self):
        """
        Get all classes in the ontology with their name and IRI.
        """
        return [
            {"label": cls.name, "iri": cls.iri}
            for cls in self.ontology.classes()
        ]

    def get_subclasses_of(self, class_name_or_iri):
        """
        Get subclasses (children) of a given class, identified by name or IRI fragment.
        """
        cls = self._resolve_class(class_name_or_iri)
        if not cls:
            print(f"[WARN] Class '{class_name_or_iri}' not found.")
            return []
        return list(cls.subclasses())

    def get_superclasses_of(self, class_name_or_iri):
        """
        Get superclasses (parents) of a given class.
        """
        cls = self._resolve_class(class_name_or_iri)
        if not cls:
            print(f"[WARN] Class '{class_name_or_iri}' not found.")
            return []
        return list(cls.is_a)

    def search_class_by_label(self, label):
        """
        Search for a class by its human-readable label (exact match).
        """
        return self.ontology.search_one(label=label)

    def search_class_by_iri_fragment(self, iri_fragment):
        """
        Search for a class containing the given fragment in its IRI.
        Useful for DOIDs, GO terms, etc.
        """
        for cls in self.ontology.classes():
            if iri_fragment in cls.iri:
                return cls
        return None

    def _resolve_class(self, identifier):
        """
        Helper to resolve a class by label or IRI fragment.
        """
        cls = self.search_class_by_label(identifier)
        if not cls:
            cls = self.search_class_by_iri_fragment(identifier)
        return cls

# if __name__ == '__main__':
#     from ontologyloader import OntologyLoader
#     loader = OntologyLoader("HumanDO.owl")
#     ontology = loader.load()

#     processor = OntologyProcessor(ontology)

#     # List first 10 classes
#     for item in processor.get_all_classes():
#         print(f"{item['label']} -> {item['iri']}")

#     # Find subclasses
#     # subclasses = processor.get_subclasses_of("infectious_disease")
#     # print("\n[Subclasses]")
#     # for cls in subclasses:
#     #     print(cls.name)

#     # IRI fragment based lookup (generic)
#     cls = processor.search_class_by_iri_fragment("http://purl.obolibrary.org/obo/DOID_9997")
#     print(f"\n[IRI Fragment Lookup] → {cls.name if cls else 'Not found'}")