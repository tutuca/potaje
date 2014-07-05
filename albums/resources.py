from restless.dj import DjangoResource
from restless.preparers import FieldsPreparer
from albums.models import Section, Album


class SectionResource(DjangoResource):
    """Resource for the Section model"""
    preparer = FieldsPreparer(
        fields={
            'name': 'name',
            'description': 'description',
        }
    )

    def detail(self, pk):
        return Section.objects.get(pk=pk)

    def list(self):
        return Section.objects.all()


class AlbumResource(DjangoResource):
    """Resource for the Album model"""
    preparer = FieldsPreparer(
        fields={
            'name': 'name',
            'section': 'section',
            'description': 'description',
            'cover': 'cover',
            'pictures': 'picture_set'
        }
    )

    def detail(self, pk):
        return Album.objects.get(pk=pk)

    def list(self):
        return Album.objects.all()
