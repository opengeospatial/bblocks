import json
from argparse import ArgumentParser
from pathlib import Path
from typing import Sequence

from scripts.generate_docs import DocGenerator
from scripts.util import load_bblocks, BuildingBlock

from ogc.na import ingest_json


def postprocess(registered_items_path: str | Path = 'registereditems',
                output_file: str | Path | None = 'register.json',
                filter_ids: str | list[str] | None = None,
                base_url: str | None = None,
                metadata_schema: str | Path | None = None):
    doc_generator = DocGenerator()

    if base_url and base_url[-1] not in ('/', '#'):
        base_url += '/'

    def do_postprocess(bblock: BuildingBlock) -> bool:
        cwd = Path()
        if base_url:
            if bblock.schema:
                rel_schema = bblock.schema.relative_to(cwd)
                schema_url = f"{base_url}{rel_schema}"
                existing_schemas = bblock.metadata.setdefault('schema', [])

                if bblock.annotated_schema:
                    rel_annotated = bblock.annotated_schema.relative_to(cwd)
                    add_schema_url = f"{base_url}{rel_annotated}"

                    # Remove old, non-annotated schema if present
                    if schema_url in existing_schemas:
                        existing_schemas.remove(schema_url)
                else:
                    add_schema_url = schema_url

                if add_schema_url not in existing_schemas:
                    existing_schemas.append(add_schema_url)

        doc_generator.generate_doc(bblock, base_url=base_url)
        return True

    if not isinstance(registered_items_path, Path):
        registered_items_path = Path(registered_items_path)

    output_bblocks = []
    for building_block in load_bblocks(registered_items_path,
                                       filter_ids=filter_ids,
                                       metadata_schema_file=metadata_schema):
        if do_postprocess(building_block):
            output_bblocks.append(building_block.metadata)

    if output_file:
        if output_file == '-':
            print(json.dumps(output_bblocks, indent=2))
        else:
            with open(output_file, 'w') as f:
                json.dump(output_bblocks, f, indent=2)


def _main():
    parser = ArgumentParser()

    parser.add_argument(
        'output_register',
        default='register.json',
        help='Output JSON Building Blocks register document',
    )

    parser.add_argument(
        '-u',
        '--base-url',
        help='Base URL for hyperlink generation',
    )

    parser.add_argument(
        '-i',
        '--filter-id',
        nargs='+',
        help='Only process building blocks matching these ids',
    )

    parser.add_argument(
        'registered_items',
        default='registereditems',
        help='Registered items directory',
    )

    parser.add_argument(
        '-N',
        '--no-output',
        action='store_true',
        help='Do not generate output JSON register document',
    )

    parser.add_argument(
        '-s',
        '--metadata-schema',
        help="JSON schema for Building Block metadata validation",
    )

    args = parser.parse_args()

    postprocess(args.registered_items,
                output_file=None if args.no_output else args.output_register,
                filter_ids=args.filter_id,
                base_url=args.base_url,
                metadata_schema=args.metadata_schema)


if __name__ == '__main__':
    _main()
