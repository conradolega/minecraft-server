import anvil
import json


def get_sign_text(sign):
    text = []
    for key in ['Text1', 'Text2', 'Text3', 'Text4']:
        line = json.loads(str(sign[key]))
        if line.get('extra'):
            text.append(line['extra'][0]['text'])
    return ' '.join(text)


region = anvil.Region.from_file('/path/to/region-file.mca')

for r_x in range(0, 32):
    for r_y in range(0, 32):
        chunk = anvil.Chunk.from_region(region, r_x, r_y)
        for block_entity in chunk.data['TileEntities']:
            if 'sign' in block_entity['id']:
                text = get_sign_text(block_entity)
                print(text)
