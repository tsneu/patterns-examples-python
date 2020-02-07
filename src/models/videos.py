from src.storage.produto import VideoStorageList
from src.models.base import SimpleResourceList, ItemList

class VideoModel(ItemList):
    _ID = 0
    _titulo = ""
    _link_web = ""

    def _to_object(self, item):
        self._ID = self._default_attr(item, 'id_video', 0)
        self._titulo = self._default_attr(item, 'titulo', "")
        self._link_web = self._default_attr(item, 'link_web', "")

    def serialize(self):
        return {
            "type": "video",
            "id": self._ID,
            "attributes": {
                "titulo": self._titulo,
                "link_web": self._link_web
            }
        }


class VideosIterator(SimpleResourceList):

    def __init__(self, _id):
        super().__init__(_id, VideoStorageList, VideoModel)
