from api import TreeNode, API
from geocoders.geocoder import Geocoder


# Инверсия дерева
class MemorizedTreeGeocoder(Geocoder):
    def __init__(self, samples: int | None = None, data: list[TreeNode] | None = None):
        super().__init__(samples=samples)
        if data is None:
            self.__data = API.get_areas()
        else:
            self.__data = data
        self.a_dict = {}

    def _t_tree(self, node: TreeNode, address: str):
        self.a_dict[node.id] = address
        for areas in node.areas:
            self._t_tree(areas, address + ", " + areas.name)

    def _apply_geocoding(self, area_id: str) -> str:
        if not self.a_dict:
            for node in self.__data:
                self._t_tree(node, node.name)

        return self.a_dict.get(area_id, "")