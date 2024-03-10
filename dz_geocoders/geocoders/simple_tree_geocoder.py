from hh_geocoding_template.api import API, TreeNode
from geocoders.geocoder import Geocoder


# Перебор дерева
class SimpleTreeGeocoder(Geocoder):
    def __init__(self, samples: int | None = None, data: list[TreeNode] | None = None):
        super().__init__(samples=samples)
        if data is None:
            self.__data = API.get_areas()
        else:
            self.__data = data

    def _apply_geocoding(self, area_id: str) -> str:
            target_node = None
            for node in self.__data:
                if node.id == area_id:
                    target_node = node
                    break

            if target_node is None:
                return "("

            address_parts = [target_node.name]
            current_node = target_node
            while current_node.id is not None:
                parent_node = None
                for node in self.__data:
                    if node.id == current_node.parent_id:
                        parent_node = node
                        break
                if parent_node is None:
                    break
                address_parts.insert(0, parent_node.name)
                current_node = parent_node

            full_address = ", ".join(address_parts)
            return full_address

