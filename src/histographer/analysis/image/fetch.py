from cytomine import Cytomine
from cytomine.models.image import ImageInstanceCollection
from cytomine.models.annotation import AnnotationCollection, Annotation
from cytomine.utilities import WholeSlide
from collections import defaultdict as dd
from pathlib import Path


def get_images_with_annotations(host, public_key, private_key, project_id, download=True, annotation_ids=None):
    """
    :param project_id:
    :return: List of dictionaries with 'image' and 'annotations'
    """
    output = []
    with Cytomine(host=host, public_key=public_key, private_key=private_key, verbose=True) as cytomine:
        annotations = AnnotationCollection()
        annotations.project = project_id

        annotations.fetch()

        image_regions = dd(list)

        for annotation in annotations:
            if annotation_ids is not None and annotation.id not in annotation_ids:
                continue
            annotation: Annotation
            path = Path('/tmp') / 'cytomine' / 'p{project}' / 'i{image}' / 'masked{id}'
            formatted = str(path).format(id=annotation.id, image=annotation.image, project=annotation.project) + '.png'
            if download and not Path(formatted).is_file():
                annotation.dump(str(path), override=True, mask=True, alpha=True)
                print(f'Dumped to {path}')
            image_regions[annotation.image]\
                .append(formatted)

        print(image_regions)
        """
        image_instances = ImageInstanceCollection().fetch('project', project_id)
        for image_instance in image_instances:

        annotations = AnnotationCollection()"""
        return image_regions


if __name__ == '__main__':
    from yaml import safe_load
    from pathlib import Path
    from skimage.color import rgb2hed
    from skimage.io import imread
    import numpy.ma as ma
    from histographer.analysis.image.segment import segment_plot_rgb
    from histographer.analysis.image.color import channel_metrics
    import numpy as np

    host = safe_load(open(Path(__file__).parents[4] / 'secrets.yml', 'r'))['host']
    image_regions = get_images_with_annotations(**host, download=True)
    print(len(image_regions))
    rgbas = [imread(im_url) for im_url in image_regions[next(iter(image_regions.keys()))]]
    print(rgbas)

    i = 0
    im = rgbas[i]
    mask = im[..., 3]

    print('before mask')
    im[mask, :] = 0
    print('before segment')
    tissue, nuclei, no_class = segment_plot_rgb(im[..., :3])
    print('after segment')

    hed = rgb2hed(im[..., :3])

    print({
        'H': channel_metrics(ma.array(hed[..., 0], mask=(tissue & mask))),
        'E': channel_metrics(ma.array(hed[..., 1], mask=(nuclei & mask)))
    })

