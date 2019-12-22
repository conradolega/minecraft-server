import anvil
import json
import logging
import os
import sys

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
REGION_DIR = '/home/user/.minecraft/saves/my_world/world/region/'

def get_sign_text(sign):
    text = []
    for key in ['Text1', 'Text2', 'Text3', 'Text4']:
        line = json.loads(str(sign[key]))
        if line.get('extra'):
            text.append(line['extra'][0]['text'])
    return ' '.join(text)

for root, dirs, files in os.walk(REGION_DIR):
    for file in files:
        region = anvil.Region.from_file(root + file)
        logging.info(str(file))
        for r_x in range(0, 32):
            for r_y in range(0, 32):
                try:
                    chunk = anvil.Chunk.from_region(region, r_x, r_y)
                except Exception:
                    continue

                for block_entity in chunk.data['TileEntities']:
                    if 'sign' in block_entity['id']:
                        text = get_sign_text(block_entity)
                        print(f"{block_entity['x']},{block_entity['z']}")
