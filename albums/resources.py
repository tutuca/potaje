from restless.dj import DjangoResource
from restless.preparers import FieldsPreparer
from albums.models import Section, Album


class SectionResource(DjangoResource):
    """Resource for the Section model"""

    preparer = FieldsPreparer(fields={})

    def detail(self, pk):
        obj = Section.objects.get(pk=pk)
        return {
            "name": obj.name,
            "albums": [
                {"pk": x.pk, "name": x.name, "cover": x.cover.url}
                for x in obj.album_set.all()
            ],
        }

    def list(self):
        return [
            {
                "name": obj.name,
                "albums": [
                    {"pk": x.pk, "name": x.name, "cover": x.cover}
                    for x in obj.album_set.all()
                ],
            }
            for obj in Section.objects.all()
        ]


class AlbumResource(DjangoResource):
    """Resource for the Album model"""

    preparer = {}

    def detail(self, pk):
        obj = Album.objects.get(pk=pk)
        return {
            "name": obj.name,
            "section": {"pk": obj.section.pk, "name": obj.section.name},
            "description": obj.description,
            "media": [
                {"name": x.caption, "url": x.image.url} for x in obj.picture_set.all()
            ],
        }

    def list(self):
        return [
            {"pk": x.pk, "name": x.name, "cover": x.cover.url}
            for x in Album.objects.all()
        ]
