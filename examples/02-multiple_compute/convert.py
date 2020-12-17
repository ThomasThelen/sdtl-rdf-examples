from sdtlconverter.ConverterV1 import ConverterV1

converter = ConverterV1('./sdtl.json')

converter.convert_sdtl_to_rdf()
# Print the RDF
print(str(converter))
# Write to disk
converter.write_jsonld()
converter.write_turtle()
