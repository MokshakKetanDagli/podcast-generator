import yaml
import xml.etree.ElementTree as xml_tree

with open('feed.yaml', 'r') as file:
    yaml_data = yaml.safe_load(file)

rss_element = xml_tree.Element('rss', {
    'version': '2.0',
    'xmlns:itunes': 'http://www.itunes.com/dtds/podcast-1.0.dtd',
    'xmlns:content': 'http://purl.org/rss/1.0/modules/content/'
})

channel_element = xml_tree.SubElement(rss_element, 'channel')

link_prefix = yaml_data['link']
xml_tree.SubElement(channel_element, 'title').text = yaml_data['title']
xml_tree.SubElement(channel_element, 'subtitle').text = yaml_data['subtitle']
xml_tree.SubElement(channel_element, 'author').text = yaml_data['author']
xml_tree.SubElement(channel_element, 'description').text = yaml_data['description']
xml_tree.SubElement(channel_element, 'category').text = yaml_data['category']
xml_tree.SubElement(channel_element, 'language').text = yaml_data['language']
xml_tree.SubElement(channel_element, 'itunes:image', {'href': link_prefix + yaml_data['image']})
xml_tree.SubElement(channel_element, 'link').text = link_prefix

for episode in yaml_data['item']:
    episode_element = xml_tree.SubElement(channel_element, 'item')
    xml_tree.SubElement(episode_element, 'title').text = episode['title']
    xml_tree.SubElement(episode_element, 'description').text = episode['description']
    xml_tree.SubElement(episode_element, 'published').text = episode['published']
    xml_tree.SubElement(episode_element, 'duration').text = episode['duration']
    xml_tree.SubElement(episode_element, 'length').text = episode['length']
    xml_tree.SubElement(episode_element, 'link').text = link_prefix + episode['file']

output_tree = xml_tree.ElementTree(rss_element)

output_tree.write('podcast.xml', encoding='UTF-8', xml_declaration=True)