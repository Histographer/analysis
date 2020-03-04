from cytomine import Cytomine
from cytomine.models.image import ImageInstanceCollection
from cytomine.models.annotation import AnnotationCollection
from cytomine.utilities import WholeSlide


def get_images_with_annotations(host, public_key, private_key, project_id):
    """
    :param project_id:
    :return: List of dictionaries with 'image' and 'annotations'
    """
    output = []
    with Cytomine(host=host, public_key=public_key, private_key=private_key, verbose=True) as cytomine:
        annotations = AnnotationCollection()
        annotations.project = project_id
        annotations.fetch()
        print(annotations)
        """
        image_instances = ImageInstanceCollection().fetch('project', project_id)
        for image_instance in image_instances:
            
        annotations = AnnotationCollection()"""


if __name__ == '__main__':
    from yaml import safe_load
    from pathlib import Path

    host = safe_load(open(Path(__file__).parents[4] / 'secrets.yml', 'r'))['host']
    get_images_with_annotations(**host)

