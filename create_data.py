import os

from renderer_data.utils import LOGGER

from renderer_data import (
    create_ships_data,
    create_planes_data,
    create_projectiles_data,
    create_achievements_data,
    create_abilities_data,
    create_building_data,
    create_modernization_data,
    create_units_data,
    create_exterior_data,
)


if __name__ == "__main__":
    os.makedirs(os.path.join(os.getcwd(), "generated"), exist_ok=True)
    create_ships_data()
    create_planes_data()
    create_projectiles_data()
    create_achievements_data()
    create_abilities_data()
    create_modernization_data()
    create_building_data()
    create_units_data()
    create_exterior_data()
    LOGGER.info("Done.")
