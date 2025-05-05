from owlready2 import get_ontology
import os

class OntologyLoader:
    def __init__(self, ontology_path: str):
        """
        Initializes the ontology loader with the given OWL file path.

        :param ontology_path: Path to the .owl ontology file
        """
        if not os.path.exists(ontology_path):
            raise FileNotFoundError(f"Ontology file not found at: {ontology_path}")
        
        self.ontology_path = ontology_path
        self.ontology = None

    def load(self):
        """
        Loads the ontology from the specified path using OWLready2.
        """
        print(f"[INFO] Loading ontology from {self.ontology_path}...")
        self.ontology = get_ontology(self.ontology_path).load()
        print(f"[INFO] Ontology loaded successfully with {len(list(self.ontology.classes()))} classes.")
        return self.ontology

    def list_classes(self):
        """
        Lists all classes (concepts) in the ontology.
        """
        if not self.ontology:
            raise ValueError("Ontology not loaded yet. Call load() first.")
        return list(self.ontology.classes())

    def list_object_properties(self):
        """
        Lists object properties in the ontology.
        """
        if not self.ontology:
            raise ValueError("Ontology not loaded yet. Call load() first.")
        return list(self.ontology.object_properties())

    def list_individuals(self):
        """
        Lists individuals (instances) in the ontology.
        """
        if not self.ontology:
            raise ValueError("Ontology not loaded yet. Call load() first.")
        return list(self.ontology.individuals())

# if __name__ == '__main__':
#     loader = OntologyLoader("HumanDO.owl")
#     ontology = loader.load()
#     print(ontology)